uniform float time;

void main(void)
{
	gl_FrontColor = gl_Color;
	gl_TexCoord[0] = gl_MultiTexCoord0;
	//gl_Position = ftransform();	
	gl_Position = vec4(gl_Vertex.xy, 0, 1);
}
