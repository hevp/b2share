import React from 'react';


export function Wait(props) {
    return (
        <div> Loading... </div>
    );
}


export function Err(props) {
    const error = props.err;
    let msg = error.text;
    if (error.data && error.data.message) {
        msg = error.data.message;
    }
    return (
        <div className={"alert alert-danger"}>
            <h3>Error <span>{error.code}</span></h3>
            <span>{msg}</span>
        </div>
    );
}
