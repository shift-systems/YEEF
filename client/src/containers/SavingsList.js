import React, { Component } from 'react';
import { connect } from 'react-redux';
import SavingsListItem from '../components/SavingsListItem';
import selectExpenses from '../selectors/expenses';
import { startGetSavings } from '../actions/savings';

class SavingList extends Component {
  constructor(props) {
    super(props);

    this.sate = {};
  }

  componentDidMount(props) {
    this.props.startGetSavings();
  }

  render() {
    const props = this.props;
    return (
      <div className="content-container">
        <div className="list-header">
          <div className="show-for-mobile">Savings</div>
          <div className="show-for-desktop">Saving</div>
          <div className="show-for-desktop">Amount</div>
        </div>
        <div className="list-body">
          {props.savings.length === 0 ? (
            <div className="list-item list-item--message">
              <span>You haven't made savings yet</span>
            </div>
          ) : (
            props.savings.map(saving => {
              return <SavingsListItem key={saving.id} {...saving} />;
            })
          )}
        </div>
      </div>
    );
  }
}

const mapDispatchToProps = dispatch => ({
  startGetSavings: path => dispatch(startGetSavings(path))
});

const mapStateToProps = state => {
  return {
    savings: selectExpenses(state.savings, state.filters)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SavingList);
