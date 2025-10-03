# SNMP MIB module (SILVERPEAK-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\silverpeak\SILVERPEAK-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:10 2025
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

(silverpeakModules,
 silverpeakProducts) = mibBuilder.importSymbols(
    "SILVERPEAK-SMI",
    "silverpeakModules",
    "silverpeakProducts")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

silverpeakProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SpsNX2500_ObjectIdentity = ObjectIdentity
spsNX2500 = _SpsNX2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 1)
)
_SpsNX3500_ObjectIdentity = ObjectIdentity
spsNX3500 = _SpsNX3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 2)
)
_SpsNX5500_ObjectIdentity = ObjectIdentity
spsNX5500 = _SpsNX5500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 3)
)
_SpsNX7500_ObjectIdentity = ObjectIdentity
spsNX7500 = _SpsNX7500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 4)
)
_SpsNX8500_ObjectIdentity = ObjectIdentity
spsNX8500 = _SpsNX8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 5)
)
_SpsNX1700_ObjectIdentity = ObjectIdentity
spsNX1700 = _SpsNX1700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 6)
)
_SpsNX2600_ObjectIdentity = ObjectIdentity
spsNX2600 = _SpsNX2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 7)
)
_SpsNX2610_ObjectIdentity = ObjectIdentity
spsNX2610 = _SpsNX2610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 8)
)
_SpsNX2700_ObjectIdentity = ObjectIdentity
spsNX2700 = _SpsNX2700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 9)
)
_SpsNX3600_ObjectIdentity = ObjectIdentity
spsNX3600 = _SpsNX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 10)
)
_SpsNX3700_ObjectIdentity = ObjectIdentity
spsNX3700 = _SpsNX3700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 11)
)
_SpsNX5504_ObjectIdentity = ObjectIdentity
spsNX5504 = _SpsNX5504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 12)
)
_SpsNX5600_ObjectIdentity = ObjectIdentity
spsNX5600 = _SpsNX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 13)
)
_SpsNX5700_ObjectIdentity = ObjectIdentity
spsNX5700 = _SpsNX5700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 14)
)
_SpsNX7504_ObjectIdentity = ObjectIdentity
spsNX7504 = _SpsNX7504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 15)
)
_SpsNX7600_ObjectIdentity = ObjectIdentity
spsNX7600 = _SpsNX7600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 16)
)
_SpsNX7700_ObjectIdentity = ObjectIdentity
spsNX7700 = _SpsNX7700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 17)
)
_SpsNX8504_ObjectIdentity = ObjectIdentity
spsNX8504 = _SpsNX8504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 18)
)
_SpsNX8600_ObjectIdentity = ObjectIdentity
spsNX8600 = _SpsNX8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 19)
)
_SpsNX8700_ObjectIdentity = ObjectIdentity
spsNX8700 = _SpsNX8700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 20)
)
_SpsNX9610_ObjectIdentity = ObjectIdentity
spsNX9610 = _SpsNX9610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 21)
)
_SpsNX9700_ObjectIdentity = ObjectIdentity
spsNX9700 = _SpsNX9700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 22)
)
_SpsVX0100_ObjectIdentity = ObjectIdentity
spsVX0100 = _SpsVX0100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 23)
)
_SpsVX2000_ObjectIdentity = ObjectIdentity
spsVX2000 = _SpsVX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 24)
)
_SpsVX5000_ObjectIdentity = ObjectIdentity
spsVX5000 = _SpsVX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 25)
)
_SpsVX1000_ObjectIdentity = ObjectIdentity
spsVX1000 = _SpsVX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 26)
)
_SpsVX3000_ObjectIdentity = ObjectIdentity
spsVX3000 = _SpsVX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 27)
)
_SpsNX10700_ObjectIdentity = ObjectIdentity
spsNX10700 = _SpsNX10700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 28)
)
_SpsVRX8_ObjectIdentity = ObjectIdentity
spsVRX8 = _SpsVRX8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 29)
)
_SpsVXXpress_ObjectIdentity = ObjectIdentity
spsVXXpress = _SpsVXXpress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 30)
)
_SpsVXUnlicensed_ObjectIdentity = ObjectIdentity
spsVXUnlicensed = _SpsVXUnlicensed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 31)
)
_SpsVX500_ObjectIdentity = ObjectIdentity
spsVX500 = _SpsVX500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 32)
)
_SpsVX6000_ObjectIdentity = ObjectIdentity
spsVX6000 = _SpsVX6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 33)
)
_SpsVX7000_ObjectIdentity = ObjectIdentity
spsVX7000 = _SpsVX7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 34)
)
_SpsVX8000_ObjectIdentity = ObjectIdentity
spsVX8000 = _SpsVX8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 35)
)
_SpsVX9000_ObjectIdentity = ObjectIdentity
spsVX9000 = _SpsVX9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 36)
)
_SpsNX11700_ObjectIdentity = ObjectIdentity
spsNX11700 = _SpsNX11700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 37)
)
_SpsVRX2_ObjectIdentity = ObjectIdentity
spsVRX2 = _SpsVRX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 38)
)
_SpsVRX4_ObjectIdentity = ObjectIdentity
spsVRX4 = _SpsVRX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 39)
)
_SpsNX6700_ObjectIdentity = ObjectIdentity
spsNX6700 = _SpsNX6700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 40)
)
_SpsVRX6_ObjectIdentity = ObjectIdentity
spsVRX6 = _SpsVRX6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 41)
)
_SpsNX700_ObjectIdentity = ObjectIdentity
spsNX700 = _SpsNX700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 42)
)
_SpsNX12700_ObjectIdentity = ObjectIdentity
spsNX12700 = _SpsNX12700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 43)
)
_SpsVX0000_ObjectIdentity = ObjectIdentity
spsVX0000 = _SpsVX0000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 44)
)
_SpsCPX_ObjectIdentity = ObjectIdentity
spsCPX = _SpsCPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 45)
)
_SpsECV_ObjectIdentity = ObjectIdentity
spsECV = _SpsECV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 46)
)
_SpsECXS_ObjectIdentity = ObjectIdentity
spsECXS = _SpsECXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 47)
)
_SpsECS_ObjectIdentity = ObjectIdentity
spsECS = _SpsECS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 48)
)
_SpsECM_ObjectIdentity = ObjectIdentity
spsECM = _SpsECM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 49)
)
_SpsECL_ObjectIdentity = ObjectIdentity
spsECL = _SpsECL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 50)
)
_SpsECXL_ObjectIdentity = ObjectIdentity
spsECXL = _SpsECXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 51)
)
_SpsECUS_ObjectIdentity = ObjectIdentity
spsECUS = _SpsECUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 52)
)
_SpsECMB_ObjectIdentity = ObjectIdentity
spsECMB = _SpsECMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 53)
)
_SpsECMP_ObjectIdentity = ObjectIdentity
spsECMP = _SpsECMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 54)
)
_SpsECLB_ObjectIdentity = ObjectIdentity
spsECLB = _SpsECLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 55)
)
_SpsECLP_ObjectIdentity = ObjectIdentity
spsECLP = _SpsECLP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 56)
)
_SpsECXLB_ObjectIdentity = ObjectIdentity
spsECXLB = _SpsECXLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 57)
)
_SpsECXLP_ObjectIdentity = ObjectIdentity
spsECXLP = _SpsECXLP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1, 2, 58)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SILVERPEAK-PRODUCTS-MIB",
    **{"silverpeakProductsMIB": silverpeakProductsMIB,
       "spsNX2500": spsNX2500,
       "spsNX3500": spsNX3500,
       "spsNX5500": spsNX5500,
       "spsNX7500": spsNX7500,
       "spsNX8500": spsNX8500,
       "spsNX1700": spsNX1700,
       "spsNX2600": spsNX2600,
       "spsNX2610": spsNX2610,
       "spsNX2700": spsNX2700,
       "spsNX3600": spsNX3600,
       "spsNX3700": spsNX3700,
       "spsNX5504": spsNX5504,
       "spsNX5600": spsNX5600,
       "spsNX5700": spsNX5700,
       "spsNX7504": spsNX7504,
       "spsNX7600": spsNX7600,
       "spsNX7700": spsNX7700,
       "spsNX8504": spsNX8504,
       "spsNX8600": spsNX8600,
       "spsNX8700": spsNX8700,
       "spsNX9610": spsNX9610,
       "spsNX9700": spsNX9700,
       "spsVX0100": spsVX0100,
       "spsVX2000": spsVX2000,
       "spsVX5000": spsVX5000,
       "spsVX1000": spsVX1000,
       "spsVX3000": spsVX3000,
       "spsNX10700": spsNX10700,
       "spsVRX8": spsVRX8,
       "spsVXXpress": spsVXXpress,
       "spsVXUnlicensed": spsVXUnlicensed,
       "spsVX500": spsVX500,
       "spsVX6000": spsVX6000,
       "spsVX7000": spsVX7000,
       "spsVX8000": spsVX8000,
       "spsVX9000": spsVX9000,
       "spsNX11700": spsNX11700,
       "spsVRX2": spsVRX2,
       "spsVRX4": spsVRX4,
       "spsNX6700": spsNX6700,
       "spsVRX6": spsVRX6,
       "spsNX700": spsNX700,
       "spsNX12700": spsNX12700,
       "spsVX0000": spsVX0000,
       "spsCPX": spsCPX,
       "spsECV": spsECV,
       "spsECXS": spsECXS,
       "spsECS": spsECS,
       "spsECM": spsECM,
       "spsECL": spsECL,
       "spsECXL": spsECXL,
       "spsECUS": spsECUS,
       "spsECMB": spsECMB,
       "spsECMP": spsECMP,
       "spsECLB": spsECLB,
       "spsECLP": spsECLP,
       "spsECXLB": spsECXLB,
       "spsECXLP": spsECXLP}
)
