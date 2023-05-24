Title: Simple Complex Number Algebra
Author: Jay Ess
Date: 2019-07-19 16:00
Tags: complex numbers, math, algebra, complex conjugate, imaginary numbers
Status: published


I decided to start reviewing some of my controls courses from university to
brush up on the fundamentals. While reviewing, I had an "Oh shit" moment when I
realized that I've forgotten some *really* basic math. Namely, working with
complex numbers. I decided to write this article so that I can easily find a
reference if I ever need it (hopefully it helps you too). (BIG thanks to Dr.
Tabrizi for putting together notes that are very comprehensible.)

## General Form of a Complex Number

<!-- Check the link -->
According to Wikipedia, [complex numbers] are

> [...] regarded in the mathematical sciences as just as "real" as the real
numbers, and are fundamental in many aspects of the scientific description of
the natural world.

Complex numbers can be written in two forms: rectangular and polar. They live
in the 2-dimensional complex plane with the horizontal axis is called the
"real" axis while the vertical axis is called the "imaginary" axis. The figure
below shows this nicely.

<figure class="image">
  <img src="{static}/img/complex_number_rect.svg"
       class="img-responsive align-center"
       alt="A complex number"
       title="A complex number"
       class="center responsive-image">
  <figcaption>
    A complex number z, as a point (red) and its position vector (blue).
    Image courtesy of <cite>
    <a href="https://en.wikipedia.org/wiki/Complex_number#/media/File:A_plus_bi.svg">
        LasinIkamusumeFan
    </a> under the
    <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">
        Creative Commons 4.0 License
    </a>.
    </cite>
  </figcaption>
</figure>

**Note** that in electrical engineering $j$ denotes the imaginary number/axis
so as to avoid confusion with the time-varying current $i$. This is the
notation that I'll be using throughout this article. If this confuses you,
then just replace every instance of $j$ with $i$.

### Rectangular Form

The rectangular form of a complex number is as follows

$$
z = a + jb.
$$

The letters $a$ and $b$ are referred to as the real and imaginary components of
the complex number $z$, respectively. In the figure above, $a$ is the
horizontal axis while $b$ is the vertical axis.

You may sometimes see $Re(z)$ and $Im(z)$ to mean the real and imaginary
components of the complex number $z$, respectively.

### Polar Form

The rectangular form of a complex number is as follows

$$
z = \|r\| e^{j\phi}.
$$

and is shown in the figure below.

<figure class="image">
  <img src="{static}/img/complex_number_polar_opt.svg"
       alt="A complex number"
       title="A complex number"
       class="center responsive-image">
  <figcaption>
    A complex number z, as a point (red) and its position vector (blue).
    Image courtesy of <cite>
    <a href="https://en.wikipedia.org/wiki/File:Complex_number_illustration_modarg.svg">
        Oleg Alexandrov
    </a> under the
    <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">
        Creative Commons 3.0 License
    </a>.
    </cite>
  </figcaption>
</figure>


$\|r\|$ is the *magnitude* and $\phi$ is the *phase angle* of the complex
number $z$, respectively. To help explain this, you can think of a complex
number as a vector in the complex plane with the magnitude being the length of
the vector and the phase angle the direction.

## Converting Between Forms

It's often useful (or necessary) to convert from one form to another to either
get information (such as magnitude) or to aid in calculations (adding complex
numbers is easier when both numbers are in rectangular form).

### Converting From Polar to Rectangular Form

To convert from polar to rectangular form, we will use Euler's formula and
multiply the result by the magnitude $\|r\|$.

<div class="math-block">
$$
\begin{align}
    z &= \|r\|\left(\cos \phi + j \sin \phi \right) \nonumber \\
      &= a + jb \label{eq:polar_to_rect}
\end{align}
$$
</div>

*Interesting side note: Euler made discoveries in so many different
fields that it started getting to the point that there were too many
discoveries/theorems being named after him, so*

> [in] an effort to avoid naming everything after Euler, some discoveries and
theorems are attributed to the first person to have proved them *after* Euler.
<sup>[1](#refs)<sup>

#### Example

It usually helps to make everything clear by having examples. So, let's see how
the conversion from polar to rectangular form actually works.

Let $z = 2 \sqrt{2} \, e^{j \, \frac{\pi}{4}}$.

The first thing that we have to do is identify the magnitude and phase angle.
Here, the magnitude is $\|r\| = 2 \sqrt{2}$ and the phase angle is
$\phi = \frac{\pi}{4}$. Now, it's just a matter of plugging everything in to
Equation $\ref{eq:polar_to_rect}$.

<div class="math-block">
$$
\begin{align*}
    a + jb &= \|r\| \left(\cos \phi + j \sin \phi \right) \\
    &= 2 \sqrt{2} \left(\cos \frac{\pi}{4} + j \sin \frac{\pi}{4} \right) \\
    &= 2 \sqrt{2} \left(\frac{\sqrt{2}}{2} + j \frac{\sqrt{2}}{2} \right) \\
    &= \boxed{2 + j2}
\end{align*}
$$
</div>

### Converting from Rectangular to Polar Form

To convert from rectangular to polar form, we will need to find the magnitude
and the phase angle of the complex number. To find the magnitude of $z$, we
will use the formula for the [Euclidean norm] (also known as the modulus, or
norm)

<div class="math-block">
$$
\begin{equation}
    \|r\| = \sqrt{a^2 + b^2}.
    \label{eq:euclidean_norm}
\end{equation}
$$
</div>

Finding the phase angle can be a little bit tricky (which is what prompted me
to write this article). Although you may be tempted to immediately use
$\phi = \tan^{-1}{\frac{b}{a}}$, you will quickly run into trouble. This
equation only works for the *first* quadrant. Therefore, you must determine
which quadrant the complex number is in, which is the tricky part. Luckily, the
table below shows you exactly how to find this out.

<!--
    IMPORTANT! Don't remove the space in front of the div! It'll cause MathJax
    to stop rendering in the table
-->
<div class="table-container">
 <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>Conditions</th>
        <th>Quadrant</th>
        <th>Range of \(\phi\)</th>
      </tr>
    </thead>
      <tbody>
        <tr>
          <td>\(a \gt 0\,\) and \(b \gt 0\)</td>
          <td>1<sup>st</sup> quadrant</td>
          <td>0° \(\lt \phi \lt\) 90°</td>
        </tr>
        <tr>
          <td>\(a \gt 0\,\) and \(b \gt 0\)</td>
          <td>2<sup>nd</sup> quadrant</td>
          <td>90° \(\lt \phi \lt\) 180°</td>
        </tr>
        <tr>
          <td>\(a \gt 0\,\) and \(b \gt 0\)</td>
          <td>3<sup>rd</sup> quadrant</td>
          <td>180° \(\lt \phi \lt\) 270°</td>
        </tr>
        <tr>
          <td>a \(\gt 0\,\) and b \(\gt 0\)</td>
          <td>4<sup>th</sup> quadrant</td>
          <td>270° \(\lt \phi \lt\) 360°</td>
        </tr>
      </tbody>
  </table>
</div>
Once you know what quadrant the complex number is in, then finding the phase
angle is pretty straightforward. Below I've created another table that lists
the formula that you need to use to find the (numerical) phase angle dependent
on the quadrant.

<!--
    IMPORTANT! Don't remove the space in front of the table! It'll cause MathJax
    to stop rendering in the table
-->
<div class="table-container">
 <table class="table is-hoverable">
    <thead>
      <tr>
        <th>Quadrant</th>
        <th>Formula</th>
      </tr>
    </thead>
      <tbody>
        <tr>
          <td>1<sup>st</sup> quadrant</td>
          <td>\(\phi = \tan^{-1}{\frac{b}{a}}\)</td>
        </tr>
        <tr>
          <td>2<sup>nd</sup> quadrant</td>
          <td>\(\phi = \pi - \tan^{-1}{\frac{\left|b\right|}{a}}\)</td>
        </tr>
        <tr>
          <td>3<sup>rd</sup> quadrant</td>
          <td>\(\phi = \pi + \tan^{-1}{\left|\frac{b}{a}\right|}\)</td>
        </tr>
        <tr>
          <td>4<sup>th</sup> quadrant</td>
          <td>\(\phi = -\tan^{-1}{\frac{\left|b\right|}{a}}\)</td>
        </tr>
      </tbody>
  </table>
</div>

#### Example

Let's convert $z = \pm 3 \pm j3$ to polar form.

##### First Quadrant

Let's first do $z = 3 + j3$. It's very simple to find the magnitude so let's do
that first.

<div class="math-block">
$$
\begin{align*}
    \|r\| &= \sqrt{a^2 + b^2} \\
          &= \sqrt{3^2 + 3^2} \\
          &= \sqrt{18} \\
          &= \boxed{3 \sqrt{2}}
\end{align*}
$$
</div>

We can tell that this number is in the first quadrant because both of the real
and imaginary components are positive. Therefore, according to the above
[table](#quadrants), we will use $\phi = \tan^{-1}{\frac{b}{a}}$ to find the phase
angle.

<div class="math-block">
$$
\begin{align*}
    \phi &= \tan^{-1}{\frac{b}{a}} \\
         &= \tan^{-1}{\frac{3}{3}} \\
         &= \boxed{\frac{\pi}{4}}
\end{align*}
$$
</div>

Combining the magnitude and phase leaves us with the polar form

<div class="math-block">
$$
\boxed{z = 3 \sqrt{2} \, e \, ^{j \frac{\pi}{4}}}
$$
</div>

##### Second Quadrant

Now, let's do $z = -3 + j3$. Again, we're going to find the magnitude first.

<div class="math-block">
$$
\begin{align*}
    \|r\| &= \sqrt{\left(-3 \right)^2 + 3^2} \\
          &= \sqrt{18} \\
          &= \boxed{3 \sqrt{2}}
\end{align*}
$$
</div>

We can tell that this number is in the second quadrant because the real
component is negative while the imaginary component is positive.
Therefore, according to the above [table](#quadrants), we will use
$\phi = \pi - \tan^{-1}{\frac{b}{\left|a\right|}}$ to find the phase angle.

<div class="math-block">
$$
\begin{align*}
    \phi &= \pi - \tan^{-1}{\frac{b}{\left|a\right|}} \\
         &= \pi - \tan^{-1}{\frac{3}{\left|-3\right|}} \\
         &= \pi - \frac{\pi}{4} \\
         &= \boxed{\frac{3\pi}{4}}
\end{align*}
$$
</div>

Combining the magnitude and phase leaves us with the polar form

<div class="math-block">
$$
\boxed{z = 3 \sqrt{2} \, e \, ^{j \frac{3\pi}{4}}}
$$
</div>

##### Third Quadrant

Now, let's do $z = -3 - j3$. Again, we're going to find the magnitude first.

<div class="math-block">
$$
\begin{align*}
    \|r\| &= \sqrt{\left(-3 \right)^2 + \left(-3 \right)^2} \\
          &= \sqrt{18} \\
          &= \boxed{3 \sqrt{2}}
\end{align*}
$$
</div>

We can tell that this number is in the third quadrant because both of the real
and imaginary components are negative. Therefore, according to the above
[table](#quadrants), we will use $\phi = \pi + \tan^{-1}{\left|\frac{b}{a}\right|}$
to find the phase angle.

<div class="math-block">
$$
\begin{align*}
    \phi &= \pi + \tan^{-1}{\left|\frac{b}{a}\right|} \\
         &= \pi + \tan^{-1}{\left|\frac{-3}{-3}\right|} \\
         &= \pi + \frac{\pi}{4} \\
         &= \boxed{\frac{5\pi}{4}}
\end{align*}
$$
</div>

Combining the magnitude and phase leaves us with the polar form

<div class="math-block">
$$
\boxed{z = 3 \sqrt{2} \, e \, ^{j \frac{5\pi}{4}}}
$$
</div>

##### Fourth Quadrant

Now, let's do $z = 3 - j3$. Again, we're going to find the magnitude first.

<div class="math-block">
$$
\begin{align*}
    \|r\| &= \sqrt{3^2 + \left(-3 \right)^2} \\
          &= \sqrt{18} \\
          &= \boxed{3 \sqrt{2}}
\end{align*}
$$
</div>

We can tell that this number is in the fourth quadrant because real component
is positive and the imaginary component is negative. Therefore, according to
the above [table](#quadrants), we will use
$\phi = -\tan^{-1}{\frac{\left|b\right|}{a}}$ to find the phase angle.

<div class="math-block">
$$
\begin{align*}
    \phi &= -\tan^{-1}{\frac{\left|b\right|}{a}} \\
         &= -\tan^{-1}{\frac{\left|-3\right|}{-3}} \\
         &= \boxed{-\frac{\pi}{4}}
\end{align*}
$$
</div>

Combining the magnitude and phase leaves us with the polar form

<div class="math-block">
$$
\boxed{z = 3 \sqrt{2} \, e \, ^{-j \frac{\pi}{4}}}
$$
</div>

## Arithmetic Operations

Now that we know how to convert from one form to another, we can perform
arithmetic operations with complex numbers.

### Addition

It's easiest to add and subtract complex numbers when they're in *rectangular*
form. So, the first thing to do is to convert all of the complex numbers to
rectangular form if necessary. Then, you simply add the components together.

For example, suppose that you have two complex numbers $z_1 = a_1 + jb_1$ and
$z_2 = a_2 + jb_2$. To get the new number $z_3 = z_1 + z_2$, you would do the
following

<div class="math-block">
$$
\begin{align*}
    z_3 &= z_1 + z_2 \\
        &= \left(a_1 + jb_1 \right) + \left(a_2 + jb_2 \right) \\
        &= \left(a_1 + a_2 \right) + j\left(b_1 + b_2 \right) \\
        &= a_3 + jb_3.
\end{align*}
$$
</div>

### Subtraction

Subtraction works similarly to addition (just like with real numbers). First,
we should make sure that all complex numbers are in rectangular form. Then, we
can simply subtract the components of each complex number.

For example, suppose that you have two complex numbers $z_1 = a_1 + jb_1$ and
$z_2 = a_2 + jb_2$. To get the new number $z_3 = z_1 + z_2$ you would do the
following

<div class="math-block">
$$
\begin{align*}
    z_3 &= z_1 - z_2 \\
        &= \left(a_1 + jb_1 \right) - \left(a_2 + jb_2 \right) \\
        &= \left(a_1 - a_2 \right) + j\left(b_1 - b_2 \right) \\
        &= a_3 + jb_3.
\end{align*}
$$
</div>

### Multiplication

In contrast to addition and subtraction, multiplication of complex numbers is
more easily performed when all complex numbers are in *polar* form.

The first thing to do when multiplying complex numbers is to make sure to
convert all of them into polar form. Next, we multiply the magnitudes and then
add the phase angles.

For example, suppose that we have two complex numbers $z_1 = r_1 \, e^{j \phi_1}$
and $z_2 = r_2 \, e^{j \phi_2}$ and we want to multiply them. To multiply
them, you would do the following

<div class="math-block">
$$
\begin{align}
    z_3 &= z_1 \cdot z_2 \\
        &= \left(r_1 \, e^{j \phi_1} \right) \cdot \left(r_2 \, e^{j \phi_2} \right) \\
        &= \left(r_1 \cdot r_2 \right) \, e^{\left(\phi_1 + \phi_2 \right)}.
\end{align}
$$
</div>

### Division

Like multiplication, division of complex numbers is easiest when all of the
complex numbers are in polar form. So, first convert all of the complex numbers
to polar form, then divide the magnitudes and *subtract* the phase angles.

For example, suppose that we have two complex numbers $z_1 = r_1 \, e^{j \phi_1}$
and $z_2 = r_2 \, e^{j \phi_2}$ and we want to multiply them. To multiply
them, you would do the following

<div class="math-block">
$$
\begin{align}
    z_3 &= \frac{z_1}{z_2} \\
        &= \frac{r_1 \, e^{j \phi_1}}{r_2 \, e^{j \phi_2}} \\
        &= \frac{r_1}{r_2} \, e^{\left(\phi_1 - \phi_2 \right)}.
\end{align}
$$
</div>

## Complex Conjugate

Every complex number has a complex conjugate and that conjugate is found by
switching the signs of the imaginary component. For example, if we have a
complex number $z = a + jb$ then its complex conjugate is $z^* = a - jb$.
Notice how only the sign of the imaginary component became negative and the
real component's sign remained the same. Because we're just switching signs of
the imaginary component, you can think of the complex conjugate as a reflection
about the real axis. Also note the $^*$ next to the variable $z$. This is one
of the notations to denote a complex conjugate.

Complex conjugates are very important in math, physics, and engineering and you
should definitely read about the [importance of complex conjugates].

## Conclusion

In this article, we learned about the different forms of a complex number and
how to convert between them. We also learned how to add, subtract, multiply,
and divide complex numbers. Finally, we learned how to find the complex
conjugate of a complex number as well. If you have any comments or questions,
please comment below.

## <a name="refs"></a>References

1. [Wikipedia - List of things named after Leonhard Euler]


<!-- Links -->
[complex numbers]: https://en.wikipedia.org/wiki/Complex_number "Wikipedia - Complex Numbers"
[Wikipedia - List of things named after Leonhard Euler]: https://en.wikipedia.org/wiki/List_of_things_named_after_Leonhard_Euler "Wikipedia - List of things named after Leonhard Euler"
[importance of complex conjugates]: https://www.allaboutcircuits.com/technical-articles/importance-of-complex-conjugates/ "All About Circuits - The Importance of Complex Conjugates"
