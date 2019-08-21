import React, { Component } from 'react';

class Login extends Component {
    // state = {}

    // variables
    usuarioRef = React.createRef();
    passwordRef = React.createRef();

    // funciones
    loginUsuario = (e) => {

        e.preventDefault();
        console.log(this.usuarioRef.current.value);
        console.log(this.passwordRef.current.value);
    }

    componentDidMount() {
        fetch('http://localhost:8000/api')
            .then(res => res.json())
            .then(json => {
                this.setState({
                    isLoaded: true,
                    items: json,
                })
            })

        console.log(this.state);
    }

    render() {
        return (
            <form onSubmit={this.loginUsuario} className="login-form">
                <div className="card mb-0">
                    <div className="card-body">
                        <div className="text-center mb-3">
                            <i className="icon-reading icon-2x text-slate-300 border-slate-300 border-3 rounded-round p-3 mb-3 mt-1"></i>
                            <h5 className="mb-0">Acceso a Linker</h5>
                            <span className="d-block text-muted">Ingrese su usuario y password</span>
                        </div>

                        <div className="form-group form-group-feedback form-group-feedback-left">
                            <input ref={this.usuarioRef} type="text" className="form-control" placeholder="Usuario" />
                            <div className="form-control-feedback">
                                <i className="icon-user text-muted"></i>
                            </div>
                        </div>

                        <div className="form-group form-group-feedback form-group-feedback-left">
                            <input ref={this.passwordRef} type="password" className="form-control" placeholder="Password" />
                            <div className="form-control-feedback">
                                <i className="icon-lock2 text-muted"></i>
                            </div>
                        </div>

                        <div className="form-group">
                            <button type="submit" className="btn btn-primary btn-block">
                                Ingresar
                                <i className="icon-circle-right2 ml-2"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </form>

        );
    }
}

export default Login;