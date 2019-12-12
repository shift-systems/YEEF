import actionTypes from './actionTypes';

export const savingSuccess = saving => ({
  type: actionTypes.SAVE_SUCCESS,
  payload: saving
});

export const savingFail = error => ({
  type: actionTypes.SAVE_FAIL,
  payload: error
});

export const startSaving = savings => {
  return dispatch => {
    const token = localStorage.getItem('yeef_token');

    fetch(`http://127.0.0.1:8000/api/v1.0/savings`, {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        Authorization: `Token ${token}`
      },
      body: JSON.stringify({ savings })
    })
      .then(res => res.json())
      .then(response => {
        if (response.savings.id) {
          dispatch(savingSuccess(response.savings));
        } else {
          dispatch(savingFail(response.savings));
        }
      })
      .catch(err => {
        console.log(err, 'This error is from saving action');
      });
  };
};

export const startGetSavings = (path = 'savings') => {
  return dispatch => {
    const token = localStorage.getItem('yeef_token');

    fetch(`http://127.0.0.1:8000/api/v1.0/${path}`, {
      method: 'GET',
      headers: {
        'content-type': 'application/json',
        Authorization: `Token ${token}`
      }
      // body: JSON.stringify({ savings })
    })
      .then(res => res.json())
      .then(response => {
        console.log(response);
        if (response.length !== 0) {
          dispatch(savingSuccess(response.savings));
        } else {
          dispatch(savingFail(response.savings));
        }
      })
      .catch(err => {
        console.log(err, 'This error is from get saving action');
      });
  };
};
