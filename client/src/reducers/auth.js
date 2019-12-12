export default (state = {}, action) => {
  switch (action.type) {
    case 'SIGNUP_SUCCESS':
      return {
        user: action.payload
      };
    case 'SIGNUP_FAIL':
      return {
        errors: action.payload
      };

    case 'LOGIN_SUCCESS':
      return {
        user: action.payload
      };
    case 'LOGIN_FAIL':
      return {
        errors: action.payload
      };
    case 'LOGOUT':
      return {};
    default:
      return state;
  }
};
