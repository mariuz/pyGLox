uniform float time;
uniform float beat;

void main(void)
{
	gl_FrontColor = gl_Color;
	gl_TexCoord[0] = gl_MultiTexCoord0;
	
	vec4 vt = gl_Vertex;

	float d = gl_Normal.z;
	float i = gl_Normal.y;
	if(i > 0)
	{
		if(d<0)
		{
			vt.x += cos(time + i * .2) * i * 0.02 * gl_Normal.x / 2.0;
			vt.z -= sin(time + i * .2) * i * 0.02 * gl_Normal.x / 2.0;
		}
		else
		{
			vt.x -= cos(time + i * .2) * i * 0.02 * gl_Normal.x / 2.0;
			vt.z += sin(time + i * .2) * i * 0.02 * gl_Normal.x / 2.0;
		}
		
		//vt.x += sin(time*0.1 * vt.y) * vt.y / 45;
		//vt.z += cos(time*0.01);
		//vt.x += sin(beat / 32);
		//vt.z += cos(beat / 32);
	}
		
	gl_Position = gl_ModelViewProjectionMatrix * vt;
	//gl_Position = ftransform();	
}
