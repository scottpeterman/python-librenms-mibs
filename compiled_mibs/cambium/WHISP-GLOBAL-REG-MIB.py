# SNMP MIB module (WHISP-GLOBAL-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cambium\WHISP-GLOBAL-REG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:31 2025
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

whispGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mot_ObjectIdentity = ObjectIdentity
mot = _Mot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161)
)
_WhispRoot_ObjectIdentity = ObjectIdentity
whispRoot = _WhispRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19)
)
_WhispReg_ObjectIdentity = ObjectIdentity
whispReg = _WhispReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1)
)
_WhispModules_ObjectIdentity = ObjectIdentity
whispModules = _WhispModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1)
)
_WhispGeneric_ObjectIdentity = ObjectIdentity
whispGeneric = _WhispGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 2)
)
_WhispProducts_ObjectIdentity = ObjectIdentity
whispProducts = _WhispProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3)
)
_WhispAps_ObjectIdentity = ObjectIdentity
whispAps = _WhispAps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1)
)
_WhispSm_ObjectIdentity = ObjectIdentity
whispSm = _WhispSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2)
)
_WhispBox_ObjectIdentity = ObjectIdentity
whispBox = _WhispBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3)
)
_WhispCMM_ObjectIdentity = ObjectIdentity
whispCMM = _WhispCMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4)
)
_WhispPlv_ObjectIdentity = ObjectIdentity
whispPlv = _WhispPlv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 5)
)
_WhispCMM4_ObjectIdentity = ObjectIdentity
whispCMM4 = _WhispCMM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 6)
)
_WhispPlvModem_ObjectIdentity = ObjectIdentity
whispPlvModem = _WhispPlvModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7)
)
_WhispPlvGateway_ObjectIdentity = ObjectIdentity
whispPlvGateway = _WhispPlvGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8)
)
_WhispPlvRepeater_ObjectIdentity = ObjectIdentity
whispPlvRepeater = _WhispPlvRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 9)
)
_WhispPlvBridge_ObjectIdentity = ObjectIdentity
whispPlvBridge = _WhispPlvBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 10)
)
_CanopySnmpAgent_ObjectIdentity = ObjectIdentity
canopySnmpAgent = _CanopySnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 250)
)
_Ucos_ObjectIdentity = ObjectIdentity
ucos = _Ucos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 250, 256)
)
_Prizm_ObjectIdentity = ObjectIdentity
prizm = _Prizm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1000)
)
_PrizmSnmpAgent_ObjectIdentity = ObjectIdentity
prizmSnmpAgent = _PrizmSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1250)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WHISP-GLOBAL-REG-MIB",
    **{"mot": mot,
       "whispRoot": whispRoot,
       "whispReg": whispReg,
       "whispModules": whispModules,
       "whispGlobalRegModule": whispGlobalRegModule,
       "whispGeneric": whispGeneric,
       "whispProducts": whispProducts,
       "whispAps": whispAps,
       "whispSm": whispSm,
       "whispBox": whispBox,
       "whispCMM": whispCMM,
       "whispPlv": whispPlv,
       "whispCMM4": whispCMM4,
       "whispPlvModem": whispPlvModem,
       "whispPlvGateway": whispPlvGateway,
       "whispPlvRepeater": whispPlvRepeater,
       "whispPlvBridge": whispPlvBridge,
       "canopySnmpAgent": canopySnmpAgent,
       "ucos": ucos,
       "prizm": prizm,
       "prizmSnmpAgent": prizmSnmpAgent}
)
