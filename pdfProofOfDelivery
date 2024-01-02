import asyncio
import time
from pyppeteer import launch
from pyppeteer_stealth import stealth
from pandas import *


async def main():
    data = read_csv("omitted.csv")
    fc = data[' Tracking'].tolist()
    browser = await launch(headless=False,userDataDir='omitted')
    page = await browser.newPage()
    await stealth(page)
    counter = 0
    i = "omitted"
    while i < len(fc):
        x = fc[i]
        delivered = False
        tracking = x.replace(" ", "")
        try:
            if '1Z' not in tracking:
                await browser.close()
                print('here')
                browser = await launch(headless=False,
                                       userDataDir='omitted')
                page = await browser.newPage()
                await stealth(page)
                await page.goto(f'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1={tracking}')
                time.sleep(5)
                await page.waitForXPath(
                    '/html/body/div[1]/div[6]/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div[1]/p[1]',
                    timeout=3000)
                element = await page.xpath(
                    '/html/body/div[1]/div[6]/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div[1]/p[1]')
                await page.screenshot(path=f'omitted/{tracking}.png')

            deliveredornot = await page.evaluate('(element) => element.textContent', element[0])
            print(deliveredornot)
            if deliveredornot == 'Delivered':
                delivered = True
            if 'Delivered On' in deliveredornot:
                delivered = True
            if delivered:
                await page.screenshot(path=f'omitted/{tracking}.png')
                counter = counter + 1
                print(counter)
        except:
            pass
        print('i value:' + str(i))
        i = i + 1


asyncio.get_event_loop().run_until_complete(main())
