import React, { useState, useEffect } from 'react';
import { Fade } from "@material-ui/core";
import MaterialTable from 'material-table';
import { makeStyles } from '@material-ui/core/styles';

import UsuariosService from './services/UsuariosService';

const  usuariosService  =  new  UsuariosService();


const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        width: '70%',
        margin: 'auto',
        marginTop: 20,
        boxShadow: '0px 0px 8px 0px rgba(0,0,0,0.4)'
    }
}));

function User(props) {
    const classes = useStyles();
    const [checked, setChecked] = useState(false);
    const [tableData, setTableData] = useState([]);


    let config = {
        columns: [
            { title: 'id1', field: 'id' },
            { title: 'rol', field: 'rol' },
            { title: 'correo', field: 'correo'},
            { title: 'contrasena', field: 'contrasena'},
            { title: 'paterno', field: 'paterno'},
            { title: 'materno', field: 'materno'},
            { title: 'nombre', field: 'nombre'},
            { title: 'nacimiento', field: 'nacimiento'},
            { title: 'telefono', field: 'telefono'},
            { title: 'domicilio', field: 'domicilio'},
        ],
        actions: [
            { icon: 'create', tooltip: 'Edit', onClick: (rowData) => alert('Edit')},
            { icon: 'lock', tooltip: 'Block', onClick: (rowData) => alert('Block')},
            { icon: 'delete', tooltip: 'Delete', onClick: (rowData) => alert('Delete')},
            { icon: 'visibility', tooltip: 'Access', onClick: (rowData) => alert('Access')},
            { icon: "add_box", tooltip: "Add", position: "toolbar", onClick: () => { alert('Add') } }
        ],
        options: {
            headerStyle: { color: 'rgba(0, 0, 0, 0.54)' },
            actionsColumnIndex: -1,
            exportButton: true,
            paging: true,
            pageSize: 10,
            pageSizeOptions: [],
            paginationType: 'normal'
        },
        localization: {
            body: { 
                emptyDataSourceMessage: 'No data' 
            },
            toolbar: { 
                searchTooltip: 'Search',
                searchPlaceholder: 'Search',
                exportTitle: 'Export'
            },
            pagination: {  
                labelRowsSelect: 'Lines',
                labelDisplayedRows: '{from} to {to} for {count} itens',
                firstTooltip: 'First',
                previousTooltip: 'Previous',
                nextTooltip: 'Next',
                lastTooltip: 'Last'
            },
            header: {
                actions: 'Actions'
            }
        }
    }

    useEffect(() => {
        setChecked(prev => !prev);

        async function loadUsers() {
            const response = await usuariosService.getUsuarios();
            setTableData(response.data);
        }

        loadUsers();
    }, [])


    return (
        <>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
            <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons" />

            <Fade in={checked} style={{ transitionDelay: checked ? '300ms' : '0ms' }}>
                <div className={classes.root}>
                    <MaterialTable editable={config.editable} options={config.options} localization={config.localization} title="Usuários" columns={config.columns} data={tableData} actions={config.actions}></MaterialTable>
                </div>
            </Fade>
        </>
    );
}

export default User;