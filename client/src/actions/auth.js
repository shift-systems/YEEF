import actionTypes from './actionTypes';

export const login = uid => ({
  type: 'LOGIN',
  uid
});

export const logout = () => ({
  type: 'LOGOUT'
});

export const signupSuccess = response => ({
  type: actionTypes.SIGNUP_SUCCESS,
  payload: response
});

export const startSignup = data => {
  return dispatch => {
    fetch(`http://127.0.0.1:8000/api/v1.0/register`, {
      method: 'POST',
      headers: {
        'content-type': 'application/json'
      },
      CORS: 'no-cors',
      body: JSON.stringify({ user: data })
    })
      .then(res => res.json())
      .then(response => {
        if (response.user.id) {
          dispatch(signupSuccess(response.user));
        } else {
          dispatch(signupFail(response.user));
        }
      });
  };
};

// export const startLogin = () => {
//   return () => {
//     return firebase.auth().signInWithPopup(googleAuthProvider);
//   };
// };

export const startLogin = data => {
  return dispatch => {
    fetch(`http://127.0.0.1:8000/api/v1.0/login`, {
      method: 'POST',
      headers: {
        'content-type': 'application/json'
      },
      CORS: 'no-cors',
      body: JSON.stringify({ user: data })
    })
      .then(res => res.json())
      .then(response => {
        if (response.user.email) {
          dispatch(signupSuccess(response.user));
        } else {
          dispatch(signupFail(response.user));
        }
      });
  };
};

export const startLogout = () => {
  return () => {
    return firebase.auth().signOut();
  };
};
