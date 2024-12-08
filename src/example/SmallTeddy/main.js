/**
 * @description: 影视爬取
 * @author: SmallTeddy
 * @see https://github.com/SmallTeddy/video-resource/blob/main/README.md
 */
import fetch from 'node-fetch';
import readline from 'readline';

// 获取用户输入
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("请输入要搜索的名称: ", (name) => {
  const currentTimestamp = Date.now();

  const cookies = {
    _clck:
      "aG%2FCmMKawpPCmmrCn2dxaWVkwphmYWlpZ8KTZm9qcWloacKTwpdnwpVkZw%3D%3D%7C2%7Cfq1%7C0%7C0",
    _clsk: `128761241771877460|${currentTimestamp}22|1|api.a3gj.cn`,
  };

  const headers = {
    Accept: "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    Connection: "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    Origin: "http://www.kkkob.com",
    "User-Agent":
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
  };

  const getToken = async () => {
    const response = await fetch("http://www.kkkob.com/v/api/getToken", {
      method: "GET",
      headers: {
        Accept:
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        Connection: "keep-alive",
        "If-None-Match": 'W/"27-vcQAX3AjsSgVDyEpCQWBBpZwj/Y"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent":
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
      },
      headers: {
        Cookie: Object.keys(cookies)
          .map((key) => `${key}=${cookies[key]}`)
          .join("; "),
      },
    });
    const data = await response.json();
    return data.token;
  };

  const appendList = (response) => {
    response.json().then((jsonResponse) => {
      if (jsonResponse.list && jsonResponse.list.length > 0) {
        jsonResponse.list.forEach((item) => {
          finalDataList.push(item);
        });
      }
    });
  };

  const search = async () => {
    const token = await getToken();
    const data = new URLSearchParams({
      name,
      token,
    });

    const response = await fetch("http://www.kkkob.com/v/api/search", {
      method: "POST",
      headers,
      body: data,
      headers: {
        Cookie: Object.keys(cookies)
          .map((key) => `${key}=${cookies[key]}`)
          .join("; "),
      },
    });
    appendList(response);
  };

  const getDJ = async () => {
    const response = await fetch("http://www.kkkob.com/v/api/getDJ", {
      method: "POST",
      headers,
      body: new URLSearchParams({ name }),
      headers: {
        Cookie: Object.keys(cookies)
          .map((key) => `${key}=${cookies[key]}`)
          .join("; "),
      },
    });
    appendList(response);
  };

  const getJuzi = async () => {
    const response = await fetch("http://www.kkkob.com/v/api/getJuzi", {
      method: "POST",
      headers,
      body: new URLSearchParams({ name }),
      headers: {
        Cookie: Object.keys(cookies)
          .map((key) => `${key}=${cookies[key]}`)
          .join("; "),
      },
    });
    appendList(response);
  };

  const getXiaoyu = async () => {
    const response = await fetch("http://www.kkkob.com/v/api/getXiaoyu", {
      method: "POST",
      headers,
      body: new URLSearchParams({ name }),
      headers: {
        Cookie: Object.keys(cookies)
          .map((key) => `${key}=${cookies[key]}`)
          .join("; "),
      },
    });
    appendList(response);
  };

  const getSearchX = async () => {
    const response = await fetch("http://www.kkkob.com/v/api/getSearchX", {
      method: "POST",
      headers,
      body: new URLSearchParams({ name }),
      headers: {
        Cookie: Object.keys(cookies)
          .map((key) => `${key}=${cookies[key]}`)
          .join("; "),
      },
    });
    appendList(response);
  };

  const showFinalList = () => {
    const processedData = finalDataList.map((item) => {
      const newItem = { ...item };
      newItem["资源名称"] = newItem.question;
      newItem["资源链接"] = newItem.answer;
      
      delete newItem.id;
      delete newItem.isTop;
      delete newItem.question;
      delete newItem.answer;
      return newItem;
    });

    console.log(JSON.stringify(processedData, null, 4));
  };

  const finalDataList = [];

  (async () => {
    await search();
    await getDJ();
    await getJuzi();
    await getXiaoyu();
    await getSearchX();
    showFinalList();
    rl.close();
  })();
});
