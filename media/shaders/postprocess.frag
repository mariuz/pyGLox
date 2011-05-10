uniform sampler2D texture;
uniform sampler2D texture2;
uniform float time;
uniform float rt_w;
uniform float rt_h;
uniform float mode;

// Original Source (of some): http://www.geeks3d.com/geexlab/shader_library.php

void main(void)
{
    vec2 uv = gl_TexCoord[0].st;
    vec4 color = texture2D(texture, uv);
	
	if(mode == 1)
	{
		float g = dot(color.rgb, vec3(0.299, 0.587, 0.114));
		color = vec4(g,g,g,1);
	}
	else if(mode == 2)
	{
		float g = dot(color.rgb, vec3(0.299, 0.587, 0.114));
		color = vec4(g * vec3(1.2, 1.0, 0.8), 1.0);
	}
	else if(mode == 3)
	{
		float x = sin(time * 0.28);
		if(x < 0.28) x = 0.28;
		
		vec2 lensRadius = vec2(x, 0.18);
		float dist = distance(uv, vec2(0.5,0.5));
		color.rgb *= smoothstep(lensRadius.x, lensRadius.y, dist);
	}
	else
	{		
		/*float dx = 10*(1./rt_w);
    	float dy = 10*(1./rt_h);
	    vec2 coord = vec2(dx*floor(uv.x/dx),dy*floor(uv.y/dy));
    	color = texture2D(texture, coord);*/
	    
	    vec3 colors[3];
    	colors[0] = vec3(0.,0.,1.);
    	colors[1] = vec3(1.,1.,0.);
    	colors[2] = vec3(1.,0.,0.);
    	
    	float lum = (color.r+color.g+color.b)/3.;
    	int ix = ( lum < 0.5 ) ? 0 : 1;
    	
    	color = vec4(mix(colors[ix],colors[ix+1],(lum-float(ix)*0.5)/0.5),1);
	}
	
	gl_FragColor = color;
}
