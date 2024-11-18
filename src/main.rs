use reqwest::blocking::{Client, Response};
use serde_json::Value;
use std::collections::HashMap;
use std::io;

fn get_token(client: &Client, _cookies: &HashMap<&str, String>) -> String {
    let response = client
        .get("http://www.kkkob.com/v/api/getToken")
        .headers(get_headers())
        .send()
        .unwrap();

    let json: Value = response.json().unwrap();
    json["token"].as_str().unwrap().to_string()
}

fn get_headers() -> reqwest::header::HeaderMap {
    let mut headers = reqwest::header::HeaderMap::new();
    headers.insert("Accept", "*/*".parse().unwrap());
    headers.insert("Accept-Language", "zh-CN,zh;q=0.9".parse().unwrap());
    headers.insert("Connection", "keep-alive".parse().unwrap());
    headers.insert(
        "Content-Type",
        "application/x-www-form-urlencoded; charset=UTF-8"
            .parse()
            .unwrap(),
    );
    headers.insert("Origin", "http://www.kkkob.com".parse().unwrap());
    headers.insert("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36".parse().unwrap());
    headers.insert("X-Requested-With", "XMLHttpRequest".parse().unwrap());
    headers
}

fn append_list(response: Response, final_data_list: &mut Vec<Value>) {
    let json_response: Value = response.json().unwrap();
    if let Some(list) = json_response["list"].as_array() {
        for item in list {
            final_data_list.push(item.clone());
        }
    }
}

fn search(
    client: &Client,
    cookies: &HashMap<&str, String>,
    name: &str,
    final_data_list: &mut Vec<Value>,
) {
    let token = get_token(client, cookies);
    let mut data = HashMap::new();
    data.insert("name", name);
    data.insert("token", &token);

    let response = client
        .post("http://www.kkkob.com/v/api/search")
        .headers(get_headers())
        .form(&data)
        .send()
        .unwrap();

    append_list(response, final_data_list);
}

fn main() {
    let client = Client::new();
    let current_timestamp = chrono::Utc::now().timestamp_millis();

    let mut cookies = HashMap::new();
    cookies.insert(
        "_clck",
        "aG%2FCmMKawpPCmmrCn2dxaWVkwphmYWlpZ8KTZm9qcWloacKTwpdnwpVkZw%3D%3D%7C2%7Cfq1%7C0%7C0"
            .to_string(),
    );
    cookies.insert(
        "_clsk",
        format!("128761241771877460|{}22|1|api.a3gj.cn", current_timestamp),
    );

    let mut final_data_list = Vec::new();

    let mut input = String::new();
    println!("请输入要搜索的名称: ");
    io::stdin().read_line(&mut input).unwrap();
    let name = input.trim();

    search(&client, &cookies, name, &mut final_data_list);

    // Implement other functions similar to search for getDJ, getJuzi, getXiaoyu, getSearchX

    // Show final list
    for item in final_data_list {
        let mut new_item = item.clone();
        if let Some(obj) = new_item.as_object_mut() {
            obj.remove("id");
            obj.remove("isTop");

            // 先将要移除的值存储在临时变量中
            let question = obj.remove("question").unwrap_or(Value::Null);
            let answer = obj.remove("answer").unwrap_or(Value::Null);

            // 然后再进行插入操作
            obj.insert("资源名称".to_string(), question);
            obj.insert("资源链接".to_string(), answer);
        }
        println!("{}", serde_json::to_string_pretty(&new_item).unwrap());
    }
}
