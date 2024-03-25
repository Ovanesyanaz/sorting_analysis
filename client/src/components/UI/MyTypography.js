import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

export const MyTypography = (props) => {
  return (
    <Typography variant={props.h} gutterBottom>{props.state}</Typography>
  );
}