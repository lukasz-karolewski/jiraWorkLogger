import React, {Component} from 'react';
import styled from 'styled-components'
import {checkCredentials, getConfig} from "../apiClient";

const StyledApp = styled.div`
  text-align: center;
`;

const Input = styled.input`
    width:100px
`;

const Button = styled.button`
    color: palevioletred;
`;


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {username: '', password: ''};
    }

    componentDidMount() {
        this.setState(getConfig());
    }

    setUsername = (event) => {
        console.log(event);
        this.setState({
            username: event.target.value
        });
    };

    setPassword = (event) => {
        this.setState({
            password: event.target.value
        });
    };

    checkCredentials = () => {
        checkCredentials(this.state.username, this.state.password)
            .then(response => {
                console.log(response);
            });
    };

    render() {
        return (
            <StyledApp>
                jira username:
                <Input type="text" value={this.state.username} onChange={this.setUsername}/>
                jira password:
                <Input type="text" value={this.state.password} onChange={this.setPassword}/>

                <Button onClick={this.checkCredentials}>Check credentials</Button>

                log as of:<Input type="date"/>

                jira_ticket:<Input type="text"/>

                hours_per_day:<Input type="number" defaultValue="8" step="1" min="0" max="12"/>

                default overhead <Input type="number" defaultValue="0.15" step="0.01" min="0" max="1"/>

                employees:
                - jira username <Input type="text"/>
                - days_off <Input type="number" defaultValue="0" step="1" min="0" max="30"/>
                - overhead <Input type="number" defaultValue="0.15" step="0.01" min="0" max="1"/>

                <Button>Log capex</Button>
            </StyledApp>
        );
    }
}

export default App;
