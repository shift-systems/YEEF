import React, { Component } from 'react';
import { connect } from 'react-redux';
import SavingsForm from '../components/SavingsForm';
import moment from 'moment';
import { startSaving } from '../actions/savings';

export class SavingsPage extends Component {
  constructor(props) {
    super(props);

    this.state = {
      comment: '',
      amount: 0.0,
      savedOn: moment(),
      calendarFocused: false,
      error: ''
    };
  }

  onCommentChange = e => {
    const comment = e.target.value;
    this.setState(() => ({ comment }));
  };
  onAmountChange = e => {
    const amount = e.target.value;

    if (!amount || amount.match(/^\d{1,}(\.\d{0,2})?$/)) {
      this.setState(() => ({ amount }));
    }
  };
  onDateChange = createdAt => {
    if (createdAt) {
      this.setState(() => ({ createdAt }));
    }
  };

  onFocusChange = ({ focused }) => {
    this.setState(() => ({ calendarFocused: focused }));
  };
  handleSubmit = e => {
    e.preventDefault();

    if (!this.state.amount) {
      this.setState(() => ({
        error: 'Please provide amount.'
      }));
    } else {
      this.setState(() => ({ error: '' }));
      this.props.startSaving({
        amount: parseFloat(this.state.amount),
        savedOn: this.state.savedOn.valueOf(),
        comment: this.state.comment
      });

      console.log(this.state);
    }
  };

  componentWillReceiveProps(props) {
    const { saving, errors, history } = props;
    if (saving.length !== 0) {
      history.push('/dashboard');
    } else if (errors) {
      const error = `Transaction failed, ${errors.reason
        .toLowerCase()
        .replace(/[^a-zA-Z ]/g, ' ')}`;
      this.setState({
        error
      });
    }

    console.log(this.state);
  }
  render() {
    return (
      <div>
        <div className="page-header">
          <div className="content-container">
            <h1 className="page-header__title">Grow your savings</h1>
          </div>
        </div>
        <div className="content-container">
          <SavingsForm
            handleSubmit={this.handleSubmit}
            onCommentChange={this.onCommentChange}
            onAmountChange={this.onAmountChange}
            onDateChange={this.onDateChange}
            onFocusChange={this.onFocusChange}
            state={this.state}
          />
        </div>
      </div>
    );
  }
}

const mapDispatchToProps = dispatch => ({
  startSaving: saving => dispatch(startSaving(saving))
});

const mapStateToProps = state => {
  console.log(state, 'state');
  return {
    saving: state.savings,
    errors: state.saveError.errors
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SavingsPage);
