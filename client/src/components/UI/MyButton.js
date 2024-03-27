import * as React from 'react';
import Button from '@mui/material/Button';

export const MyButton = (props) => {
  return (
      <Button sx={{ minWidth: "100%",maxWidth: "100%"}} variant="contained" onClick={props.onclk} disabled={props.disabled}>{props.children}</Button>
  );
}