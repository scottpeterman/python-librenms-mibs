# SNMP MIB module (GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\delta\GLOBAL-REG
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:20 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

globalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Delta_ObjectIdentity = ObjectIdentity
delta = _Delta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246)
)
_Root_ObjectIdentity = ObjectIdentity
root = _Root_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2)
)
_Reg_ObjectIdentity = ObjectIdentity
reg = _Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 1)
)
_ControllerReg_ObjectIdentity = ObjectIdentity
controllerReg = _ControllerReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 2)
)
_ControllerOrionReg_ObjectIdentity = ObjectIdentity
controllerOrionReg = _ControllerOrionReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    controllerOrionReg.setStatus("current")
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 2)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3)
)
_Controller_ObjectIdentity = ObjectIdentity
controller = _Controller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1)
)
_Orion_ObjectIdentity = ObjectIdentity
orion = _Orion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1)
)
_Caps_ObjectIdentity = ObjectIdentity
caps = _Caps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 4)
)
_Regs_ObjectIdentity = ObjectIdentity
regs = _Regs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 5)
)
_Expr_ObjectIdentity = ObjectIdentity
expr = _Expr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GLOBAL-REG",
    **{"delta": delta,
       "root": root,
       "reg": reg,
       "modules": modules,
       "globalRegModule": globalRegModule,
       "controllerReg": controllerReg,
       "controllerOrionReg": controllerOrionReg,
       "generic": generic,
       "products": products,
       "controller": controller,
       "orion": orion,
       "caps": caps,
       "regs": regs,
       "expr": expr}
)
