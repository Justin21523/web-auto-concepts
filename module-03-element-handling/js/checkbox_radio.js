const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page    = await browser.newPage();
  await page.goto('https://example.com/form-options');

  // 1. 使用 API 直接打勾
  await page.check("input[type='radio'][value='opt1']");
  await page.check("input[type='checkbox'][value='chk2']");

  // 2. 驗證
  const radioChecked    = await page.isChecked("input[type='radio'][value='opt1']");
  const checkboxChecked = await page.isChecked("input[type='checkbox'][value='chk2']");
  console.log("Radio selected:", radioChecked);
  console.log("Checkbox selected:", checkboxChecked);

  await browser.close();
})();
