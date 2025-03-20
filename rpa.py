import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cas.intranet.infosec.ctripcorp.com/login.html?service=http%3A%2F%2Ftripfinancials.basebiz.ctripcorp.com%2Fsys%2Findex%3Fmodule%3D301424&appId=100027719")
    page.get_by_role("textbox", name="域账户名").fill("jingwensong")
    page.get_by_role("textbox", name="域账户密码").fill("TR019069sjw06")
    page.get_by_role("button", name="登录").click()
    page.get_by_text("资金池").click()
    page.get_by_text("资金收款认领").click()
    page.locator("iframe").nth(1).content_frame.get_by_role("button", name="导入领用").click()
    page.locator("iframe").nth(1).content_frame.get_by_role("button", name="选择领款文件").click()
    page.locator("iframe").nth(1).content_frame.get_by_role("button", name="开始上传").click()

    # ---------------------
    context.storage_state(path="auth.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
