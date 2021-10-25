import * as actionTypes from './actions';

const initialState = {
    uid: '',
    firstname: '',
    lastname: '',
    email: '',
    physicians: [],
    facilities: [],
    journals: [],
}

const reducer = (state = initialState, action) => {
    switch(action.type) {
        case actionTypes.SET_ID:
            return {
                ...state,
                uid: action.val
            }
            
        case actionTypes.SET_FIRSTNAME:
            return {
                ...state,
                firstname: action.val
            }

        case actionTypes.SET_LASTNAME:
            return {
                ...state,
                lastname: action.val
            }

        case actionTypes.SET_EMAIL:
            return {
                ...state,
                email: action.val
            }

        case actionTypes.SET_PHYSICIANS:
            return {
                ...state,
                physicians: action.val
            }
        
        case actionTypes.ADD_PHYSICIAN:
            return {
                ...state,
                physicians: [action.val, ...state.physicians]
            }

        case actionTypes.SET_FACILITIES:
            return {
                ...state,
                facilities: action.val
            }

        case actionTypes.ADD_FACILITY:
            return {
                ...state,
                facilities: [action.val, ...state.facilities]
            }   

        case actionTypes.SET_JOURNALS:
            return {
                ...state,
                journals: action.val
            }

        case actionTypes.ADD_JOURNAL:
            return {
                ...state,
                journals: [action.val, ...state.journals]
            }
    }
    return state
}

export default reducer