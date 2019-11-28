export default (state = {}, action) => {
  switch (action.type) {
    case 'SIGNUP_SUCCESS':
      return {
        user: action.user
      };
    case 'SIGNUP_FAIL':
      return {
        errors: action.user
      };

    case 'LOGIN_SUCCESS':
      return {
        user: action.user
      };
    case 'LOGIN_FAIL':
      return {
        errors: action.user
      };
    case 'LOGOUT':
      return {};
    default:
      return state;
  }
};
