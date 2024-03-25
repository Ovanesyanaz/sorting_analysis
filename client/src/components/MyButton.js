import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

export const MyButton = (props) => {
  return (
    <Stack spacing={2} direction="row">
      <Button variant="contained" onClick={props.onclk} disabled={props.disabled}>click</Button>
    </Stack>
  );
}