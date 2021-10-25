import React from 'react';
import SignUp from '../screens/SignUp/SignUpScreen';
import renderer from 'react-test-renderer';

describe('Testing SignUp Component', () => {
    it("renders as expected", () => {
        const tree = renderer.create(<SignUp />).toJSON();
        expect(tree).toMatchSnapshot();
    });
});

describe('SignUp state is initialized correctly', () => {
    const SignUpData = renderer.create(<SignUp />).getInstance();
    it("email is empty to start", () => {
        expect(SignUpData.state.email).toEqual("");
    })
    it("password is empty to start", () => {
        expect(SignUpData.state.password).toEqual("");
    })
    it("firstname is empty to start", () => {
        expect(SignUpData.state.firstname).toEqual("");
    })
    it("lastname is empty to start", () => {
        expect(SignUpData.state.lastname).toEqual("");
    })
})