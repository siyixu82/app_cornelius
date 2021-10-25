import React from 'react';
import Login from '../screens/Login/LoginScreen';
import renderer from 'react-test-renderer';

describe('Testing Login Component', () => {
    it("renders as expected", () => {
        const tree = renderer.create(<Login />).toJSON();
        expect(tree).toMatchSnapshot();
    });
});

describe('Login state is initialized correctly', () => {
    const LoginData = renderer.create(<Login />).getInstance();
    it("username is empty to start", () => {
        expect(LoginData.state.username).toEqual("");
    })
    it("password is empty to start", () => {
        expect(LoginData.state.password).toEqual("");
    })
})