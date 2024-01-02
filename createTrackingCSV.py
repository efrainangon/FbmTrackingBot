import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
omitted = "This was omitted"
async def main():
    data = []
    header = ['AmazonID','Tracking','Carrier']
    browser = await launch(headless=False,userDataDir=omitted)
    page = await browser.newPage()
    await stealth(page)
    await page.goto(omitted)
    await page.waitForXPath('//*[@id="orders-table"]/tbody/tr[1]',timeout=100000)
    while True:
        counter= omitted
        counter2= omitted
        page = omitted
        if page==0:
            break
        for x in range(page):
            print(x+counter2)
            try:
                await page.waitForXPath(f'//*[@id="orders-table"]/tbody/tr[{x+1}]/td[3]/div/div[1]/a',timeout=5000)
                element = await page.xpath(f'//*[@id="orders-table"]/tbody/tr[{x+1}]/td[3]/div/div[1]/a')
                orderid=await page.evaluate('(element) => element.textContent', element[0])
                href=await page.evaluate('(element) => element.href', element[0])
                print(orderid)
                refund=False
                try:
                    await page.waitForXPath(f'/html/body/div[1]/div[2]/div/div/div[3]/div[4]/div[2]/div[3]/div/div[2]/table/tbody/tr[{x+1}]/td[7]/div/div[2]/div/div/span/span',timeout=2500)
                    element = await page.xpath(f'/html/body/div[1]/div[2]/div/div/div[3]/div[4]/div[2]/div[3]/div/div[2]/table/tbody/tr[{x+1}]/td[7]/div/div[2]/div/div/span/span')
                    await page.evaluate('(element) => element.textContent', element[0])
                    refund=True
                except:
                    pass
                if refund==False:
                    await page.goto(href)
                    await page.waitForXPath('//*[@id="MYO-app"]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div/span/span')
                    try:
                        element= await page.xpath("//*[@id='MYO-app']/div/div[1]/div[1]/div/div[8]/div/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/span")
                        tracking = await page.evaluate('(element) => element.textContent', element[0])
                    except:
                        omitted
                    print(tracking)
                    carrier='USPS'
                    if '1Z' in tracking:
                        carrier='UPS'
                    data.append([orderid,tracking,carrier])
                    await page.goto(f"https://sellercentral.amazon.com/orders-v3/mfn/shipped?page={counter}")
                    await page.waitForXPath('//*[@id="orders-table"]/tbody/tr[1]')
                else:
                    print("Refunded")
            except Exception as e:
                logger.error('Failed to upload to ftp: ' + str(e))
                await page.goto(f"https://sellercentral.amazon.com/orders-v3/mfn/shipped?page={counter}")
                page+=1
    filename = omitted
    with open(filename, 'w') as file:
        for header in header:
            file.write(str(header) + ', ')
        file.write('\n')
        for row in data:
            for x in row:
                file.write(str(x) + ', ')
            file.write('\n')
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
