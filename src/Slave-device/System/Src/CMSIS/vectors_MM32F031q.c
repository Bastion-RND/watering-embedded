/*
 * This file is part of the µOS++ distribution.
 *   (https://github.com/micro-os-plus)
 * Copyright (c) 2014 Liviu Ionescu.
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom
 * the Software is furnished to do so, subject to the following
 * conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 */

// ----------------------------------------------------------------------------

#include "cortexm/ExceptionHandlers.h"

// ----------------------------------------------------------------------------

void __attribute__((weak))
Default_Handler(void);

// Forward declaration of the specific IRQ handlers. These are aliased
// to the Default_Handler, which is a 'forever' loop. When the application
// defines a handler (with the same name), this will automatically take
// precedence over these weak definitions
//

void __attribute__ ((weak, alias ("Default_Handler")))
WWDG_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
PVD_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
FLASH_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
RCC_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
EXTI0_1_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
EXTI2_3_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
EXTI4_15_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
DMA1_Channel1_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
DMA1_Channel2_3_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
DMA1_Channel4_5_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
ADC_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
TIM1_BRK_UP_TRG_COM_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
TIM1_CC_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
TIM2_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
TIM3_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
TIM14_0_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
TIM16_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
TIM17_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
I2C1_EV_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
SPI1_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
SPI2_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
UART1_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
UART2_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
CAN1_TX_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
USB_FS_WKUP_IRQHandler(void);

void __attribute__ ((weak, alias ("Default_Handler")))
Dummy_Handler(void);


// ----------------------------------------------------------------------------

extern unsigned int _estack;

typedef void
(* const pHandler)(void);

// ----------------------------------------------------------------------------

// The vector table.
// This relies on the linker script to place at correct location in memory.

__attribute__ ((section(".isr_vector"),used))
pHandler __isr_vectors[] =
  { //
    (pHandler) &_estack,                          // The initial stack pointer
    Reset_Handler,                            // The reset handler

    NMI_Handler,                              // The NMI handler
    HardFault_Handler,                        // The hard fault handler

#if defined(__ARM_ARCH_7M__) || defined(__ARM_ARCH_7EM__)
    MemManage_Handler,                        // The MPU fault handler
    BusFault_Handler,// The bus fault handler
    UsageFault_Handler,// The usage fault handler
#else
    0, 0, 0,				  // Reserved
#endif
    0,                                        // Reserved
    0,                                        // Reserved
    0,                                        // Reserved
    0,                                        // Reserved
    SVC_Handler,                              // SVCall handler
#if defined(__ARM_ARCH_7M__) || defined(__ARM_ARCH_7EM__)
    DebugMon_Handler,                         // Debug monitor handler
#else
    0,					  // Reserved
#endif
    0,                                        // Reserved
    PendSV_Handler,                           // The PendSV handler
    SysTick_Handler,                          // The SysTick handler

    // ----------------------------------------------------------------------
    // MM32F031q vectors
    WWDG_IRQHandler,
    PVD_IRQHandler,
    Dummy_Handler, /* Reserved */
    FLASH_IRQHandler,
    RCC_IRQHandler,
    EXTI0_1_IRQHandler,
    EXTI2_3_IRQHandler,
    EXTI4_15_IRQHandler,
    Dummy_Handler, /* Reserved */
    DMA1_Channel1_IRQHandler,
    DMA1_Channel2_3_IRQHandler,
    DMA1_Channel4_5_IRQHandler,
    ADC_IRQHandler,
    TIM1_BRK_UP_TRG_COM_IRQHandler,
    TIM1_CC_IRQHandler,
    TIM2_IRQHandler,
    TIM3_IRQHandler,
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    TIM14_0_IRQHandler,
    Dummy_Handler, /* Reserved */
    TIM16_IRQHandler,
    TIM17_IRQHandler,
    I2C1_EV_IRQHandler,
    Dummy_Handler, /* Reserved */
    SPI1_IRQHandler,
    SPI2_IRQHandler,
    UART1_IRQHandler,
    UART2_IRQHandler,
    Dummy_Handler, /* Reserved */
    CAN1_TX_IRQHandler,
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    Dummy_Handler, /* Reserved */
    USB_FS_WKUP_IRQHandler,
  };

// ----------------------------------------------------------------------------

// Processor ends up here if an unexpected interrupt occurs or a specific
// handler is not present in the application code.

void __attribute__ ((section(".after_vectors")))
Default_Handler(void)
{
  while (1)
  {
  }
}

// ----------------------------------------------------------------------------
