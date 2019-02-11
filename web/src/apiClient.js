const API_ROOT = (process.env.NODE_ENV === 'production' ? "https://8lt5ajicxf.execute-api.us-west-2.amazonaws.com/api/" : "http://localhost:8000");

export function getConfig() {
    return {
        "jira_ticket": "BASE-3115",
        "hours_per_day": 8,
        "default_overhead": 0.15,
        // "as_of": "2019-01-25T18:00:01Z",
        "employees": [
            {
                "name": "test",
                "days_off": 0
            }
        ]
    }
}

export function saveConfig(config) {
    console.log('test');
}

export function checkCredentials(username, password) {
    return fetch(`${API_ROOT}/check-credentials`, {
        method: "POST",
        headers: new Headers([
            ['Content-Type', "application/json"]
        ]),
        body: JSON.stringify({username, password})
    });
}

export function processEmployee(config) {

}

export function login() {
}


export function logout() {

}
