 class SpecialStructure {
     int * values;
     SpecialStructure(int N) {..}
     int get(int row, int col) {..}
     int set(int row, int col, int val) {..}
};



void SpecialStructure::SpecialStructure(int N){
	values=new int[N*N];
}

int SpecialStructure::set(int row,int col,int val){
	int N=sizeof(values)/sizeof(int);
	if (row>=N){
		row=2*(N-1)-row;
	}
	if (col>row){
		throw("not allowed");
		return 0;
	}
	else{
		row+=(row*row);
		row=row/2;
		row+=col;
		values[row]=val;
	}
	return 1;
}


int SpecialStructure::get(int row,int col){
	int N=sizeof(values)/sizeof(int);
	if (row>=N){
		row=2*(N-1)-row;
	}
	if (col>row){
		throw("not allowed");
		return 0;
	}
	else{
		row+=row*row;
		row=row/2;
		row+=col;
		return values[row];
	}
	return 1;


}