const API_ROOT = "https://uym0p1wqoc.execute-api.us-west-2.amazonaws.com/api/";

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

}

export function checkCredentials(config) {

}

export function processEmployee(config) {

}

export function login() {
}


export function logout() {

}
