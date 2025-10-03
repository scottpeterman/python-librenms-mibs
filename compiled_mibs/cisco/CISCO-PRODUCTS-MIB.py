# SNMP MIB module (CISCO-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:27:11 2025
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

(ciscoModules,
 ciscoProducts) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoModules",
    "ciscoProducts")

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

ciscoProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 2)
)
if mibBuilder.loadTexts:
    ciscoProductsMIB.setRevisions(
        ("2013-05-28 00:00",
         "2005-04-20 19:30",
         "2005-04-18 19:30",
         "2002-04-05 14:00",
         "1995-05-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGatewayServer_ObjectIdentity = ObjectIdentity
ciscoGatewayServer = _CiscoGatewayServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1)
)
_CiscoTerminalServer_ObjectIdentity = ObjectIdentity
ciscoTerminalServer = _CiscoTerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2)
)
_CiscoTrouter_ObjectIdentity = ObjectIdentity
ciscoTrouter = _CiscoTrouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3)
)
_CiscoProtocolTranslator_ObjectIdentity = ObjectIdentity
ciscoProtocolTranslator = _CiscoProtocolTranslator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 4)
)
_CiscoIGS_ObjectIdentity = ObjectIdentity
ciscoIGS = _CiscoIGS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 5)
)
_Cisco3000_ObjectIdentity = ObjectIdentity
cisco3000 = _Cisco3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 6)
)
_Cisco4000_ObjectIdentity = ObjectIdentity
cisco4000 = _Cisco4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 7)
)
_Cisco7000_ObjectIdentity = ObjectIdentity
cisco7000 = _Cisco7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 8)
)
_CiscoCS500_ObjectIdentity = ObjectIdentity
ciscoCS500 = _CiscoCS500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 9)
)
_Cisco2000_ObjectIdentity = ObjectIdentity
cisco2000 = _Cisco2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 10)
)
_CiscoAGSplus_ObjectIdentity = ObjectIdentity
ciscoAGSplus = _CiscoAGSplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 11)
)
_Cisco7010_ObjectIdentity = ObjectIdentity
cisco7010 = _Cisco7010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 12)
)
_Cisco2500_ObjectIdentity = ObjectIdentity
cisco2500 = _Cisco2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 13)
)
_Cisco4500_ObjectIdentity = ObjectIdentity
cisco4500 = _Cisco4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 14)
)
_Cisco2102_ObjectIdentity = ObjectIdentity
cisco2102 = _Cisco2102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 15)
)
_Cisco2202_ObjectIdentity = ObjectIdentity
cisco2202 = _Cisco2202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 16)
)
_Cisco2501_ObjectIdentity = ObjectIdentity
cisco2501 = _Cisco2501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 17)
)
_Cisco2502_ObjectIdentity = ObjectIdentity
cisco2502 = _Cisco2502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 18)
)
_Cisco2503_ObjectIdentity = ObjectIdentity
cisco2503 = _Cisco2503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 19)
)
_Cisco2504_ObjectIdentity = ObjectIdentity
cisco2504 = _Cisco2504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 20)
)
_Cisco2505_ObjectIdentity = ObjectIdentity
cisco2505 = _Cisco2505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 21)
)
_Cisco2506_ObjectIdentity = ObjectIdentity
cisco2506 = _Cisco2506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 22)
)
_Cisco2507_ObjectIdentity = ObjectIdentity
cisco2507 = _Cisco2507_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 23)
)
_Cisco2508_ObjectIdentity = ObjectIdentity
cisco2508 = _Cisco2508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 24)
)
_Cisco2509_ObjectIdentity = ObjectIdentity
cisco2509 = _Cisco2509_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 25)
)
_Cisco2510_ObjectIdentity = ObjectIdentity
cisco2510 = _Cisco2510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 26)
)
_Cisco2511_ObjectIdentity = ObjectIdentity
cisco2511 = _Cisco2511_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 27)
)
_Cisco2512_ObjectIdentity = ObjectIdentity
cisco2512 = _Cisco2512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 28)
)
_Cisco2513_ObjectIdentity = ObjectIdentity
cisco2513 = _Cisco2513_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 29)
)
_Cisco2514_ObjectIdentity = ObjectIdentity
cisco2514 = _Cisco2514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 30)
)
_Cisco2515_ObjectIdentity = ObjectIdentity
cisco2515 = _Cisco2515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 31)
)
_Cisco3101_ObjectIdentity = ObjectIdentity
cisco3101 = _Cisco3101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 32)
)
_Cisco3102_ObjectIdentity = ObjectIdentity
cisco3102 = _Cisco3102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 33)
)
_Cisco3103_ObjectIdentity = ObjectIdentity
cisco3103 = _Cisco3103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 34)
)
_Cisco3104_ObjectIdentity = ObjectIdentity
cisco3104 = _Cisco3104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 35)
)
_Cisco3202_ObjectIdentity = ObjectIdentity
cisco3202 = _Cisco3202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 36)
)
_Cisco3204_ObjectIdentity = ObjectIdentity
cisco3204 = _Cisco3204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 37)
)
_CiscoAccessProRC_ObjectIdentity = ObjectIdentity
ciscoAccessProRC = _CiscoAccessProRC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 38)
)
_CiscoAccessProEC_ObjectIdentity = ObjectIdentity
ciscoAccessProEC = _CiscoAccessProEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 39)
)
_Cisco1000_ObjectIdentity = ObjectIdentity
cisco1000 = _Cisco1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 40)
)
_Cisco1003_ObjectIdentity = ObjectIdentity
cisco1003 = _Cisco1003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 41)
)
_Cisco2516_ObjectIdentity = ObjectIdentity
cisco2516 = _Cisco2516_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 42)
)
_Cisco1020_ObjectIdentity = ObjectIdentity
cisco1020 = _Cisco1020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 43)
)
_Cisco1004_ObjectIdentity = ObjectIdentity
cisco1004 = _Cisco1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 44)
)
_Cisco7507_ObjectIdentity = ObjectIdentity
cisco7507 = _Cisco7507_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 45)
)
_Cisco7513_ObjectIdentity = ObjectIdentity
cisco7513 = _Cisco7513_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 46)
)
_Cisco7506_ObjectIdentity = ObjectIdentity
cisco7506 = _Cisco7506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 47)
)
_Cisco7505_ObjectIdentity = ObjectIdentity
cisco7505 = _Cisco7505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 48)
)
_Cisco1005_ObjectIdentity = ObjectIdentity
cisco1005 = _Cisco1005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 49)
)
_Cisco4700_ObjectIdentity = ObjectIdentity
cisco4700 = _Cisco4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 50)
)
_CiscoPro1003_ObjectIdentity = ObjectIdentity
ciscoPro1003 = _CiscoPro1003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 51)
)
_CiscoPro1004_ObjectIdentity = ObjectIdentity
ciscoPro1004 = _CiscoPro1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 52)
)
_CiscoPro1005_ObjectIdentity = ObjectIdentity
ciscoPro1005 = _CiscoPro1005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 53)
)
_CiscoPro1020_ObjectIdentity = ObjectIdentity
ciscoPro1020 = _CiscoPro1020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 54)
)
_CiscoPro2500PCE_ObjectIdentity = ObjectIdentity
ciscoPro2500PCE = _CiscoPro2500PCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 55)
)
_CiscoPro2501_ObjectIdentity = ObjectIdentity
ciscoPro2501 = _CiscoPro2501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 56)
)
_CiscoPro2503_ObjectIdentity = ObjectIdentity
ciscoPro2503 = _CiscoPro2503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 57)
)
_CiscoPro2505_ObjectIdentity = ObjectIdentity
ciscoPro2505 = _CiscoPro2505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 58)
)
_CiscoPro2507_ObjectIdentity = ObjectIdentity
ciscoPro2507 = _CiscoPro2507_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 59)
)
_CiscoPro2509_ObjectIdentity = ObjectIdentity
ciscoPro2509 = _CiscoPro2509_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 60)
)
_CiscoPro2511_ObjectIdentity = ObjectIdentity
ciscoPro2511 = _CiscoPro2511_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 61)
)
_CiscoPro2514_ObjectIdentity = ObjectIdentity
ciscoPro2514 = _CiscoPro2514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 62)
)
_CiscoPro2516_ObjectIdentity = ObjectIdentity
ciscoPro2516 = _CiscoPro2516_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 63)
)
_CiscoPro2519_ObjectIdentity = ObjectIdentity
ciscoPro2519 = _CiscoPro2519_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 64)
)
_CiscoPro2521_ObjectIdentity = ObjectIdentity
ciscoPro2521 = _CiscoPro2521_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 65)
)
_CiscoPro4500_ObjectIdentity = ObjectIdentity
ciscoPro4500 = _CiscoPro4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 66)
)
_Cisco2517_ObjectIdentity = ObjectIdentity
cisco2517 = _Cisco2517_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 67)
)
_Cisco2518_ObjectIdentity = ObjectIdentity
cisco2518 = _Cisco2518_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 68)
)
_Cisco2519_ObjectIdentity = ObjectIdentity
cisco2519 = _Cisco2519_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 69)
)
_Cisco2520_ObjectIdentity = ObjectIdentity
cisco2520 = _Cisco2520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 70)
)
_Cisco2521_ObjectIdentity = ObjectIdentity
cisco2521 = _Cisco2521_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 71)
)
_Cisco2522_ObjectIdentity = ObjectIdentity
cisco2522 = _Cisco2522_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 72)
)
_Cisco2523_ObjectIdentity = ObjectIdentity
cisco2523 = _Cisco2523_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 73)
)
_Cisco2524_ObjectIdentity = ObjectIdentity
cisco2524 = _Cisco2524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 74)
)
_Cisco2525_ObjectIdentity = ObjectIdentity
cisco2525 = _Cisco2525_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 75)
)
_CiscoPro751_ObjectIdentity = ObjectIdentity
ciscoPro751 = _CiscoPro751_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 76)
)
_CiscoPro752_ObjectIdentity = ObjectIdentity
ciscoPro752 = _CiscoPro752_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 77)
)
_CiscoPro753_ObjectIdentity = ObjectIdentity
ciscoPro753 = _CiscoPro753_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 78)
)
_CiscoPro901_ObjectIdentity = ObjectIdentity
ciscoPro901 = _CiscoPro901_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 79)
)
_CiscoPro902_ObjectIdentity = ObjectIdentity
ciscoPro902 = _CiscoPro902_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 80)
)
_Cisco751_ObjectIdentity = ObjectIdentity
cisco751 = _Cisco751_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 81)
)
_Cisco752_ObjectIdentity = ObjectIdentity
cisco752 = _Cisco752_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 82)
)
_Cisco753_ObjectIdentity = ObjectIdentity
cisco753 = _Cisco753_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 83)
)
_CiscoPro741_ObjectIdentity = ObjectIdentity
ciscoPro741 = _CiscoPro741_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 84)
)
_CiscoPro742_ObjectIdentity = ObjectIdentity
ciscoPro742 = _CiscoPro742_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 85)
)
_CiscoPro743_ObjectIdentity = ObjectIdentity
ciscoPro743 = _CiscoPro743_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 86)
)
_CiscoPro744_ObjectIdentity = ObjectIdentity
ciscoPro744 = _CiscoPro744_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 87)
)
_CiscoPro761_ObjectIdentity = ObjectIdentity
ciscoPro761 = _CiscoPro761_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 88)
)
_CiscoPro762_ObjectIdentity = ObjectIdentity
ciscoPro762 = _CiscoPro762_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 89)
)
_CiscoPro763_ObjectIdentity = ObjectIdentity
ciscoPro763 = _CiscoPro763_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 90)
)
_CiscoPro764_ObjectIdentity = ObjectIdentity
ciscoPro764 = _CiscoPro764_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 91)
)
_CiscoPro765_ObjectIdentity = ObjectIdentity
ciscoPro765 = _CiscoPro765_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 92)
)
_CiscoPro766_ObjectIdentity = ObjectIdentity
ciscoPro766 = _CiscoPro766_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 93)
)
_Cisco741_ObjectIdentity = ObjectIdentity
cisco741 = _Cisco741_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 94)
)
_Cisco742_ObjectIdentity = ObjectIdentity
cisco742 = _Cisco742_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 95)
)
_Cisco743_ObjectIdentity = ObjectIdentity
cisco743 = _Cisco743_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 96)
)
_Cisco744_ObjectIdentity = ObjectIdentity
cisco744 = _Cisco744_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 97)
)
_Cisco761_ObjectIdentity = ObjectIdentity
cisco761 = _Cisco761_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 98)
)
_Cisco762_ObjectIdentity = ObjectIdentity
cisco762 = _Cisco762_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 99)
)
_Cisco763_ObjectIdentity = ObjectIdentity
cisco763 = _Cisco763_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 100)
)
_Cisco764_ObjectIdentity = ObjectIdentity
cisco764 = _Cisco764_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 101)
)
_Cisco765_ObjectIdentity = ObjectIdentity
cisco765 = _Cisco765_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 102)
)
_Cisco766_ObjectIdentity = ObjectIdentity
cisco766 = _Cisco766_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 103)
)
_CiscoPro2520_ObjectIdentity = ObjectIdentity
ciscoPro2520 = _CiscoPro2520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 104)
)
_CiscoPro2522_ObjectIdentity = ObjectIdentity
ciscoPro2522 = _CiscoPro2522_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 105)
)
_CiscoPro2524_ObjectIdentity = ObjectIdentity
ciscoPro2524 = _CiscoPro2524_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 106)
)
_CiscoLS1010_ObjectIdentity = ObjectIdentity
ciscoLS1010 = _CiscoLS1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 107)
)
_Cisco7206_ObjectIdentity = ObjectIdentity
cisco7206 = _Cisco7206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 108)
)
_CiscoAS5200_ObjectIdentity = ObjectIdentity
ciscoAS5200 = _CiscoAS5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 109)
)
_Cisco3640_ObjectIdentity = ObjectIdentity
cisco3640 = _Cisco3640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 110)
)
_CiscoCatalyst3500_ObjectIdentity = ObjectIdentity
ciscoCatalyst3500 = _CiscoCatalyst3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111)
)
_CiscoWSX3011_ObjectIdentity = ObjectIdentity
ciscoWSX3011 = _CiscoWSX3011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 112)
)
_Cisco1601_ObjectIdentity = ObjectIdentity
cisco1601 = _Cisco1601_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 113)
)
_Cisco1602_ObjectIdentity = ObjectIdentity
cisco1602 = _Cisco1602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 114)
)
_Cisco1603_ObjectIdentity = ObjectIdentity
cisco1603 = _Cisco1603_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 115)
)
_Cisco1604_ObjectIdentity = ObjectIdentity
cisco1604 = _Cisco1604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 116)
)
_CiscoPro1601_ObjectIdentity = ObjectIdentity
ciscoPro1601 = _CiscoPro1601_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 117)
)
_CiscoPro1602_ObjectIdentity = ObjectIdentity
ciscoPro1602 = _CiscoPro1602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 118)
)
_CiscoPro1603_ObjectIdentity = ObjectIdentity
ciscoPro1603 = _CiscoPro1603_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 119)
)
_CiscoPro1604_ObjectIdentity = ObjectIdentity
ciscoPro1604 = _CiscoPro1604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 120)
)
_CiscoWSX5301_ObjectIdentity = ObjectIdentity
ciscoWSX5301 = _CiscoWSX5301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 121)
)
_Cisco3620_ObjectIdentity = ObjectIdentity
cisco3620 = _Cisco3620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 122)
)
_CiscoPro3620_ObjectIdentity = ObjectIdentity
ciscoPro3620 = _CiscoPro3620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 123)
)
_CiscoPro3640_ObjectIdentity = ObjectIdentity
ciscoPro3640 = _CiscoPro3640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 124)
)
_Cisco7204_ObjectIdentity = ObjectIdentity
cisco7204 = _Cisco7204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 125)
)
_Cisco771_ObjectIdentity = ObjectIdentity
cisco771 = _Cisco771_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 126)
)
_Cisco772_ObjectIdentity = ObjectIdentity
cisco772 = _Cisco772_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 127)
)
_Cisco775_ObjectIdentity = ObjectIdentity
cisco775 = _Cisco775_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 128)
)
_Cisco776_ObjectIdentity = ObjectIdentity
cisco776 = _Cisco776_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 129)
)
_CiscoPro2502_ObjectIdentity = ObjectIdentity
ciscoPro2502 = _CiscoPro2502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 130)
)
_CiscoPro2504_ObjectIdentity = ObjectIdentity
ciscoPro2504 = _CiscoPro2504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 131)
)
_CiscoPro2506_ObjectIdentity = ObjectIdentity
ciscoPro2506 = _CiscoPro2506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 132)
)
_CiscoPro2508_ObjectIdentity = ObjectIdentity
ciscoPro2508 = _CiscoPro2508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 133)
)
_CiscoPro2510_ObjectIdentity = ObjectIdentity
ciscoPro2510 = _CiscoPro2510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 134)
)
_CiscoPro2512_ObjectIdentity = ObjectIdentity
ciscoPro2512 = _CiscoPro2512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 135)
)
_CiscoPro2513_ObjectIdentity = ObjectIdentity
ciscoPro2513 = _CiscoPro2513_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 136)
)
_CiscoPro2515_ObjectIdentity = ObjectIdentity
ciscoPro2515 = _CiscoPro2515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 137)
)
_CiscoPro2517_ObjectIdentity = ObjectIdentity
ciscoPro2517 = _CiscoPro2517_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 138)
)
_CiscoPro2518_ObjectIdentity = ObjectIdentity
ciscoPro2518 = _CiscoPro2518_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 139)
)
_CiscoPro2523_ObjectIdentity = ObjectIdentity
ciscoPro2523 = _CiscoPro2523_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 140)
)
_CiscoPro2525_ObjectIdentity = ObjectIdentity
ciscoPro2525 = _CiscoPro2525_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 141)
)
_CiscoPro4700_ObjectIdentity = ObjectIdentity
ciscoPro4700 = _CiscoPro4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 142)
)
_CiscoPro316T_ObjectIdentity = ObjectIdentity
ciscoPro316T = _CiscoPro316T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 147)
)
_CiscoPro316C_ObjectIdentity = ObjectIdentity
ciscoPro316C = _CiscoPro316C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 148)
)
_CiscoPro3116_ObjectIdentity = ObjectIdentity
ciscoPro3116 = _CiscoPro3116_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 149)
)
_Catalyst116T_ObjectIdentity = ObjectIdentity
catalyst116T = _Catalyst116T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 150)
)
_Catalyst116C_ObjectIdentity = ObjectIdentity
catalyst116C = _Catalyst116C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 151)
)
_Catalyst1116_ObjectIdentity = ObjectIdentity
catalyst1116 = _Catalyst1116_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 152)
)
_CiscoAS2509RJ_ObjectIdentity = ObjectIdentity
ciscoAS2509RJ = _CiscoAS2509RJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 153)
)
_CiscoAS2511RJ_ObjectIdentity = ObjectIdentity
ciscoAS2511RJ = _CiscoAS2511RJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 154)
)
_CiscoMC3810_ObjectIdentity = ObjectIdentity
ciscoMC3810 = _CiscoMC3810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 157)
)
_Cisco1503_ObjectIdentity = ObjectIdentity
cisco1503 = _Cisco1503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 160)
)
_Cisco1502_ObjectIdentity = ObjectIdentity
cisco1502 = _Cisco1502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 161)
)
_CiscoAS5300_ObjectIdentity = ObjectIdentity
ciscoAS5300 = _CiscoAS5300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 162)
)
_CiscoLS1015_ObjectIdentity = ObjectIdentity
ciscoLS1015 = _CiscoLS1015_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 164)
)
_Cisco2501FRADFX_ObjectIdentity = ObjectIdentity
cisco2501FRADFX = _Cisco2501FRADFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 165)
)
_Cisco2501LANFRADFX_ObjectIdentity = ObjectIdentity
cisco2501LANFRADFX = _Cisco2501LANFRADFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 166)
)
_Cisco2502LANFRADFX_ObjectIdentity = ObjectIdentity
cisco2502LANFRADFX = _Cisco2502LANFRADFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 167)
)
_CiscoWSX5302_ObjectIdentity = ObjectIdentity
ciscoWSX5302 = _CiscoWSX5302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 168)
)
_CiscoFastHub216T_ObjectIdentity = ObjectIdentity
ciscoFastHub216T = _CiscoFastHub216T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 169)
)
_Catalyst2908xl_ObjectIdentity = ObjectIdentity
catalyst2908xl = _Catalyst2908xl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 170)
)
_Catalyst2916mxl_ObjectIdentity = ObjectIdentity
catalyst2916mxl = _Catalyst2916mxl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 171)
)
_Cisco1605_ObjectIdentity = ObjectIdentity
cisco1605 = _Cisco1605_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 172)
)
_Cisco12012_ObjectIdentity = ObjectIdentity
cisco12012 = _Cisco12012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 173)
)
_Catalyst1912C_ObjectIdentity = ObjectIdentity
catalyst1912C = _Catalyst1912C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 175)
)
_CiscoMicroWebServer2_ObjectIdentity = ObjectIdentity
ciscoMicroWebServer2 = _CiscoMicroWebServer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 176)
)
_CiscoFastHubBMMTX_ObjectIdentity = ObjectIdentity
ciscoFastHubBMMTX = _CiscoFastHubBMMTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 177)
)
_CiscoFastHubBMMFX_ObjectIdentity = ObjectIdentity
ciscoFastHubBMMFX = _CiscoFastHubBMMFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 178)
)
_CiscoUBR7246_ObjectIdentity = ObjectIdentity
ciscoUBR7246 = _CiscoUBR7246_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 179)
)
_Cisco6400_ObjectIdentity = ObjectIdentity
cisco6400 = _Cisco6400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 180)
)
_Cisco12004_ObjectIdentity = ObjectIdentity
cisco12004 = _Cisco12004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 181)
)
_Cisco12008_ObjectIdentity = ObjectIdentity
cisco12008 = _Cisco12008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 182)
)
_Catalyst2924XL_ObjectIdentity = ObjectIdentity
catalyst2924XL = _Catalyst2924XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 183)
)
_Catalyst2924CXL_ObjectIdentity = ObjectIdentity
catalyst2924CXL = _Catalyst2924CXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 184)
)
_Cisco2610_ObjectIdentity = ObjectIdentity
cisco2610 = _Cisco2610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 185)
)
_Cisco2611_ObjectIdentity = ObjectIdentity
cisco2611 = _Cisco2611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 186)
)
_Cisco2612_ObjectIdentity = ObjectIdentity
cisco2612 = _Cisco2612_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 187)
)
_CiscoAS5800_ObjectIdentity = ObjectIdentity
ciscoAS5800 = _CiscoAS5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 188)
)
_CiscoSC3640_ObjectIdentity = ObjectIdentity
ciscoSC3640 = _CiscoSC3640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 189)
)
_Cisco8510_ObjectIdentity = ObjectIdentity
cisco8510 = _Cisco8510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 190)
)
_CiscoUBR904_ObjectIdentity = ObjectIdentity
ciscoUBR904 = _CiscoUBR904_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 191)
)
_Cisco6200_ObjectIdentity = ObjectIdentity
cisco6200 = _Cisco6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 192)
)
_Cisco7202_ObjectIdentity = ObjectIdentity
cisco7202 = _Cisco7202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 194)
)
_Cisco2613_ObjectIdentity = ObjectIdentity
cisco2613 = _Cisco2613_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 195)
)
_Cisco8515_ObjectIdentity = ObjectIdentity
cisco8515 = _Cisco8515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 196)
)
_Catalyst9006_ObjectIdentity = ObjectIdentity
catalyst9006 = _Catalyst9006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 197)
)
_Catalyst9009_ObjectIdentity = ObjectIdentity
catalyst9009 = _Catalyst9009_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 198)
)
_CiscoRPM_ObjectIdentity = ObjectIdentity
ciscoRPM = _CiscoRPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 199)
)
_Cisco1710_ObjectIdentity = ObjectIdentity
cisco1710 = _Cisco1710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 200)
)
_Cisco1720_ObjectIdentity = ObjectIdentity
cisco1720 = _Cisco1720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 201)
)
_Catalyst8540msr_ObjectIdentity = ObjectIdentity
catalyst8540msr = _Catalyst8540msr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 202)
)
_Catalyst8540csr_ObjectIdentity = ObjectIdentity
catalyst8540csr = _Catalyst8540csr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 203)
)
_Cisco7576_ObjectIdentity = ObjectIdentity
cisco7576 = _Cisco7576_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 204)
)
_Cisco3660_ObjectIdentity = ObjectIdentity
cisco3660 = _Cisco3660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 205)
)
_Cisco1401_ObjectIdentity = ObjectIdentity
cisco1401 = _Cisco1401_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 206)
)
_Cisco2620_ObjectIdentity = ObjectIdentity
cisco2620 = _Cisco2620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 208)
)
_Cisco2621_ObjectIdentity = ObjectIdentity
cisco2621 = _Cisco2621_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 209)
)
_CiscoUBR7223_ObjectIdentity = ObjectIdentity
ciscoUBR7223 = _CiscoUBR7223_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 210)
)
_Cisco6400Nrp_ObjectIdentity = ObjectIdentity
cisco6400Nrp = _Cisco6400Nrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 211)
)
_Cisco801_ObjectIdentity = ObjectIdentity
cisco801 = _Cisco801_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 212)
)
_Cisco802_ObjectIdentity = ObjectIdentity
cisco802 = _Cisco802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 213)
)
_Cisco803_ObjectIdentity = ObjectIdentity
cisco803 = _Cisco803_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 214)
)
_Cisco804_ObjectIdentity = ObjectIdentity
cisco804 = _Cisco804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 215)
)
_Cisco1750_ObjectIdentity = ObjectIdentity
cisco1750 = _Cisco1750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 216)
)
_Catalyst2924XLv_ObjectIdentity = ObjectIdentity
catalyst2924XLv = _Catalyst2924XLv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 217)
)
_Catalyst2924CXLv_ObjectIdentity = ObjectIdentity
catalyst2924CXLv = _Catalyst2924CXLv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 218)
)
_Catalyst2912XL_ObjectIdentity = ObjectIdentity
catalyst2912XL = _Catalyst2912XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 219)
)
_Catalyst2924MXL_ObjectIdentity = ObjectIdentity
catalyst2924MXL = _Catalyst2924MXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 220)
)
_Catalyst2912MfXL_ObjectIdentity = ObjectIdentity
catalyst2912MfXL = _Catalyst2912MfXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 221)
)
_Cisco7206VXR_ObjectIdentity = ObjectIdentity
cisco7206VXR = _Cisco7206VXR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 222)
)
_Cisco7204VXR_ObjectIdentity = ObjectIdentity
cisco7204VXR = _Cisco7204VXR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 223)
)
_Cisco1538M_ObjectIdentity = ObjectIdentity
cisco1538M = _Cisco1538M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 224)
)
_Cisco1548M_ObjectIdentity = ObjectIdentity
cisco1548M = _Cisco1548M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 225)
)
_CiscoFasthub100_ObjectIdentity = ObjectIdentity
ciscoFasthub100 = _CiscoFasthub100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 226)
)
_CiscoPIXFirewall_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall = _CiscoPIXFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 227)
)
_CiscoMGX8850_ObjectIdentity = ObjectIdentity
ciscoMGX8850 = _CiscoMGX8850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 228)
)
_CiscoMGX8830_ObjectIdentity = ObjectIdentity
ciscoMGX8830 = _CiscoMGX8830_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 229)
)
_Catalyst8510msr_ObjectIdentity = ObjectIdentity
catalyst8510msr = _Catalyst8510msr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 230)
)
_Catalyst8515msr_ObjectIdentity = ObjectIdentity
catalyst8515msr = _Catalyst8515msr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 231)
)
_CiscoIGX8410_ObjectIdentity = ObjectIdentity
ciscoIGX8410 = _CiscoIGX8410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 232)
)
_CiscoIGX8420_ObjectIdentity = ObjectIdentity
ciscoIGX8420 = _CiscoIGX8420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 233)
)
_CiscoIGX8430_ObjectIdentity = ObjectIdentity
ciscoIGX8430 = _CiscoIGX8430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 234)
)
_CiscoIGX8450_ObjectIdentity = ObjectIdentity
ciscoIGX8450 = _CiscoIGX8450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 235)
)
_CiscoBPX8620_ObjectIdentity = ObjectIdentity
ciscoBPX8620 = _CiscoBPX8620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 237)
)
_CiscoBPX8650_ObjectIdentity = ObjectIdentity
ciscoBPX8650 = _CiscoBPX8650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 238)
)
_CiscoBPX8680_ObjectIdentity = ObjectIdentity
ciscoBPX8680 = _CiscoBPX8680_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 239)
)
_CiscoCacheEngine_ObjectIdentity = ObjectIdentity
ciscoCacheEngine = _CiscoCacheEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 240)
)
_CiscoCat6000_ObjectIdentity = ObjectIdentity
ciscoCat6000 = _CiscoCat6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 241)
)
_CiscoBPXSes_ObjectIdentity = ObjectIdentity
ciscoBPXSes = _CiscoBPXSes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 242)
)
_CiscoIGXSes_ObjectIdentity = ObjectIdentity
ciscoIGXSes = _CiscoIGXSes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 243)
)
_CiscoLocalDirector_ObjectIdentity = ObjectIdentity
ciscoLocalDirector = _CiscoLocalDirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 244)
)
_Cisco805_ObjectIdentity = ObjectIdentity
cisco805 = _Cisco805_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 245)
)
_Catalyst3508GXL_ObjectIdentity = ObjectIdentity
catalyst3508GXL = _Catalyst3508GXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 246)
)
_Catalyst3512XL_ObjectIdentity = ObjectIdentity
catalyst3512XL = _Catalyst3512XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 247)
)
_Catalyst3524XL_ObjectIdentity = ObjectIdentity
catalyst3524XL = _Catalyst3524XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 248)
)
_Cisco1407_ObjectIdentity = ObjectIdentity
cisco1407 = _Cisco1407_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 249)
)
_Cisco1417_ObjectIdentity = ObjectIdentity
cisco1417 = _Cisco1417_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 250)
)
_Cisco6100_ObjectIdentity = ObjectIdentity
cisco6100 = _Cisco6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 251)
)
_Cisco6130_ObjectIdentity = ObjectIdentity
cisco6130 = _Cisco6130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 252)
)
_Cisco6260_ObjectIdentity = ObjectIdentity
cisco6260 = _Cisco6260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 253)
)
_CiscoOpticalRegenerator_ObjectIdentity = ObjectIdentity
ciscoOpticalRegenerator = _CiscoOpticalRegenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 254)
)
_CiscoUBR924_ObjectIdentity = ObjectIdentity
ciscoUBR924 = _CiscoUBR924_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 255)
)
_CiscoWSX6302Msm_ObjectIdentity = ObjectIdentity
ciscoWSX6302Msm = _CiscoWSX6302Msm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 256)
)
_Catalyst5kRsfc_ObjectIdentity = ObjectIdentity
catalyst5kRsfc = _Catalyst5kRsfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 257)
)
_Catalyst6kMsfc_ObjectIdentity = ObjectIdentity
catalyst6kMsfc = _Catalyst6kMsfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 258)
)
_Cisco7120Quadt1_ObjectIdentity = ObjectIdentity
cisco7120Quadt1 = _Cisco7120Quadt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 259)
)
_Cisco7120T3_ObjectIdentity = ObjectIdentity
cisco7120T3 = _Cisco7120T3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 260)
)
_Cisco7120E3_ObjectIdentity = ObjectIdentity
cisco7120E3 = _Cisco7120E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 261)
)
_Cisco7120At3_ObjectIdentity = ObjectIdentity
cisco7120At3 = _Cisco7120At3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 262)
)
_Cisco7120Ae3_ObjectIdentity = ObjectIdentity
cisco7120Ae3 = _Cisco7120Ae3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 263)
)
_Cisco7120Smi3_ObjectIdentity = ObjectIdentity
cisco7120Smi3 = _Cisco7120Smi3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 264)
)
_Cisco7140Dualt3_ObjectIdentity = ObjectIdentity
cisco7140Dualt3 = _Cisco7140Dualt3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 265)
)
_Cisco7140Duale3_ObjectIdentity = ObjectIdentity
cisco7140Duale3 = _Cisco7140Duale3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 266)
)
_Cisco7140Dualat3_ObjectIdentity = ObjectIdentity
cisco7140Dualat3 = _Cisco7140Dualat3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 267)
)
_Cisco7140Dualae3_ObjectIdentity = ObjectIdentity
cisco7140Dualae3 = _Cisco7140Dualae3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 268)
)
_Cisco7140Dualmm3_ObjectIdentity = ObjectIdentity
cisco7140Dualmm3 = _Cisco7140Dualmm3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 269)
)
_Cisco827QuadV_ObjectIdentity = ObjectIdentity
cisco827QuadV = _Cisco827QuadV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 270)
)
_CiscoUBR7246VXR_ObjectIdentity = ObjectIdentity
ciscoUBR7246VXR = _CiscoUBR7246VXR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 271)
)
_Cisco10400_ObjectIdentity = ObjectIdentity
cisco10400 = _Cisco10400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 272)
)
_Cisco12016_ObjectIdentity = ObjectIdentity
cisco12016 = _Cisco12016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 273)
)
_CiscoAs5400_ObjectIdentity = ObjectIdentity
ciscoAs5400 = _CiscoAs5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 274)
)
_Cat2948gL3_ObjectIdentity = ObjectIdentity
cat2948gL3 = _Cat2948gL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 275)
)
_Cisco7140Octt1_ObjectIdentity = ObjectIdentity
cisco7140Octt1 = _Cisco7140Octt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 276)
)
_Cisco7140Dualfe_ObjectIdentity = ObjectIdentity
cisco7140Dualfe = _Cisco7140Dualfe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 277)
)
_Cat3548XL_ObjectIdentity = ObjectIdentity
cat3548XL = _Cat3548XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 278)
)
_CiscoVG200_ObjectIdentity = ObjectIdentity
ciscoVG200 = _CiscoVG200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 279)
)
_Cat6006_ObjectIdentity = ObjectIdentity
cat6006 = _Cat6006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 280)
)
_Cat6009_ObjectIdentity = ObjectIdentity
cat6009 = _Cat6009_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 281)
)
_Cat6506_ObjectIdentity = ObjectIdentity
cat6506 = _Cat6506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 282)
)
_Cat6509_ObjectIdentity = ObjectIdentity
cat6509 = _Cat6509_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 283)
)
_Cisco827_ObjectIdentity = ObjectIdentity
cisco827 = _Cisco827_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 284)
)
_CiscoManagementEngine1100_ObjectIdentity = ObjectIdentity
ciscoManagementEngine1100 = _CiscoManagementEngine1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 285)
)
_CiscoMc3810V3_ObjectIdentity = ObjectIdentity
ciscoMc3810V3 = _CiscoMc3810V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 286)
)
_Cat3524tXLEn_ObjectIdentity = ObjectIdentity
cat3524tXLEn = _Cat3524tXLEn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 287)
)
_Cisco7507z_ObjectIdentity = ObjectIdentity
cisco7507z = _Cisco7507z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 288)
)
_Cisco7513z_ObjectIdentity = ObjectIdentity
cisco7513z = _Cisco7513z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 289)
)
_Cisco7507mx_ObjectIdentity = ObjectIdentity
cisco7507mx = _Cisco7507mx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 290)
)
_Cisco7513mx_ObjectIdentity = ObjectIdentity
cisco7513mx = _Cisco7513mx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 291)
)
_CiscoUBR912C_ObjectIdentity = ObjectIdentity
ciscoUBR912C = _CiscoUBR912C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 292)
)
_CiscoUBR912S_ObjectIdentity = ObjectIdentity
ciscoUBR912S = _CiscoUBR912S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 293)
)
_CiscoUBR914_ObjectIdentity = ObjectIdentity
ciscoUBR914 = _CiscoUBR914_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 294)
)
_Cisco802J_ObjectIdentity = ObjectIdentity
cisco802J = _Cisco802J_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 295)
)
_Cisco804J_ObjectIdentity = ObjectIdentity
cisco804J = _Cisco804J_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 296)
)
_Cisco6160_ObjectIdentity = ObjectIdentity
cisco6160 = _Cisco6160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 297)
)
_Cat4908gL3_ObjectIdentity = ObjectIdentity
cat4908gL3 = _Cat4908gL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 298)
)
_Cisco6015_ObjectIdentity = ObjectIdentity
cisco6015 = _Cisco6015_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 299)
)
_Cat4232L3_ObjectIdentity = ObjectIdentity
cat4232L3 = _Cat4232L3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 300)
)
_Catalyst6kMsfc2_ObjectIdentity = ObjectIdentity
catalyst6kMsfc2 = _Catalyst6kMsfc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 301)
)
_Cisco7750Mrp200_ObjectIdentity = ObjectIdentity
cisco7750Mrp200 = _Cisco7750Mrp200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 302)
)
_Cisco7750Ssp80_ObjectIdentity = ObjectIdentity
cisco7750Ssp80 = _Cisco7750Ssp80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 303)
)
_CiscoMGX8230_ObjectIdentity = ObjectIdentity
ciscoMGX8230 = _CiscoMGX8230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 304)
)
_CiscoMGX8250_ObjectIdentity = ObjectIdentity
ciscoMGX8250 = _CiscoMGX8250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 305)
)
_CiscoCVA122_ObjectIdentity = ObjectIdentity
ciscoCVA122 = _CiscoCVA122_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 306)
)
_CiscoCVA124_ObjectIdentity = ObjectIdentity
ciscoCVA124 = _CiscoCVA124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 307)
)
_CiscoAs5850_ObjectIdentity = ObjectIdentity
ciscoAs5850 = _CiscoAs5850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 308)
)
_Cat6509Sp_ObjectIdentity = ObjectIdentity
cat6509Sp = _Cat6509Sp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 310)
)
_CiscoMGX8240_ObjectIdentity = ObjectIdentity
ciscoMGX8240 = _CiscoMGX8240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 311)
)
_Cat4840gL3_ObjectIdentity = ObjectIdentity
cat4840gL3 = _Cat4840gL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 312)
)
_CiscoAS5350_ObjectIdentity = ObjectIdentity
ciscoAS5350 = _CiscoAS5350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 313)
)
_Cisco7750_ObjectIdentity = ObjectIdentity
cisco7750 = _Cisco7750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 314)
)
_CiscoMGX8950_ObjectIdentity = ObjectIdentity
ciscoMGX8950 = _CiscoMGX8950_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 315)
)
_CiscoUBR925_ObjectIdentity = ObjectIdentity
ciscoUBR925 = _CiscoUBR925_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 316)
)
_CiscoUBR10012_ObjectIdentity = ObjectIdentity
ciscoUBR10012 = _CiscoUBR10012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 317)
)
_Catalyst4kGateway_ObjectIdentity = ObjectIdentity
catalyst4kGateway = _Catalyst4kGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 318)
)
_Cisco2650_ObjectIdentity = ObjectIdentity
cisco2650 = _Cisco2650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 319)
)
_Cisco2651_ObjectIdentity = ObjectIdentity
cisco2651 = _Cisco2651_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 320)
)
_Cisco826QuadV_ObjectIdentity = ObjectIdentity
cisco826QuadV = _Cisco826QuadV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 321)
)
_Cisco826_ObjectIdentity = ObjectIdentity
cisco826 = _Cisco826_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 322)
)
_Catalyst295012_ObjectIdentity = ObjectIdentity
catalyst295012 = _Catalyst295012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 323)
)
_Catalyst295024_ObjectIdentity = ObjectIdentity
catalyst295024 = _Catalyst295024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 324)
)
_Catalyst295024C_ObjectIdentity = ObjectIdentity
catalyst295024C = _Catalyst295024C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 325)
)
_Cisco1751_ObjectIdentity = ObjectIdentity
cisco1751 = _Cisco1751_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 326)
)
_Cisco1730Iad8Fxs_ObjectIdentity = ObjectIdentity
cisco1730Iad8Fxs = _Cisco1730Iad8Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 327)
)
_Cisco1730Iad16Fxs_ObjectIdentity = ObjectIdentity
cisco1730Iad16Fxs = _Cisco1730Iad16Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 328)
)
_Cisco626_ObjectIdentity = ObjectIdentity
cisco626 = _Cisco626_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 329)
)
_Cisco627_ObjectIdentity = ObjectIdentity
cisco627 = _Cisco627_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 330)
)
_Cisco633_ObjectIdentity = ObjectIdentity
cisco633 = _Cisco633_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 331)
)
_Cisco673_ObjectIdentity = ObjectIdentity
cisco673 = _Cisco673_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 332)
)
_Cisco675_ObjectIdentity = ObjectIdentity
cisco675 = _Cisco675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 333)
)
_Cisco675e_ObjectIdentity = ObjectIdentity
cisco675e = _Cisco675e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 334)
)
_Cisco676_ObjectIdentity = ObjectIdentity
cisco676 = _Cisco676_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 335)
)
_Cisco677_ObjectIdentity = ObjectIdentity
cisco677 = _Cisco677_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 336)
)
_Cisco678_ObjectIdentity = ObjectIdentity
cisco678 = _Cisco678_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 337)
)
_Cisco3661Ac_ObjectIdentity = ObjectIdentity
cisco3661Ac = _Cisco3661Ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 338)
)
_Cisco3661Dc_ObjectIdentity = ObjectIdentity
cisco3661Dc = _Cisco3661Dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 339)
)
_Cisco3662Ac_ObjectIdentity = ObjectIdentity
cisco3662Ac = _Cisco3662Ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 340)
)
_Cisco3662Dc_ObjectIdentity = ObjectIdentity
cisco3662Dc = _Cisco3662Dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 341)
)
_Cisco3662AcCo_ObjectIdentity = ObjectIdentity
cisco3662AcCo = _Cisco3662AcCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 342)
)
_Cisco3662DcCo_ObjectIdentity = ObjectIdentity
cisco3662DcCo = _Cisco3662DcCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 343)
)
_CiscoUBR7111_ObjectIdentity = ObjectIdentity
ciscoUBR7111 = _CiscoUBR7111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 344)
)
_CiscoUBR7111E_ObjectIdentity = ObjectIdentity
ciscoUBR7111E = _CiscoUBR7111E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 345)
)
_CiscoUBR7114_ObjectIdentity = ObjectIdentity
ciscoUBR7114 = _CiscoUBR7114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 346)
)
_CiscoUBR7114E_ObjectIdentity = ObjectIdentity
ciscoUBR7114E = _CiscoUBR7114E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 347)
)
_Cisco12010_ObjectIdentity = ObjectIdentity
cisco12010 = _Cisco12010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 348)
)
_Cisco8110_ObjectIdentity = ObjectIdentity
cisco8110 = _Cisco8110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 349)
)
_Cisco8120_ObjectIdentity = ObjectIdentity
cisco8120 = _Cisco8120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 350)
)
_CiscoUBR905_ObjectIdentity = ObjectIdentity
ciscoUBR905 = _CiscoUBR905_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 351)
)
_CiscoIDS_ObjectIdentity = ObjectIdentity
ciscoIDS = _CiscoIDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 352)
)
_CiscoSOHO77_ObjectIdentity = ObjectIdentity
ciscoSOHO77 = _CiscoSOHO77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 353)
)
_CiscoSOHO76_ObjectIdentity = ObjectIdentity
ciscoSOHO76 = _CiscoSOHO76_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 354)
)
_Cisco7150Dualfe_ObjectIdentity = ObjectIdentity
cisco7150Dualfe = _Cisco7150Dualfe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 355)
)
_Cisco7150Octt1_ObjectIdentity = ObjectIdentity
cisco7150Octt1 = _Cisco7150Octt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 356)
)
_Cisco7150Dualt3_ObjectIdentity = ObjectIdentity
cisco7150Dualt3 = _Cisco7150Dualt3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 357)
)
_CiscoOlympus_ObjectIdentity = ObjectIdentity
ciscoOlympus = _CiscoOlympus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 358)
)
_Catalyst2950t24_ObjectIdentity = ObjectIdentity
catalyst2950t24 = _Catalyst2950t24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 359)
)
_CiscoVPS1110_ObjectIdentity = ObjectIdentity
ciscoVPS1110 = _CiscoVPS1110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 360)
)
_CiscoContentEngine_ObjectIdentity = ObjectIdentity
ciscoContentEngine = _CiscoContentEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 361)
)
_CiscoIAD2420_ObjectIdentity = ObjectIdentity
ciscoIAD2420 = _CiscoIAD2420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 362)
)
_Cisco677i_ObjectIdentity = ObjectIdentity
cisco677i = _Cisco677i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 363)
)
_Cisco674_ObjectIdentity = ObjectIdentity
cisco674 = _Cisco674_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 364)
)
_CiscoDPA7630_ObjectIdentity = ObjectIdentity
ciscoDPA7630 = _CiscoDPA7630_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 365)
)
_Catalyst355024_ObjectIdentity = ObjectIdentity
catalyst355024 = _Catalyst355024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 366)
)
_Catalyst355048_ObjectIdentity = ObjectIdentity
catalyst355048 = _Catalyst355048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 367)
)
_Catalyst355012T_ObjectIdentity = ObjectIdentity
catalyst355012T = _Catalyst355012T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 368)
)
_Catalyst2924LREXL_ObjectIdentity = ObjectIdentity
catalyst2924LREXL = _Catalyst2924LREXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 369)
)
_Catalyst2912LREXL_ObjectIdentity = ObjectIdentity
catalyst2912LREXL = _Catalyst2912LREXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 370)
)
_CiscoCVA122E_ObjectIdentity = ObjectIdentity
ciscoCVA122E = _CiscoCVA122E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 371)
)
_CiscoCVA124E_ObjectIdentity = ObjectIdentity
ciscoCVA124E = _CiscoCVA124E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 372)
)
_CiscoURM_ObjectIdentity = ObjectIdentity
ciscoURM = _CiscoURM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 373)
)
_CiscoURM2FE_ObjectIdentity = ObjectIdentity
ciscoURM2FE = _CiscoURM2FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 374)
)
_CiscoURM2FE2V_ObjectIdentity = ObjectIdentity
ciscoURM2FE2V = _CiscoURM2FE2V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 375)
)
_Cisco7401VXR_ObjectIdentity = ObjectIdentity
cisco7401VXR = _Cisco7401VXR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 376)
)
_Cisco951_ObjectIdentity = ObjectIdentity
cisco951 = _Cisco951_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 377)
)
_Cisco952_ObjectIdentity = ObjectIdentity
cisco952 = _Cisco952_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 378)
)
_CiscoCAP340_ObjectIdentity = ObjectIdentity
ciscoCAP340 = _CiscoCAP340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 379)
)
_CiscoCAP350_ObjectIdentity = ObjectIdentity
ciscoCAP350 = _CiscoCAP350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 380)
)
_CiscoDPA7610_ObjectIdentity = ObjectIdentity
ciscoDPA7610 = _CiscoDPA7610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 381)
)
_Cisco828_ObjectIdentity = ObjectIdentity
cisco828 = _Cisco828_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 382)
)
_CiscoSOHO78_ObjectIdentity = ObjectIdentity
ciscoSOHO78 = _CiscoSOHO78_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 383)
)
_Cisco806_ObjectIdentity = ObjectIdentity
cisco806 = _Cisco806_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 384)
)
_Cisco12416_ObjectIdentity = ObjectIdentity
cisco12416 = _Cisco12416_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 385)
)
_Cat2948gL3Dc_ObjectIdentity = ObjectIdentity
cat2948gL3Dc = _Cat2948gL3Dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 386)
)
_Cat4908gL3Dc_ObjectIdentity = ObjectIdentity
cat4908gL3Dc = _Cat4908gL3Dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 387)
)
_Cisco12406_ObjectIdentity = ObjectIdentity
cisco12406 = _Cisco12406_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 388)
)
_CiscoPIXFirewall506_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall506 = _CiscoPIXFirewall506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 389)
)
_CiscoPIXFirewall515_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall515 = _CiscoPIXFirewall515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 390)
)
_CiscoPIXFirewall520_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall520 = _CiscoPIXFirewall520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 391)
)
_CiscoPIXFirewall525_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall525 = _CiscoPIXFirewall525_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 392)
)
_CiscoPIXFirewall535_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall535 = _CiscoPIXFirewall535_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 393)
)
_Cisco12410_ObjectIdentity = ObjectIdentity
cisco12410 = _Cisco12410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 394)
)
_Cisco811_ObjectIdentity = ObjectIdentity
cisco811 = _Cisco811_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 395)
)
_Cisco813_ObjectIdentity = ObjectIdentity
cisco813 = _Cisco813_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 396)
)
_Cisco10720_ObjectIdentity = ObjectIdentity
cisco10720 = _Cisco10720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 397)
)
_CiscoMWR1900_ObjectIdentity = ObjectIdentity
ciscoMWR1900 = _CiscoMWR1900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 398)
)
_Cisco4224_ObjectIdentity = ObjectIdentity
cisco4224 = _Cisco4224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 399)
)
_CiscoWSC6513_ObjectIdentity = ObjectIdentity
ciscoWSC6513 = _CiscoWSC6513_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 400)
)
_Cisco7603_ObjectIdentity = ObjectIdentity
cisco7603 = _Cisco7603_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 401)
)
_Cisco7606_ObjectIdentity = ObjectIdentity
cisco7606 = _Cisco7606_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 402)
)
_Cisco7401ASR_ObjectIdentity = ObjectIdentity
cisco7401ASR = _Cisco7401ASR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 403)
)
_CiscoVG248_ObjectIdentity = ObjectIdentity
ciscoVG248 = _CiscoVG248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 404)
)
_CiscoHSE_ObjectIdentity = ObjectIdentity
ciscoHSE = _CiscoHSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 405)
)
_CiscoONS15540ESP_ObjectIdentity = ObjectIdentity
ciscoONS15540ESP = _CiscoONS15540ESP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 406)
)
_CiscoSN5420_ObjectIdentity = ObjectIdentity
ciscoSN5420 = _CiscoSN5420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 407)
)
_CiscoIcs7750Ce300_ObjectIdentity = ObjectIdentity
ciscoIcs7750Ce300 = _CiscoIcs7750Ce300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 408)
)
_CiscoCe507_ObjectIdentity = ObjectIdentity
ciscoCe507 = _CiscoCe507_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 409)
)
_CiscoCe560_ObjectIdentity = ObjectIdentity
ciscoCe560 = _CiscoCe560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 410)
)
_CiscoCe590_ObjectIdentity = ObjectIdentity
ciscoCe590 = _CiscoCe590_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 411)
)
_CiscoCe7320_ObjectIdentity = ObjectIdentity
ciscoCe7320 = _CiscoCe7320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 412)
)
_Cisco2691_ObjectIdentity = ObjectIdentity
cisco2691 = _Cisco2691_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 413)
)
_Cisco3725_ObjectIdentity = ObjectIdentity
cisco3725 = _Cisco3725_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 414)
)
_Cisco3640A_ObjectIdentity = ObjectIdentity
cisco3640A = _Cisco3640A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 415)
)
_Cisco1760_ObjectIdentity = ObjectIdentity
cisco1760 = _Cisco1760_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 416)
)
_CiscoPIXFirewall501_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall501 = _CiscoPIXFirewall501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 417)
)
_Cisco2610M_ObjectIdentity = ObjectIdentity
cisco2610M = _Cisco2610M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 418)
)
_Cisco2611M_ObjectIdentity = ObjectIdentity
cisco2611M = _Cisco2611M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 419)
)
_CiscoGP10_ObjectIdentity = ObjectIdentity
ciscoGP10 = _CiscoGP10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 420)
)
_CiscoMC21_ObjectIdentity = ObjectIdentity
ciscoMC21 = _CiscoMC21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 421)
)
_CiscoSN51_ObjectIdentity = ObjectIdentity
ciscoSN51 = _CiscoSN51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 422)
)
_Cisco12404_ObjectIdentity = ObjectIdentity
cisco12404 = _Cisco12404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 423)
)
_Cisco9004_ObjectIdentity = ObjectIdentity
cisco9004 = _Cisco9004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 424)
)
_Cisco3631Co_ObjectIdentity = ObjectIdentity
cisco3631Co = _Cisco3631Co_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 425)
)
_Catalyst295012G_ObjectIdentity = ObjectIdentity
catalyst295012G = _Catalyst295012G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 427)
)
_Catalyst295024G_ObjectIdentity = ObjectIdentity
catalyst295024G = _Catalyst295024G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 428)
)
_Catalyst295048G_ObjectIdentity = ObjectIdentity
catalyst295048G = _Catalyst295048G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 429)
)
_Catalyst295024S_ObjectIdentity = ObjectIdentity
catalyst295024S = _Catalyst295024S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 430)
)
_Catalyst355012G_ObjectIdentity = ObjectIdentity
catalyst355012G = _Catalyst355012G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 431)
)
_CiscoCE507AV_ObjectIdentity = ObjectIdentity
ciscoCE507AV = _CiscoCE507AV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 432)
)
_CiscoCE560AV_ObjectIdentity = ObjectIdentity
ciscoCE560AV = _CiscoCE560AV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 433)
)
_CiscoIE2105_ObjectIdentity = ObjectIdentity
ciscoIE2105 = _CiscoIE2105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 434)
)
_CiscoMGX8850Pxm1E_ObjectIdentity = ObjectIdentity
ciscoMGX8850Pxm1E = _CiscoMGX8850Pxm1E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 435)
)
_Cisco3745_ObjectIdentity = ObjectIdentity
cisco3745 = _Cisco3745_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 436)
)
_Cisco10005_ObjectIdentity = ObjectIdentity
cisco10005 = _Cisco10005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 437)
)
_Cisco10008_ObjectIdentity = ObjectIdentity
cisco10008 = _Cisco10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 438)
)
_Cisco7304_ObjectIdentity = ObjectIdentity
cisco7304 = _Cisco7304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 439)
)
_CiscoRpmXf_ObjectIdentity = ObjectIdentity
ciscoRpmXf = _CiscoRpmXf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 440)
)
_CiscoOsm4oc3PosSmIr_ObjectIdentity = ObjectIdentity
ciscoOsm4oc3PosSmIr = _CiscoOsm4oc3PosSmIr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 441)
)
_CiscoOsm4oc3PosMmSr_ObjectIdentity = ObjectIdentity
ciscoOsm4oc3PosMmSr = _CiscoOsm4oc3PosMmSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 442)
)
_CiscoOsm4oc3PosSmLr_ObjectIdentity = ObjectIdentity
ciscoOsm4oc3PosSmLr = _CiscoOsm4oc3PosSmLr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 443)
)
_Cisco1721_ObjectIdentity = ObjectIdentity
cisco1721 = _Cisco1721_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 444)
)
_Cat4000Sup3_ObjectIdentity = ObjectIdentity
cat4000Sup3 = _Cat4000Sup3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 445)
)
_Cisco827H_ObjectIdentity = ObjectIdentity
cisco827H = _Cisco827H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 446)
)
_CiscoSOHO77H_ObjectIdentity = ObjectIdentity
ciscoSOHO77H = _CiscoSOHO77H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 447)
)
_Cat4006_ObjectIdentity = ObjectIdentity
cat4006 = _Cat4006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 448)
)
_CiscoWSC6503_ObjectIdentity = ObjectIdentity
ciscoWSC6503 = _CiscoWSC6503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 449)
)
_CiscoPIXFirewall506E_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall506E = _CiscoPIXFirewall506E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 450)
)
_CiscoPIXFirewall515E_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall515E = _CiscoPIXFirewall515E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 451)
)
_Cat355024Dc_ObjectIdentity = ObjectIdentity
cat355024Dc = _Cat355024Dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 452)
)
_Cat355024Mmf_ObjectIdentity = ObjectIdentity
cat355024Mmf = _Cat355024Mmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 453)
)
_CiscoCE2636_ObjectIdentity = ObjectIdentity
ciscoCE2636 = _CiscoCE2636_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 454)
)
_CiscoDwCE_ObjectIdentity = ObjectIdentity
ciscoDwCE = _CiscoDwCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 455)
)
_Cisco7750Mrp300_ObjectIdentity = ObjectIdentity
cisco7750Mrp300 = _Cisco7750Mrp300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 456)
)
_CiscoRPMPR_ObjectIdentity = ObjectIdentity
ciscoRPMPR = _CiscoRPMPR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 457)
)
_Cisco14MGX8830Pxm1E_ObjectIdentity = ObjectIdentity
cisco14MGX8830Pxm1E = _Cisco14MGX8830Pxm1E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 458)
)
_CiscoWlse_ObjectIdentity = ObjectIdentity
ciscoWlse = _CiscoWlse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 459)
)
_CiscoONS15530_ObjectIdentity = ObjectIdentity
ciscoONS15530 = _CiscoONS15530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 460)
)
_CiscoONS15530NEBS_ObjectIdentity = ObjectIdentity
ciscoONS15530NEBS = _CiscoONS15530NEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 461)
)
_CiscoONS15530ETSI_ObjectIdentity = ObjectIdentity
ciscoONS15530ETSI = _CiscoONS15530ETSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 462)
)
_CiscoSOHO71_ObjectIdentity = ObjectIdentity
ciscoSOHO71 = _CiscoSOHO71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 463)
)
_Cisco6400UAC_ObjectIdentity = ObjectIdentity
cisco6400UAC = _Cisco6400UAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 464)
)
_Cisco2610XM_ObjectIdentity = ObjectIdentity
cisco2610XM = _Cisco2610XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 466)
)
_Cisco2611XM_ObjectIdentity = ObjectIdentity
cisco2611XM = _Cisco2611XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 467)
)
_Cisco2620XM_ObjectIdentity = ObjectIdentity
cisco2620XM = _Cisco2620XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 468)
)
_Cisco2621XM_ObjectIdentity = ObjectIdentity
cisco2621XM = _Cisco2621XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 469)
)
_Cisco2650XM_ObjectIdentity = ObjectIdentity
cisco2650XM = _Cisco2650XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 470)
)
_Cisco2651XM_ObjectIdentity = ObjectIdentity
cisco2651XM = _Cisco2651XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 471)
)
_Catalyst295024GDC_ObjectIdentity = ObjectIdentity
catalyst295024GDC = _Catalyst295024GDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 472)
)
_CiscoAIRAP1200_ObjectIdentity = ObjectIdentity
ciscoAIRAP1200 = _CiscoAIRAP1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 474)
)
_CiscoSN5428_ObjectIdentity = ObjectIdentity
ciscoSN5428 = _CiscoSN5428_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 475)
)
_Cisco7301_ObjectIdentity = ObjectIdentity
cisco7301 = _Cisco7301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 476)
)
_Cisco12816_ObjectIdentity = ObjectIdentity
cisco12816 = _Cisco12816_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 477)
)
_Cisco12810_ObjectIdentity = ObjectIdentity
cisco12810 = _Cisco12810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 478)
)
_Cisco3250_ObjectIdentity = ObjectIdentity
cisco3250 = _Cisco3250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 479)
)
_Catalyst295024SX_ObjectIdentity = ObjectIdentity
catalyst295024SX = _Catalyst295024SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 480)
)
_CiscoONS15540ESPx_ObjectIdentity = ObjectIdentity
ciscoONS15540ESPx = _CiscoONS15540ESPx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 481)
)
_Catalyst295024LRESt_ObjectIdentity = ObjectIdentity
catalyst295024LRESt = _Catalyst295024LRESt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 482)
)
_Catalyst29508LRESt_ObjectIdentity = ObjectIdentity
catalyst29508LRESt = _Catalyst29508LRESt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 483)
)
_Catalyst295024LREG_ObjectIdentity = ObjectIdentity
catalyst295024LREG = _Catalyst295024LREG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 484)
)
_Catalyst355024PWR_ObjectIdentity = ObjectIdentity
catalyst355024PWR = _Catalyst355024PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 485)
)
_CiscoCDM4630_ObjectIdentity = ObjectIdentity
ciscoCDM4630 = _CiscoCDM4630_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 486)
)
_CiscoCDM4650_ObjectIdentity = ObjectIdentity
ciscoCDM4650 = _CiscoCDM4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 487)
)
_Catalyst2955T12_ObjectIdentity = ObjectIdentity
catalyst2955T12 = _Catalyst2955T12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 488)
)
_Catalyst2955C12_ObjectIdentity = ObjectIdentity
catalyst2955C12 = _Catalyst2955C12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 489)
)
_CiscoCE508_ObjectIdentity = ObjectIdentity
ciscoCE508 = _CiscoCE508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 490)
)
_CiscoCE565_ObjectIdentity = ObjectIdentity
ciscoCE565 = _CiscoCE565_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 491)
)
_CiscoCE7325_ObjectIdentity = ObjectIdentity
ciscoCE7325 = _CiscoCE7325_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 492)
)
_CiscoONS15454_ObjectIdentity = ObjectIdentity
ciscoONS15454 = _CiscoONS15454_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 493)
)
_CiscoONS15327_ObjectIdentity = ObjectIdentity
ciscoONS15327 = _CiscoONS15327_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 494)
)
_Cisco837_ObjectIdentity = ObjectIdentity
cisco837 = _Cisco837_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 495)
)
_CiscoSOHO97_ObjectIdentity = ObjectIdentity
ciscoSOHO97 = _CiscoSOHO97_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 496)
)
_Cisco831_ObjectIdentity = ObjectIdentity
cisco831 = _Cisco831_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 497)
)
_CiscoSOHO91_ObjectIdentity = ObjectIdentity
ciscoSOHO91 = _CiscoSOHO91_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 498)
)
_Cisco836_ObjectIdentity = ObjectIdentity
cisco836 = _Cisco836_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 499)
)
_CiscoSOHO96_ObjectIdentity = ObjectIdentity
ciscoSOHO96 = _CiscoSOHO96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 500)
)
_Cat4507_ObjectIdentity = ObjectIdentity
cat4507 = _Cat4507_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 501)
)
_Cat4506_ObjectIdentity = ObjectIdentity
cat4506 = _Cat4506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 502)
)
_Cat4503_ObjectIdentity = ObjectIdentity
cat4503 = _Cat4503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 503)
)
_CiscoCE7305_ObjectIdentity = ObjectIdentity
ciscoCE7305 = _CiscoCE7305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 504)
)
_CiscoCE510_ObjectIdentity = ObjectIdentity
ciscoCE510 = _CiscoCE510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 505)
)
_CiscoAIRAP1100_ObjectIdentity = ObjectIdentity
ciscoAIRAP1100 = _CiscoAIRAP1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 507)
)
_Catalyst2955S12_ObjectIdentity = ObjectIdentity
catalyst2955S12 = _Catalyst2955S12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 508)
)
_Cisco7609_ObjectIdentity = ObjectIdentity
cisco7609 = _Cisco7609_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 509)
)
_CiscoWSC65509_ObjectIdentity = ObjectIdentity
ciscoWSC65509 = _CiscoWSC65509_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 510)
)
_Catalyst375024_ObjectIdentity = ObjectIdentity
catalyst375024 = _Catalyst375024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 511)
)
_Catalyst375048_ObjectIdentity = ObjectIdentity
catalyst375048 = _Catalyst375048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 512)
)
_Catalyst375024TS_ObjectIdentity = ObjectIdentity
catalyst375024TS = _Catalyst375024TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 513)
)
_Catalyst375024T_ObjectIdentity = ObjectIdentity
catalyst375024T = _Catalyst375024T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 514)
)
_Catalyst37xxStack_ObjectIdentity = ObjectIdentity
catalyst37xxStack = _Catalyst37xxStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 516)
)
_CiscoGSS_ObjectIdentity = ObjectIdentity
ciscoGSS = _CiscoGSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 517)
)
_CiscoPrimaryGSSM_ObjectIdentity = ObjectIdentity
ciscoPrimaryGSSM = _CiscoPrimaryGSSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 518)
)
_CiscoStandbyGSSM_ObjectIdentity = ObjectIdentity
ciscoStandbyGSSM = _CiscoStandbyGSSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 519)
)
_CiscoMWR1941DC_ObjectIdentity = ObjectIdentity
ciscoMWR1941DC = _CiscoMWR1941DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 520)
)
_CiscoDSC9216K9_ObjectIdentity = ObjectIdentity
ciscoDSC9216K9 = _CiscoDSC9216K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 521)
)
_Cat6500FirewallSm_ObjectIdentity = ObjectIdentity
cat6500FirewallSm = _Cat6500FirewallSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 522)
)
_CiscoSCA11000_ObjectIdentity = ObjectIdentity
ciscoSCA11000 = _CiscoSCA11000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 523)
)
_CiscoCSM_ObjectIdentity = ObjectIdentity
ciscoCSM = _CiscoCSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 524)
)
_CiscoAIRAP1210_ObjectIdentity = ObjectIdentity
ciscoAIRAP1210 = _CiscoAIRAP1210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 525)
)
_CiscoSCA211000_ObjectIdentity = ObjectIdentity
ciscoSCA211000 = _CiscoSCA211000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 526)
)
_Catalyst297024_ObjectIdentity = ObjectIdentity
catalyst297024 = _Catalyst297024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 527)
)
_Cisco7613_ObjectIdentity = ObjectIdentity
cisco7613 = _Cisco7613_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 528)
)
_CiscoSN54282_ObjectIdentity = ObjectIdentity
ciscoSN54282 = _CiscoSN54282_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 529)
)
_Catalyst3750Ge12Sfp_ObjectIdentity = ObjectIdentity
catalyst3750Ge12Sfp = _Catalyst3750Ge12Sfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 530)
)
_CiscoCR4430_ObjectIdentity = ObjectIdentity
ciscoCR4430 = _CiscoCR4430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 531)
)
_CiscoCR4450_ObjectIdentity = ObjectIdentity
ciscoCR4450 = _CiscoCR4450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 532)
)
_CiscoAIRBR1410_ObjectIdentity = ObjectIdentity
ciscoAIRBR1410 = _CiscoAIRBR1410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 533)
)
_CiscoWSC6509neba_ObjectIdentity = ObjectIdentity
ciscoWSC6509neba = _CiscoWSC6509neba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 534)
)
_Catalyst375048PS_ObjectIdentity = ObjectIdentity
catalyst375048PS = _Catalyst375048PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 535)
)
_Catalyst375024PS_ObjectIdentity = ObjectIdentity
catalyst375024PS = _Catalyst375024PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 536)
)
_Catalyst4510_ObjectIdentity = ObjectIdentity
catalyst4510 = _Catalyst4510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 537)
)
_Cisco1711_ObjectIdentity = ObjectIdentity
cisco1711 = _Cisco1711_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 538)
)
_Cisco1712_ObjectIdentity = ObjectIdentity
cisco1712 = _Cisco1712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 539)
)
_Catalyst29408TT_ObjectIdentity = ObjectIdentity
catalyst29408TT = _Catalyst29408TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 540)
)
_Catalyst29408TF_ObjectIdentity = ObjectIdentity
catalyst29408TF = _Catalyst29408TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 542)
)
_Cisco3825_ObjectIdentity = ObjectIdentity
cisco3825 = _Cisco3825_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 543)
)
_Cisco3845_ObjectIdentity = ObjectIdentity
cisco3845 = _Cisco3845_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 544)
)
_Cisco2430Iad24Fxs_ObjectIdentity = ObjectIdentity
cisco2430Iad24Fxs = _Cisco2430Iad24Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 545)
)
_Cisco2431Iad8Fxs_ObjectIdentity = ObjectIdentity
cisco2431Iad8Fxs = _Cisco2431Iad8Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 546)
)
_Cisco2431Iad16Fxs_ObjectIdentity = ObjectIdentity
cisco2431Iad16Fxs = _Cisco2431Iad16Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 547)
)
_Cisco2431Iad1T1E1_ObjectIdentity = ObjectIdentity
cisco2431Iad1T1E1 = _Cisco2431Iad1T1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 548)
)
_Cisco2432Iad24Fxs_ObjectIdentity = ObjectIdentity
cisco2432Iad24Fxs = _Cisco2432Iad24Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 549)
)
_Cisco1701ADSLBRI_ObjectIdentity = ObjectIdentity
cisco1701ADSLBRI = _Cisco1701ADSLBRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 550)
)
_Catalyst2950St24LRE997_ObjectIdentity = ObjectIdentity
catalyst2950St24LRE997 = _Catalyst2950St24LRE997_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 551)
)
_CiscoAirAp350IOS_ObjectIdentity = ObjectIdentity
ciscoAirAp350IOS = _CiscoAirAp350IOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 552)
)
_Cisco3220_ObjectIdentity = ObjectIdentity
cisco3220 = _Cisco3220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 553)
)
_Cat6500SslSm_ObjectIdentity = ObjectIdentity
cat6500SslSm = _Cat6500SslSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 554)
)
_CiscoSIMSE_ObjectIdentity = ObjectIdentity
ciscoSIMSE = _CiscoSIMSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 555)
)
_CiscoESSE_ObjectIdentity = ObjectIdentity
ciscoESSE = _CiscoESSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 556)
)
_Catalyst6kSup720_ObjectIdentity = ObjectIdentity
catalyst6kSup720 = _Catalyst6kSup720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 557)
)
_CiscoVG224_ObjectIdentity = ObjectIdentity
ciscoVG224 = _CiscoVG224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 558)
)
_Catalyst295048T_ObjectIdentity = ObjectIdentity
catalyst295048T = _Catalyst295048T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 559)
)
_Catalyst295048SX_ObjectIdentity = ObjectIdentity
catalyst295048SX = _Catalyst295048SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 560)
)
_Catalyst297024TS_ObjectIdentity = ObjectIdentity
catalyst297024TS = _Catalyst297024TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 561)
)
_CiscoNmNam_ObjectIdentity = ObjectIdentity
ciscoNmNam = _CiscoNmNam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 562)
)
_Catalyst356024PS_ObjectIdentity = ObjectIdentity
catalyst356024PS = _Catalyst356024PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 563)
)
_Catalyst356048PS_ObjectIdentity = ObjectIdentity
catalyst356048PS = _Catalyst356048PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 564)
)
_CiscoAIRBR1300_ObjectIdentity = ObjectIdentity
ciscoAIRBR1300 = _CiscoAIRBR1300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 565)
)
_Cisco851_ObjectIdentity = ObjectIdentity
cisco851 = _Cisco851_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 566)
)
_Cisco857_ObjectIdentity = ObjectIdentity
cisco857 = _Cisco857_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 567)
)
_Cisco876_ObjectIdentity = ObjectIdentity
cisco876 = _Cisco876_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 568)
)
_Cisco877_ObjectIdentity = ObjectIdentity
cisco877 = _Cisco877_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 569)
)
_Cisco878_ObjectIdentity = ObjectIdentity
cisco878 = _Cisco878_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 570)
)
_Cisco871_ObjectIdentity = ObjectIdentity
cisco871 = _Cisco871_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 571)
)
_UMG9820_ObjectIdentity = ObjectIdentity
uMG9820 = _UMG9820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 572)
)
_Catalyst6kGateway_ObjectIdentity = ObjectIdentity
catalyst6kGateway = _Catalyst6kGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 573)
)
_Catalyst375024ME_ObjectIdentity = ObjectIdentity
catalyst375024ME = _Catalyst375024ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 574)
)
_Catalyst4000NAM_ObjectIdentity = ObjectIdentity
catalyst4000NAM = _Catalyst4000NAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 575)
)
_Cisco2811_ObjectIdentity = ObjectIdentity
cisco2811 = _Cisco2811_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 576)
)
_Cisco2821_ObjectIdentity = ObjectIdentity
cisco2821 = _Cisco2821_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 577)
)
_Cisco2851_ObjectIdentity = ObjectIdentity
cisco2851 = _Cisco2851_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 578)
)
_Cisco3201WMIC_ObjectIdentity = ObjectIdentity
cisco3201WMIC = _Cisco3201WMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 581)
)
_CiscoMCS7815I_ObjectIdentity = ObjectIdentity
ciscoMCS7815I = _CiscoMCS7815I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 582)
)
_CiscoMCS7825H_ObjectIdentity = ObjectIdentity
ciscoMCS7825H = _CiscoMCS7825H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 583)
)
_CiscoMCS7835H_ObjectIdentity = ObjectIdentity
ciscoMCS7835H = _CiscoMCS7835H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 584)
)
_CiscoMCS7835I_ObjectIdentity = ObjectIdentity
ciscoMCS7835I = _CiscoMCS7835I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 585)
)
_CiscoMCS7845H_ObjectIdentity = ObjectIdentity
ciscoMCS7845H = _CiscoMCS7845H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 586)
)
_CiscoMCS7845I_ObjectIdentity = ObjectIdentity
ciscoMCS7845I = _CiscoMCS7845I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 587)
)
_CiscoMCS7855I_ObjectIdentity = ObjectIdentity
ciscoMCS7855I = _CiscoMCS7855I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 588)
)
_CiscoMCS7865I_ObjectIdentity = ObjectIdentity
ciscoMCS7865I = _CiscoMCS7865I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 589)
)
_Cisco12006_ObjectIdentity = ObjectIdentity
cisco12006 = _Cisco12006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 590)
)
_Catalyst3750G16TD_ObjectIdentity = ObjectIdentity
catalyst3750G16TD = _Catalyst3750G16TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 591)
)
_CiscoIGESM_ObjectIdentity = ObjectIdentity
ciscoIGESM = _CiscoIGESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 592)
)
_CiscoCCM_ObjectIdentity = ObjectIdentity
ciscoCCM = _CiscoCCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 593)
)
_Cisco1718_ObjectIdentity = ObjectIdentity
cisco1718 = _Cisco1718_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 594)
)
_CiscoCe511K9_ObjectIdentity = ObjectIdentity
ciscoCe511K9 = _CiscoCe511K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 595)
)
_CiscoCe566K9_ObjectIdentity = ObjectIdentity
ciscoCe566K9 = _CiscoCe566K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 596)
)
_CiscoMGX8830Pxm45_ObjectIdentity = ObjectIdentity
ciscoMGX8830Pxm45 = _CiscoMGX8830Pxm45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 597)
)
_CiscoMGX8880_ObjectIdentity = ObjectIdentity
ciscoMGX8880 = _CiscoMGX8880_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 598)
)
_CiscoWsSvcWLAN1K9_ObjectIdentity = ObjectIdentity
ciscoWsSvcWLAN1K9 = _CiscoWsSvcWLAN1K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 599)
)
_CiscoCe7306K9_ObjectIdentity = ObjectIdentity
ciscoCe7306K9 = _CiscoCe7306K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 600)
)
_CiscoCe7326K9_ObjectIdentity = ObjectIdentity
ciscoCe7326K9 = _CiscoCe7326K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 601)
)
_Catalyst3750G24PS_ObjectIdentity = ObjectIdentity
catalyst3750G24PS = _Catalyst3750G24PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 602)
)
_Catalyst3750G48PS_ObjectIdentity = ObjectIdentity
catalyst3750G48PS = _Catalyst3750G48PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 603)
)
_Catalyst3750G48TS_ObjectIdentity = ObjectIdentity
catalyst3750G48TS = _Catalyst3750G48TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 604)
)
_CiscoBMGX8830Pxm45_ObjectIdentity = ObjectIdentity
ciscoBMGX8830Pxm45 = _CiscoBMGX8830Pxm45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 606)
)
_CiscoBMGX8830Pxm1E_ObjectIdentity = ObjectIdentity
ciscoBMGX8830Pxm1E = _CiscoBMGX8830Pxm1E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 607)
)
_CiscoBMGX8850Pxm45_ObjectIdentity = ObjectIdentity
ciscoBMGX8850Pxm45 = _CiscoBMGX8850Pxm45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 608)
)
_CiscoBMGX8850Pxm1E_ObjectIdentity = ObjectIdentity
ciscoBMGX8850Pxm1E = _CiscoBMGX8850Pxm1E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 609)
)
_CiscoSSLCSM_ObjectIdentity = ObjectIdentity
ciscoSSLCSM = _CiscoSSLCSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 610)
)
_CiscoNetworkRegistrar_ObjectIdentity = ObjectIdentity
ciscoNetworkRegistrar = _CiscoNetworkRegistrar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 611)
)
_CiscoCe501K9_ObjectIdentity = ObjectIdentity
ciscoCe501K9 = _CiscoCe501K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 612)
)
_CiscoCRS16S_ObjectIdentity = ObjectIdentity
ciscoCRS16S = _CiscoCRS16S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 613)
)
_Catalyst3560G24PS_ObjectIdentity = ObjectIdentity
catalyst3560G24PS = _Catalyst3560G24PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 614)
)
_Catalyst3560G24TS_ObjectIdentity = ObjectIdentity
catalyst3560G24TS = _Catalyst3560G24TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 615)
)
_Catalyst3560G48PS_ObjectIdentity = ObjectIdentity
catalyst3560G48PS = _Catalyst3560G48PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 616)
)
_Catalyst3560G48TS_ObjectIdentity = ObjectIdentity
catalyst3560G48TS = _Catalyst3560G48TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 617)
)
_CiscoAIRAP1130_ObjectIdentity = ObjectIdentity
ciscoAIRAP1130 = _CiscoAIRAP1130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 618)
)
_Cisco2801_ObjectIdentity = ObjectIdentity
cisco2801 = _Cisco2801_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 619)
)
_Cisco1841_ObjectIdentity = ObjectIdentity
cisco1841 = _Cisco1841_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 620)
)
_CiscoWsSvcMWAM1_ObjectIdentity = ObjectIdentity
ciscoWsSvcMWAM1 = _CiscoWsSvcMWAM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 621)
)
_CiscoNMCUE_ObjectIdentity = ObjectIdentity
ciscoNMCUE = _CiscoNMCUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 622)
)
_CiscoAIMCUE_ObjectIdentity = ObjectIdentity
ciscoAIMCUE = _CiscoAIMCUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 623)
)
_Catalyst3750G24TS1U_ObjectIdentity = ObjectIdentity
catalyst3750G24TS1U = _Catalyst3750G24TS1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 624)
)
_Cisco371098HP001_ObjectIdentity = ObjectIdentity
cisco371098HP001 = _Cisco371098HP001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 625)
)
_Catalyst4948_ObjectIdentity = ObjectIdentity
catalyst4948 = _Catalyst4948_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 626)
)
_CiscoSB101_ObjectIdentity = ObjectIdentity
ciscoSB101 = _CiscoSB101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 627)
)
_CiscoSB106_ObjectIdentity = ObjectIdentity
ciscoSB106 = _CiscoSB106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 628)
)
_CiscoSB107_ObjectIdentity = ObjectIdentity
ciscoSB107 = _CiscoSB107_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 629)
)
_CiscoWLSE1130_ObjectIdentity = ObjectIdentity
ciscoWLSE1130 = _CiscoWLSE1130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 630)
)
_CiscoWLSE1030_ObjectIdentity = ObjectIdentity
ciscoWLSE1030 = _CiscoWLSE1030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 631)
)
_CiscoHSE1140_ObjectIdentity = ObjectIdentity
ciscoHSE1140 = _CiscoHSE1140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 632)
)
_Catalyst356024TS_ObjectIdentity = ObjectIdentity
catalyst356024TS = _Catalyst356024TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 633)
)
_Catalyst356048TS_ObjectIdentity = ObjectIdentity
catalyst356048TS = _Catalyst356048TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 634)
)
_CiscoWsSvcadsm1K9_ObjectIdentity = ObjectIdentity
ciscoWsSvcadsm1K9 = _CiscoWsSvcadsm1K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 635)
)
_CiscoWsSvcagsm1K9_ObjectIdentity = ObjectIdentity
ciscoWsSvcagsm1K9 = _CiscoWsSvcagsm1K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 636)
)
_CiscoONS15310_ObjectIdentity = ObjectIdentity
ciscoONS15310 = _CiscoONS15310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 637)
)
_Cisco1801_ObjectIdentity = ObjectIdentity
cisco1801 = _Cisco1801_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 638)
)
_Cisco1802_ObjectIdentity = ObjectIdentity
cisco1802 = _Cisco1802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 639)
)
_Cisco1803_ObjectIdentity = ObjectIdentity
cisco1803 = _Cisco1803_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 640)
)
_Cisco1811_ObjectIdentity = ObjectIdentity
cisco1811 = _Cisco1811_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 641)
)
_Cisco1812_ObjectIdentity = ObjectIdentity
cisco1812 = _Cisco1812_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 642)
)
_CiscoCRS8S_ObjectIdentity = ObjectIdentity
ciscoCRS8S = _CiscoCRS8S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 643)
)
_CiscoIDS4210_ObjectIdentity = ObjectIdentity
ciscoIDS4210 = _CiscoIDS4210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 645)
)
_CiscoIDS4215_ObjectIdentity = ObjectIdentity
ciscoIDS4215 = _CiscoIDS4215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 646)
)
_CiscoIDS4235_ObjectIdentity = ObjectIdentity
ciscoIDS4235 = _CiscoIDS4235_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 647)
)
_CiscoIPS4240_ObjectIdentity = ObjectIdentity
ciscoIPS4240 = _CiscoIPS4240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 648)
)
_CiscoIDS4250_ObjectIdentity = ObjectIdentity
ciscoIDS4250 = _CiscoIDS4250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 649)
)
_CiscoIDS4250SX_ObjectIdentity = ObjectIdentity
ciscoIDS4250SX = _CiscoIDS4250SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 650)
)
_CiscoIDS4250XL_ObjectIdentity = ObjectIdentity
ciscoIDS4250XL = _CiscoIDS4250XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 651)
)
_CiscoIPS4255_ObjectIdentity = ObjectIdentity
ciscoIPS4255 = _CiscoIPS4255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 652)
)
_CiscoIDSIDSM2_ObjectIdentity = ObjectIdentity
ciscoIDSIDSM2 = _CiscoIDSIDSM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 653)
)
_CiscoIDSNMCIDS_ObjectIdentity = ObjectIdentity
ciscoIDSNMCIDS = _CiscoIDSNMCIDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 654)
)
_CiscoIPSSSM20_ObjectIdentity = ObjectIdentity
ciscoIPSSSM20 = _CiscoIPSSSM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 655)
)
_Catalyst375024FS_ObjectIdentity = ObjectIdentity
catalyst375024FS = _Catalyst375024FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 656)
)
_CiscoWSC6504E_ObjectIdentity = ObjectIdentity
ciscoWSC6504E = _CiscoWSC6504E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 657)
)
_Cisco7604_ObjectIdentity = ObjectIdentity
cisco7604 = _Cisco7604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 658)
)
_Catalyst494810GE_ObjectIdentity = ObjectIdentity
catalyst494810GE = _Catalyst494810GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 659)
)
_CiscoIGESMSFP_ObjectIdentity = ObjectIdentity
ciscoIGESMSFP = _CiscoIGESMSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 660)
)
_CiscoFE6326K9_ObjectIdentity = ObjectIdentity
ciscoFE6326K9 = _CiscoFE6326K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 661)
)
_CiscoIPSSSM10_ObjectIdentity = ObjectIdentity
ciscoIPSSSM10 = _CiscoIPSSSM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 662)
)
_CiscoNme16Es1Ge_ObjectIdentity = ObjectIdentity
ciscoNme16Es1Ge = _CiscoNme16Es1Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 663)
)
_CiscoNmeX24Es1Ge_ObjectIdentity = ObjectIdentity
ciscoNmeX24Es1Ge = _CiscoNmeX24Es1Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 664)
)
_CiscoNmeXd24Es2St_ObjectIdentity = ObjectIdentity
ciscoNmeXd24Es2St = _CiscoNmeXd24Es2St_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 665)
)
_CiscoNmeXd48Es2Ge_ObjectIdentity = ObjectIdentity
ciscoNmeXd48Es2Ge = _CiscoNmeXd48Es2Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 666)
)
_Cisco3202WMIC_ObjectIdentity = ObjectIdentity
cisco3202WMIC = _Cisco3202WMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 667)
)
_CiscoAs5400XM_ObjectIdentity = ObjectIdentity
ciscoAs5400XM = _CiscoAs5400XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 668)
)
_CiscoASA5510_ObjectIdentity = ObjectIdentity
ciscoASA5510 = _CiscoASA5510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 669)
)
_CiscoASA5520_ObjectIdentity = ObjectIdentity
ciscoASA5520 = _CiscoASA5520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 670)
)
_CiscoASA5520sc_ObjectIdentity = ObjectIdentity
ciscoASA5520sc = _CiscoASA5520sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 671)
)
_CiscoASA5540_ObjectIdentity = ObjectIdentity
ciscoASA5540 = _CiscoASA5540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 672)
)
_CiscoASA5540sc_ObjectIdentity = ObjectIdentity
ciscoASA5540sc = _CiscoASA5540sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 673)
)
_CiscoWsSvcFwm1sc_ObjectIdentity = ObjectIdentity
ciscoWsSvcFwm1sc = _CiscoWsSvcFwm1sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 674)
)
_CiscoPIXFirewall535sc_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall535sc = _CiscoPIXFirewall535sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 675)
)
_CiscoPIXFirewall525sc_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall525sc = _CiscoPIXFirewall525sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 676)
)
_CiscoPIXFirewall515Esc_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall515Esc = _CiscoPIXFirewall515Esc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 677)
)
_CiscoPIXFirewall515sc_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall515sc = _CiscoPIXFirewall515sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 678)
)
_CiscoAs5350XM_ObjectIdentity = ObjectIdentity
ciscoAs5350XM = _CiscoAs5350XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 679)
)
_CiscoFe7326K9_ObjectIdentity = ObjectIdentity
ciscoFe7326K9 = _CiscoFe7326K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 680)
)
_CiscoFe511K9_ObjectIdentity = ObjectIdentity
ciscoFe511K9 = _CiscoFe511K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 681)
)
_CiscoSCEDispatcher_ObjectIdentity = ObjectIdentity
ciscoSCEDispatcher = _CiscoSCEDispatcher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 682)
)
_CiscoSCE1000_ObjectIdentity = ObjectIdentity
ciscoSCE1000 = _CiscoSCE1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 683)
)
_CiscoSCE2000_ObjectIdentity = ObjectIdentity
ciscoSCE2000 = _CiscoSCE2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 684)
)
_CiscoAIRAP1240_ObjectIdentity = ObjectIdentity
ciscoAIRAP1240 = _CiscoAIRAP1240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 685)
)
_CiscoDSC9120CLK9_ObjectIdentity = ObjectIdentity
ciscoDSC9120CLK9 = _CiscoDSC9120CLK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 686)
)
_CiscoFe611K9_ObjectIdentity = ObjectIdentity
ciscoFe611K9 = _CiscoFe611K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 687)
)
_Catalyst3750Ge12SfpDc_ObjectIdentity = ObjectIdentity
catalyst3750Ge12SfpDc = _Catalyst3750Ge12SfpDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 688)
)
_Cisco3271_ObjectIdentity = ObjectIdentity
cisco3271 = _Cisco3271_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 689)
)
_Cisco3272_ObjectIdentity = ObjectIdentity
cisco3272 = _Cisco3272_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 690)
)
_Cisco3241_ObjectIdentity = ObjectIdentity
cisco3241 = _Cisco3241_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 691)
)
_Cisco3242_ObjectIdentity = ObjectIdentity
cisco3242 = _Cisco3242_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 692)
)
_CiscoICM_ObjectIdentity = ObjectIdentity
ciscoICM = _CiscoICM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 693)
)
_Catalyst296024_ObjectIdentity = ObjectIdentity
catalyst296024 = _Catalyst296024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 694)
)
_Catalyst296048_ObjectIdentity = ObjectIdentity
catalyst296048 = _Catalyst296048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 695)
)
_Catalyst2960G24_ObjectIdentity = ObjectIdentity
catalyst2960G24 = _Catalyst2960G24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 696)
)
_Catalyst2960G48_ObjectIdentity = ObjectIdentity
catalyst2960G48 = _Catalyst2960G48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 697)
)
_Catalyst45503_ObjectIdentity = ObjectIdentity
catalyst45503 = _Catalyst45503_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 698)
)
_Catalyst45506_ObjectIdentity = ObjectIdentity
catalyst45506 = _Catalyst45506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 699)
)
_Catalyst45507_ObjectIdentity = ObjectIdentity
catalyst45507 = _Catalyst45507_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 700)
)
_Catalyst455010_ObjectIdentity = ObjectIdentity
catalyst455010 = _Catalyst455010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 701)
)
_CiscoNme16Es1GeNoPwr_ObjectIdentity = ObjectIdentity
ciscoNme16Es1GeNoPwr = _CiscoNme16Es1GeNoPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 702)
)
_CiscoNmeX24Es1GeNoPwr_ObjectIdentity = ObjectIdentity
ciscoNmeX24Es1GeNoPwr = _CiscoNmeX24Es1GeNoPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 703)
)
_CiscoNmeXd24Es2StNoPwr_ObjectIdentity = ObjectIdentity
ciscoNmeXd24Es2StNoPwr = _CiscoNmeXd24Es2StNoPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 704)
)
_CiscoNmeXd48Es2GeNoPwr_ObjectIdentity = ObjectIdentity
ciscoNmeXd48Es2GeNoPwr = _CiscoNmeXd48Es2GeNoPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 705)
)
_Catalyst6kMsfc2a_ObjectIdentity = ObjectIdentity
catalyst6kMsfc2a = _Catalyst6kMsfc2a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 706)
)
_CiscoEDI_ObjectIdentity = ObjectIdentity
ciscoEDI = _CiscoEDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 707)
)
_CiscoCe611K9_ObjectIdentity = ObjectIdentity
ciscoCe611K9 = _CiscoCe611K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 708)
)
_CiscoWLSEs20_ObjectIdentity = ObjectIdentity
ciscoWLSEs20 = _CiscoWLSEs20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 709)
)
_CiscoMPX_ObjectIdentity = ObjectIdentity
ciscoMPX = _CiscoMPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 710)
)
_CiscoNMCUEEC_ObjectIdentity = ObjectIdentity
ciscoNMCUEEC = _CiscoNMCUEEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 711)
)
_CiscoWLSE1132_ObjectIdentity = ObjectIdentity
ciscoWLSE1132 = _CiscoWLSE1132_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 712)
)
_CiscoME6340ACA_ObjectIdentity = ObjectIdentity
ciscoME6340ACA = _CiscoME6340ACA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 713)
)
_CiscoME6340DCA_ObjectIdentity = ObjectIdentity
ciscoME6340DCA = _CiscoME6340DCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 714)
)
_CiscoME6340DCB_ObjectIdentity = ObjectIdentity
ciscoME6340DCB = _CiscoME6340DCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 715)
)
_Catalyst296024TT_ObjectIdentity = ObjectIdentity
catalyst296024TT = _Catalyst296024TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 716)
)
_Catalyst296048TT_ObjectIdentity = ObjectIdentity
catalyst296048TT = _Catalyst296048TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 717)
)
_CiscoIGESMSFPT_ObjectIdentity = ObjectIdentity
ciscoIGESMSFPT = _CiscoIGESMSFPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 718)
)
_CiscoMEC6524gs8s_ObjectIdentity = ObjectIdentity
ciscoMEC6524gs8s = _CiscoMEC6524gs8s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 719)
)
_CiscoMEC6524gt8s_ObjectIdentity = ObjectIdentity
ciscoMEC6524gt8s = _CiscoMEC6524gt8s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 720)
)
_CiscoMEC6724s10x2_ObjectIdentity = ObjectIdentity
ciscoMEC6724s10x2 = _CiscoMEC6724s10x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 721)
)
_CiscoMEC6724t10x2_ObjectIdentity = ObjectIdentity
ciscoMEC6724t10x2 = _CiscoMEC6724t10x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 722)
)
_CiscoPaldron_ObjectIdentity = ObjectIdentity
ciscoPaldron = _CiscoPaldron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 723)
)
_CatalystsExpress50024TT_ObjectIdentity = ObjectIdentity
catalystsExpress50024TT = _CatalystsExpress50024TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 724)
)
_CatalystsExpress50024LC_ObjectIdentity = ObjectIdentity
catalystsExpress50024LC = _CatalystsExpress50024LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 725)
)
_CatalystsExpress50024PC_ObjectIdentity = ObjectIdentity
catalystsExpress50024PC = _CatalystsExpress50024PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 726)
)
_CatalystsExpress50012TC_ObjectIdentity = ObjectIdentity
catalystsExpress50012TC = _CatalystsExpress50012TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 727)
)
_CiscoIGESMT_ObjectIdentity = ObjectIdentity
ciscoIGESMT = _CiscoIGESMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 728)
)
_CiscoACE04G_ObjectIdentity = ObjectIdentity
ciscoACE04G = _CiscoACE04G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 729)
)
_CiscoACE10K9_ObjectIdentity = ObjectIdentity
ciscoACE10K9 = _CiscoACE10K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 730)
)
_Cisco5750_ObjectIdentity = ObjectIdentity
cisco5750 = _Cisco5750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 731)
)
_CiscoMWR1941DCA_ObjectIdentity = ObjectIdentity
ciscoMWR1941DCA = _CiscoMWR1941DCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 732)
)
_Cisco815_ObjectIdentity = ObjectIdentity
cisco815 = _Cisco815_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 733)
)
_Cisco240024TSA_ObjectIdentity = ObjectIdentity
cisco240024TSA = _Cisco240024TSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 734)
)
_Cisco240024TSD_ObjectIdentity = ObjectIdentity
cisco240024TSD = _Cisco240024TSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 735)
)
_Cisco340024TSA_ObjectIdentity = ObjectIdentity
cisco340024TSA = _Cisco340024TSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 736)
)
_Cisco340024TSD_ObjectIdentity = ObjectIdentity
cisco340024TSD = _Cisco340024TSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 737)
)
_CiscoCrs18Linecard_ObjectIdentity = ObjectIdentity
ciscoCrs18Linecard = _CiscoCrs18Linecard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 738)
)
_CiscoCrs1Fabric_ObjectIdentity = ObjectIdentity
ciscoCrs1Fabric = _CiscoCrs1Fabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 739)
)
_CiscoFE2636_ObjectIdentity = ObjectIdentity
ciscoFE2636 = _CiscoFE2636_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 740)
)
_CiscoIDS4220_ObjectIdentity = ObjectIdentity
ciscoIDS4220 = _CiscoIDS4220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 741)
)
_CiscoIDS4230_ObjectIdentity = ObjectIdentity
ciscoIDS4230 = _CiscoIDS4230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 742)
)
_CiscoIPS4260_ObjectIdentity = ObjectIdentity
ciscoIPS4260 = _CiscoIPS4260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 743)
)
_CiscoWsSvcSAMIBB_ObjectIdentity = ObjectIdentity
ciscoWsSvcSAMIBB = _CiscoWsSvcSAMIBB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 744)
)
_CiscoASA5505_ObjectIdentity = ObjectIdentity
ciscoASA5505 = _CiscoASA5505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 745)
)
_CiscoMCS7825I_ObjectIdentity = ObjectIdentity
ciscoMCS7825I = _CiscoMCS7825I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 746)
)
_CiscoWsC3750g24ps_ObjectIdentity = ObjectIdentity
ciscoWsC3750g24ps = _CiscoWsC3750g24ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 747)
)
_CiscoWs3020Hpq_ObjectIdentity = ObjectIdentity
ciscoWs3020Hpq = _CiscoWs3020Hpq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 748)
)
_CiscoWs3030Del_ObjectIdentity = ObjectIdentity
ciscoWs3030Del = _CiscoWs3030Del_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 749)
)
_CiscoSpaOc48posSfp_ObjectIdentity = ObjectIdentity
ciscoSpaOc48posSfp = _CiscoSpaOc48posSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 750)
)
_Catalyst6kEnhancedGateway_ObjectIdentity = ObjectIdentity
catalyst6kEnhancedGateway = _Catalyst6kEnhancedGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 751)
)
_CiscoWLSE1133_ObjectIdentity = ObjectIdentity
ciscoWLSE1133 = _CiscoWLSE1133_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 752)
)
_CiscoASA5550_ObjectIdentity = ObjectIdentity
ciscoASA5550 = _CiscoASA5550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 753)
)
_CiscoNMAONK9_ObjectIdentity = ObjectIdentity
ciscoNMAONK9 = _CiscoNMAONK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 754)
)
_CiscoNMAONWS_ObjectIdentity = ObjectIdentity
ciscoNMAONWS = _CiscoNMAONWS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 755)
)
_CiscoNMAONAPS_ObjectIdentity = ObjectIdentity
ciscoNMAONAPS = _CiscoNMAONAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 756)
)
_CiscoWae612K9_ObjectIdentity = ObjectIdentity
ciscoWae612K9 = _CiscoWae612K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 757)
)
_CiscoAIRAP1250_ObjectIdentity = ObjectIdentity
ciscoAIRAP1250 = _CiscoAIRAP1250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 758)
)
_CiscoCe512K9_ObjectIdentity = ObjectIdentity
ciscoCe512K9 = _CiscoCe512K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 759)
)
_CiscoFe512K9_ObjectIdentity = ObjectIdentity
ciscoFe512K9 = _CiscoFe512K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 760)
)
_CiscoCe612K9_ObjectIdentity = ObjectIdentity
ciscoCe612K9 = _CiscoCe612K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 761)
)
_CiscoFe612K9_ObjectIdentity = ObjectIdentity
ciscoFe612K9 = _CiscoFe612K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 762)
)
_CiscoASA5550sc_ObjectIdentity = ObjectIdentity
ciscoASA5550sc = _CiscoASA5550sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 763)
)
_CiscoASA5520sy_ObjectIdentity = ObjectIdentity
ciscoASA5520sy = _CiscoASA5520sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 764)
)
_CiscoASA5540sy_ObjectIdentity = ObjectIdentity
ciscoASA5540sy = _CiscoASA5540sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 765)
)
_CiscoASA5550sy_ObjectIdentity = ObjectIdentity
ciscoASA5550sy = _CiscoASA5550sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 766)
)
_CiscoWsSvcFwm1sy_ObjectIdentity = ObjectIdentity
ciscoWsSvcFwm1sy = _CiscoWsSvcFwm1sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 767)
)
_CiscoPIXFirewall515sy_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall515sy = _CiscoPIXFirewall515sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 768)
)
_CiscoPIXFirewall515Esy_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall515Esy = _CiscoPIXFirewall515Esy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 769)
)
_CiscoPIXFirewall525sy_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall525sy = _CiscoPIXFirewall525sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 770)
)
_CiscoPIXFirewall535sy_ObjectIdentity = ObjectIdentity
ciscoPIXFirewall535sy = _CiscoPIXFirewall535sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 771)
)
_CiscoIpRanOpt4p_ObjectIdentity = ObjectIdentity
ciscoIpRanOpt4p = _CiscoIpRanOpt4p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 772)
)
_CiscoASA5510sc_ObjectIdentity = ObjectIdentity
ciscoASA5510sc = _CiscoASA5510sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 773)
)
_CiscoASA5510sy_ObjectIdentity = ObjectIdentity
ciscoASA5510sy = _CiscoASA5510sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 774)
)
_CiscoJumpgate_ObjectIdentity = ObjectIdentity
ciscoJumpgate = _CiscoJumpgate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 775)
)
_CiscoOe512K9_ObjectIdentity = ObjectIdentity
ciscoOe512K9 = _CiscoOe512K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 776)
)
_CiscoOe612K9_ObjectIdentity = ObjectIdentity
ciscoOe612K9 = _CiscoOe612K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 777)
)
_Catalyst3750G24WS25_ObjectIdentity = ObjectIdentity
catalyst3750G24WS25 = _Catalyst3750G24WS25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 778)
)
_Catalyst3750G24WS50_ObjectIdentity = ObjectIdentity
catalyst3750G24WS50 = _Catalyst3750G24WS50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 779)
)
_CiscoMe3400g12CsA_ObjectIdentity = ObjectIdentity
ciscoMe3400g12CsA = _CiscoMe3400g12CsA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 780)
)
_CiscoMe3400g12CsD_ObjectIdentity = ObjectIdentity
ciscoMe3400g12CsD = _CiscoMe3400g12CsD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 781)
)
_Cisco877M_ObjectIdentity = ObjectIdentity
cisco877M = _Cisco877M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 782)
)
_Cisco1801M_ObjectIdentity = ObjectIdentity
cisco1801M = _Cisco1801M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 783)
)
_CatalystWsCBS3040FSC_ObjectIdentity = ObjectIdentity
catalystWsCBS3040FSC = _CatalystWsCBS3040FSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 784)
)
_CiscoOe511K9_ObjectIdentity = ObjectIdentity
ciscoOe511K9 = _CiscoOe511K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 785)
)
_CiscoOe611K9_ObjectIdentity = ObjectIdentity
ciscoOe611K9 = _CiscoOe611K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 786)
)
_CiscoOe7326K9_ObjectIdentity = ObjectIdentity
ciscoOe7326K9 = _CiscoOe7326K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 787)
)
_CiscoMe492410GE_ObjectIdentity = ObjectIdentity
ciscoMe492410GE = _CiscoMe492410GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 788)
)
_Catalyst3750E24TD_ObjectIdentity = ObjectIdentity
catalyst3750E24TD = _Catalyst3750E24TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 789)
)
_Catalyst3750E48TD_ObjectIdentity = ObjectIdentity
catalyst3750E48TD = _Catalyst3750E48TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 790)
)
_Catalyst3750E48PD_ObjectIdentity = ObjectIdentity
catalyst3750E48PD = _Catalyst3750E48PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 791)
)
_Catalyst3750E24PD_ObjectIdentity = ObjectIdentity
catalyst3750E24PD = _Catalyst3750E24PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 792)
)
_Catalyst3560E24TD_ObjectIdentity = ObjectIdentity
catalyst3560E24TD = _Catalyst3560E24TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 793)
)
_Catalyst3560E48TD_ObjectIdentity = ObjectIdentity
catalyst3560E48TD = _Catalyst3560E48TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 794)
)
_Catalyst3560E24PD_ObjectIdentity = ObjectIdentity
catalyst3560E24PD = _Catalyst3560E24PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 795)
)
_Catalyst3560E48PD_ObjectIdentity = ObjectIdentity
catalyst3560E48PD = _Catalyst3560E48PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 796)
)
_Catalyst35608PC_ObjectIdentity = ObjectIdentity
catalyst35608PC = _Catalyst35608PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 797)
)
_Catalyst29608TC_ObjectIdentity = ObjectIdentity
catalyst29608TC = _Catalyst29608TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 798)
)
_Catalyst2960G8TC_ObjectIdentity = ObjectIdentity
catalyst2960G8TC = _Catalyst2960G8TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 799)
)
_CiscoTSPri_ObjectIdentity = ObjectIdentity
ciscoTSPri = _CiscoTSPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 800)
)
_CiscoTSSec_ObjectIdentity = ObjectIdentity
ciscoTSSec = _CiscoTSSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 801)
)
_CiscoUWIpPhone7921G_ObjectIdentity = ObjectIdentity
ciscoUWIpPhone7921G = _CiscoUWIpPhone7921G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 802)
)
_CiscoUWIpPhone7920_ObjectIdentity = ObjectIdentity
ciscoUWIpPhone7920 = _CiscoUWIpPhone7920_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 803)
)
_Cisco3200WirelessMic_ObjectIdentity = ObjectIdentity
cisco3200WirelessMic = _Cisco3200WirelessMic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 804)
)
_CiscoISRWireless_ObjectIdentity = ObjectIdentity
ciscoISRWireless = _CiscoISRWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 805)
)
_CiscoIPSVirtual_ObjectIdentity = ObjectIdentity
ciscoIPSVirtual = _CiscoIPSVirtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 806)
)
_CiscoIDS4215Virtual_ObjectIdentity = ObjectIdentity
ciscoIDS4215Virtual = _CiscoIDS4215Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 807)
)
_CiscoIDS4235Virtual_ObjectIdentity = ObjectIdentity
ciscoIDS4235Virtual = _CiscoIDS4235Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 808)
)
_CiscoIDS4250Virtual_ObjectIdentity = ObjectIdentity
ciscoIDS4250Virtual = _CiscoIDS4250Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 809)
)
_CiscoIDS4250SXVirtual_ObjectIdentity = ObjectIdentity
ciscoIDS4250SXVirtual = _CiscoIDS4250SXVirtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 810)
)
_CiscoIDS4250XLVirtual_ObjectIdentity = ObjectIdentity
ciscoIDS4250XLVirtual = _CiscoIDS4250XLVirtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 811)
)
_CiscoIDS4240Virtual_ObjectIdentity = ObjectIdentity
ciscoIDS4240Virtual = _CiscoIDS4240Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 812)
)
_CiscoIDS4255Virtual_ObjectIdentity = ObjectIdentity
ciscoIDS4255Virtual = _CiscoIDS4255Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 813)
)
_CiscoIDS4260Virtual_ObjectIdentity = ObjectIdentity
ciscoIDS4260Virtual = _CiscoIDS4260Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 814)
)
_CiscoIDSIDSM2Virtual_ObjectIdentity = ObjectIdentity
ciscoIDSIDSM2Virtual = _CiscoIDSIDSM2Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 815)
)
_CiscoIPSSSM20Virtual_ObjectIdentity = ObjectIdentity
ciscoIPSSSM20Virtual = _CiscoIPSSSM20Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 816)
)
_CiscoIPSSSM10Virtual_ObjectIdentity = ObjectIdentity
ciscoIPSSSM10Virtual = _CiscoIPSSSM10Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 817)
)
_CiscoNMWLCE_ObjectIdentity = ObjectIdentity
ciscoNMWLCE = _CiscoNMWLCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 818)
)
_Cisco3205WirelessMic_ObjectIdentity = ObjectIdentity
cisco3205WirelessMic = _Cisco3205WirelessMic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 819)
)
_Cisco5720_ObjectIdentity = ObjectIdentity
cisco5720 = _Cisco5720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 820)
)
_Cisco7201_ObjectIdentity = ObjectIdentity
cisco7201 = _Cisco7201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 821)
)
_CiscoCrs14S_ObjectIdentity = ObjectIdentity
ciscoCrs14S = _CiscoCrs14S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 822)
)
_CiscoNmWae_ObjectIdentity = ObjectIdentity
ciscoNmWae = _CiscoNmWae_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 823)
)
_CiscoACE4710K9_ObjectIdentity = ObjectIdentity
ciscoACE4710K9 = _CiscoACE4710K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 824)
)
_CiscoMe3400g2csA_ObjectIdentity = ObjectIdentity
ciscoMe3400g2csA = _CiscoMe3400g2csA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 825)
)
_CiscoNmeNam_ObjectIdentity = ObjectIdentity
ciscoNmeNam = _CiscoNmeNam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 826)
)
_CiscoUbr7225Vxr_ObjectIdentity = ObjectIdentity
ciscoUbr7225Vxr = _CiscoUbr7225Vxr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 827)
)
_CiscoAirWlc2106K9_ObjectIdentity = ObjectIdentity
ciscoAirWlc2106K9 = _CiscoAirWlc2106K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 828)
)
_CiscoMwr1951DC_ObjectIdentity = ObjectIdentity
ciscoMwr1951DC = _CiscoMwr1951DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 829)
)
_CiscoIPS4270_ObjectIdentity = ObjectIdentity
ciscoIPS4270 = _CiscoIPS4270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 830)
)
_CiscoIPS4270Virtual_ObjectIdentity = ObjectIdentity
ciscoIPS4270Virtual = _CiscoIPS4270Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 831)
)
_CiscoWSC6509ve_ObjectIdentity = ObjectIdentity
ciscoWSC6509ve = _CiscoWSC6509ve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 832)
)
_Cisco5740_ObjectIdentity = ObjectIdentity
cisco5740 = _Cisco5740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 833)
)
_Cisco861_ObjectIdentity = ObjectIdentity
cisco861 = _Cisco861_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 834)
)
_Cisco866_ObjectIdentity = ObjectIdentity
cisco866 = _Cisco866_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 835)
)
_Cisco867_ObjectIdentity = ObjectIdentity
cisco867 = _Cisco867_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 836)
)
_Cisco881_ObjectIdentity = ObjectIdentity
cisco881 = _Cisco881_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 837)
)
_Cisco881G_ObjectIdentity = ObjectIdentity
cisco881G = _Cisco881G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 838)
)
_CiscoIad881F_ObjectIdentity = ObjectIdentity
ciscoIad881F = _CiscoIad881F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 839)
)
_Cisco881Srst_ObjectIdentity = ObjectIdentity
cisco881Srst = _Cisco881Srst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 840)
)
_CiscoIad881B_ObjectIdentity = ObjectIdentity
ciscoIad881B = _CiscoIad881B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 841)
)
_Cisco886_ObjectIdentity = ObjectIdentity
cisco886 = _Cisco886_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 842)
)
_Cisco886G_ObjectIdentity = ObjectIdentity
cisco886G = _Cisco886G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 843)
)
_CiscoIad886F_ObjectIdentity = ObjectIdentity
ciscoIad886F = _CiscoIad886F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 844)
)
_CiscoIad886B_ObjectIdentity = ObjectIdentity
ciscoIad886B = _CiscoIad886B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 845)
)
_Cisco886Srst_ObjectIdentity = ObjectIdentity
cisco886Srst = _Cisco886Srst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 846)
)
_Cisco887_ObjectIdentity = ObjectIdentity
cisco887 = _Cisco887_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 847)
)
_Cisco887G_ObjectIdentity = ObjectIdentity
cisco887G = _Cisco887G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 848)
)
_CiscoIad887F_ObjectIdentity = ObjectIdentity
ciscoIad887F = _CiscoIad887F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 849)
)
_CiscoIad887B_ObjectIdentity = ObjectIdentity
ciscoIad887B = _CiscoIad887B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 850)
)
_Cisco887Srst_ObjectIdentity = ObjectIdentity
cisco887Srst = _Cisco887Srst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 851)
)
_Cisco888_ObjectIdentity = ObjectIdentity
cisco888 = _Cisco888_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 852)
)
_Cisco888G_ObjectIdentity = ObjectIdentity
cisco888G = _Cisco888G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 853)
)
_CiscoIad888F_ObjectIdentity = ObjectIdentity
ciscoIad888F = _CiscoIad888F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 854)
)
_CiscoIad888B_ObjectIdentity = ObjectIdentity
ciscoIad888B = _CiscoIad888B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 855)
)
_Cisco888Srst_ObjectIdentity = ObjectIdentity
cisco888Srst = _Cisco888Srst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 856)
)
_Cisco891_ObjectIdentity = ObjectIdentity
cisco891 = _Cisco891_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 857)
)
_Cisco892_ObjectIdentity = ObjectIdentity
cisco892 = _Cisco892_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 858)
)
_Cisco885D3_ObjectIdentity = ObjectIdentity
cisco885D3 = _Cisco885D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 859)
)
_CiscoIad885FD3_ObjectIdentity = ObjectIdentity
ciscoIad885FD3 = _CiscoIad885FD3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 860)
)
_Cisco885EJ3_ObjectIdentity = ObjectIdentity
cisco885EJ3 = _Cisco885EJ3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 861)
)
_Cisco7603s_ObjectIdentity = ObjectIdentity
cisco7603s = _Cisco7603s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 862)
)
_Cisco7606s_ObjectIdentity = ObjectIdentity
cisco7606s = _Cisco7606s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 863)
)
_Cisco7609s_ObjectIdentity = ObjectIdentity
cisco7609s = _Cisco7609s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 864)
)
_Cisco7600Seb_ObjectIdentity = ObjectIdentity
cisco7600Seb = _Cisco7600Seb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 865)
)
_CiscoNMECUE_ObjectIdentity = ObjectIdentity
ciscoNMECUE = _CiscoNMECUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 866)
)
_CiscoAIM2CUE_ObjectIdentity = ObjectIdentity
ciscoAIM2CUE = _CiscoAIM2CUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 867)
)
_CiscoUC500_ObjectIdentity = ObjectIdentity
ciscoUC500 = _CiscoUC500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 868)
)
_Cisco860Ap_ObjectIdentity = ObjectIdentity
cisco860Ap = _Cisco860Ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 869)
)
_Cisco880Ap_ObjectIdentity = ObjectIdentity
cisco880Ap = _Cisco880Ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 870)
)
_Cisco890Ap_ObjectIdentity = ObjectIdentity
cisco890Ap = _Cisco890Ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 871)
)
_Cisco1900Ap_ObjectIdentity = ObjectIdentity
cisco1900Ap = _Cisco1900Ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 872)
)
_Cisco340024FSA_ObjectIdentity = ObjectIdentity
cisco340024FSA = _Cisco340024FSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 873)
)
_Catalyst4503e_ObjectIdentity = ObjectIdentity
catalyst4503e = _Catalyst4503e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 874)
)
_Catalyst4506e_ObjectIdentity = ObjectIdentity
catalyst4506e = _Catalyst4506e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 875)
)
_Catalyst4507re_ObjectIdentity = ObjectIdentity
catalyst4507re = _Catalyst4507re_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 876)
)
_Catalyst4510re_ObjectIdentity = ObjectIdentity
catalyst4510re = _Catalyst4510re_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 877)
)
_CiscoUC520s8U4FXOK9_ObjectIdentity = ObjectIdentity
ciscoUC520s8U4FXOK9 = _CiscoUC520s8U4FXOK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 878)
)
_CiscoUC520s8U4FXOWK9_ObjectIdentity = ObjectIdentity
ciscoUC520s8U4FXOWK9 = _CiscoUC520s8U4FXOWK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 879)
)
_CiscoUC520s8U2BRIK9_ObjectIdentity = ObjectIdentity
ciscoUC520s8U2BRIK9 = _CiscoUC520s8U2BRIK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 880)
)
_CiscoUC520s8U2BRIWK9_ObjectIdentity = ObjectIdentity
ciscoUC520s8U2BRIWK9 = _CiscoUC520s8U2BRIWK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 881)
)
_CiscoUC520s16U4FXOK9_ObjectIdentity = ObjectIdentity
ciscoUC520s16U4FXOK9 = _CiscoUC520s16U4FXOK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 882)
)
_CiscoUC520s16U4FXOWK9_ObjectIdentity = ObjectIdentity
ciscoUC520s16U4FXOWK9 = _CiscoUC520s16U4FXOWK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 883)
)
_CiscoUC520s16U2BRIK9_ObjectIdentity = ObjectIdentity
ciscoUC520s16U2BRIK9 = _CiscoUC520s16U2BRIK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 884)
)
_CiscoUC520s16U2BRIWK9_ObjectIdentity = ObjectIdentity
ciscoUC520s16U2BRIWK9 = _CiscoUC520s16U2BRIWK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 885)
)
_CiscoUC520m32U8FXOK9_ObjectIdentity = ObjectIdentity
ciscoUC520m32U8FXOK9 = _CiscoUC520m32U8FXOK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 886)
)
_CiscoUC520m32U8FXOWK9_ObjectIdentity = ObjectIdentity
ciscoUC520m32U8FXOWK9 = _CiscoUC520m32U8FXOWK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 887)
)
_CiscoUC520m32U4BRIK9_ObjectIdentity = ObjectIdentity
ciscoUC520m32U4BRIK9 = _CiscoUC520m32U4BRIK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 888)
)
_CiscoUC520m32U4BRIWK9_ObjectIdentity = ObjectIdentity
ciscoUC520m32U4BRIWK9 = _CiscoUC520m32U4BRIWK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 889)
)
_CiscoUC520m48U12FXOK9_ObjectIdentity = ObjectIdentity
ciscoUC520m48U12FXOK9 = _CiscoUC520m48U12FXOK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 890)
)
_CiscoUC520m48U12FXOWK9_ObjectIdentity = ObjectIdentity
ciscoUC520m48U12FXOWK9 = _CiscoUC520m48U12FXOWK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 891)
)
_CiscoUC520m48U6BRIK9_ObjectIdentity = ObjectIdentity
ciscoUC520m48U6BRIK9 = _CiscoUC520m48U6BRIK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 892)
)
_CiscoUC520m48U6BRIWK9_ObjectIdentity = ObjectIdentity
ciscoUC520m48U6BRIWK9 = _CiscoUC520m48U6BRIWK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 893)
)
_CiscoUC520m48U1T1E1FK9_ObjectIdentity = ObjectIdentity
ciscoUC520m48U1T1E1FK9 = _CiscoUC520m48U1T1E1FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 894)
)
_CiscoUC520m48U1T1E1BK9_ObjectIdentity = ObjectIdentity
ciscoUC520m48U1T1E1BK9 = _CiscoUC520m48U1T1E1BK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 895)
)
_Catalyst65xxVirtualSwitch_ObjectIdentity = ObjectIdentity
catalyst65xxVirtualSwitch = _Catalyst65xxVirtualSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 896)
)
_CatalystExpress5208PC_ObjectIdentity = ObjectIdentity
catalystExpress5208PC = _CatalystExpress5208PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 897)
)
_CiscoMCS7816I_ObjectIdentity = ObjectIdentity
ciscoMCS7816I = _CiscoMCS7816I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 898)
)
_CiscoMCS7828I_ObjectIdentity = ObjectIdentity
ciscoMCS7828I = _CiscoMCS7828I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 899)
)
_CiscoMCS7816H_ObjectIdentity = ObjectIdentity
ciscoMCS7816H = _CiscoMCS7816H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 900)
)
_CiscoMCS7828H_ObjectIdentity = ObjectIdentity
ciscoMCS7828H = _CiscoMCS7828H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 901)
)
_Cisco1861Uc2BK9_ObjectIdentity = ObjectIdentity
cisco1861Uc2BK9 = _Cisco1861Uc2BK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 902)
)
_Cisco1861Uc4FK9_ObjectIdentity = ObjectIdentity
cisco1861Uc4FK9 = _Cisco1861Uc4FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 903)
)
_Cisco1861Srst2BK9_ObjectIdentity = ObjectIdentity
cisco1861Srst2BK9 = _Cisco1861Srst2BK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 904)
)
_Cisco1861Srst4FK9_ObjectIdentity = ObjectIdentity
cisco1861Srst4FK9 = _Cisco1861Srst4FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 905)
)
_CiscoNmeApa_ObjectIdentity = ObjectIdentity
ciscoNmeApa = _CiscoNmeApa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 906)
)
_CiscoOe7330K9_ObjectIdentity = ObjectIdentity
ciscoOe7330K9 = _CiscoOe7330K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 907)
)
_CiscoOe7350K9_ObjectIdentity = ObjectIdentity
ciscoOe7350K9 = _CiscoOe7350K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 908)
)
_CiscoWsCbs3110gS_ObjectIdentity = ObjectIdentity
ciscoWsCbs3110gS = _CiscoWsCbs3110gS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 909)
)
_CiscoWsCbs3110gSt_ObjectIdentity = ObjectIdentity
ciscoWsCbs3110gSt = _CiscoWsCbs3110gSt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 910)
)
_CiscoWsCbs3110xS_ObjectIdentity = ObjectIdentity
ciscoWsCbs3110xS = _CiscoWsCbs3110xS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 911)
)
_CiscoWsCbs3110xSt_ObjectIdentity = ObjectIdentity
ciscoWsCbs3110xSt = _CiscoWsCbs3110xSt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 912)
)
_CiscoSce8000_ObjectIdentity = ObjectIdentity
ciscoSce8000 = _CiscoSce8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 913)
)
_CiscoASA5580_ObjectIdentity = ObjectIdentity
ciscoASA5580 = _CiscoASA5580_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 914)
)
_CiscoASA5580sc_ObjectIdentity = ObjectIdentity
ciscoASA5580sc = _CiscoASA5580sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 915)
)
_CiscoASA5580sy_ObjectIdentity = ObjectIdentity
ciscoASA5580sy = _CiscoASA5580sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 916)
)
_Cat4900M_ObjectIdentity = ObjectIdentity
cat4900M = _Cat4900M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 917)
)
_CatWsCbs3120gS_ObjectIdentity = ObjectIdentity
catWsCbs3120gS = _CatWsCbs3120gS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 918)
)
_CatWsCbs3120xS_ObjectIdentity = ObjectIdentity
catWsCbs3120xS = _CatWsCbs3120xS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 919)
)
_CatWsCbs3032Del_ObjectIdentity = ObjectIdentity
catWsCbs3032Del = _CatWsCbs3032Del_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 920)
)
_CatWsCbs3130gS_ObjectIdentity = ObjectIdentity
catWsCbs3130gS = _CatWsCbs3130gS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 921)
)
_CatWsCbs3130xS_ObjectIdentity = ObjectIdentity
catWsCbs3130xS = _CatWsCbs3130xS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 922)
)
_CiscoASR1002_ObjectIdentity = ObjectIdentity
ciscoASR1002 = _CiscoASR1002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 923)
)
_CiscoASR1004_ObjectIdentity = ObjectIdentity
ciscoASR1004 = _CiscoASR1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 924)
)
_CiscoASR1006_ObjectIdentity = ObjectIdentity
ciscoASR1006 = _CiscoASR1006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 925)
)
_Cisco520WirelessController_ObjectIdentity = ObjectIdentity
cisco520WirelessController = _Cisco520WirelessController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 926)
)
_Cat296048TCS_ObjectIdentity = ObjectIdentity
cat296048TCS = _Cat296048TCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 927)
)
_Cat296024TCS_ObjectIdentity = ObjectIdentity
cat296024TCS = _Cat296024TCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 928)
)
_Cat296024S_ObjectIdentity = ObjectIdentity
cat296024S = _Cat296024S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 929)
)
_Cat3560e12d_ObjectIdentity = ObjectIdentity
cat3560e12d = _Cat3560e12d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 930)
)
_CiscoCatRfgw_ObjectIdentity = ObjectIdentity
ciscoCatRfgw = _CiscoCatRfgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 931)
)
_CatExpress52024TT_ObjectIdentity = ObjectIdentity
catExpress52024TT = _CatExpress52024TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 932)
)
_CatExpress52024LC_ObjectIdentity = ObjectIdentity
catExpress52024LC = _CatExpress52024LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 933)
)
_CatExpress52024PC_ObjectIdentity = ObjectIdentity
catExpress52024PC = _CatExpress52024PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 934)
)
_CatExpress520G24TC_ObjectIdentity = ObjectIdentity
catExpress520G24TC = _CatExpress520G24TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 935)
)
_CiscoCDScde100_ObjectIdentity = ObjectIdentity
ciscoCDScde100 = _CiscoCDScde100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 936)
)
_CiscoCDScde200_ObjectIdentity = ObjectIdentity
ciscoCDScde200 = _CiscoCDScde200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 937)
)
_CiscoCDScde300_ObjectIdentity = ObjectIdentity
ciscoCDScde300 = _CiscoCDScde300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 938)
)
_Cisco1861SrstCue2BK9_ObjectIdentity = ObjectIdentity
cisco1861SrstCue2BK9 = _Cisco1861SrstCue2BK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 939)
)
_Cisco1861SrstCue4FK9_ObjectIdentity = ObjectIdentity
cisco1861SrstCue4FK9 = _Cisco1861SrstCue4FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 940)
)
_CiscoVFrameDataCenter_ObjectIdentity = ObjectIdentity
ciscoVFrameDataCenter = _CiscoVFrameDataCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 941)
)
_CiscoVQEServer_ObjectIdentity = ObjectIdentity
ciscoVQEServer = _CiscoVQEServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 942)
)
_CiscoIPSSSM40Virtual_ObjectIdentity = ObjectIdentity
ciscoIPSSSM40Virtual = _CiscoIPSSSM40Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 943)
)
_CiscoIPSSSM40_ObjectIdentity = ObjectIdentity
ciscoIPSSSM40 = _CiscoIPSSSM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 944)
)
_CiscoVgd1t3_ObjectIdentity = ObjectIdentity
ciscoVgd1t3 = _CiscoVgd1t3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 945)
)
_CiscoCBS3100_ObjectIdentity = ObjectIdentity
ciscoCBS3100 = _CiscoCBS3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 946)
)
_CiscoCBS3110_ObjectIdentity = ObjectIdentity
ciscoCBS3110 = _CiscoCBS3110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 947)
)
_CiscoCBS3120_ObjectIdentity = ObjectIdentity
ciscoCBS3120 = _CiscoCBS3120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 948)
)
_CiscoCBS3130_ObjectIdentity = ObjectIdentity
ciscoCBS3130 = _CiscoCBS3130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 949)
)
_Catalyst296024PC_ObjectIdentity = ObjectIdentity
catalyst296024PC = _Catalyst296024PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 950)
)
_Catalyst296024LT_ObjectIdentity = ObjectIdentity
catalyst296024LT = _Catalyst296024LT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 951)
)
_Catalyst2960PD8TT_ObjectIdentity = ObjectIdentity
catalyst2960PD8TT = _Catalyst2960PD8TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 952)
)
_CiscoSpa2x1geSynce_ObjectIdentity = ObjectIdentity
ciscoSpa2x1geSynce = _CiscoSpa2x1geSynce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 953)
)
_CiscoN5kC5020pBa_ObjectIdentity = ObjectIdentity
ciscoN5kC5020pBa = _CiscoN5kC5020pBa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 954)
)
_CiscoN5kC5020pBd_ObjectIdentity = ObjectIdentity
ciscoN5kC5020pBd = _CiscoN5kC5020pBd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 955)
)
_Catalyst3560E12SD_ObjectIdentity = ObjectIdentity
catalyst3560E12SD = _Catalyst3560E12SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 956)
)
_CiscoOe674_ObjectIdentity = ObjectIdentity
ciscoOe674 = _CiscoOe674_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 957)
)
_CiscoIE30004TC_ObjectIdentity = ObjectIdentity
ciscoIE30004TC = _CiscoIE30004TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 958)
)
_CiscoIE30008TC_ObjectIdentity = ObjectIdentity
ciscoIE30008TC = _CiscoIE30008TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 959)
)
_CiscoRAIE1783MS06T_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MS06T = _CiscoRAIE1783MS06T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 960)
)
_CiscoRAIE1783MS10T_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MS10T = _CiscoRAIE1783MS10T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 961)
)
_Cisco2435Iad8fxs_ObjectIdentity = ObjectIdentity
cisco2435Iad8fxs = _Cisco2435Iad8fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 962)
)
_CiscoVG204_ObjectIdentity = ObjectIdentity
ciscoVG204 = _CiscoVG204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 963)
)
_CiscoVG202_ObjectIdentity = ObjectIdentity
ciscoVG202 = _CiscoVG202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 964)
)
_Catalyst291824TT_ObjectIdentity = ObjectIdentity
catalyst291824TT = _Catalyst291824TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 965)
)
_Catalyst291824TC_ObjectIdentity = ObjectIdentity
catalyst291824TC = _Catalyst291824TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 966)
)
_Catalyst291848TT_ObjectIdentity = ObjectIdentity
catalyst291848TT = _Catalyst291848TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 967)
)
_Catalyst291848TC_ObjectIdentity = ObjectIdentity
catalyst291848TC = _Catalyst291848TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 968)
)
_CiscoVQETools_ObjectIdentity = ObjectIdentity
ciscoVQETools = _CiscoVQETools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 969)
)
_CiscoUC520m24U4BRIK9_ObjectIdentity = ObjectIdentity
ciscoUC520m24U4BRIK9 = _CiscoUC520m24U4BRIK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 970)
)
_CiscoUC520m24U8FXOK9_ObjectIdentity = ObjectIdentity
ciscoUC520m24U8FXOK9 = _CiscoUC520m24U8FXOK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 971)
)
_CiscoUC520s16U2BRIWK9J_ObjectIdentity = ObjectIdentity
ciscoUC520s16U2BRIWK9J = _CiscoUC520s16U2BRIWK9J_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 972)
)
_CiscoUC520s8U2BRIWK9J_ObjectIdentity = ObjectIdentity
ciscoUC520s8U2BRIWK9J = _CiscoUC520s8U2BRIWK9J_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 973)
)
_CiscoVSIntSp_ObjectIdentity = ObjectIdentity
ciscoVSIntSp = _CiscoVSIntSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 974)
)
_CiscoVSSP_ObjectIdentity = ObjectIdentity
ciscoVSSP = _CiscoVSSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 975)
)
_CiscoVSHydecoder_ObjectIdentity = ObjectIdentity
ciscoVSHydecoder = _CiscoVSHydecoder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 976)
)
_CiscoVSDecoder_ObjectIdentity = ObjectIdentity
ciscoVSDecoder = _CiscoVSDecoder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 977)
)
_CiscoVSEncoder4P_ObjectIdentity = ObjectIdentity
ciscoVSEncoder4P = _CiscoVSEncoder4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 978)
)
_CiscoVSEncoder1P_ObjectIdentity = ObjectIdentity
ciscoVSEncoder1P = _CiscoVSEncoder1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 979)
)
_CiscoSCS1000K9_ObjectIdentity = ObjectIdentity
ciscoSCS1000K9 = _CiscoSCS1000K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 980)
)
_Cisco1805_ObjectIdentity = ObjectIdentity
cisco1805 = _Cisco1805_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 981)
)
_CiscoCe7341_ObjectIdentity = ObjectIdentity
ciscoCe7341 = _CiscoCe7341_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 982)
)
_CiscoCe7371_ObjectIdentity = ObjectIdentity
ciscoCe7371 = _CiscoCe7371_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 983)
)
_Cisco7613s_ObjectIdentity = ObjectIdentity
cisco7613s = _Cisco7613s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 984)
)
_CiscoOe574_ObjectIdentity = ObjectIdentity
ciscoOe574 = _CiscoOe574_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 985)
)
_CiscoOe474_ObjectIdentity = ObjectIdentity
ciscoOe474 = _CiscoOe474_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 986)
)
_CiscoOe274_ObjectIdentity = ObjectIdentity
ciscoOe274 = _CiscoOe274_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 987)
)
_CiscoAp801agn_ObjectIdentity = ObjectIdentity
ciscoAp801agn = _CiscoAp801agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 988)
)
_CiscoAp801gn_ObjectIdentity = ObjectIdentity
ciscoAp801gn = _CiscoAp801gn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 989)
)
_Cisco1861WSrstCue4FK9_ObjectIdentity = ObjectIdentity
cisco1861WSrstCue4FK9 = _Cisco1861WSrstCue4FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 990)
)
_Cisco1861WSrstCue2BK9_ObjectIdentity = ObjectIdentity
cisco1861WSrstCue2BK9 = _Cisco1861WSrstCue2BK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 991)
)
_Cisco1861WSrst4FK9_ObjectIdentity = ObjectIdentity
cisco1861WSrst4FK9 = _Cisco1861WSrst4FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 992)
)
_Cisco1861WSrst2BK9_ObjectIdentity = ObjectIdentity
cisco1861WSrst2BK9 = _Cisco1861WSrst2BK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 993)
)
_Cisco1861WUc4FK9_ObjectIdentity = ObjectIdentity
cisco1861WUc4FK9 = _Cisco1861WUc4FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 994)
)
_Cisco1861WUc2BK9_ObjectIdentity = ObjectIdentity
cisco1861WUc2BK9 = _Cisco1861WUc2BK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 995)
)
_CiscoCe674_ObjectIdentity = ObjectIdentity
ciscoCe674 = _CiscoCe674_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 996)
)
_CiscoVQEIST_ObjectIdentity = ObjectIdentity
ciscoVQEIST = _CiscoVQEIST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 997)
)
_CiscoAIRAP1160_ObjectIdentity = ObjectIdentity
ciscoAIRAP1160 = _CiscoAIRAP1160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 998)
)
_CiscoWsCbs3012Ibm_ObjectIdentity = ObjectIdentity
ciscoWsCbs3012Ibm = _CiscoWsCbs3012Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 999)
)
_CiscoWsCbs3012IbmI_ObjectIdentity = ObjectIdentity
ciscoWsCbs3012IbmI = _CiscoWsCbs3012IbmI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1000)
)
_CiscoWsCbs3125gS_ObjectIdentity = ObjectIdentity
ciscoWsCbs3125gS = _CiscoWsCbs3125gS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1001)
)
_CiscoWsCbs3125xS_ObjectIdentity = ObjectIdentity
ciscoWsCbs3125xS = _CiscoWsCbs3125xS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1002)
)
_CiscoTSPriG2_ObjectIdentity = ObjectIdentity
ciscoTSPriG2 = _CiscoTSPriG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1003)
)
_Catalyst492810GE_ObjectIdentity = ObjectIdentity
catalyst492810GE = _Catalyst492810GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1004)
)
_Catalyst296048TTS_ObjectIdentity = ObjectIdentity
catalyst296048TTS = _Catalyst296048TTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1005)
)
_Catalyst29608TCS_ObjectIdentity = ObjectIdentity
catalyst29608TCS = _Catalyst29608TCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1006)
)
_CiscoMe3400eg2csA_ObjectIdentity = ObjectIdentity
ciscoMe3400eg2csA = _CiscoMe3400eg2csA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1007)
)
_CiscoMe3400eg12csM_ObjectIdentity = ObjectIdentity
ciscoMe3400eg12csM = _CiscoMe3400eg12csM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1008)
)
_CiscoMe3400e24tsM_ObjectIdentity = ObjectIdentity
ciscoMe3400e24tsM = _CiscoMe3400e24tsM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1009)
)
_CiscoIPSSSC5Virtual_ObjectIdentity = ObjectIdentity
ciscoIPSSSC5Virtual = _CiscoIPSSSC5Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1010)
)
_CiscoSR520FE_ObjectIdentity = ObjectIdentity
ciscoSR520FE = _CiscoSR520FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1011)
)
_CiscoSR520ADSL_ObjectIdentity = ObjectIdentity
ciscoSR520ADSL = _CiscoSR520ADSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1012)
)
_CiscoSR520ADSLi_ObjectIdentity = ObjectIdentity
ciscoSR520ADSLi = _CiscoSR520ADSLi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1013)
)
_CiscoMwr2941DC_ObjectIdentity = ObjectIdentity
ciscoMwr2941DC = _CiscoMwr2941DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1014)
)
_Catalyst356012PCS_ObjectIdentity = ObjectIdentity
catalyst356012PCS = _Catalyst356012PCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1015)
)
_Catalyst296048PSTL_ObjectIdentity = ObjectIdentity
catalyst296048PSTL = _Catalyst296048PSTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1016)
)
_CiscoASR9010_ObjectIdentity = ObjectIdentity
ciscoASR9010 = _CiscoASR9010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1017)
)
_CiscoASR9006_ObjectIdentity = ObjectIdentity
ciscoASR9006 = _CiscoASR9006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1018)
)
_Catalyst3560v224tsD_ObjectIdentity = ObjectIdentity
catalyst3560v224tsD = _Catalyst3560v224tsD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1019)
)
_Catalyst3560v224ts_ObjectIdentity = ObjectIdentity
catalyst3560v224ts = _Catalyst3560v224ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1020)
)
_Catalyst3560v224ps_ObjectIdentity = ObjectIdentity
catalyst3560v224ps = _Catalyst3560v224ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1021)
)
_Catalyst3750v224ts_ObjectIdentity = ObjectIdentity
catalyst3750v224ts = _Catalyst3750v224ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1022)
)
_Catalyst3750v224ps_ObjectIdentity = ObjectIdentity
catalyst3750v224ps = _Catalyst3750v224ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1023)
)
_Catalyst3560v248ts_ObjectIdentity = ObjectIdentity
catalyst3560v248ts = _Catalyst3560v248ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1024)
)
_Catalyst3560v248ps_ObjectIdentity = ObjectIdentity
catalyst3560v248ps = _Catalyst3560v248ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1025)
)
_Catalyst3750v248ts_ObjectIdentity = ObjectIdentity
catalyst3750v248ts = _Catalyst3750v248ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1026)
)
_Catalyst3750v248ps_ObjectIdentity = ObjectIdentity
catalyst3750v248ps = _Catalyst3750v248ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1027)
)
_CiscoHwicCableD2_ObjectIdentity = ObjectIdentity
ciscoHwicCableD2 = _CiscoHwicCableD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1028)
)
_CiscoHwicCableEJ2_ObjectIdentity = ObjectIdentity
ciscoHwicCableEJ2 = _CiscoHwicCableEJ2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1029)
)
_CiscoBr1430_ObjectIdentity = ObjectIdentity
ciscoBr1430 = _CiscoBr1430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1030)
)
_CiscoAIRBR1430_ObjectIdentity = ObjectIdentity
ciscoAIRBR1430 = _CiscoAIRBR1430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1031)
)
_CiscoNamApp2204_ObjectIdentity = ObjectIdentity
ciscoNamApp2204 = _CiscoNamApp2204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1032)
)
_CiscoNamApp2220_ObjectIdentity = ObjectIdentity
ciscoNamApp2220 = _CiscoNamApp2220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1033)
)
_CiscoAIRAP1141_ObjectIdentity = ObjectIdentity
ciscoAIRAP1141 = _CiscoAIRAP1141_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1034)
)
_CiscoAIRAP1142_ObjectIdentity = ObjectIdentity
ciscoAIRAP1142 = _CiscoAIRAP1142_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1035)
)
_CiscoASR14K4S_ObjectIdentity = ObjectIdentity
ciscoASR14K4S = _CiscoASR14K4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1036)
)
_CiscoASR14K8S_ObjectIdentity = ObjectIdentity
ciscoASR14K8S = _CiscoASR14K8S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1037)
)
_Cisco18xxx_ObjectIdentity = ObjectIdentity
cisco18xxx = _Cisco18xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1038)
)
_CiscoIPSSSC5_ObjectIdentity = ObjectIdentity
ciscoIPSSSC5 = _CiscoIPSSSC5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1039)
)
_Cisco887Vdsl2_ObjectIdentity = ObjectIdentity
cisco887Vdsl2 = _Cisco887Vdsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1040)
)
_Cisco3945_ObjectIdentity = ObjectIdentity
cisco3945 = _Cisco3945_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1041)
)
_Cisco3925_ObjectIdentity = ObjectIdentity
cisco3925 = _Cisco3925_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1042)
)
_Cisco2951_ObjectIdentity = ObjectIdentity
cisco2951 = _Cisco2951_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1043)
)
_Cisco2921_ObjectIdentity = ObjectIdentity
cisco2921 = _Cisco2921_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1044)
)
_Cisco2911_ObjectIdentity = ObjectIdentity
cisco2911 = _Cisco2911_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1045)
)
_Cisco2901_ObjectIdentity = ObjectIdentity
cisco2901 = _Cisco2901_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1046)
)
_Cisco1941_ObjectIdentity = ObjectIdentity
cisco1941 = _Cisco1941_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1047)
)
_CiscoSm2k15Es1GePoe_ObjectIdentity = ObjectIdentity
ciscoSm2k15Es1GePoe = _CiscoSm2k15Es1GePoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1048)
)
_CiscoSm3k15Es1GePoe_ObjectIdentity = ObjectIdentity
ciscoSm3k15Es1GePoe = _CiscoSm3k15Es1GePoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1049)
)
_CiscoSm3k16GePoe_ObjectIdentity = ObjectIdentity
ciscoSm3k16GePoe = _CiscoSm3k16GePoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1050)
)
_CiscoSm2k23Es1Ge_ObjectIdentity = ObjectIdentity
ciscoSm2k23Es1Ge = _CiscoSm2k23Es1Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1051)
)
_CiscoSm2k23Es1GePoe_ObjectIdentity = ObjectIdentity
ciscoSm2k23Es1GePoe = _CiscoSm2k23Es1GePoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1052)
)
_CiscoSm3k23Es1GePoe_ObjectIdentity = ObjectIdentity
ciscoSm3k23Es1GePoe = _CiscoSm3k23Es1GePoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1053)
)
_CiscoSm3k24GePoe_ObjectIdentity = ObjectIdentity
ciscoSm3k24GePoe = _CiscoSm3k24GePoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1054)
)
_CiscoSmXd2k48Es2SFP_ObjectIdentity = ObjectIdentity
ciscoSmXd2k48Es2SFP = _CiscoSmXd2k48Es2SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1055)
)
_CiscoSmXd3k48Es2SFPPoe_ObjectIdentity = ObjectIdentity
ciscoSmXd3k48Es2SFPPoe = _CiscoSmXd3k48Es2SFPPoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1056)
)
_CiscoSmXd3k48Ge2SFPPoe_ObjectIdentity = ObjectIdentity
ciscoSmXd3k48Ge2SFPPoe = _CiscoSmXd3k48Ge2SFPPoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1057)
)
_CiscoEsw52024pK9_ObjectIdentity = ObjectIdentity
ciscoEsw52024pK9 = _CiscoEsw52024pK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1058)
)
_CiscoEsw54024pK9_ObjectIdentity = ObjectIdentity
ciscoEsw54024pK9 = _CiscoEsw54024pK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1059)
)
_CiscoEsw52048pK9_ObjectIdentity = ObjectIdentity
ciscoEsw52048pK9 = _CiscoEsw52048pK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1060)
)
_CiscoEsw52024K9_ObjectIdentity = ObjectIdentity
ciscoEsw52024K9 = _CiscoEsw52024K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1061)
)
_CiscoEsw54024K9_ObjectIdentity = ObjectIdentity
ciscoEsw54024K9 = _CiscoEsw54024K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1062)
)
_CiscoEsw52048K9_ObjectIdentity = ObjectIdentity
ciscoEsw52048K9 = _CiscoEsw52048K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1063)
)
_CiscoEsw54048K9_ObjectIdentity = ObjectIdentity
ciscoEsw54048K9 = _CiscoEsw54048K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1064)
)
_Cisco1861_ObjectIdentity = ObjectIdentity
cisco1861 = _Cisco1861_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1065)
)
_CiscoUC520_ObjectIdentity = ObjectIdentity
ciscoUC520 = _CiscoUC520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1066)
)
_CatalystWSC2975GS48PSL_ObjectIdentity = ObjectIdentity
catalystWSC2975GS48PSL = _CatalystWSC2975GS48PSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1067)
)
_CatalystC2975Stack_ObjectIdentity = ObjectIdentity
catalystC2975Stack = _CatalystC2975Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1068)
)
_Cisco5500Wlc_ObjectIdentity = ObjectIdentity
cisco5500Wlc = _Cisco5500Wlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1069)
)
_CiscoSR520T1_ObjectIdentity = ObjectIdentity
ciscoSR520T1 = _CiscoSR520T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1070)
)
_CiscoPwrC3900Poe_ObjectIdentity = ObjectIdentity
ciscoPwrC3900Poe = _CiscoPwrC3900Poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1071)
)
_CiscoPwrC3900AC_ObjectIdentity = ObjectIdentity
ciscoPwrC3900AC = _CiscoPwrC3900AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1072)
)
_CiscoPwrC2921C2951Poe_ObjectIdentity = ObjectIdentity
ciscoPwrC2921C2951Poe = _CiscoPwrC2921C2951Poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1073)
)
_CiscoPwrC2921C2951AC_ObjectIdentity = ObjectIdentity
ciscoPwrC2921C2951AC = _CiscoPwrC2921C2951AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1074)
)
_CiscoPwrC2911Poe_ObjectIdentity = ObjectIdentity
ciscoPwrC2911Poe = _CiscoPwrC2911Poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1075)
)
_CiscoPwrC2911AC_ObjectIdentity = ObjectIdentity
ciscoPwrC2911AC = _CiscoPwrC2911AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1076)
)
_CiscoPwrC2901Poe_ObjectIdentity = ObjectIdentity
ciscoPwrC2901Poe = _CiscoPwrC2901Poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1077)
)
_CiscoPwrC1941C2901AC_ObjectIdentity = ObjectIdentity
ciscoPwrC1941C2901AC = _CiscoPwrC1941C2901AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1078)
)
_CiscoPwrC1941Poe_ObjectIdentity = ObjectIdentity
ciscoPwrC1941Poe = _CiscoPwrC1941Poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1079)
)
_CiscoPwrC3900DC_ObjectIdentity = ObjectIdentity
ciscoPwrC3900DC = _CiscoPwrC3900DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1080)
)
_CiscoPwrC2921C2951DC_ObjectIdentity = ObjectIdentity
ciscoPwrC2921C2951DC = _CiscoPwrC2921C2951DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1081)
)
_CiscoPwrC2911DC_ObjectIdentity = ObjectIdentity
ciscoPwrC2911DC = _CiscoPwrC2911DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1082)
)
_CiscoRpsAdptrC2921C2951_ObjectIdentity = ObjectIdentity
ciscoRpsAdptrC2921C2951 = _CiscoRpsAdptrC2921C2951_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1083)
)
_CiscoRpsAdptrC2911_ObjectIdentity = ObjectIdentity
ciscoRpsAdptrC2911 = _CiscoRpsAdptrC2911_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1084)
)
_CiscoIPSSSC2_ObjectIdentity = ObjectIdentity
ciscoIPSSSC2 = _CiscoIPSSSC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1085)
)
_CiscoIPSSSC2Virtual_ObjectIdentity = ObjectIdentity
ciscoIPSSSC2Virtual = _CiscoIPSSSC2Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1086)
)
_CatalystWSCBS3140XS_ObjectIdentity = ObjectIdentity
catalystWSCBS3140XS = _CatalystWSCBS3140XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1087)
)
_CatalystWSCBS3140GS_ObjectIdentity = ObjectIdentity
catalystWSCBS3140GS = _CatalystWSCBS3140GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1088)
)
_CatalystWSCBS3042FSC_ObjectIdentity = ObjectIdentity
catalystWSCBS3042FSC = _CatalystWSCBS3042FSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1089)
)
_CatalystWSCBS3150XS_ObjectIdentity = ObjectIdentity
catalystWSCBS3150XS = _CatalystWSCBS3150XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1090)
)
_CatalystWSCBS3150GS_ObjectIdentity = ObjectIdentity
catalystWSCBS3150GS = _CatalystWSCBS3150GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1091)
)
_CatalystWSCBS3052NEC_ObjectIdentity = ObjectIdentity
catalystWSCBS3052NEC = _CatalystWSCBS3052NEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1092)
)
_CiscoCBS3140Stack_ObjectIdentity = ObjectIdentity
ciscoCBS3140Stack = _CiscoCBS3140Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1093)
)
_CiscoCBS3150Stack_ObjectIdentity = ObjectIdentity
ciscoCBS3150Stack = _CiscoCBS3150Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1094)
)
_Cisco1941W_ObjectIdentity = ObjectIdentity
cisco1941W = _Cisco1941W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1095)
)
_CiscoC888E_ObjectIdentity = ObjectIdentity
ciscoC888E = _CiscoC888E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1096)
)
_CiscoC888EG_ObjectIdentity = ObjectIdentity
ciscoC888EG = _CiscoC888EG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1097)
)
_CiscoIad888EB_ObjectIdentity = ObjectIdentity
ciscoIad888EB = _CiscoIad888EB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1098)
)
_CiscoIad888EF_ObjectIdentity = ObjectIdentity
ciscoIad888EF = _CiscoIad888EF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1099)
)
_CiscoC888ESRST_ObjectIdentity = ObjectIdentity
ciscoC888ESRST = _CiscoC888ESRST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1100)
)
_CiscoASA5505W_ObjectIdentity = ObjectIdentity
ciscoASA5505W = _CiscoASA5505W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1101)
)
_Cisco3845nv_ObjectIdentity = ObjectIdentity
cisco3845nv = _Cisco3845nv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1102)
)
_Cisco3825nv_ObjectIdentity = ObjectIdentity
cisco3825nv = _Cisco3825nv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1103)
)
_CatalystWSC235048TD_ObjectIdentity = ObjectIdentity
catalystWSC235048TD = _CatalystWSC235048TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1104)
)
_Cisco887M_ObjectIdentity = ObjectIdentity
cisco887M = _Cisco887M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1105)
)
_CiscoVg250_ObjectIdentity = ObjectIdentity
ciscoVg250 = _CiscoVg250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1106)
)
_CiscoVg226e_ObjectIdentity = ObjectIdentity
ciscoVg226e = _CiscoVg226e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1107)
)
_CiscoDsIbm8GfcK9_ObjectIdentity = ObjectIdentity
ciscoDsIbm8GfcK9 = _CiscoDsIbm8GfcK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1108)
)
_CiscoDsHp8GfcK9_ObjectIdentity = ObjectIdentity
ciscoDsHp8GfcK9 = _CiscoDsHp8GfcK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1109)
)
_CiscoDsDell8GfcK9_ObjectIdentity = ObjectIdentity
ciscoDsDell8GfcK9 = _CiscoDsDell8GfcK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1110)
)
_CiscoDsC9148K9_ObjectIdentity = ObjectIdentity
ciscoDsC9148K9 = _CiscoDsC9148K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1111)
)
_CiscoCeVirtualBlade_ObjectIdentity = ObjectIdentity
ciscoCeVirtualBlade = _CiscoCeVirtualBlade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1112)
)
_CiscoCDScde420_ObjectIdentity = ObjectIdentity
ciscoCDScde420 = _CiscoCDScde420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1113)
)
_CiscoCDScde220_ObjectIdentity = ObjectIdentity
ciscoCDScde220 = _CiscoCDScde220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1114)
)
_CiscoCDScde110_ObjectIdentity = ObjectIdentity
ciscoCDScde110 = _CiscoCDScde110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1115)
)
_CiscoASR1002F_ObjectIdentity = ObjectIdentity
ciscoASR1002F = _CiscoASR1002F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1116)
)
_CiscoSecureAccessControlSystem_ObjectIdentity = ObjectIdentity
ciscoSecureAccessControlSystem = _CiscoSecureAccessControlSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1117)
)
_Cisco861Npe_ObjectIdentity = ObjectIdentity
cisco861Npe = _Cisco861Npe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1118)
)
_Cisco881Npe_ObjectIdentity = ObjectIdentity
cisco881Npe = _Cisco881Npe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1119)
)
_Cisco881GNpe_ObjectIdentity = ObjectIdentity
cisco881GNpe = _Cisco881GNpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1120)
)
_Cisco887Npe_ObjectIdentity = ObjectIdentity
cisco887Npe = _Cisco887Npe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1121)
)
_Cisco888GNpe_ObjectIdentity = ObjectIdentity
cisco888GNpe = _Cisco888GNpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1122)
)
_Cisco891Npe_ObjectIdentity = ObjectIdentity
cisco891Npe = _Cisco891Npe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1123)
)
_CiscoAIRAP3501_ObjectIdentity = ObjectIdentity
ciscoAIRAP3501 = _CiscoAIRAP3501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1124)
)
_CiscoAIRAP3502_ObjectIdentity = ObjectIdentity
ciscoAIRAP3502 = _CiscoAIRAP3502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1125)
)
_CiscoCDScde400_ObjectIdentity = ObjectIdentity
ciscoCDScde400 = _CiscoCDScde400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1126)
)
_CiscoSA520K9_ObjectIdentity = ObjectIdentity
ciscoSA520K9 = _CiscoSA520K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1127)
)
_CiscoSA520WK9_ObjectIdentity = ObjectIdentity
ciscoSA520WK9 = _CiscoSA520WK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1128)
)
_CiscoSA540K9_ObjectIdentity = ObjectIdentity
ciscoSA540K9 = _CiscoSA540K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1129)
)
_CiscoSps2004B_ObjectIdentity = ObjectIdentity
ciscoSps2004B = _CiscoSps2004B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1130)
)
_CiscoSps204B_ObjectIdentity = ObjectIdentity
ciscoSps204B = _CiscoSps204B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1131)
)
_CiscoUC560T1E1K9_ObjectIdentity = ObjectIdentity
ciscoUC560T1E1K9 = _CiscoUC560T1E1K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1132)
)
_CiscoUC560BRIK9_ObjectIdentity = ObjectIdentity
ciscoUC560BRIK9 = _CiscoUC560BRIK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1133)
)
_CiscoUC560FXOK9_ObjectIdentity = ObjectIdentity
ciscoUC560FXOK9 = _CiscoUC560FXOK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1134)
)
_CiscoAp541nAK9_ObjectIdentity = ObjectIdentity
ciscoAp541nAK9 = _CiscoAp541nAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1135)
)
_CiscoAp541nEK9_ObjectIdentity = ObjectIdentity
ciscoAp541nEK9 = _CiscoAp541nEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1136)
)
_CiscoAp541nNK9_ObjectIdentity = ObjectIdentity
ciscoAp541nNK9 = _CiscoAp541nNK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1137)
)
_Cisco887GVdsl2_ObjectIdentity = ObjectIdentity
cisco887GVdsl2 = _Cisco887GVdsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1138)
)
_Cisco887SrstVdsl2_ObjectIdentity = ObjectIdentity
cisco887SrstVdsl2 = _Cisco887SrstVdsl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1139)
)
_CiscoUc540wFxoK9_ObjectIdentity = ObjectIdentity
ciscoUc540wFxoK9 = _CiscoUc540wFxoK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1140)
)
_CiscoUc540wBriK9_ObjectIdentity = ObjectIdentity
ciscoUc540wBriK9 = _CiscoUc540wBriK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1141)
)
_CiscoCaServer_ObjectIdentity = ObjectIdentity
ciscoCaServer = _CiscoCaServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1142)
)
_CiscoCaManager_ObjectIdentity = ObjectIdentity
ciscoCaManager = _CiscoCaManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1143)
)
_Cisco3925SPE200_ObjectIdentity = ObjectIdentity
cisco3925SPE200 = _Cisco3925SPE200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1144)
)
_Cisco3945SPE250_ObjectIdentity = ObjectIdentity
cisco3945SPE250 = _Cisco3945SPE250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1145)
)
_Catalyst296024LCS_ObjectIdentity = ObjectIdentity
catalyst296024LCS = _Catalyst296024LCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1146)
)
_Catalyst296024PCS_ObjectIdentity = ObjectIdentity
catalyst296024PCS = _Catalyst296024PCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1147)
)
_Catalyst296048PSTS_ObjectIdentity = ObjectIdentity
catalyst296048PSTS = _Catalyst296048PSTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1148)
)
_CiscoISM_ObjectIdentity = ObjectIdentity
ciscoISM = _CiscoISM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1149)
)
_CiscoSM_ObjectIdentity = ObjectIdentity
ciscoSM = _CiscoSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1150)
)
_CiscoNMEAXP_ObjectIdentity = ObjectIdentity
ciscoNMEAXP = _CiscoNMEAXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1151)
)
_CiscoAIMAXP_ObjectIdentity = ObjectIdentity
ciscoAIMAXP = _CiscoAIMAXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1152)
)
_CiscoAIM2AXP_ObjectIdentity = ObjectIdentity
ciscoAIM2AXP = _CiscoAIM2AXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1153)
)
_CiscoSRP521_ObjectIdentity = ObjectIdentity
ciscoSRP521 = _CiscoSRP521_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1154)
)
_CiscoSRP526_ObjectIdentity = ObjectIdentity
ciscoSRP526 = _CiscoSRP526_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1155)
)
_CiscoSRP527_ObjectIdentity = ObjectIdentity
ciscoSRP527 = _CiscoSRP527_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1156)
)
_CiscoSRP541_ObjectIdentity = ObjectIdentity
ciscoSRP541 = _CiscoSRP541_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1157)
)
_CiscoSRP546_ObjectIdentity = ObjectIdentity
ciscoSRP546 = _CiscoSRP546_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1158)
)
_CiscoSRP547_ObjectIdentity = ObjectIdentity
ciscoSRP547 = _CiscoSRP547_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1159)
)
_CiscoVS510FXO_ObjectIdentity = ObjectIdentity
ciscoVS510FXO = _CiscoVS510FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1160)
)
_CiscoNmWae900_ObjectIdentity = ObjectIdentity
ciscoNmWae900 = _CiscoNmWae900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1161)
)
_CiscoNmWae700_ObjectIdentity = ObjectIdentity
ciscoNmWae700 = _CiscoNmWae700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1162)
)
_Cisco5940RA_ObjectIdentity = ObjectIdentity
cisco5940RA = _Cisco5940RA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1163)
)
_Cisco5940RC_ObjectIdentity = ObjectIdentity
cisco5940RC = _Cisco5940RC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1164)
)
_CiscoASR1001_ObjectIdentity = ObjectIdentity
ciscoASR1001 = _CiscoASR1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1165)
)
_CiscoASR1013_ObjectIdentity = ObjectIdentity
ciscoASR1013 = _CiscoASR1013_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1166)
)
_CiscoCDScde205_ObjectIdentity = ObjectIdentity
ciscoCDScde205 = _CiscoCDScde205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1167)
)
_CiscoPwr1941AC_ObjectIdentity = ObjectIdentity
ciscoPwr1941AC = _CiscoPwr1941AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1168)
)
_CiscoNamWaasVirtualBlade_ObjectIdentity = ObjectIdentity
ciscoNamWaasVirtualBlade = _CiscoNamWaasVirtualBlade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1169)
)
_CiscoRaie1783Rms06t_ObjectIdentity = ObjectIdentity
ciscoRaie1783Rms06t = _CiscoRaie1783Rms06t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1170)
)
_CiscoRaie1783Rms10t_ObjectIdentity = ObjectIdentity
ciscoRaie1783Rms10t = _CiscoRaie1783Rms10t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1171)
)
_Cisco1941WEK9_ObjectIdentity = ObjectIdentity
cisco1941WEK9 = _Cisco1941WEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1172)
)
_Cisco1941WPK9_ObjectIdentity = ObjectIdentity
cisco1941WPK9 = _Cisco1941WPK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1173)
)
_Cisco1941WNK9_ObjectIdentity = ObjectIdentity
cisco1941WNK9 = _Cisco1941WNK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1174)
)
_CiscoMXE5600_ObjectIdentity = ObjectIdentity
ciscoMXE5600 = _CiscoMXE5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1175)
)
_CiscoEsw5408pK9_ObjectIdentity = ObjectIdentity
ciscoEsw5408pK9 = _CiscoEsw5408pK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1176)
)
_CiscoEsw5208pK9_ObjectIdentity = ObjectIdentity
ciscoEsw5208pK9 = _CiscoEsw5208pK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1177)
)
_Catalyst4948e10GE_ObjectIdentity = ObjectIdentity
catalyst4948e10GE = _Catalyst4948e10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1178)
)
_Cat2960x48tsS_ObjectIdentity = ObjectIdentity
cat2960x48tsS = _Cat2960x48tsS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1179)
)
_Cat2960x24tsS_ObjectIdentity = ObjectIdentity
cat2960x24tsS = _Cat2960x24tsS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1180)
)
_Cat2960xs48fpdL_ObjectIdentity = ObjectIdentity
cat2960xs48fpdL = _Cat2960xs48fpdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1181)
)
_Cat2960xs48lpdL_ObjectIdentity = ObjectIdentity
cat2960xs48lpdL = _Cat2960xs48lpdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1182)
)
_Cat2960xs48ltdL_ObjectIdentity = ObjectIdentity
cat2960xs48ltdL = _Cat2960xs48ltdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1183)
)
_Cat2960xs24pdL_ObjectIdentity = ObjectIdentity
cat2960xs24pdL = _Cat2960xs24pdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1184)
)
_Cat2960xs24tdL_ObjectIdentity = ObjectIdentity
cat2960xs24tdL = _Cat2960xs24tdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1185)
)
_Cat2960xs48fpsL_ObjectIdentity = ObjectIdentity
cat2960xs48fpsL = _Cat2960xs48fpsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1186)
)
_Cat2960xs48lpsL_ObjectIdentity = ObjectIdentity
cat2960xs48lpsL = _Cat2960xs48lpsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1187)
)
_Cat2960xs24psL_ObjectIdentity = ObjectIdentity
cat2960xs24psL = _Cat2960xs24psL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1188)
)
_Cat2960xs48tsL_ObjectIdentity = ObjectIdentity
cat2960xs48tsL = _Cat2960xs48tsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1189)
)
_Cat2960xs24tsL_ObjectIdentity = ObjectIdentity
cat2960xs24tsL = _Cat2960xs24tsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1190)
)
_Cisco1921k9_ObjectIdentity = ObjectIdentity
cisco1921k9 = _Cisco1921k9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1191)
)
_Cisco1905k9_ObjectIdentity = ObjectIdentity
cisco1905k9 = _Cisco1905k9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1192)
)
_CiscoPwrC1921C1905AC_ObjectIdentity = ObjectIdentity
ciscoPwrC1921C1905AC = _CiscoPwrC1921C1905AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1193)
)
_CiscoASA5585Ssp10_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp10 = _CiscoASA5585Ssp10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1194)
)
_CiscoASA5585Ssp20_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp20 = _CiscoASA5585Ssp20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1195)
)
_CiscoASA5585Ssp40_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp40 = _CiscoASA5585Ssp40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1196)
)
_CiscoASA5585Ssp60_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp60 = _CiscoASA5585Ssp60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1197)
)
_CiscoASA5585Ssp10sc_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp10sc = _CiscoASA5585Ssp10sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1198)
)
_CiscoASA5585Ssp20sc_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp20sc = _CiscoASA5585Ssp20sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1199)
)
_CiscoASA5585Ssp40sc_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp40sc = _CiscoASA5585Ssp40sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1200)
)
_CiscoASA5585Ssp60sc_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp60sc = _CiscoASA5585Ssp60sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1201)
)
_CiscoASA5585Ssp10sy_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp10sy = _CiscoASA5585Ssp10sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1202)
)
_CiscoASA5585Ssp20sy_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp20sy = _CiscoASA5585Ssp20sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1203)
)
_CiscoASA5585Ssp40sy_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp40sy = _CiscoASA5585Ssp40sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1204)
)
_CiscoASA5585Ssp60sy_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp60sy = _CiscoASA5585Ssp60sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1205)
)
_Cisco3925SPE250_ObjectIdentity = ObjectIdentity
cisco3925SPE250 = _Cisco3925SPE250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1206)
)
_Cisco3945SPE200_ObjectIdentity = ObjectIdentity
cisco3945SPE200 = _Cisco3945SPE200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1207)
)
_Cat29xxStack_ObjectIdentity = ObjectIdentity
cat29xxStack = _Cat29xxStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1208)
)
_CiscoOeNm302_ObjectIdentity = ObjectIdentity
ciscoOeNm302 = _CiscoOeNm302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1209)
)
_CiscoOeNm502_ObjectIdentity = ObjectIdentity
ciscoOeNm502 = _CiscoOeNm502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1210)
)
_CiscoOeNm522_ObjectIdentity = ObjectIdentity
ciscoOeNm522 = _CiscoOeNm522_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1211)
)
_CiscoOeSmSre700_ObjectIdentity = ObjectIdentity
ciscoOeSmSre700 = _CiscoOeSmSre700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1212)
)
_CiscoOeSmSre900_ObjectIdentity = ObjectIdentity
ciscoOeSmSre900 = _CiscoOeSmSre900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1213)
)
_CiscoVsaNam_ObjectIdentity = ObjectIdentity
ciscoVsaNam = _CiscoVsaNam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1214)
)
_CiscoMwr2941DCA_ObjectIdentity = ObjectIdentity
ciscoMwr2941DCA = _CiscoMwr2941DCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1215)
)
_CiscoN7KC7018IOS_ObjectIdentity = ObjectIdentity
ciscoN7KC7018IOS = _CiscoN7KC7018IOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1216)
)
_CiscoN7KC7010IOS_ObjectIdentity = ObjectIdentity
ciscoN7KC7010IOS = _CiscoN7KC7010IOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1217)
)
_CiscoN4KDellEth_ObjectIdentity = ObjectIdentity
ciscoN4KDellEth = _CiscoN4KDellEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1218)
)
_CiscoN4KDellCiscoEth_ObjectIdentity = ObjectIdentity
ciscoN4KDellCiscoEth = _CiscoN4KDellCiscoEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1219)
)
_Cisco1941WCK9_ObjectIdentity = ObjectIdentity
cisco1941WCK9 = _Cisco1941WCK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1220)
)
_CiscoCDScde2202s3_ObjectIdentity = ObjectIdentity
ciscoCDScde2202s3 = _CiscoCDScde2202s3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1221)
)
_Cat3750x24_ObjectIdentity = ObjectIdentity
cat3750x24 = _Cat3750x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1222)
)
_Cat3750x48_ObjectIdentity = ObjectIdentity
cat3750x48 = _Cat3750x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1223)
)
_Cat3750x24P_ObjectIdentity = ObjectIdentity
cat3750x24P = _Cat3750x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1224)
)
_Cat3750x48P_ObjectIdentity = ObjectIdentity
cat3750x48P = _Cat3750x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1225)
)
_Cat3560x24_ObjectIdentity = ObjectIdentity
cat3560x24 = _Cat3560x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1226)
)
_Cat3560x48_ObjectIdentity = ObjectIdentity
cat3560x48 = _Cat3560x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1227)
)
_Cat3560x24P_ObjectIdentity = ObjectIdentity
cat3560x24P = _Cat3560x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1228)
)
_Cat3560x48P_ObjectIdentity = ObjectIdentity
cat3560x48P = _Cat3560x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1229)
)
_CiscoNMEAIR_ObjectIdentity = ObjectIdentity
ciscoNMEAIR = _CiscoNMEAIR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1230)
)
_CiscoACE30K9_ObjectIdentity = ObjectIdentity
ciscoACE30K9 = _CiscoACE30K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1231)
)
_CiscoASA5585SspIps10_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps10 = _CiscoASA5585SspIps10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1232)
)
_CiscoASA5585SspIps20_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps20 = _CiscoASA5585SspIps20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1233)
)
_CiscoASA5585SspIps40_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps40 = _CiscoASA5585SspIps40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1234)
)
_CiscoASA5585SspIps60_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps60 = _CiscoASA5585SspIps60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1235)
)
_Cisco1841CK9_ObjectIdentity = ObjectIdentity
cisco1841CK9 = _Cisco1841CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1236)
)
_Cisco2801CK9_ObjectIdentity = ObjectIdentity
cisco2801CK9 = _Cisco2801CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1237)
)
_Cisco2811CK9_ObjectIdentity = ObjectIdentity
cisco2811CK9 = _Cisco2811CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1238)
)
_Cisco2821CK9_ObjectIdentity = ObjectIdentity
cisco2821CK9 = _Cisco2821CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1239)
)
_Cisco2851CK9_ObjectIdentity = ObjectIdentity
cisco2851CK9 = _Cisco2851CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1240)
)
_Cisco3825CK9_ObjectIdentity = ObjectIdentity
cisco3825CK9 = _Cisco3825CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1241)
)
_Cisco3845CK9_ObjectIdentity = ObjectIdentity
cisco3845CK9 = _Cisco3845CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1242)
)
_Cisco3825CnvK9_ObjectIdentity = ObjectIdentity
cisco3825CnvK9 = _Cisco3825CnvK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1243)
)
_Cisco3845CnvK9_ObjectIdentity = ObjectIdentity
cisco3845CnvK9 = _Cisco3845CnvK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1244)
)
_CiscoCGS252024TC_ObjectIdentity = ObjectIdentity
ciscoCGS252024TC = _CiscoCGS252024TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1245)
)
_CiscoCGS252016S8PC_ObjectIdentity = ObjectIdentity
ciscoCGS252016S8PC = _CiscoCGS252016S8PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1246)
)
_CiscoAIRAP1262_ObjectIdentity = ObjectIdentity
ciscoAIRAP1262 = _CiscoAIRAP1262_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1247)
)
_CiscoAIRAP1261_ObjectIdentity = ObjectIdentity
ciscoAIRAP1261 = _CiscoAIRAP1261_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1248)
)
_Cisco892F_ObjectIdentity = ObjectIdentity
cisco892F = _Cisco892F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1249)
)
_CiscoMe3600x24fsM_ObjectIdentity = ObjectIdentity
ciscoMe3600x24fsM = _CiscoMe3600x24fsM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1250)
)
_CiscoMe3600x24tsM_ObjectIdentity = ObjectIdentity
ciscoMe3600x24tsM = _CiscoMe3600x24tsM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1251)
)
_CiscoMe3800x24fsM_ObjectIdentity = ObjectIdentity
ciscoMe3800x24fsM = _CiscoMe3800x24fsM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1252)
)
_CiscoCGR2010_ObjectIdentity = ObjectIdentity
ciscoCGR2010 = _CiscoCGR2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1253)
)
_CiscoPwrCGR20xxCGS25xxPoeAC_ObjectIdentity = ObjectIdentity
ciscoPwrCGR20xxCGS25xxPoeAC = _CiscoPwrCGR20xxCGS25xxPoeAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1254)
)
_CiscoPwrCGR20xxCGS25xxPoeDC_ObjectIdentity = ObjectIdentity
ciscoPwrCGR20xxCGS25xxPoeDC = _CiscoPwrCGR20xxCGS25xxPoeDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1255)
)
_CatWsC2960s48tsS_ObjectIdentity = ObjectIdentity
catWsC2960s48tsS = _CatWsC2960s48tsS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1256)
)
_CatWsC2960s24tsS_ObjectIdentity = ObjectIdentity
catWsC2960s24tsS = _CatWsC2960s24tsS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1257)
)
_CatWsC2960s48fpdL_ObjectIdentity = ObjectIdentity
catWsC2960s48fpdL = _CatWsC2960s48fpdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1258)
)
_CatWsC2960s48ldpL_ObjectIdentity = ObjectIdentity
catWsC2960s48ldpL = _CatWsC2960s48ldpL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1259)
)
_CatWsC2960s48tdL_ObjectIdentity = ObjectIdentity
catWsC2960s48tdL = _CatWsC2960s48tdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1260)
)
_CatWsC2960s24pdL_ObjectIdentity = ObjectIdentity
catWsC2960s24pdL = _CatWsC2960s24pdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1261)
)
_CatWsC2960s24tdL_ObjectIdentity = ObjectIdentity
catWsC2960s24tdL = _CatWsC2960s24tdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1262)
)
_CatWsC2960s48fpsL_ObjectIdentity = ObjectIdentity
catWsC2960s48fpsL = _CatWsC2960s48fpsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1263)
)
_CatWsC2960s48lpsL_ObjectIdentity = ObjectIdentity
catWsC2960s48lpsL = _CatWsC2960s48lpsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1264)
)
_CatWsC2960s24psL_ObjectIdentity = ObjectIdentity
catWsC2960s24psL = _CatWsC2960s24psL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1265)
)
_CatWsC2960s48tsL_ObjectIdentity = ObjectIdentity
catWsC2960s48tsL = _CatWsC2960s48tsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1266)
)
_CatWsC2960s24tsL_ObjectIdentity = ObjectIdentity
catWsC2960s24tsL = _CatWsC2960s24tsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1267)
)
_Cisco1906CK9_ObjectIdentity = ObjectIdentity
cisco1906CK9 = _Cisco1906CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1268)
)
_CiscoAIRAP1042_ObjectIdentity = ObjectIdentity
ciscoAIRAP1042 = _CiscoAIRAP1042_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1269)
)
_CiscoAIRAP1041_ObjectIdentity = ObjectIdentity
ciscoAIRAP1041 = _CiscoAIRAP1041_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1270)
)
_Cisco887VaM_ObjectIdentity = ObjectIdentity
cisco887VaM = _Cisco887VaM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1271)
)
_Cisco867Va_ObjectIdentity = ObjectIdentity
cisco867Va = _Cisco867Va_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1272)
)
_Cisco886Va_ObjectIdentity = ObjectIdentity
cisco886Va = _Cisco886Va_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1273)
)
_Cisco887Va_ObjectIdentity = ObjectIdentity
cisco887Va = _Cisco887Va_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1274)
)
_CiscoASASm1sc_ObjectIdentity = ObjectIdentity
ciscoASASm1sc = _CiscoASASm1sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1275)
)
_CiscoASASm1sy_ObjectIdentity = ObjectIdentity
ciscoASASm1sy = _CiscoASASm1sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1276)
)
_CiscoASASm1_ObjectIdentity = ObjectIdentity
ciscoASASm1 = _CiscoASASm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1277)
)
_Cat2960cPD8TT_ObjectIdentity = ObjectIdentity
cat2960cPD8TT = _Cat2960cPD8TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1278)
)
_CiscoAirCt2504K9_ObjectIdentity = ObjectIdentity
ciscoAirCt2504K9 = _CiscoAirCt2504K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1279)
)
_CiscoISMAXP_ObjectIdentity = ObjectIdentity
ciscoISMAXP = _CiscoISMAXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1280)
)
_CiscoSMAXP_ObjectIdentity = ObjectIdentity
ciscoSMAXP = _CiscoSMAXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1281)
)
_CiscoAxpSmSre900_ObjectIdentity = ObjectIdentity
ciscoAxpSmSre900 = _CiscoAxpSmSre900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1282)
)
_CiscoAxpSmSre700_ObjectIdentity = ObjectIdentity
ciscoAxpSmSre700 = _CiscoAxpSmSre700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1283)
)
_CiscoAxpIsmSre300_ObjectIdentity = ObjectIdentity
ciscoAxpIsmSre300 = _CiscoAxpIsmSre300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1284)
)
_CiscoCDSISM_ObjectIdentity = ObjectIdentity
ciscoCDSISM = _CiscoCDSISM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1285)
)
_Cat4507rpluse_ObjectIdentity = ObjectIdentity
cat4507rpluse = _Cat4507rpluse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1286)
)
_Cat4510rpluse_ObjectIdentity = ObjectIdentity
cat4510rpluse = _Cat4510rpluse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1287)
)
_CiscoAxpNme302_ObjectIdentity = ObjectIdentity
ciscoAxpNme302 = _CiscoAxpNme302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1288)
)
_CiscoAxpNme502_ObjectIdentity = ObjectIdentity
ciscoAxpNme502 = _CiscoAxpNme502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1289)
)
_CiscoAxpNme522_ObjectIdentity = ObjectIdentity
ciscoAxpNme522 = _CiscoAxpNme522_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1290)
)
_CiscoACE20K9_ObjectIdentity = ObjectIdentity
ciscoACE20K9 = _CiscoACE20K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1291)
)
_CiscoWsC236048tdS_ObjectIdentity = ObjectIdentity
ciscoWsC236048tdS = _CiscoWsC236048tdS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1292)
)
_CiscoWiSM2_ObjectIdentity = ObjectIdentity
ciscoWiSM2 = _CiscoWiSM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1293)
)
_CiscoCDScde250_ObjectIdentity = ObjectIdentity
ciscoCDScde250 = _CiscoCDScde250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1294)
)
_Cisco7500Wlc_ObjectIdentity = ObjectIdentity
cisco7500Wlc = _Cisco7500Wlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1295)
)
_CiscoAnmVirtualApp_ObjectIdentity = ObjectIdentity
ciscoAnmVirtualApp = _CiscoAnmVirtualApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1296)
)
_CiscoECDS3100_ObjectIdentity = ObjectIdentity
ciscoECDS3100 = _CiscoECDS3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1297)
)
_CiscoECDS1100_ObjectIdentity = ObjectIdentity
ciscoECDS1100 = _CiscoECDS1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1298)
)
_Cisco881G2_ObjectIdentity = ObjectIdentity
cisco881G2 = _Cisco881G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1299)
)
_CatWsC3750v224fsS_ObjectIdentity = ObjectIdentity
catWsC3750v224fsS = _CatWsC3750v224fsS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1300)
)
_CiscoOeVWaas_ObjectIdentity = ObjectIdentity
ciscoOeVWaas = _CiscoOeVWaas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1301)
)
_CiscoASA5585Ssp10K7_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp10K7 = _CiscoASA5585Ssp10K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1302)
)
_CiscoASA5585Ssp20K7_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp20K7 = _CiscoASA5585Ssp20K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1303)
)
_CiscoASA5585Ssp40K7_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp40K7 = _CiscoASA5585Ssp40K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1304)
)
_CiscoASA5585Ssp60K7_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp60K7 = _CiscoASA5585Ssp60K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1305)
)
_CiscoASA5585Ssp10K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp10K7sc = _CiscoASA5585Ssp10K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1306)
)
_CiscoASA5585Ssp20K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp20K7sc = _CiscoASA5585Ssp20K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1307)
)
_CiscoASA5585Ssp40K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp40K7sc = _CiscoASA5585Ssp40K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1308)
)
_CiscoASA5585Ssp60K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp60K7sc = _CiscoASA5585Ssp60K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1309)
)
_CiscoASA5585Ssp10K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp10K7sy = _CiscoASA5585Ssp10K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1310)
)
_CiscoASA5585Ssp20K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp20K7sy = _CiscoASA5585Ssp20K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1311)
)
_CiscoASA5585Ssp40K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp40K7sy = _CiscoASA5585Ssp40K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1312)
)
_CiscoASA5585Ssp60K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5585Ssp60K7sy = _CiscoASA5585Ssp60K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1313)
)
_CiscoSreSmNam_ObjectIdentity = ObjectIdentity
ciscoSreSmNam = _CiscoSreSmNam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1314)
)
_Cat2960cPD8PT_ObjectIdentity = ObjectIdentity
cat2960cPD8PT = _Cat2960cPD8PT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1315)
)
_Cat2960cG8TC_ObjectIdentity = ObjectIdentity
cat2960cG8TC = _Cat2960cG8TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1316)
)
_Cat3560cG8PC_ObjectIdentity = ObjectIdentity
cat3560cG8PC = _Cat3560cG8PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1317)
)
_Cat3560cG8TC_ObjectIdentity = ObjectIdentity
cat3560cG8TC = _Cat3560cG8TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1318)
)
_CiscoIE301016S8PC_ObjectIdentity = ObjectIdentity
ciscoIE301016S8PC = _CiscoIE301016S8PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1319)
)
_CiscoIE301024TC_ObjectIdentity = ObjectIdentity
ciscoIE301024TC = _CiscoIE301024TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1320)
)
_CiscoRAIE1783RMSB10T_ObjectIdentity = ObjectIdentity
ciscoRAIE1783RMSB10T = _CiscoRAIE1783RMSB10T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1321)
)
_CiscoRAIE1783RMSB06T_ObjectIdentity = ObjectIdentity
ciscoRAIE1783RMSB06T = _CiscoRAIE1783RMSB06T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1322)
)
_CiscoASA5585SspIps10K7_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps10K7 = _CiscoASA5585SspIps10K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1323)
)
_CiscoASA5585SspIps20K7_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps20K7 = _CiscoASA5585SspIps20K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1324)
)
_CiscoASA5585SspIps40K7_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps40K7 = _CiscoASA5585SspIps40K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1325)
)
_CiscoASA5585SspIps60K7_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps60K7 = _CiscoASA5585SspIps60K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1326)
)
_Catalyst4948ef10GE_ObjectIdentity = ObjectIdentity
catalyst4948ef10GE = _Catalyst4948ef10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1327)
)
_Cat292824TCC_ObjectIdentity = ObjectIdentity
cat292824TCC = _Cat292824TCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1328)
)
_Cat292848TCC_ObjectIdentity = ObjectIdentity
cat292848TCC = _Cat292848TCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1329)
)
_Cat292824LTC_ObjectIdentity = ObjectIdentity
cat292824LTC = _Cat292824LTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1330)
)
_CiscoCrs16SB_ObjectIdentity = ObjectIdentity
ciscoCrs16SB = _CiscoCrs16SB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1331)
)
_CiscoQuad_ObjectIdentity = ObjectIdentity
ciscoQuad = _CiscoQuad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1332)
)
_CiscoASASm1K7sc_ObjectIdentity = ObjectIdentity
ciscoASASm1K7sc = _CiscoASASm1K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1334)
)
_CiscoASASm1K7sy_ObjectIdentity = ObjectIdentity
ciscoASASm1K7sy = _CiscoASASm1K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1335)
)
_CiscoASASm1K7_ObjectIdentity = ObjectIdentity
ciscoASASm1K7 = _CiscoASASm1K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1336)
)
_CiscoPwrCGR2010PoeAC_ObjectIdentity = ObjectIdentity
ciscoPwrCGR2010PoeAC = _CiscoPwrCGR2010PoeAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1337)
)
_CiscoPwrCGR2010PoeDC_ObjectIdentity = ObjectIdentity
ciscoPwrCGR2010PoeDC = _CiscoPwrCGR2010PoeDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1338)
)
_Cisco1861eUc2BK9_ObjectIdentity = ObjectIdentity
cisco1861eUc2BK9 = _Cisco1861eUc2BK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1339)
)
_Cisco1861eUc4FK9_ObjectIdentity = ObjectIdentity
cisco1861eUc4FK9 = _Cisco1861eUc4FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1340)
)
_CiscoC1861eSrstFK9_ObjectIdentity = ObjectIdentity
ciscoC1861eSrstFK9 = _CiscoC1861eSrstFK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1341)
)
_CiscoC1861eSrstBK9_ObjectIdentity = ObjectIdentity
ciscoC1861eSrstBK9 = _CiscoC1861eSrstBK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1342)
)
_CiscoC1861eSrstCFK9_ObjectIdentity = ObjectIdentity
ciscoC1861eSrstCFK9 = _CiscoC1861eSrstCFK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1343)
)
_CiscoC1861eSrstCBK9_ObjectIdentity = ObjectIdentity
ciscoC1861eSrstCBK9 = _CiscoC1861eSrstCBK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1344)
)
_CiscoGrwicDes6s_ObjectIdentity = ObjectIdentity
ciscoGrwicDes6s = _CiscoGrwicDes6s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1346)
)
_CiscoGrwicDes2s8pc_ObjectIdentity = ObjectIdentity
ciscoGrwicDes2s8pc = _CiscoGrwicDes2s8pc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1347)
)
_CiscoUCVirtualMachine_ObjectIdentity = ObjectIdentity
ciscoUCVirtualMachine = _CiscoUCVirtualMachine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1348)
)
_CiscoWave8541_ObjectIdentity = ObjectIdentity
ciscoWave8541 = _CiscoWave8541_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1349)
)
_CiscoWave7571_ObjectIdentity = ObjectIdentity
ciscoWave7571 = _CiscoWave7571_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1350)
)
_CiscoWave7541_ObjectIdentity = ObjectIdentity
ciscoWave7541 = _CiscoWave7541_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1351)
)
_CiscoWave694_ObjectIdentity = ObjectIdentity
ciscoWave694 = _CiscoWave694_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1352)
)
_CiscoWave594_ObjectIdentity = ObjectIdentity
ciscoWave594 = _CiscoWave594_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1353)
)
_CiscoWave294_ObjectIdentity = ObjectIdentity
ciscoWave294 = _CiscoWave294_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1354)
)
_Cisco5915RC_ObjectIdentity = ObjectIdentity
cisco5915RC = _Cisco5915RC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1355)
)
_Cisco5915RA_ObjectIdentity = ObjectIdentity
cisco5915RA = _Cisco5915RA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1356)
)
_Cisco867VAEK9_ObjectIdentity = ObjectIdentity
cisco867VAEK9 = _Cisco867VAEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1358)
)
_Cisco866VAEK9_ObjectIdentity = ObjectIdentity
cisco866VAEK9 = _Cisco866VAEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1359)
)
_Cisco867VAE_ObjectIdentity = ObjectIdentity
cisco867VAE = _Cisco867VAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1360)
)
_Cisco866VAE_ObjectIdentity = ObjectIdentity
cisco866VAE = _Cisco866VAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1361)
)
_CiscoAp802gn_ObjectIdentity = ObjectIdentity
ciscoAp802gn = _CiscoAp802gn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1362)
)
_CiscoAp802agn_ObjectIdentity = ObjectIdentity
ciscoAp802agn = _CiscoAp802agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1363)
)
_CatwsC2960C8tcS_ObjectIdentity = ObjectIdentity
catwsC2960C8tcS = _CatwsC2960C8tcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1364)
)
_CatwsC2960C8tcL_ObjectIdentity = ObjectIdentity
catwsC2960C8tcL = _CatwsC2960C8tcL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1365)
)
_CatwsC2960C8pcL_ObjectIdentity = ObjectIdentity
catwsC2960C8pcL = _CatwsC2960C8pcL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1366)
)
_CatwsC2960C12pcL_ObjectIdentity = ObjectIdentity
catwsC2960C12pcL = _CatwsC2960C12pcL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1367)
)
_CatwsC3560CPD8ptS_ObjectIdentity = ObjectIdentity
catwsC3560CPD8ptS = _CatwsC3560CPD8ptS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1368)
)
_Cisco1841ve_ObjectIdentity = ObjectIdentity
cisco1841ve = _Cisco1841ve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1369)
)
_Cisco2811ve_ObjectIdentity = ObjectIdentity
cisco2811ve = _Cisco2811ve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1370)
)
_Cisco881WAK9_ObjectIdentity = ObjectIdentity
cisco881WAK9 = _Cisco881WAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1371)
)
_Cisco881WEK9_ObjectIdentity = ObjectIdentity
cisco881WEK9 = _Cisco881WEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1372)
)
_Cisco881WPK9_ObjectIdentity = ObjectIdentity
cisco881WPK9 = _Cisco881WPK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1373)
)
_Cisco886VaWEK9_ObjectIdentity = ObjectIdentity
cisco886VaWEK9 = _Cisco886VaWEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1374)
)
_Cisco887VamWEK9_ObjectIdentity = ObjectIdentity
cisco887VamWEK9 = _Cisco887VamWEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1375)
)
_Cisco887VaWAK9_ObjectIdentity = ObjectIdentity
cisco887VaWAK9 = _Cisco887VaWAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1376)
)
_Cisco887VaWEK9_ObjectIdentity = ObjectIdentity
cisco887VaWEK9 = _Cisco887VaWEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1377)
)
_Cisco819GUK9_ObjectIdentity = ObjectIdentity
cisco819GUK9 = _Cisco819GUK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1378)
)
_Cisco819GSK9_ObjectIdentity = ObjectIdentity
cisco819GSK9 = _Cisco819GSK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1379)
)
_Cisco819GVK9_ObjectIdentity = ObjectIdentity
cisco819GVK9 = _Cisco819GVK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1380)
)
_Cisco819GBK9_ObjectIdentity = ObjectIdentity
cisco819GBK9 = _Cisco819GBK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1381)
)
_Cisco819G7AK9_ObjectIdentity = ObjectIdentity
cisco819G7AK9 = _Cisco819G7AK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1382)
)
_Cisco819G7K9_ObjectIdentity = ObjectIdentity
cisco819G7K9 = _Cisco819G7K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1383)
)
_Cisco819HGUK9_ObjectIdentity = ObjectIdentity
cisco819HGUK9 = _Cisco819HGUK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1384)
)
_Cisco819HGSK9_ObjectIdentity = ObjectIdentity
cisco819HGSK9 = _Cisco819HGSK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1385)
)
_Cisco819HGVK9_ObjectIdentity = ObjectIdentity
cisco819HGVK9 = _Cisco819HGVK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1386)
)
_Cisco819HGBK9_ObjectIdentity = ObjectIdentity
cisco819HGBK9 = _Cisco819HGBK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1387)
)
_Cisco819HG7AK9_ObjectIdentity = ObjectIdentity
cisco819HG7AK9 = _Cisco819HG7AK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1388)
)
_Cisco819HG7K9_ObjectIdentity = ObjectIdentity
cisco819HG7K9 = _Cisco819HG7K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1389)
)
_Cisco886Vag7K9_ObjectIdentity = ObjectIdentity
cisco886Vag7K9 = _Cisco886Vag7K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1390)
)
_Cisco887VagSK9_ObjectIdentity = ObjectIdentity
cisco887VagSK9 = _Cisco887VagSK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1391)
)
_Cisco887Vag7K9_ObjectIdentity = ObjectIdentity
cisco887Vag7K9 = _Cisco887Vag7K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1392)
)
_Cisco887Vamg7K9_ObjectIdentity = ObjectIdentity
cisco887Vamg7K9 = _Cisco887Vamg7K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1393)
)
_Cisco888Eg7K9_ObjectIdentity = ObjectIdentity
cisco888Eg7K9 = _Cisco888Eg7K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1394)
)
_Cisco881GUK9_ObjectIdentity = ObjectIdentity
cisco881GUK9 = _Cisco881GUK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1395)
)
_Cisco881GSK9_ObjectIdentity = ObjectIdentity
cisco881GSK9 = _Cisco881GSK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1396)
)
_Cisco881GVK9_ObjectIdentity = ObjectIdentity
cisco881GVK9 = _Cisco881GVK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1397)
)
_Cisco881GBK9_ObjectIdentity = ObjectIdentity
cisco881GBK9 = _Cisco881GBK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1398)
)
_Cisco881G7K9_ObjectIdentity = ObjectIdentity
cisco881G7K9 = _Cisco881G7K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1399)
)
_Cisco881G7AK9_ObjectIdentity = ObjectIdentity
cisco881G7AK9 = _Cisco881G7AK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1400)
)
_Cat3750x24s_ObjectIdentity = ObjectIdentity
cat3750x24s = _Cat3750x24s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1404)
)
_Cat3750x12s_ObjectIdentity = ObjectIdentity
cat3750x12s = _Cat3750x12s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1405)
)
_CiscoNME_ObjectIdentity = ObjectIdentity
ciscoNME = _CiscoNME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1406)
)
_CiscoASA5512_ObjectIdentity = ObjectIdentity
ciscoASA5512 = _CiscoASA5512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1407)
)
_CiscoASA5525_ObjectIdentity = ObjectIdentity
ciscoASA5525 = _CiscoASA5525_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1408)
)
_CiscoASA5545_ObjectIdentity = ObjectIdentity
ciscoASA5545 = _CiscoASA5545_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1409)
)
_CiscoASA5555_ObjectIdentity = ObjectIdentity
ciscoASA5555 = _CiscoASA5555_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1410)
)
_CiscoASA5512sc_ObjectIdentity = ObjectIdentity
ciscoASA5512sc = _CiscoASA5512sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1411)
)
_CiscoASA5525sc_ObjectIdentity = ObjectIdentity
ciscoASA5525sc = _CiscoASA5525sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1412)
)
_CiscoASA5545sc_ObjectIdentity = ObjectIdentity
ciscoASA5545sc = _CiscoASA5545sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1413)
)
_CiscoASA5555sc_ObjectIdentity = ObjectIdentity
ciscoASA5555sc = _CiscoASA5555sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1414)
)
_CiscoASA5512sy_ObjectIdentity = ObjectIdentity
ciscoASA5512sy = _CiscoASA5512sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1415)
)
_CiscoASA5515sy_ObjectIdentity = ObjectIdentity
ciscoASA5515sy = _CiscoASA5515sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1416)
)
_CiscoASA5525sy_ObjectIdentity = ObjectIdentity
ciscoASA5525sy = _CiscoASA5525sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1417)
)
_CiscoASA5545sy_ObjectIdentity = ObjectIdentity
ciscoASA5545sy = _CiscoASA5545sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1418)
)
_CiscoASA5555sy_ObjectIdentity = ObjectIdentity
ciscoASA5555sy = _CiscoASA5555sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1419)
)
_CiscoASA5515sc_ObjectIdentity = ObjectIdentity
ciscoASA5515sc = _CiscoASA5515sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1420)
)
_CiscoASA5515_ObjectIdentity = ObjectIdentity
ciscoASA5515 = _CiscoASA5515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1421)
)
_CiscoPCM_ObjectIdentity = ObjectIdentity
ciscoPCM = _CiscoPCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1422)
)
_CiscoIse3315K9_ObjectIdentity = ObjectIdentity
ciscoIse3315K9 = _CiscoIse3315K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1423)
)
_CiscoIse3395K9_ObjectIdentity = ObjectIdentity
ciscoIse3395K9 = _CiscoIse3395K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1424)
)
_CiscoIse3355K9_ObjectIdentity = ObjectIdentity
ciscoIse3355K9 = _CiscoIse3355K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1425)
)
_CiscoIseVmK9_ObjectIdentity = ObjectIdentity
ciscoIseVmK9 = _CiscoIseVmK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1426)
)
_CiscoIPS4345_ObjectIdentity = ObjectIdentity
ciscoIPS4345 = _CiscoIPS4345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1428)
)
_CiscoIPS4360_ObjectIdentity = ObjectIdentity
ciscoIPS4360 = _CiscoIPS4360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1429)
)
_CiscoEcdsVB_ObjectIdentity = ObjectIdentity
ciscoEcdsVB = _CiscoEcdsVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1432)
)
_CiscoTsCodecG2_ObjectIdentity = ObjectIdentity
ciscoTsCodecG2 = _CiscoTsCodecG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1433)
)
_CiscoTsCodecG2C_ObjectIdentity = ObjectIdentity
ciscoTsCodecG2C = _CiscoTsCodecG2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1434)
)
_CiscoTSCodecG2RC_ObjectIdentity = ObjectIdentity
ciscoTSCodecG2RC = _CiscoTSCodecG2RC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1435)
)
_CiscoTSCodecG2R_ObjectIdentity = ObjectIdentity
ciscoTSCodecG2R = _CiscoTSCodecG2R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1436)
)
_CiscoASA5585SspIps10Virtual_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps10Virtual = _CiscoASA5585SspIps10Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1437)
)
_CiscoASA5585SspIps20Virtual_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps20Virtual = _CiscoASA5585SspIps20Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1438)
)
_CiscoASA5585SspIps40Virtual_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps40Virtual = _CiscoASA5585SspIps40Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1439)
)
_CiscoASA5585SspIps60Virtual_ObjectIdentity = ObjectIdentity
ciscoASA5585SspIps60Virtual = _CiscoASA5585SspIps60Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1440)
)
_CiscoASR903_ObjectIdentity = ObjectIdentity
ciscoASR903 = _CiscoASR903_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1441)
)
_CiscoASA5512K7_ObjectIdentity = ObjectIdentity
ciscoASA5512K7 = _CiscoASA5512K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1442)
)
_CiscoASA5515K7_ObjectIdentity = ObjectIdentity
ciscoASA5515K7 = _CiscoASA5515K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1443)
)
_CiscoASA5525K7_ObjectIdentity = ObjectIdentity
ciscoASA5525K7 = _CiscoASA5525K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1444)
)
_CiscoASA5545K7_ObjectIdentity = ObjectIdentity
ciscoASA5545K7 = _CiscoASA5545K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1445)
)
_CiscoASA5555K7_ObjectIdentity = ObjectIdentity
ciscoASA5555K7 = _CiscoASA5555K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1446)
)
_CiscoASA5512K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5512K7sc = _CiscoASA5512K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1447)
)
_CiscoASA5515K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5515K7sc = _CiscoASA5515K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1448)
)
_CiscoASA5525K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5525K7sc = _CiscoASA5525K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1449)
)
_CiscoASA5545K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5545K7sc = _CiscoASA5545K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1450)
)
_CiscoASA5555K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5555K7sc = _CiscoASA5555K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1451)
)
_CiscoASA5512K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5512K7sy = _CiscoASA5512K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1452)
)
_CiscoASA5515K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5515K7sy = _CiscoASA5515K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1453)
)
_CiscoASA5525K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5525K7sy = _CiscoASA5525K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1454)
)
_CiscoASA5545K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5545K7sy = _CiscoASA5545K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1455)
)
_CiscoASA5555K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5555K7sy = _CiscoASA5555K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1456)
)
_CiscoASR5500_ObjectIdentity = ObjectIdentity
ciscoASR5500 = _CiscoASR5500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1457)
)
_CiscoXfp10Ger192IrL_ObjectIdentity = ObjectIdentity
ciscoXfp10Ger192IrL = _CiscoXfp10Ger192IrL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1462)
)
_CiscoXfp10Glr192SrL_ObjectIdentity = ObjectIdentity
ciscoXfp10Glr192SrL = _CiscoXfp10Glr192SrL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1463)
)
_CiscoXfp10Gzr192LrL_ObjectIdentity = ObjectIdentity
ciscoXfp10Gzr192LrL = _CiscoXfp10Gzr192LrL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1464)
)
_CatwsC3560C12pcS_ObjectIdentity = ObjectIdentity
catwsC3560C12pcS = _CatwsC3560C12pcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1465)
)
_CatwsC3560C8pcS_ObjectIdentity = ObjectIdentity
catwsC3560C8pcS = _CatwsC3560C8pcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1466)
)
_CiscoCRSFabBP_ObjectIdentity = ObjectIdentity
ciscoCRSFabBP = _CiscoCRSFabBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1467)
)
_CiscoIE20004TS_ObjectIdentity = ObjectIdentity
ciscoIE20004TS = _CiscoIE20004TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1468)
)
_CiscoIE20004T_ObjectIdentity = ObjectIdentity
ciscoIE20004T = _CiscoIE20004T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1469)
)
_CiscoIE20004TSG_ObjectIdentity = ObjectIdentity
ciscoIE20004TSG = _CiscoIE20004TSG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1470)
)
_CiscoIE20004TG_ObjectIdentity = ObjectIdentity
ciscoIE20004TG = _CiscoIE20004TG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1471)
)
_CiscoIE20008TC_ObjectIdentity = ObjectIdentity
ciscoIE20008TC = _CiscoIE20008TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1472)
)
_CiscoIE20008TCG_ObjectIdentity = ObjectIdentity
ciscoIE20008TCG = _CiscoIE20008TCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1473)
)
_CiscoIE200016TC_ObjectIdentity = ObjectIdentity
ciscoIE200016TC = _CiscoIE200016TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1474)
)
_CiscoIE200016TCG_ObjectIdentity = ObjectIdentity
ciscoIE200016TCG = _CiscoIE200016TCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1475)
)
_CiscoRAIE1783BMS06SL_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS06SL = _CiscoRAIE1783BMS06SL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1476)
)
_CiscoRAIE1783BMS06TL_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS06TL = _CiscoRAIE1783BMS06TL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1477)
)
_CiscoRAIE1783BMS06TA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS06TA = _CiscoRAIE1783BMS06TA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1478)
)
_CiscoRAIE1783BMS06SGL_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS06SGL = _CiscoRAIE1783BMS06SGL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1479)
)
_CiscoRAIE1783BMS06SGA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS06SGA = _CiscoRAIE1783BMS06SGA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1480)
)
_CiscoRAIE1783BMS06TGL_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS06TGL = _CiscoRAIE1783BMS06TGL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1481)
)
_CiscoRAIE1783BMS06TGA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS06TGA = _CiscoRAIE1783BMS06TGA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1482)
)
_CiscoRAIE1783BMS10CL_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS10CL = _CiscoRAIE1783BMS10CL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1483)
)
_CiscoRAIE1783BMS10CA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS10CA = _CiscoRAIE1783BMS10CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1484)
)
_CiscoRAIE1783BMS10CGL_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS10CGL = _CiscoRAIE1783BMS10CGL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1485)
)
_CiscoRAIE1783BMS10CGA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS10CGA = _CiscoRAIE1783BMS10CGA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1486)
)
_CiscoRAIE1783BMS10CGP_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS10CGP = _CiscoRAIE1783BMS10CGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1487)
)
_CiscoRAIE1783BMS10CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS10CGN = _CiscoRAIE1783BMS10CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1488)
)
_CiscoRAIE1783BMS20CL_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS20CL = _CiscoRAIE1783BMS20CL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1489)
)
_CiscoRAIE1783BMS20CA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS20CA = _CiscoRAIE1783BMS20CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1490)
)
_CiscoRAIE1783BMS20CGL_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS20CGL = _CiscoRAIE1783BMS20CGL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1491)
)
_CiscoRAIE1783BMS20CGP_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS20CGP = _CiscoRAIE1783BMS20CGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1492)
)
_CiscoRAIE1783BMS20CGPK_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS20CGPK = _CiscoRAIE1783BMS20CGPK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1493)
)
_Cisco819HG4GGK9_ObjectIdentity = ObjectIdentity
cisco819HG4GGK9 = _Cisco819HG4GGK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1494)
)
_Cisco819G4GAK9_ObjectIdentity = ObjectIdentity
cisco819G4GAK9 = _Cisco819G4GAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1495)
)
_Cisco819G4GVK9_ObjectIdentity = ObjectIdentity
cisco819G4GVK9 = _Cisco819G4GVK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1496)
)
_Cisco819G4GGK9_ObjectIdentity = ObjectIdentity
cisco819G4GGK9 = _Cisco819G4GGK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1497)
)
_CiscoUcsC200_ObjectIdentity = ObjectIdentity
ciscoUcsC200 = _CiscoUcsC200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1512)
)
_CiscoUcsC210_ObjectIdentity = ObjectIdentity
ciscoUcsC210 = _CiscoUcsC210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1513)
)
_CiscoUcsC250_ObjectIdentity = ObjectIdentity
ciscoUcsC250 = _CiscoUcsC250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1514)
)
_CiscoUcsC260_ObjectIdentity = ObjectIdentity
ciscoUcsC260 = _CiscoUcsC260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1515)
)
_CiscoUcsC460_ObjectIdentity = ObjectIdentity
ciscoUcsC460 = _CiscoUcsC460_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1516)
)
_CiscoRAIE1783BMS06SA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS06SA = _CiscoRAIE1783BMS06SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1519)
)
_CiscoIE200016TCGX_ObjectIdentity = ObjectIdentity
ciscoIE200016TCGX = _CiscoIE200016TCGX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1520)
)
_CiscoASR901_ObjectIdentity = ObjectIdentity
ciscoASR901 = _CiscoASR901_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1521)
)
_CiscoASR901E_ObjectIdentity = ObjectIdentity
ciscoASR901E = _CiscoASR901E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1522)
)
_CiscoOeSmSre910_ObjectIdentity = ObjectIdentity
ciscoOeSmSre910 = _CiscoOeSmSre910_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1523)
)
_CiscoOeSmSre710_ObjectIdentity = ObjectIdentity
ciscoOeSmSre710 = _CiscoOeSmSre710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1524)
)
_CiscoASR1002X_ObjectIdentity = ObjectIdentity
ciscoASR1002X = _CiscoASR1002X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1525)
)
_CiscoNam2304_ObjectIdentity = ObjectIdentity
ciscoNam2304 = _CiscoNam2304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1527)
)
_CiscoNam2320_ObjectIdentity = ObjectIdentity
ciscoNam2320 = _CiscoNam2320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1528)
)
_CiscoNam3_ObjectIdentity = ObjectIdentity
ciscoNam3 = _CiscoNam3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1529)
)
_Cisco819HG4GAK9_ObjectIdentity = ObjectIdentity
cisco819HG4GAK9 = _Cisco819HG4GAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1530)
)
_CiscoECDS50IVB_ObjectIdentity = ObjectIdentity
ciscoECDS50IVB = _CiscoECDS50IVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1536)
)
_CiscoCSR1000v_ObjectIdentity = ObjectIdentity
ciscoCSR1000v = _CiscoCSR1000v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1537)
)
_CiscoASR5000_ObjectIdentity = ObjectIdentity
ciscoASR5000 = _CiscoASR5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1538)
)
_CiscoflowAgent3000_ObjectIdentity = ObjectIdentity
ciscoflowAgent3000 = _CiscoflowAgent3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1539)
)
_CiscoTelePresenceMCU5310_ObjectIdentity = ObjectIdentity
ciscoTelePresenceMCU5310 = _CiscoTelePresenceMCU5310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1540)
)
_CiscoTelePresenceMCU5320_ObjectIdentity = ObjectIdentity
ciscoTelePresenceMCU5320 = _CiscoTelePresenceMCU5320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1541)
)
_Cisco888ea_ObjectIdentity = ObjectIdentity
cisco888ea = _Cisco888ea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1542)
)
_CiscoVG350_ObjectIdentity = ObjectIdentity
ciscoVG350 = _CiscoVG350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1557)
)
_Cisco881GW7AK9_ObjectIdentity = ObjectIdentity
cisco881GW7AK9 = _Cisco881GW7AK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1560)
)
_Cisco881GW7EK9_ObjectIdentity = ObjectIdentity
cisco881GW7EK9 = _Cisco881GW7EK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1561)
)
_Cisco881GWSAK9_ObjectIdentity = ObjectIdentity
cisco881GWSAK9 = _Cisco881GWSAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1562)
)
_Cisco881GWVAK9_ObjectIdentity = ObjectIdentity
cisco881GWVAK9 = _Cisco881GWVAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1563)
)
_Cisco887Vagw7AK9_ObjectIdentity = ObjectIdentity
cisco887Vagw7AK9 = _Cisco887Vagw7AK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1564)
)
_Cisco887Vagw7EK9_ObjectIdentity = ObjectIdentity
cisco887Vagw7EK9 = _Cisco887Vagw7EK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1565)
)
_Cisco881WDAK9_ObjectIdentity = ObjectIdentity
cisco881WDAK9 = _Cisco881WDAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1566)
)
_Cisco881WDEK9_ObjectIdentity = ObjectIdentity
cisco881WDEK9 = _Cisco881WDEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1567)
)
_Cisco887VaWDAK9_ObjectIdentity = ObjectIdentity
cisco887VaWDAK9 = _Cisco887VaWDAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1568)
)
_Cisco887VaWDEK9_ObjectIdentity = ObjectIdentity
cisco887VaWDEK9 = _Cisco887VaWDEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1569)
)
_Cisco819HGW7EK9_ObjectIdentity = ObjectIdentity
cisco819HGW7EK9 = _Cisco819HGW7EK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1570)
)
_Cisco819HGW7NK9_ObjectIdentity = ObjectIdentity
cisco819HGW7NK9 = _Cisco819HGW7NK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1571)
)
_Cisco819HGW7AAK9_ObjectIdentity = ObjectIdentity
cisco819HGW7AAK9 = _Cisco819HGW7AAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1572)
)
_Cisco819HGWVAK9_ObjectIdentity = ObjectIdentity
cisco819HGWVAK9 = _Cisco819HGWVAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1573)
)
_Cisco819HGWSAK9_ObjectIdentity = ObjectIdentity
cisco819HGWSAK9 = _Cisco819HGWSAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1574)
)
_Cisco819HK9_ObjectIdentity = ObjectIdentity
cisco819HK9 = _Cisco819HK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1575)
)
_Cisco819HWDEK9_ObjectIdentity = ObjectIdentity
cisco819HWDEK9 = _Cisco819HWDEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1576)
)
_Cisco819HWDAK9_ObjectIdentity = ObjectIdentity
cisco819HWDAK9 = _Cisco819HWDAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1577)
)
_Cisco812G7K9_ObjectIdentity = ObjectIdentity
cisco812G7K9 = _Cisco812G7K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1578)
)
_Cisco812GCIFI7EK9_ObjectIdentity = ObjectIdentity
cisco812GCIFI7EK9 = _Cisco812GCIFI7EK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1579)
)
_Cisco812GCIFI7NK9_ObjectIdentity = ObjectIdentity
cisco812GCIFI7NK9 = _Cisco812GCIFI7NK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1580)
)
_Cisco812GCIFIVAK9_ObjectIdentity = ObjectIdentity
cisco812GCIFIVAK9 = _Cisco812GCIFIVAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1581)
)
_Cisco812GCIFISAK9_ObjectIdentity = ObjectIdentity
cisco812GCIFISAK9 = _Cisco812GCIFISAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1582)
)
_Cisco819GUMK9_ObjectIdentity = ObjectIdentity
cisco819GUMK9 = _Cisco819GUMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1583)
)
_Cisco819GSMK9_ObjectIdentity = ObjectIdentity
cisco819GSMK9 = _Cisco819GSMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1584)
)
_Cisco819GVMK9_ObjectIdentity = ObjectIdentity
cisco819GVMK9 = _Cisco819GVMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1585)
)
_Cisco819GBMK9_ObjectIdentity = ObjectIdentity
cisco819GBMK9 = _Cisco819GBMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1586)
)
_Cisco819G7AMK9_ObjectIdentity = ObjectIdentity
cisco819G7AMK9 = _Cisco819G7AMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1587)
)
_Cisco819G7MK9_ObjectIdentity = ObjectIdentity
cisco819G7MK9 = _Cisco819G7MK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1588)
)
_Cisco819HGUMK9_ObjectIdentity = ObjectIdentity
cisco819HGUMK9 = _Cisco819HGUMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1589)
)
_Cisco819HGSMK9_ObjectIdentity = ObjectIdentity
cisco819HGSMK9 = _Cisco819HGSMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1590)
)
_Cisco819HGVMK9_ObjectIdentity = ObjectIdentity
cisco819HGVMK9 = _Cisco819HGVMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1591)
)
_Cisco819HGBMK9_ObjectIdentity = ObjectIdentity
cisco819HGBMK9 = _Cisco819HGBMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1592)
)
_Cisco819HG7AMK9_ObjectIdentity = ObjectIdentity
cisco819HG7AMK9 = _Cisco819HG7AMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1593)
)
_Cisco819HG7MK9_ObjectIdentity = ObjectIdentity
cisco819HG7MK9 = _Cisco819HG7MK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1594)
)
_CiscoCDScde2502s6_ObjectIdentity = ObjectIdentity
ciscoCDScde2502s6 = _CiscoCDScde2502s6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1595)
)
_CiscoCDScde2502m0_ObjectIdentity = ObjectIdentity
ciscoCDScde2502m0 = _CiscoCDScde2502m0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1596)
)
_CiscoCDScde2502s8_ObjectIdentity = ObjectIdentity
ciscoCDScde2502s8 = _CiscoCDScde2502s8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1597)
)
_Cisco881V_ObjectIdentity = ObjectIdentity
cisco881V = _Cisco881V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1600)
)
_Cisco887vaV_ObjectIdentity = ObjectIdentity
cisco887vaV = _Cisco887vaV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1601)
)
_Cisco887vaVW_ObjectIdentity = ObjectIdentity
cisco887vaVW = _Cisco887vaVW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1602)
)
_CiscoMDE10XVB_ObjectIdentity = ObjectIdentity
ciscoMDE10XVB = _CiscoMDE10XVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1603)
)
_Cat4500X16_ObjectIdentity = ObjectIdentity
cat4500X16 = _Cat4500X16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1605)
)
_Cat4500X32_ObjectIdentity = ObjectIdentity
cat4500X32 = _Cat4500X32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1606)
)
_CiscoCDScde2502s9_ObjectIdentity = ObjectIdentity
ciscoCDScde2502s9 = _CiscoCDScde2502s9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1607)
)
_CiscoCDScde2502s10_ObjectIdentity = ObjectIdentity
ciscoCDScde2502s10 = _CiscoCDScde2502s10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1608)
)
_CiscoASA5585Nm20x1GE_ObjectIdentity = ObjectIdentity
ciscoASA5585Nm20x1GE = _CiscoASA5585Nm20x1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1610)
)
_CiscoCDScdeGeneric_ObjectIdentity = ObjectIdentity
ciscoCDScdeGeneric = _CiscoCDScdeGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1611)
)
_CiscoASA1000Vsy_ObjectIdentity = ObjectIdentity
ciscoASA1000Vsy = _CiscoASA1000Vsy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1612)
)
_CiscoASA1000Vsc_ObjectIdentity = ObjectIdentity
ciscoASA1000Vsc = _CiscoASA1000Vsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1613)
)
_CiscoASA1000V_ObjectIdentity = ObjectIdentity
ciscoASA1000V = _CiscoASA1000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1614)
)
_Cisco8500WLC_ObjectIdentity = ObjectIdentity
cisco8500WLC = _Cisco8500WLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1615)
)
_CiscoASA5585Nm8x10GE_ObjectIdentity = ObjectIdentity
ciscoASA5585Nm8x10GE = _CiscoASA5585Nm8x10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1617)
)
_CiscoASA5585Nm4x10GE_ObjectIdentity = ObjectIdentity
ciscoASA5585Nm4x10GE = _CiscoASA5585Nm4x10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1618)
)
_CiscoISR4400_ObjectIdentity = ObjectIdentity
ciscoISR4400 = _CiscoISR4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1619)
)
_Cisco892FspK9_ObjectIdentity = ObjectIdentity
cisco892FspK9 = _Cisco892FspK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1620)
)
_Cisco897VaMK9_ObjectIdentity = ObjectIdentity
cisco897VaMK9 = _Cisco897VaMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1622)
)
_Cisco897VawEK9_ObjectIdentity = ObjectIdentity
cisco897VawEK9 = _Cisco897VawEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1624)
)
_Cisco897VawAK9_ObjectIdentity = ObjectIdentity
cisco897VawAK9 = _Cisco897VawAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1625)
)
_Cisco897VaK9_ObjectIdentity = ObjectIdentity
cisco897VaK9 = _Cisco897VaK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1626)
)
_Cisco896VaK9_ObjectIdentity = ObjectIdentity
cisco896VaK9 = _Cisco896VaK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1627)
)
_CiscoVirtualWlc_ObjectIdentity = ObjectIdentity
ciscoVirtualWlc = _CiscoVirtualWlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1631)
)
_CiscoAIRAP802agn_ObjectIdentity = ObjectIdentity
ciscoAIRAP802agn = _CiscoAIRAP802agn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1632)
)
_CiscoAp802Hagn_ObjectIdentity = ObjectIdentity
ciscoAp802Hagn = _CiscoAp802Hagn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1633)
)
_CiscoE160DP_ObjectIdentity = ObjectIdentity
ciscoE160DP = _CiscoE160DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1634)
)
_CiscoE160D_ObjectIdentity = ObjectIdentity
ciscoE160D = _CiscoE160D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1635)
)
_CiscoE140DP_ObjectIdentity = ObjectIdentity
ciscoE140DP = _CiscoE140DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1636)
)
_CiscoE140D_ObjectIdentity = ObjectIdentity
ciscoE140D = _CiscoE140D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1637)
)
_CiscoE140S_ObjectIdentity = ObjectIdentity
ciscoE140S = _CiscoE140S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1638)
)
_CiscoASR9001_ObjectIdentity = ObjectIdentity
ciscoASR9001 = _CiscoASR9001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1639)
)
_CiscoASR9922_ObjectIdentity = ObjectIdentity
ciscoASR9922 = _CiscoASR9922_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1640)
)
_Cat385048P_ObjectIdentity = ObjectIdentity
cat385048P = _Cat385048P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1641)
)
_Cat385024P_ObjectIdentity = ObjectIdentity
cat385024P = _Cat385024P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1642)
)
_Cat385048_ObjectIdentity = ObjectIdentity
cat385048 = _Cat385048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1643)
)
_Cat385024_ObjectIdentity = ObjectIdentity
cat385024 = _Cat385024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1644)
)
_Cisco5760wlc_ObjectIdentity = ObjectIdentity
cisco5760wlc = _Cisco5760wlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1645)
)
_CiscoVSGateway_ObjectIdentity = ObjectIdentity
ciscoVSGateway = _CiscoVSGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1646)
)
_CiscoIbiza_ObjectIdentity = ObjectIdentity
ciscoIbiza = _CiscoIbiza_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1647)
)
_CiscoSkyros_ObjectIdentity = ObjectIdentity
ciscoSkyros = _CiscoSkyros_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1648)
)
_CiscoAIRAP1601_ObjectIdentity = ObjectIdentity
ciscoAIRAP1601 = _CiscoAIRAP1601_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1656)
)
_CiscoAIRAP2600_ObjectIdentity = ObjectIdentity
ciscoAIRAP2600 = _CiscoAIRAP2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1657)
)
_CiscoCRS8SB_ObjectIdentity = ObjectIdentity
ciscoCRS8SB = _CiscoCRS8SB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1658)
)
_CiscoAIRAP2602_ObjectIdentity = ObjectIdentity
ciscoAIRAP2602 = _CiscoAIRAP2602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1659)
)
_CiscoAIRAP1602_ObjectIdentity = ObjectIdentity
ciscoAIRAP1602 = _CiscoAIRAP1602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1660)
)
_CiscoAIRAP3602_ObjectIdentity = ObjectIdentity
ciscoAIRAP3602 = _CiscoAIRAP3602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1661)
)
_CiscoAIRAP3601_ObjectIdentity = ObjectIdentity
ciscoAIRAP3601 = _CiscoAIRAP3601_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1662)
)
_CiscoAIRAP1552_ObjectIdentity = ObjectIdentity
ciscoAIRAP1552 = _CiscoAIRAP1552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1664)
)
_CiscoAIRAP1553_ObjectIdentity = ObjectIdentity
ciscoAIRAP1553 = _CiscoAIRAP1553_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1665)
)
_CiscoNgsm3k16gepoeplus_ObjectIdentity = ObjectIdentity
ciscoNgsm3k16gepoeplus = _CiscoNgsm3k16gepoeplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1666)
)
_CiscoNexus1010X_ObjectIdentity = ObjectIdentity
ciscoNexus1010X = _CiscoNexus1010X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1667)
)
_CiscoNexus1110S_ObjectIdentity = ObjectIdentity
ciscoNexus1110S = _CiscoNexus1110S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1668)
)
_CiscoNexus1110X_ObjectIdentity = ObjectIdentity
ciscoNexus1110X = _CiscoNexus1110X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1669)
)
_CiscoNexus1110XL_ObjectIdentity = ObjectIdentity
ciscoNexus1110XL = _CiscoNexus1110XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1670)
)
_CiscoHsE300K9_ObjectIdentity = ObjectIdentity
ciscoHsE300K9 = _CiscoHsE300K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1674)
)
_Cisco866VAEWEK9_ObjectIdentity = ObjectIdentity
cisco866VAEWEK9 = _Cisco866VAEWEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1675)
)
_Cisco867VAEWAK9_ObjectIdentity = ObjectIdentity
cisco867VAEWAK9 = _Cisco867VAEWAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1676)
)
_Cisco867VAEWEK9_ObjectIdentity = ObjectIdentity
cisco867VAEWEK9 = _Cisco867VAEWEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1677)
)
_Cisco867VAEPOEWAK9_ObjectIdentity = ObjectIdentity
cisco867VAEPOEWAK9 = _Cisco867VAEPOEWAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1678)
)
_CiscoSmES3x24P_ObjectIdentity = ObjectIdentity
ciscoSmES3x24P = _CiscoSmES3x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1679)
)
_CiscoSmDES3x48P_ObjectIdentity = ObjectIdentity
ciscoSmDES3x48P = _CiscoSmDES3x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1680)
)
_CiscoOeKWaas_ObjectIdentity = ObjectIdentity
ciscoOeKWaas = _CiscoOeKWaas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1681)
)
_CiscoUcsC220_ObjectIdentity = ObjectIdentity
ciscoUcsC220 = _CiscoUcsC220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1682)
)
_CiscoUcsC240_ObjectIdentity = ObjectIdentity
ciscoUcsC240 = _CiscoUcsC240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1683)
)
_CiscoUcsC22_ObjectIdentity = ObjectIdentity
ciscoUcsC22 = _CiscoUcsC22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1684)
)
_CiscoUcsC24_ObjectIdentity = ObjectIdentity
ciscoUcsC24 = _CiscoUcsC24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1685)
)
_CiscoCDScde2202s4_ObjectIdentity = ObjectIdentity
ciscoCDScde2202s4 = _CiscoCDScde2202s4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1686)
)
_CiscoCDScde4604r1_ObjectIdentity = ObjectIdentity
ciscoCDScde4604r1 = _CiscoCDScde4604r1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1687)
)
_CiscoASR1002XC_ObjectIdentity = ObjectIdentity
ciscoASR1002XC = _CiscoASR1002XC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1688)
)
_CatWsC2960x48fpdL_ObjectIdentity = ObjectIdentity
catWsC2960x48fpdL = _CatWsC2960x48fpdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1690)
)
_CatWsC2960x48lpdL_ObjectIdentity = ObjectIdentity
catWsC2960x48lpdL = _CatWsC2960x48lpdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1691)
)
_CatWsC2960x48tdL_ObjectIdentity = ObjectIdentity
catWsC2960x48tdL = _CatWsC2960x48tdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1692)
)
_CatWsC2960x24pdL_ObjectIdentity = ObjectIdentity
catWsC2960x24pdL = _CatWsC2960x24pdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1693)
)
_CatWsC2960x24tdL_ObjectIdentity = ObjectIdentity
catWsC2960x24tdL = _CatWsC2960x24tdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1694)
)
_CatWsC2960x48fpsL_ObjectIdentity = ObjectIdentity
catWsC2960x48fpsL = _CatWsC2960x48fpsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1695)
)
_CatWsC2960x48lpsL_ObjectIdentity = ObjectIdentity
catWsC2960x48lpsL = _CatWsC2960x48lpsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1696)
)
_CatWsC2960x24psL_ObjectIdentity = ObjectIdentity
catWsC2960x24psL = _CatWsC2960x24psL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1697)
)
_CatWsC2960x48tsL_ObjectIdentity = ObjectIdentity
catWsC2960x48tsL = _CatWsC2960x48tsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1698)
)
_CatWsC2960x24tsL_ObjectIdentity = ObjectIdentity
catWsC2960x24tsL = _CatWsC2960x24tsL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1699)
)
_CatWsC2960x24psqL_ObjectIdentity = ObjectIdentity
catWsC2960x24psqL = _CatWsC2960x24psqL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1700)
)
_CatWsC2960x48lpsS_ObjectIdentity = ObjectIdentity
catWsC2960x48lpsS = _CatWsC2960x48lpsS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1701)
)
_CatWsC2960x24psS_ObjectIdentity = ObjectIdentity
catWsC2960x24psS = _CatWsC2960x24psS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1702)
)
_CatWsC2960x48tsLL_ObjectIdentity = ObjectIdentity
catWsC2960x48tsLL = _CatWsC2960x48tsLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1703)
)
_CatWsC2960x24tsLL_ObjectIdentity = ObjectIdentity
catWsC2960x24tsLL = _CatWsC2960x24tsLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1704)
)
_CiscoISR4441_ObjectIdentity = ObjectIdentity
ciscoISR4441 = _CiscoISR4441_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1705)
)
_CiscoISR4442_ObjectIdentity = ObjectIdentity
ciscoISR4442 = _CiscoISR4442_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1706)
)
_CiscoISR4451_ObjectIdentity = ObjectIdentity
ciscoISR4451 = _CiscoISR4451_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1707)
)
_CiscoISR4452_ObjectIdentity = ObjectIdentity
ciscoISR4452 = _CiscoISR4452_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1708)
)
_CiscoASR9912_ObjectIdentity = ObjectIdentity
ciscoASR9912 = _CiscoASR9912_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1709)
)
_Cat3560x48U_ObjectIdentity = ObjectIdentity
cat3560x48U = _Cat3560x48U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1710)
)
_Cat3560x24U_ObjectIdentity = ObjectIdentity
cat3560x24U = _Cat3560x24U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1711)
)
_Cat3750x48U_ObjectIdentity = ObjectIdentity
cat3750x48U = _Cat3750x48U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1712)
)
_Cat3750x24U_ObjectIdentity = ObjectIdentity
cat3750x24U = _Cat3750x24U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1713)
)
_CiscoIE20008TCGN_ObjectIdentity = ObjectIdentity
ciscoIE20008TCGN = _CiscoIE20008TCGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1714)
)
_CiscoIE200016TCGN_ObjectIdentity = ObjectIdentity
ciscoIE200016TCGN = _CiscoIE200016TCGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1715)
)
_CiscoIem30004SM_ObjectIdentity = ObjectIdentity
ciscoIem30004SM = _CiscoIem30004SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1720)
)
_CiscoIem30008SM_ObjectIdentity = ObjectIdentity
ciscoIem30008SM = _CiscoIem30008SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1721)
)
_Cisco1783MX04S_ObjectIdentity = ObjectIdentity
cisco1783MX04S = _Cisco1783MX04S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1722)
)
_Cisco1783MX08S_ObjectIdentity = ObjectIdentity
cisco1783MX08S = _Cisco1783MX08S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1723)
)
_CiscoASR901TenGigDCE_ObjectIdentity = ObjectIdentity
ciscoASR901TenGigDCE = _CiscoASR901TenGigDCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1724)
)
_CiscoASR901TenGigACE_ObjectIdentity = ObjectIdentity
ciscoASR901TenGigACE = _CiscoASR901TenGigACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1725)
)
_CiscoASR901TenGigDC_ObjectIdentity = ObjectIdentity
ciscoASR901TenGigDC = _CiscoASR901TenGigDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1726)
)
_CiscoASR901TenGigAC_ObjectIdentity = ObjectIdentity
ciscoASR901TenGigAC = _CiscoASR901TenGigAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1727)
)
_CiscoIE200016TCGP_ObjectIdentity = ObjectIdentity
ciscoIE200016TCGP = _CiscoIE200016TCGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1729)
)
_CiscoIE200016TCGEP_ObjectIdentity = ObjectIdentity
ciscoIE200016TCGEP = _CiscoIE200016TCGEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1730)
)
_CiscoIE200016TCGNXP_ObjectIdentity = ObjectIdentity
ciscoIE200016TCGNXP = _CiscoIE200016TCGNXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1731)
)
_Cat4xxxVirtualSwitch_ObjectIdentity = ObjectIdentity
cat4xxxVirtualSwitch = _Cat4xxxVirtualSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1732)
)
_CiscoRAIE1783BMS20CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS20CGN = _CiscoRAIE1783BMS20CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1733)
)
_CiscoRAIE1783BMS12T4E2CGP_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS12T4E2CGP = _CiscoRAIE1783BMS12T4E2CGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1735)
)
_CiscoRAIE1783BMS12T4E2CGNK_ObjectIdentity = ObjectIdentity
ciscoRAIE1783BMS12T4E2CGNK = _CiscoRAIE1783BMS12T4E2CGNK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1736)
)
_CiscoMds9848512K9SM_ObjectIdentity = ObjectIdentity
ciscoMds9848512K9SM = _CiscoMds9848512K9SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1737)
)
_CiscoMds9710SM_ObjectIdentity = ObjectIdentity
ciscoMds9710SM = _CiscoMds9710SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1738)
)
_CiscoMds9710FM_ObjectIdentity = ObjectIdentity
ciscoMds9710FM = _CiscoMds9710FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1739)
)
_CiscoMds9710FCS_ObjectIdentity = ObjectIdentity
ciscoMds9710FCS = _CiscoMds9710FCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1740)
)
_CiscoMDS9250iIFSPS_ObjectIdentity = ObjectIdentity
ciscoMDS9250iIFSPS = _CiscoMDS9250iIFSPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1741)
)
_CiscoMDS9250iIFSDC_ObjectIdentity = ObjectIdentity
ciscoMDS9250iIFSDC = _CiscoMDS9250iIFSDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1742)
)
_CiscoMDS9250iIFS_ObjectIdentity = ObjectIdentity
ciscoMDS9250iIFS = _CiscoMDS9250iIFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1743)
)
_CiscoNexus1000VH_ObjectIdentity = ObjectIdentity
ciscoNexus1000VH = _CiscoNexus1000VH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1744)
)
_Cat38xxstack_ObjectIdentity = ObjectIdentity
cat38xxstack = _Cat38xxstack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1745)
)
_CiscoVG202XM_ObjectIdentity = ObjectIdentity
ciscoVG202XM = _CiscoVG202XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1746)
)
_CiscoVG204XM_ObjectIdentity = ObjectIdentity
ciscoVG204XM = _CiscoVG204XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1747)
)
_CiscoWsC2960P48PstL_ObjectIdentity = ObjectIdentity
ciscoWsC2960P48PstL = _CiscoWsC2960P48PstL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1748)
)
_CiscoWsC2960P24PcL_ObjectIdentity = ObjectIdentity
ciscoWsC2960P24PcL = _CiscoWsC2960P24PcL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1749)
)
_CiscoWsC2960P24LcL_ObjectIdentity = ObjectIdentity
ciscoWsC2960P24LcL = _CiscoWsC2960P24LcL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1750)
)
_CiscoWsC2960P48TcL_ObjectIdentity = ObjectIdentity
ciscoWsC2960P48TcL = _CiscoWsC2960P48TcL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1751)
)
_CiscoWsC2960P24TcL_ObjectIdentity = ObjectIdentity
ciscoWsC2960P24TcL = _CiscoWsC2960P24TcL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1752)
)
_CiscoWsC2960P48PstS_ObjectIdentity = ObjectIdentity
ciscoWsC2960P48PstS = _CiscoWsC2960P48PstS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1753)
)
_CiscoWsC2960P24PcS_ObjectIdentity = ObjectIdentity
ciscoWsC2960P24PcS = _CiscoWsC2960P24PcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1754)
)
_CiscoWsC2960P24LcS_ObjectIdentity = ObjectIdentity
ciscoWsC2960P24LcS = _CiscoWsC2960P24LcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1755)
)
_CiscoWsC2960P48TcS_ObjectIdentity = ObjectIdentity
ciscoWsC2960P48TcS = _CiscoWsC2960P48TcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1756)
)
_CiscoWsC2960P24TcS_ObjectIdentity = ObjectIdentity
ciscoWsC2960P24TcS = _CiscoWsC2960P24TcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1757)
)
_CiscoASR9904_ObjectIdentity = ObjectIdentity
ciscoASR9904 = _CiscoASR9904_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1762)
)
_CiscoME2600X_ObjectIdentity = ObjectIdentity
ciscoME2600X = _CiscoME2600X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1763)
)
_CiscoPanini_ObjectIdentity = ObjectIdentity
ciscoPanini = _CiscoPanini_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1764)
)
_CiscoC6807xl_ObjectIdentity = ObjectIdentity
ciscoC6807xl = _CiscoC6807xl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1765)
)
_Cat385024U_ObjectIdentity = ObjectIdentity
cat385024U = _Cat385024U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1767)
)
_Cat385048U_ObjectIdentity = ObjectIdentity
cat385048U = _Cat385048U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1768)
)
_CiscoVG310_ObjectIdentity = ObjectIdentity
ciscoVG310 = _CiscoVG310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1769)
)
_CiscoVG320_ObjectIdentity = ObjectIdentity
ciscoVG320 = _CiscoVG320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1770)
)
_CiscoC6880xle_ObjectIdentity = ObjectIdentity
ciscoC6880xle = _CiscoC6880xle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1784)
)
_Cat45Sup8e_ObjectIdentity = ObjectIdentity
cat45Sup8e = _Cat45Sup8e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1796)
)
_CiscoWsC2960XR48FpdI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR48FpdI = _CiscoWsC2960XR48FpdI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1797)
)
_CiscoWsC2960XR48LpdI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR48LpdI = _CiscoWsC2960XR48LpdI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1798)
)
_CiscoWsC2960XR48TdI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR48TdI = _CiscoWsC2960XR48TdI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1799)
)
_CiscoWsC2960XR24PdI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR24PdI = _CiscoWsC2960XR24PdI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1800)
)
_CiscoWsC2960XR24TdI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR24TdI = _CiscoWsC2960XR24TdI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1801)
)
_CiscoWsC2960XR48FpsI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR48FpsI = _CiscoWsC2960XR48FpsI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1802)
)
_CiscoWsC2960XR48LpsI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR48LpsI = _CiscoWsC2960XR48LpsI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1803)
)
_CiscoWsC2960XR48TsI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR48TsI = _CiscoWsC2960XR48TsI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1804)
)
_CiscoWsC2960XR24PsI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR24PsI = _CiscoWsC2960XR24PsI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1805)
)
_CiscoWsC2960XR24TsI_ObjectIdentity = ObjectIdentity
ciscoWsC2960XR24TsI = _CiscoWsC2960XR24TsI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1806)
)
_CiscoUCSC460M4Rackserver_ObjectIdentity = ObjectIdentity
ciscoUCSC460M4Rackserver = _CiscoUCSC460M4Rackserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1817)
)
_CiscoA901S4SGFD_ObjectIdentity = ObjectIdentity
ciscoA901S4SGFD = _CiscoA901S4SGFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1818)
)
_CiscoA901S3SGFD_ObjectIdentity = ObjectIdentity
ciscoA901S3SGFD = _CiscoA901S3SGFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1819)
)
_CiscoA901S2SGFD_ObjectIdentity = ObjectIdentity
ciscoA901S2SGFD = _CiscoA901S2SGFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1820)
)
_CiscoA901S3SGFAH_ObjectIdentity = ObjectIdentity
ciscoA901S3SGFAH = _CiscoA901S3SGFAH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1821)
)
_CiscoA901S2SGFAH_ObjectIdentity = ObjectIdentity
ciscoA901S2SGFAH = _CiscoA901S2SGFAH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1822)
)
_CiscoC365024TS_ObjectIdentity = ObjectIdentity
ciscoC365024TS = _CiscoC365024TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1823)
)
_CiscoC365048TS_ObjectIdentity = ObjectIdentity
ciscoC365048TS = _CiscoC365048TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1824)
)
_CiscoC365024PS_ObjectIdentity = ObjectIdentity
ciscoC365024PS = _CiscoC365024PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1825)
)
_CiscoC365048PS_ObjectIdentity = ObjectIdentity
ciscoC365048PS = _CiscoC365048PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1826)
)
_CiscoC365024TD_ObjectIdentity = ObjectIdentity
ciscoC365024TD = _CiscoC365024TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1827)
)
_CiscoC365048TD_ObjectIdentity = ObjectIdentity
ciscoC365048TD = _CiscoC365048TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1828)
)
_CiscoC365024PD_ObjectIdentity = ObjectIdentity
ciscoC365024PD = _CiscoC365024PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1829)
)
_CiscoC365048PD_ObjectIdentity = ObjectIdentity
ciscoC365048PD = _CiscoC365048PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1830)
)
_CiscoIE2000U4STSG_ObjectIdentity = ObjectIdentity
ciscoIE2000U4STSG = _CiscoIE2000U4STSG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1839)
)
_CiscoIE2000U16TCGP_ObjectIdentity = ObjectIdentity
ciscoIE2000U16TCGP = _CiscoIE2000U16TCGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1840)
)
_CiscoIE20008T67B_ObjectIdentity = ObjectIdentity
ciscoIE20008T67B = _CiscoIE20008T67B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1841)
)
_CiscoIE200016T67B_ObjectIdentity = ObjectIdentity
ciscoIE200016T67B = _CiscoIE200016T67B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1842)
)
_CiscoIE200024T67B_ObjectIdentity = ObjectIdentity
ciscoIE200024T67B = _CiscoIE200024T67B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1843)
)
_CiscoIE20008T67PGE_ObjectIdentity = ObjectIdentity
ciscoIE20008T67PGE = _CiscoIE20008T67PGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1844)
)
_CiscoIE200016T67PGE_ObjectIdentity = ObjectIdentity
ciscoIE200016T67PGE = _CiscoIE200016T67PGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1845)
)
_CiscoRAIE1783ZMS8TA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783ZMS8TA = _CiscoRAIE1783ZMS8TA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1846)
)
_CiscoRAIE1783ZMS16TA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783ZMS16TA = _CiscoRAIE1783ZMS16TA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1847)
)
_CiscoRAIE1783ZMS24TA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783ZMS24TA = _CiscoRAIE1783ZMS24TA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1848)
)
_CiscoRAIE1783ZMS4T4E2TGP_ObjectIdentity = ObjectIdentity
ciscoRAIE1783ZMS4T4E2TGP = _CiscoRAIE1783ZMS4T4E2TGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1849)
)
_CiscoRAIE1783ZMS8T8E2TGP_ObjectIdentity = ObjectIdentity
ciscoRAIE1783ZMS8T8E2TGP = _CiscoRAIE1783ZMS8T8E2TGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1850)
)
_CiscoNcs6008_ObjectIdentity = ObjectIdentity
ciscoNcs6008 = _CiscoNcs6008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1851)
)
_CiscoC881K9_ObjectIdentity = ObjectIdentity
ciscoC881K9 = _CiscoC881K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1852)
)
_CiscoC886VaK9_ObjectIdentity = ObjectIdentity
ciscoC886VaK9 = _CiscoC886VaK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1853)
)
_CiscoC886VaJK9_ObjectIdentity = ObjectIdentity
ciscoC886VaJK9 = _CiscoC886VaJK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1854)
)
_CiscoC887VaK9_ObjectIdentity = ObjectIdentity
ciscoC887VaK9 = _CiscoC887VaK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1855)
)
_CiscoC887VaMK9_ObjectIdentity = ObjectIdentity
ciscoC887VaMK9 = _CiscoC887VaMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1856)
)
_CiscoC888K9_ObjectIdentity = ObjectIdentity
ciscoC888K9 = _CiscoC888K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1857)
)
_CiscoC891FK9_ObjectIdentity = ObjectIdentity
ciscoC891FK9 = _CiscoC891FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1858)
)
_CiscoC891FwAK9_ObjectIdentity = ObjectIdentity
ciscoC891FwAK9 = _CiscoC891FwAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1859)
)
_CiscoC891FwEK9_ObjectIdentity = ObjectIdentity
ciscoC891FwEK9 = _CiscoC891FwEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1860)
)
_CiscoASR1001X_ObjectIdentity = ObjectIdentity
ciscoASR1001X = _CiscoASR1001X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1861)
)
_Cisco1783WAP5100xK9_ObjectIdentity = ObjectIdentity
cisco1783WAP5100xK9 = _Cisco1783WAP5100xK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1862)
)
_CiscoCDScde2502s5_ObjectIdentity = ObjectIdentity
ciscoCDScde2502s5 = _CiscoCDScde2502s5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1863)
)
_CiscoUcsE140S_ObjectIdentity = ObjectIdentity
ciscoUcsE140S = _CiscoUcsE140S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1864)
)
_CiscoNXNAM1_ObjectIdentity = ObjectIdentity
ciscoNXNAM1 = _CiscoNXNAM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1865)
)
_CiscoC6800ia48fpdL_ObjectIdentity = ObjectIdentity
ciscoC6800ia48fpdL = _CiscoC6800ia48fpdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1866)
)
_CiscoC6800ia48tdL_ObjectIdentity = ObjectIdentity
ciscoC6800ia48tdL = _CiscoC6800ia48tdL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1867)
)
_CiscoIE2000U4TG_ObjectIdentity = ObjectIdentity
ciscoIE2000U4TG = _CiscoIE2000U4TG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1868)
)
_CiscoIE2000U4TSG_ObjectIdentity = ObjectIdentity
ciscoIE2000U4TSG = _CiscoIE2000U4TSG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1869)
)
_CiscoIE2000U8TCG_ObjectIdentity = ObjectIdentity
ciscoIE2000U8TCG = _CiscoIE2000U8TCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1870)
)
_CiscoIE2000U16TCG_ObjectIdentity = ObjectIdentity
ciscoIE2000U16TCG = _CiscoIE2000U16TCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1871)
)
_CiscoIE2000U16TCGX_ObjectIdentity = ObjectIdentity
ciscoIE2000U16TCGX = _CiscoIE2000U16TCGX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1872)
)
_CiscoAIRAP3702_ObjectIdentity = ObjectIdentity
ciscoAIRAP3702 = _CiscoAIRAP3702_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1873)
)
_CiscoAIRAP702_ObjectIdentity = ObjectIdentity
ciscoAIRAP702 = _CiscoAIRAP702_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1874)
)
_CiscoAIRAP1532_ObjectIdentity = ObjectIdentity
ciscoAIRAP1532 = _CiscoAIRAP1532_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1875)
)
_CiscoEsxNAM_ObjectIdentity = ObjectIdentity
ciscoEsxNAM = _CiscoEsxNAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1876)
)
_CiscoKvmNAM_ObjectIdentity = ObjectIdentity
ciscoKvmNAM = _CiscoKvmNAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1877)
)
_CiscoHyperNAM_ObjectIdentity = ObjectIdentity
ciscoHyperNAM = _CiscoHyperNAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1878)
)
_CiscoC385024S_ObjectIdentity = ObjectIdentity
ciscoC385024S = _CiscoC385024S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1879)
)
_CiscoC385012S_ObjectIdentity = ObjectIdentity
ciscoC385012S = _CiscoC385012S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1880)
)
_CiscoC365048PQ_ObjectIdentity = ObjectIdentity
ciscoC365048PQ = _CiscoC365048PQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1881)
)
_CiscoC365048TQ_ObjectIdentity = ObjectIdentity
ciscoC365048TQ = _CiscoC365048TQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1882)
)
_CiscoASR902_ObjectIdentity = ObjectIdentity
ciscoASR902 = _CiscoASR902_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1897)
)
_CiscoME1200_ObjectIdentity = ObjectIdentity
ciscoME1200 = _CiscoME1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1899)
)
_CiscoVASA_ObjectIdentity = ObjectIdentity
ciscoVASA = _CiscoVASA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1902)
)
_CiscoVASASy_ObjectIdentity = ObjectIdentity
ciscoVASASy = _CiscoVASASy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1903)
)
_CiscoVASASc_ObjectIdentity = ObjectIdentity
ciscoVASASc = _CiscoVASASc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1904)
)
_CiscoN9Kc9508_ObjectIdentity = ObjectIdentity
ciscoN9Kc9508 = _CiscoN9Kc9508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1915)
)
_CiscoWapAP702_ObjectIdentity = ObjectIdentity
ciscoWapAP702 = _CiscoWapAP702_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1916)
)
_CiscoWapAP2602_ObjectIdentity = ObjectIdentity
ciscoWapAP2602 = _CiscoWapAP2602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1917)
)
_CiscoWapAP1602_ObjectIdentity = ObjectIdentity
ciscoWapAP1602 = _CiscoWapAP1602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1918)
)
_CiscoN9KC93128TX_ObjectIdentity = ObjectIdentity
ciscoN9KC93128TX = _CiscoN9KC93128TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1923)
)
_CiscoN9KC9396TX_ObjectIdentity = ObjectIdentity
ciscoN9KC9396TX = _CiscoN9KC9396TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1924)
)
_CiscoN9KC9396PX_ObjectIdentity = ObjectIdentity
ciscoN9KC9396PX = _CiscoN9KC9396PX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1925)
)
_CiscoWlcCt5508K9_ObjectIdentity = ObjectIdentity
ciscoWlcCt5508K9 = _CiscoWlcCt5508K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1926)
)
_CiscoWlcCt2504K9_ObjectIdentity = ObjectIdentity
ciscoWlcCt2504K9 = _CiscoWlcCt2504K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1927)
)
_CiscoUcsEN120S_ObjectIdentity = ObjectIdentity
ciscoUcsEN120S = _CiscoUcsEN120S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1931)
)
_CiscoUcsEN140N_ObjectIdentity = ObjectIdentity
ciscoUcsEN140N = _CiscoUcsEN140N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1932)
)
_CiscoUcsEN120E_ObjectIdentity = ObjectIdentity
ciscoUcsEN120E = _CiscoUcsEN120E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1933)
)
_CiscoC68xxVirtualSwitch_ObjectIdentity = ObjectIdentity
ciscoC68xxVirtualSwitch = _CiscoC68xxVirtualSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1934)
)
_CiscoISR4431_ObjectIdentity = ObjectIdentity
ciscoISR4431 = _CiscoISR4431_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1935)
)
_CiscoC6880x_ObjectIdentity = ObjectIdentity
ciscoC6880x = _CiscoC6880x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1936)
)
_CiscoCPT50_ObjectIdentity = ObjectIdentity
ciscoCPT50 = _CiscoCPT50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1937)
)
_CiscoAIRAP2702_ObjectIdentity = ObjectIdentity
ciscoAIRAP2702 = _CiscoAIRAP2702_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1938)
)
_CiscoNCS4016_ObjectIdentity = ObjectIdentity
ciscoNCS4016 = _CiscoNCS4016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1939)
)
_CiscoCSE340WG32K9_ObjectIdentity = ObjectIdentity
ciscoCSE340WG32K9 = _CiscoCSE340WG32K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1940)
)
_CiscoCSE340WG32AK9_ObjectIdentity = ObjectIdentity
ciscoCSE340WG32AK9 = _CiscoCSE340WG32AK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1941)
)
_CiscoCSE340WG32CK9_ObjectIdentity = ObjectIdentity
ciscoCSE340WG32CK9 = _CiscoCSE340WG32CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1942)
)
_CiscoCSE340WG32EK9_ObjectIdentity = ObjectIdentity
ciscoCSE340WG32EK9 = _CiscoCSE340WG32EK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1943)
)
_CiscoCSE340WG32NK9_ObjectIdentity = ObjectIdentity
ciscoCSE340WG32NK9 = _CiscoCSE340WG32NK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1944)
)
_CiscoCSE340WM32K9_ObjectIdentity = ObjectIdentity
ciscoCSE340WM32K9 = _CiscoCSE340WM32K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1945)
)
_CiscoCSE340WM32AK9_ObjectIdentity = ObjectIdentity
ciscoCSE340WM32AK9 = _CiscoCSE340WM32AK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1946)
)
_CiscoCSE340WM32CK9_ObjectIdentity = ObjectIdentity
ciscoCSE340WM32CK9 = _CiscoCSE340WM32CK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1947)
)
_CiscoCSE340WM32EK9_ObjectIdentity = ObjectIdentity
ciscoCSE340WM32EK9 = _CiscoCSE340WM32EK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1948)
)
_CiscoCSE340WM32NK9_ObjectIdentity = ObjectIdentity
ciscoCSE340WM32NK9 = _CiscoCSE340WM32NK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1949)
)
_CiscoitpRT1081K9_ObjectIdentity = ObjectIdentity
ciscoitpRT1081K9 = _CiscoitpRT1081K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1952)
)
_CiscoitpRT1091FK9_ObjectIdentity = ObjectIdentity
ciscoitpRT1091FK9 = _CiscoitpRT1091FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1953)
)
_CiscoitpPwr30WAC_ObjectIdentity = ObjectIdentity
ciscoitpPwr30WAC = _CiscoitpPwr30WAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1954)
)
_CiscoitpPwr60WAC_ObjectIdentity = ObjectIdentity
ciscoitpPwr60WAC = _CiscoitpPwr60WAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1955)
)
_CiscoitpPwr60WACV2_ObjectIdentity = ObjectIdentity
ciscoitpPwr60WACV2 = _CiscoitpPwr60WACV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1956)
)
_CiscoitpPwr125WAC_ObjectIdentity = ObjectIdentity
ciscoitpPwr125WAC = _CiscoitpPwr125WAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1957)
)
_CiscoitpRT2241K9_ObjectIdentity = ObjectIdentity
ciscoitpRT2241K9 = _CiscoitpRT2241K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1958)
)
_CiscoitpRT2221K9_ObjectIdentity = ObjectIdentity
ciscoitpRT2221K9 = _CiscoitpRT2221K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1959)
)
_CiscoitpRT2241WCK9_ObjectIdentity = ObjectIdentity
ciscoitpRT2241WCK9 = _CiscoitpRT2241WCK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1960)
)
_CiscoitpAxpIsmSre300_ObjectIdentity = ObjectIdentity
ciscoitpAxpIsmSre300 = _CiscoitpAxpIsmSre300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1961)
)
_CiscoitpPwr2241AC_ObjectIdentity = ObjectIdentity
ciscoitpPwr2241AC = _CiscoitpPwr2241AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1962)
)
_CiscoitpRT3211K9_ObjectIdentity = ObjectIdentity
ciscoitpRT3211K9 = _CiscoitpRT3211K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1963)
)
_CiscoitpRT3221K9_ObjectIdentity = ObjectIdentity
ciscoitpRT3221K9 = _CiscoitpRT3221K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1964)
)
_CiscoitpRT3201K9_ObjectIdentity = ObjectIdentity
ciscoitpRT3201K9 = _CiscoitpRT3201K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1965)
)
_CiscoitpPwrRT3201AC_ObjectIdentity = ObjectIdentity
ciscoitpPwrRT3201AC = _CiscoitpPwrRT3201AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1966)
)
_CiscoitpPwrRT3211AC_ObjectIdentity = ObjectIdentity
ciscoitpPwrRT3211AC = _CiscoitpPwrRT3211AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1967)
)
_CiscoitpPwrRT3211DC_ObjectIdentity = ObjectIdentity
ciscoitpPwrRT3211DC = _CiscoitpPwrRT3211DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1968)
)
_CiscoitpPwrRT32AC_ObjectIdentity = ObjectIdentity
ciscoitpPwrRT32AC = _CiscoitpPwrRT32AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1969)
)
_CiscoitpRpsAdptrRT3211_ObjectIdentity = ObjectIdentity
ciscoitpRpsAdptrRT3211 = _CiscoitpRpsAdptrRT3211_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1970)
)
_CiscoitpRpsAdptrRT32_ObjectIdentity = ObjectIdentity
ciscoitpRpsAdptrRT32 = _CiscoitpRpsAdptrRT32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1971)
)
_CiscoitpAxpSmSre710_ObjectIdentity = ObjectIdentity
ciscoitpAxpSmSre710 = _CiscoitpAxpSmSre710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1972)
)
_CiscoitpAxpSmSre910_ObjectIdentity = ObjectIdentity
ciscoitpAxpSmSre910 = _CiscoitpAxpSmSre910_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1973)
)
_CiscoN9Kc9516_ObjectIdentity = ObjectIdentity
ciscoN9Kc9516 = _CiscoN9Kc9516_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1996)
)
_CiscoN9Kc9504_ObjectIdentity = ObjectIdentity
ciscoN9Kc9504 = _CiscoN9Kc9504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1997)
)
_CiscoDoorCGR1240_ObjectIdentity = ObjectIdentity
ciscoDoorCGR1240 = _CiscoDoorCGR1240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1998)
)
_CiscoISR4351_ObjectIdentity = ObjectIdentity
ciscoISR4351 = _CiscoISR4351_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1999)
)
_CiscoWRP500_ObjectIdentity = ObjectIdentity
ciscoWRP500 = _CiscoWRP500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2000)
)
_Cisco897VABK9_ObjectIdentity = ObjectIdentity
cisco897VABK9 = _Cisco897VABK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2008)
)
_Cisco819HWDCK9_ObjectIdentity = ObjectIdentity
cisco819HWDCK9 = _Cisco819HWDCK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2023)
)
_CatAIRCT57006_ObjectIdentity = ObjectIdentity
catAIRCT57006 = _CatAIRCT57006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2026)
)
_Cisco897VAMGLTEGAK9_ObjectIdentity = ObjectIdentity
cisco897VAMGLTEGAK9 = _Cisco897VAMGLTEGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2045)
)
_Cisco899GLTESTK9_ObjectIdentity = ObjectIdentity
cisco899GLTESTK9 = _Cisco899GLTESTK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2046)
)
_Cisco899GLTENAK9_ObjectIdentity = ObjectIdentity
cisco899GLTENAK9 = _Cisco899GLTENAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2048)
)
_Cisco899GLTEVZK9_ObjectIdentity = ObjectIdentity
cisco899GLTEVZK9 = _Cisco899GLTEVZK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2049)
)
_Cisco819G4GNAK9_ObjectIdentity = ObjectIdentity
cisco819G4GNAK9 = _Cisco819G4GNAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2050)
)
_Cisco819G4GSTK9_ObjectIdentity = ObjectIdentity
cisco819G4GSTK9 = _Cisco819G4GSTK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2051)
)
_Cisco898EAGLTEGAK9_ObjectIdentity = ObjectIdentity
cisco898EAGLTEGAK9 = _Cisco898EAGLTEGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2052)
)
_Cisco897VAGLTEGAK9_ObjectIdentity = ObjectIdentity
cisco897VAGLTEGAK9 = _Cisco897VAGLTEGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2053)
)
_Cisco896VAGLTEGAK9_ObjectIdentity = ObjectIdentity
cisco896VAGLTEGAK9 = _Cisco896VAGLTEGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2055)
)
_Cisco899GLTEGAK9_ObjectIdentity = ObjectIdentity
cisco899GLTEGAK9 = _Cisco899GLTEGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2056)
)
_Cisco881G4GGAK9_ObjectIdentity = ObjectIdentity
cisco881G4GGAK9 = _Cisco881G4GGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2057)
)
_Cisco887VAG4GGAK9_ObjectIdentity = ObjectIdentity
cisco887VAG4GGAK9 = _Cisco887VAG4GGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2058)
)
_Cisco819G4GGAK9_ObjectIdentity = ObjectIdentity
cisco819G4GGAK9 = _Cisco819G4GGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2059)
)
_Cisco819G4GVZK9_ObjectIdentity = ObjectIdentity
cisco819G4GVZK9 = _Cisco819G4GVZK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2060)
)
_CiscoIOG910WK9_ObjectIdentity = ObjectIdentity
ciscoIOG910WK9 = _CiscoIOG910WK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2063)
)
_CiscoIOG910GK9_ObjectIdentity = ObjectIdentity
ciscoIOG910GK9 = _CiscoIOG910GK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2064)
)
_CiscoIOG910K9_ObjectIdentity = ObjectIdentity
ciscoIOG910K9 = _CiscoIOG910K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2065)
)
_Cat36xxstack_ObjectIdentity = ObjectIdentity
cat36xxstack = _Cat36xxstack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2066)
)
_Cat57xxstack_ObjectIdentity = ObjectIdentity
cat57xxstack = _Cat57xxstack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2067)
)
_CiscoISR4331_ObjectIdentity = ObjectIdentity
ciscoISR4331 = _CiscoISR4331_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2068)
)
_CiscoIE40004TC4GE_ObjectIdentity = ObjectIdentity
ciscoIE40004TC4GE = _CiscoIE40004TC4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2069)
)
_CiscoIE40008T4GE_ObjectIdentity = ObjectIdentity
ciscoIE40008T4GE = _CiscoIE40008T4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2070)
)
_CiscoIE40008S4GE_ObjectIdentity = ObjectIdentity
ciscoIE40008S4GE = _CiscoIE40008S4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2071)
)
_CiscoIE40004T4P4GE_ObjectIdentity = ObjectIdentity
ciscoIE40004T4P4GE = _CiscoIE40004T4P4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2072)
)
_CiscoIE400016T4GE_ObjectIdentity = ObjectIdentity
ciscoIE400016T4GE = _CiscoIE400016T4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2073)
)
_CiscoIE40004S8P4GE_ObjectIdentity = ObjectIdentity
ciscoIE40004S8P4GE = _CiscoIE40004S8P4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2074)
)
_CiscoIE40008GT4GE_ObjectIdentity = ObjectIdentity
ciscoIE40008GT4GE = _CiscoIE40008GT4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2075)
)
_CiscoIE40008GS4GE_ObjectIdentity = ObjectIdentity
ciscoIE40008GS4GE = _CiscoIE40008GS4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2076)
)
_CiscoIE40004GC4GP4GE_ObjectIdentity = ObjectIdentity
ciscoIE40004GC4GP4GE = _CiscoIE40004GC4GP4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2077)
)
_CiscoIE400016GT4GE_ObjectIdentity = ObjectIdentity
ciscoIE400016GT4GE = _CiscoIE400016GT4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2078)
)
_CiscoIE40008GT8GP4GE_ObjectIdentity = ObjectIdentity
ciscoIE40008GT8GP4GE = _CiscoIE40008GT8GP4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2079)
)
_CiscoIE40004GS8GP4GE_ObjectIdentity = ObjectIdentity
ciscoIE40004GS8GP4GE = _CiscoIE40004GS8GP4GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2080)
)
_CiscoRAIE1783HMS4C4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS4C4CGN = _CiscoRAIE1783HMS4C4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2081)
)
_CiscoRAIE1783HMS8T4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS8T4CGN = _CiscoRAIE1783HMS8T4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2082)
)
_CiscoRAIE1783HMS8S4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS8S4CGN = _CiscoRAIE1783HMS8S4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2083)
)
_CiscoRAIE1783HMS4T4E4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS4T4E4CGN = _CiscoRAIE1783HMS4T4E4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2084)
)
_CiscoRAIE1783HMS16T4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS16T4CGN = _CiscoRAIE1783HMS16T4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2085)
)
_CiscoRAIE1783HMS4S8E4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS4S8E4CGN = _CiscoRAIE1783HMS4S8E4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2086)
)
_CiscoRAIE1783HMS8TG4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS8TG4CGN = _CiscoRAIE1783HMS8TG4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2087)
)
_CiscoRAIE1783HMS8SG4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS8SG4CGN = _CiscoRAIE1783HMS8SG4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2088)
)
_CiscoRAIE1783HMS4EG8CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS4EG8CGN = _CiscoRAIE1783HMS4EG8CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2089)
)
_CiscoRAIE1783HMS16TG4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS16TG4CGN = _CiscoRAIE1783HMS16TG4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2090)
)
_CiscoRAIE1783HMS8TG8EG4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS8TG8EG4CGN = _CiscoRAIE1783HMS8TG8EG4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2091)
)
_CiscoRAIE1783HMS4SG8EG4CGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS4SG8EG4CGN = _CiscoRAIE1783HMS4SG8EG4CGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2092)
)
_CiscoISR4321_ObjectIdentity = ObjectIdentity
ciscoISR4321 = _CiscoISR4321_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2093)
)
_CiscoCSE340G32K9_ObjectIdentity = ObjectIdentity
ciscoCSE340G32K9 = _CiscoCSE340G32K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2094)
)
_CiscoCSE340M32K9_ObjectIdentity = ObjectIdentity
ciscoCSE340M32K9 = _CiscoCSE340M32K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2095)
)
_CiscoSCE10000_ObjectIdentity = ObjectIdentity
ciscoSCE10000 = _CiscoSCE10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2096)
)
_CiscoVirtualSCE_ObjectIdentity = ObjectIdentity
ciscoVirtualSCE = _CiscoVirtualSCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2097)
)
_CiscoASR901AC10GS_ObjectIdentity = ObjectIdentity
ciscoASR901AC10GS = _CiscoASR901AC10GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2098)
)
_CiscoASR901DC10GS_ObjectIdentity = ObjectIdentity
ciscoASR901DC10GS = _CiscoASR901DC10GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2099)
)
_CiscoASR92024SZIM_ObjectIdentity = ObjectIdentity
ciscoASR92024SZIM = _CiscoASR92024SZIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2100)
)
_CiscoASR92024TZM_ObjectIdentity = ObjectIdentity
ciscoASR92024TZM = _CiscoASR92024TZM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2101)
)
_CiscoASR92024SZM_ObjectIdentity = ObjectIdentity
ciscoASR92024SZM = _CiscoASR92024SZM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2102)
)
_CiscoIR809GLTESTK9_ObjectIdentity = ObjectIdentity
ciscoIR809GLTESTK9 = _CiscoIR809GLTESTK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2103)
)
_CiscoIR809GLTEVZK9_ObjectIdentity = ObjectIdentity
ciscoIR809GLTEVZK9 = _CiscoIR809GLTEVZK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2104)
)
_CiscoIR809GLTEGAK9_ObjectIdentity = ObjectIdentity
ciscoIR809GLTEGAK9 = _CiscoIR809GLTEGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2105)
)
_CiscoIR809GLTENAK9_ObjectIdentity = ObjectIdentity
ciscoIR809GLTENAK9 = _CiscoIR809GLTENAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2106)
)
_CiscoIR829GWLTESTAK9_ObjectIdentity = ObjectIdentity
ciscoIR829GWLTESTAK9 = _CiscoIR829GWLTESTAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2107)
)
_CiscoIR829GWLTEVZAK9_ObjectIdentity = ObjectIdentity
ciscoIR829GWLTEVZAK9 = _CiscoIR829GWLTEVZAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2108)
)
_CiscoIR829GWLTEGAZK9_ObjectIdentity = ObjectIdentity
ciscoIR829GWLTEGAZK9 = _CiscoIR829GWLTEGAZK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2109)
)
_CiscoIR829GWLTEGAEK9_ObjectIdentity = ObjectIdentity
ciscoIR829GWLTEGAEK9 = _CiscoIR829GWLTEGAEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2110)
)
_CiscoIR829GWLTENAAK9_ObjectIdentity = ObjectIdentity
ciscoIR829GWLTENAAK9 = _CiscoIR829GWLTENAAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2111)
)
_CiscoWallander1x1GESKU_ObjectIdentity = ObjectIdentity
ciscoWallander1x1GESKU = _CiscoWallander1x1GESKU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2112)
)
_CiscoWallander2x1GESKU_ObjectIdentity = ObjectIdentity
ciscoWallander2x1GESKU = _CiscoWallander2x1GESKU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2113)
)
_CiscoASA5506_ObjectIdentity = ObjectIdentity
ciscoASA5506 = _CiscoASA5506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2114)
)
_CiscoASA5506sc_ObjectIdentity = ObjectIdentity
ciscoASA5506sc = _CiscoASA5506sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2115)
)
_CiscoASA5506sy_ObjectIdentity = ObjectIdentity
ciscoASA5506sy = _CiscoASA5506sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2116)
)
_CiscoASA5506W_ObjectIdentity = ObjectIdentity
ciscoASA5506W = _CiscoASA5506W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2117)
)
_CiscoASA5506Wsc_ObjectIdentity = ObjectIdentity
ciscoASA5506Wsc = _CiscoASA5506Wsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2118)
)
_CiscoASA5506Wsy_ObjectIdentity = ObjectIdentity
ciscoASA5506Wsy = _CiscoASA5506Wsy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2119)
)
_CiscoASA5508_ObjectIdentity = ObjectIdentity
ciscoASA5508 = _CiscoASA5508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2120)
)
_CiscoASA5508sc_ObjectIdentity = ObjectIdentity
ciscoASA5508sc = _CiscoASA5508sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2121)
)
_CiscoASA5508sy_ObjectIdentity = ObjectIdentity
ciscoASA5508sy = _CiscoASA5508sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2122)
)
_CiscoASA5506K7_ObjectIdentity = ObjectIdentity
ciscoASA5506K7 = _CiscoASA5506K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2123)
)
_CiscoASA5506K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5506K7sc = _CiscoASA5506K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2124)
)
_CiscoASA5506K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5506K7sy = _CiscoASA5506K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2125)
)
_CiscoASA5508K7_ObjectIdentity = ObjectIdentity
ciscoASA5508K7 = _CiscoASA5508K7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2126)
)
_CiscoASA5508K7sc_ObjectIdentity = ObjectIdentity
ciscoASA5508K7sc = _CiscoASA5508K7sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2127)
)
_CiscoASA5508K7sy_ObjectIdentity = ObjectIdentity
ciscoASA5508K7sy = _CiscoASA5508K7sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2128)
)
_CiscoAIRAP1702_ObjectIdentity = ObjectIdentity
ciscoAIRAP1702 = _CiscoAIRAP1702_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2129)
)
_CatwsC3560CX8ptS_ObjectIdentity = ObjectIdentity
catwsC3560CX8ptS = _CatwsC3560CX8ptS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2130)
)
_CatwsC3560CX8XpdS_ObjectIdentity = ObjectIdentity
catwsC3560CX8XpdS = _CatwsC3560CX8XpdS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2131)
)
_CatwsC3560CX12pdS_ObjectIdentity = ObjectIdentity
catwsC3560CX12pdS = _CatwsC3560CX12pdS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2132)
)
_CatwsC3560CX12tcS_ObjectIdentity = ObjectIdentity
catwsC3560CX12tcS = _CatwsC3560CX12tcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2133)
)
_CatwsC3560CX12pcS_ObjectIdentity = ObjectIdentity
catwsC3560CX12pcS = _CatwsC3560CX12pcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2134)
)
_CatwsC3560CX8tcS_ObjectIdentity = ObjectIdentity
catwsC3560CX8tcS = _CatwsC3560CX8tcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2135)
)
_CatwsC3560CX8pcS_ObjectIdentity = ObjectIdentity
catwsC3560CX8pcS = _CatwsC3560CX8pcS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2136)
)
_CatwsC2960CX8tcL_ObjectIdentity = ObjectIdentity
catwsC2960CX8tcL = _CatwsC2960CX8tcL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2137)
)
_Cisco2911TK9_ObjectIdentity = ObjectIdentity
cisco2911TK9 = _Cisco2911TK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2138)
)
_CiscoSNS3495K9_ObjectIdentity = ObjectIdentity
ciscoSNS3495K9 = _CiscoSNS3495K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2139)
)
_CiscoSNS3415K9_ObjectIdentity = ObjectIdentity
ciscoSNS3415K9 = _CiscoSNS3415K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2140)
)
_CiscocBR8_ObjectIdentity = ObjectIdentity
ciscocBR8 = _CiscocBR8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2141)
)
_CiscoPwrC2911DCPOE_ObjectIdentity = ObjectIdentity
ciscoPwrC2911DCPOE = _CiscoPwrC2911DCPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2142)
)
_CiscoASR1006X_ObjectIdentity = ObjectIdentity
ciscoASR1006X = _CiscoASR1006X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2143)
)
_CiscoASR1009X_ObjectIdentity = ObjectIdentity
ciscoASR1009X = _CiscoASR1009X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2144)
)
_CiscoAIRAP702w_ObjectIdentity = ObjectIdentity
ciscoAIRAP702w = _CiscoAIRAP702w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2146)
)
_CiscoAIRAP1572_ObjectIdentity = ObjectIdentity
ciscoAIRAP1572 = _CiscoAIRAP1572_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2147)
)
_Cisco891x24XK9_ObjectIdentity = ObjectIdentity
cisco891x24XK9 = _Cisco891x24XK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2148)
)
_CiscoUCSEN120E54_ObjectIdentity = ObjectIdentity
ciscoUCSEN120E54 = _CiscoUCSEN120E54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2149)
)
_CiscoUCSEN120E108_ObjectIdentity = ObjectIdentity
ciscoUCSEN120E108 = _CiscoUCSEN120E108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2151)
)
_CiscoUCSEN120E208_ObjectIdentity = ObjectIdentity
ciscoUCSEN120E208 = _CiscoUCSEN120E208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2154)
)
_CiscoASR9204SZD_ObjectIdentity = ObjectIdentity
ciscoASR9204SZD = _CiscoASR9204SZD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2155)
)
_CiscoASR9208SZ0A_ObjectIdentity = ObjectIdentity
ciscoASR9208SZ0A = _CiscoASR9208SZ0A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2156)
)
_CiscoASR92012CZA_ObjectIdentity = ObjectIdentity
ciscoASR92012CZA = _CiscoASR92012CZA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2157)
)
_CiscoASR92012CZD_ObjectIdentity = ObjectIdentity
ciscoASR92012CZD = _CiscoASR92012CZD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2158)
)
_CiscoASR9204SZA_ObjectIdentity = ObjectIdentity
ciscoASR9204SZA = _CiscoASR9204SZA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2159)
)
_CiscoASR92010SZ0D_ObjectIdentity = ObjectIdentity
ciscoASR92010SZ0D = _CiscoASR92010SZ0D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2160)
)
_CiscoTSCodecG3_ObjectIdentity = ObjectIdentity
ciscoTSCodecG3 = _CiscoTSCodecG3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2161)
)
_CiscoC385012XS_ObjectIdentity = ObjectIdentity
ciscoC385012XS = _CiscoC385012XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2162)
)
_CiscoC385024XS_ObjectIdentity = ObjectIdentity
ciscoC385024XS = _CiscoC385024XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2163)
)
_CiscoC385048XS_ObjectIdentity = ObjectIdentity
ciscoC385048XS = _CiscoC385048XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2164)
)
_CiscoC385012X48U_ObjectIdentity = ObjectIdentity
ciscoC385012X48U = _CiscoC385012X48U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2165)
)
_CiscoC385024XU_ObjectIdentity = ObjectIdentity
ciscoC385024XU = _CiscoC385024XU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2166)
)
_CiscoRAIE1783ZMS4T4E2TGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783ZMS4T4E2TGN = _CiscoRAIE1783ZMS4T4E2TGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2168)
)
_CiscoRAIE1783ZMS8T8E2TGN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783ZMS8T8E2TGN = _CiscoRAIE1783ZMS8T8E2TGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2169)
)
_Cisco5520WLC_ObjectIdentity = ObjectIdentity
cisco5520WLC = _Cisco5520WLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2170)
)
_Cisco8540Wlc_ObjectIdentity = ObjectIdentity
cisco8540Wlc = _Cisco8540Wlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2171)
)
_CiscoRAIE1783HMS8TG4CGR_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS8TG4CGR = _CiscoRAIE1783HMS8TG4CGR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2172)
)
_CiscoRAIE1783HMS8SG4CGR_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS8SG4CGR = _CiscoRAIE1783HMS8SG4CGR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2173)
)
_CiscoRAIE1783HMS4EG8CGR_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS4EG8CGR = _CiscoRAIE1783HMS4EG8CGR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2174)
)
_CiscoRAIE1783HMS16TG4CGR_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS16TG4CGR = _CiscoRAIE1783HMS16TG4CGR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2175)
)
_CiscoRAIE1783HMS8TG8EG4CGR_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS8TG8EG4CGR = _CiscoRAIE1783HMS8TG8EG4CGR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2176)
)
_CiscoRAIE1783HMS4SG8EG4CGR_ObjectIdentity = ObjectIdentity
ciscoRAIE1783HMS4SG8EG4CGR = _CiscoRAIE1783HMS4SG8EG4CGR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2177)
)
_CiscoUCSC220M4_ObjectIdentity = ObjectIdentity
ciscoUCSC220M4 = _CiscoUCSC220M4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2178)
)
_CiscoUCSC240M4_ObjectIdentity = ObjectIdentity
ciscoUCSC240M4 = _CiscoUCSC240M4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2179)
)
_CiscoUCSC3160_ObjectIdentity = ObjectIdentity
ciscoUCSC3160 = _CiscoUCSC3160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2180)
)
_Cisco1941WTK9_ObjectIdentity = ObjectIdentity
cisco1941WTK9 = _Cisco1941WTK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2181)
)
_CiscoUCSC3260_ObjectIdentity = ObjectIdentity
ciscoUCSC3260 = _CiscoUCSC3260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2182)
)
_CiscoUCSE160DM2K9_ObjectIdentity = ObjectIdentity
ciscoUCSE160DM2K9 = _CiscoUCSE160DM2K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2183)
)
_CiscoUCSE180DM2K9_ObjectIdentity = ObjectIdentity
ciscoUCSE180DM2K9 = _CiscoUCSE180DM2K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2184)
)
_CiscoCDScde2802s5_ObjectIdentity = ObjectIdentity
ciscoCDScde2802s5 = _CiscoCDScde2802s5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2185)
)
_CiscoCDScde2802s10_ObjectIdentity = ObjectIdentity
ciscoCDScde2802s10 = _CiscoCDScde2802s10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2186)
)
_CiscoCDScde2802s21_ObjectIdentity = ObjectIdentity
ciscoCDScde2802s21 = _CiscoCDScde2802s21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2187)
)
_CiscoCDScde2802h0_ObjectIdentity = ObjectIdentity
ciscoCDScde2802h0 = _CiscoCDScde2802h0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2188)
)
_CiscoCDScde2802h13_ObjectIdentity = ObjectIdentity
ciscoCDScde2802h13 = _CiscoCDScde2802h13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2189)
)
_CiscoCDScde2802h26_ObjectIdentity = ObjectIdentity
ciscoCDScde2802h26 = _CiscoCDScde2802h26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2190)
)
_CiscoWSC2960CX8PCL_ObjectIdentity = ObjectIdentity
ciscoWSC2960CX8PCL = _CiscoWSC2960CX8PCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2191)
)
_Cisco1941WIK9_ObjectIdentity = ObjectIdentity
cisco1941WIK9 = _Cisco1941WIK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2192)
)
_CiscoFp7030K9_ObjectIdentity = ObjectIdentity
ciscoFp7030K9 = _CiscoFp7030K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2193)
)
_CiscoFp7050K9_ObjectIdentity = ObjectIdentity
ciscoFp7050K9 = _CiscoFp7050K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2194)
)
_CiscoFp7110K9_ObjectIdentity = ObjectIdentity
ciscoFp7110K9 = _CiscoFp7110K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2195)
)
_CiscoFp7110FiK9_ObjectIdentity = ObjectIdentity
ciscoFp7110FiK9 = _CiscoFp7110FiK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2196)
)
_CiscoFp7115K9_ObjectIdentity = ObjectIdentity
ciscoFp7115K9 = _CiscoFp7115K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2197)
)
_CiscoFp7120K9_ObjectIdentity = ObjectIdentity
ciscoFp7120K9 = _CiscoFp7120K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2198)
)
_CiscoFp7120FiK9_ObjectIdentity = ObjectIdentity
ciscoFp7120FiK9 = _CiscoFp7120FiK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2199)
)
_CiscoFp7125K9_ObjectIdentity = ObjectIdentity
ciscoFp7125K9 = _CiscoFp7125K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2200)
)
_CiscoFp8120K9_ObjectIdentity = ObjectIdentity
ciscoFp8120K9 = _CiscoFp8120K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2201)
)
_CiscoFp8130K9_ObjectIdentity = ObjectIdentity
ciscoFp8130K9 = _CiscoFp8130K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2202)
)
_CiscoFp8140K9_ObjectIdentity = ObjectIdentity
ciscoFp8140K9 = _CiscoFp8140K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2203)
)
_CiscoFp8250K9_ObjectIdentity = ObjectIdentity
ciscoFp8250K9 = _CiscoFp8250K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2204)
)
_CiscoFp8260K9_ObjectIdentity = ObjectIdentity
ciscoFp8260K9 = _CiscoFp8260K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2205)
)
_CiscoFp8270K9_ObjectIdentity = ObjectIdentity
ciscoFp8270K9 = _CiscoFp8270K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2206)
)
_CiscoFp8290K9_ObjectIdentity = ObjectIdentity
ciscoFp8290K9 = _CiscoFp8290K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2207)
)
_CiscoFp8350K9_ObjectIdentity = ObjectIdentity
ciscoFp8350K9 = _CiscoFp8350K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2208)
)
_CiscoFp8360K9_ObjectIdentity = ObjectIdentity
ciscoFp8360K9 = _CiscoFp8360K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2209)
)
_CiscoFp8370K9_ObjectIdentity = ObjectIdentity
ciscoFp8370K9 = _CiscoFp8370K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2210)
)
_CiscoFp8390K9_ObjectIdentity = ObjectIdentity
ciscoFp8390K9 = _CiscoFp8390K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2211)
)
_CiscoFs750K9_ObjectIdentity = ObjectIdentity
ciscoFs750K9 = _CiscoFs750K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2212)
)
_CiscoFs1500K9_ObjectIdentity = ObjectIdentity
ciscoFs1500K9 = _CiscoFs1500K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2213)
)
_CiscoFs3500K9_ObjectIdentity = ObjectIdentity
ciscoFs3500K9 = _CiscoFs3500K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2214)
)
_CiscoFs4000K9_ObjectIdentity = ObjectIdentity
ciscoFs4000K9 = _CiscoFs4000K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2215)
)
_CiscoAmp7150K9_ObjectIdentity = ObjectIdentity
ciscoAmp7150K9 = _CiscoAmp7150K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2216)
)
_CiscoAmp8050K9_ObjectIdentity = ObjectIdentity
ciscoAmp8050K9 = _CiscoAmp8050K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2217)
)
_CiscoAmp8150K9_ObjectIdentity = ObjectIdentity
ciscoAmp8150K9 = _CiscoAmp8150K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2218)
)
_CiscoAmp8350K9_ObjectIdentity = ObjectIdentity
ciscoAmp8350K9 = _CiscoAmp8350K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2219)
)
_CiscoAmp8360K9_ObjectIdentity = ObjectIdentity
ciscoAmp8360K9 = _CiscoAmp8360K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2220)
)
_CiscoAmp8370K9_ObjectIdentity = ObjectIdentity
ciscoAmp8370K9 = _CiscoAmp8370K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2221)
)
_CiscoAmp8390K9_ObjectIdentity = ObjectIdentity
ciscoAmp8390K9 = _CiscoAmp8390K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2222)
)
_CiscoFpSsl1500K9_ObjectIdentity = ObjectIdentity
ciscoFpSsl1500K9 = _CiscoFpSsl1500K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2223)
)
_CiscoFpSsl1500FiK9_ObjectIdentity = ObjectIdentity
ciscoFpSsl1500FiK9 = _CiscoFpSsl1500FiK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2224)
)
_CiscoFpSsl2000K9_ObjectIdentity = ObjectIdentity
ciscoFpSsl2000K9 = _CiscoFpSsl2000K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2225)
)
_CiscoFpSsl8200K9_ObjectIdentity = ObjectIdentity
ciscoFpSsl8200K9 = _CiscoFpSsl8200K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2226)
)
_CiscoFp7010K9_ObjectIdentity = ObjectIdentity
ciscoFp7010K9 = _CiscoFp7010K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2227)
)
_CiscoFp7020K9_ObjectIdentity = ObjectIdentity
ciscoFp7020K9 = _CiscoFp7020K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2228)
)
_Cisco841Mx4XK9_ObjectIdentity = ObjectIdentity
cisco841Mx4XK9 = _Cisco841Mx4XK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2229)
)
_Cisco841Mx8XK9_ObjectIdentity = ObjectIdentity
cisco841Mx8XK9 = _Cisco841Mx8XK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2230)
)
_CiscoC819GWLTEMNAAK9_ObjectIdentity = ObjectIdentity
ciscoC819GWLTEMNAAK9 = _CiscoC819GWLTEMNAAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2231)
)
_CiscoC819GWLTEGAEK9_ObjectIdentity = ObjectIdentity
ciscoC819GWLTEGAEK9 = _CiscoC819GWLTEGAEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2232)
)
_CiscoIE500012S12P10G_ObjectIdentity = ObjectIdentity
ciscoIE500012S12P10G = _CiscoIE500012S12P10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2233)
)
_CiscoRAIE1783IMS28NAC_ObjectIdentity = ObjectIdentity
ciscoRAIE1783IMS28NAC = _CiscoRAIE1783IMS28NAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2234)
)
_CiscoRAIE1783IMS28NDC_ObjectIdentity = ObjectIdentity
ciscoRAIE1783IMS28NDC = _CiscoRAIE1783IMS28NDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2235)
)
_CiscoRAIE1783IMS28RAC_ObjectIdentity = ObjectIdentity
ciscoRAIE1783IMS28RAC = _CiscoRAIE1783IMS28RAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2236)
)
_CiscoRAIE1783IMS28RDC_ObjectIdentity = ObjectIdentity
ciscoRAIE1783IMS28RDC = _CiscoRAIE1783IMS28RDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2237)
)
_CiscoACIController_ObjectIdentity = ObjectIdentity
ciscoACIController = _CiscoACIController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2238)
)
_CiscoAIRAPIW3702_ObjectIdentity = ObjectIdentity
ciscoAIRAPIW3702 = _CiscoAIRAPIW3702_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2240)
)
_CiscoASA5506H_ObjectIdentity = ObjectIdentity
ciscoASA5506H = _CiscoASA5506H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2241)
)
_CiscoASA5516_ObjectIdentity = ObjectIdentity
ciscoASA5516 = _CiscoASA5516_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2242)
)
_CiscoASA5506Hsc_ObjectIdentity = ObjectIdentity
ciscoASA5506Hsc = _CiscoASA5506Hsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2243)
)
_CiscoASA5516sc_ObjectIdentity = ObjectIdentity
ciscoASA5516sc = _CiscoASA5516sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2244)
)
_CiscoASA5506Hsy_ObjectIdentity = ObjectIdentity
ciscoASA5506Hsy = _CiscoASA5506Hsy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2245)
)
_CiscoASA5516sy_ObjectIdentity = ObjectIdentity
ciscoASA5516sy = _CiscoASA5516sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2246)
)
_CiscoASR92016SZIM_ObjectIdentity = ObjectIdentity
ciscoASR92016SZIM = _CiscoASR92016SZIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2247)
)
_CiscoIR829GWLTEMAAK9_ObjectIdentity = ObjectIdentity
ciscoIR829GWLTEMAAK9 = _CiscoIR829GWLTEMAAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2248)
)
_CiscoPwsX474812X48uE_ObjectIdentity = ObjectIdentity
ciscoPwsX474812X48uE = _CiscoPwsX474812X48uE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2249)
)
_CiscoASR1002HX_ObjectIdentity = ObjectIdentity
ciscoASR1002HX = _CiscoASR1002HX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2252)
)
_CiscoNCS4009_ObjectIdentity = ObjectIdentity
ciscoNCS4009 = _CiscoNCS4009_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2253)
)
_CiscoRAISA1783SAD2T2Ssy_ObjectIdentity = ObjectIdentity
ciscoRAISA1783SAD2T2Ssy = _CiscoRAISA1783SAD2T2Ssy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2254)
)
_CiscoRAISA1783SAD4T0Ssy_ObjectIdentity = ObjectIdentity
ciscoRAISA1783SAD4T0Ssy = _CiscoRAISA1783SAD4T0Ssy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2255)
)
_CiscoISA30002C2Fsy_ObjectIdentity = ObjectIdentity
ciscoISA30002C2Fsy = _CiscoISA30002C2Fsy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2256)
)
_CiscoISA30004Csy_ObjectIdentity = ObjectIdentity
ciscoISA30004Csy = _CiscoISA30004Csy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2257)
)
_CiscoISA4000sy_ObjectIdentity = ObjectIdentity
ciscoISA4000sy = _CiscoISA4000sy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2258)
)
_CiscoISA4000sc_ObjectIdentity = ObjectIdentity
ciscoISA4000sc = _CiscoISA4000sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2259)
)
_CiscoRAISA1783SAD2T2Ssc_ObjectIdentity = ObjectIdentity
ciscoRAISA1783SAD2T2Ssc = _CiscoRAISA1783SAD2T2Ssc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2260)
)
_CiscoRAISA1783SAD4T0Ssc_ObjectIdentity = ObjectIdentity
ciscoRAISA1783SAD4T0Ssc = _CiscoRAISA1783SAD4T0Ssc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2261)
)
_CiscoISA30002C2Fsc_ObjectIdentity = ObjectIdentity
ciscoISA30002C2Fsc = _CiscoISA30002C2Fsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2262)
)
_CiscoISA30004Csc_ObjectIdentity = ObjectIdentity
ciscoISA30004Csc = _CiscoISA30004Csc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2263)
)
_CiscoIOSXRv9000_ObjectIdentity = ObjectIdentity
ciscoIOSXRv9000 = _CiscoIOSXRv9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2264)
)
_CiscoSNS3515K9_ObjectIdentity = ObjectIdentity
ciscoSNS3515K9 = _CiscoSNS3515K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2265)
)
_CiscoSNS3595K9_ObjectIdentity = ObjectIdentity
ciscoSNS3595K9 = _CiscoSNS3595K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2266)
)
_CiscoISA30002C2F_ObjectIdentity = ObjectIdentity
ciscoISA30002C2F = _CiscoISA30002C2F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2267)
)
_CiscoISA30004C_ObjectIdentity = ObjectIdentity
ciscoISA30004C = _CiscoISA30004C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2268)
)
_CiscoRAISA1783SAD4T0S_ObjectIdentity = ObjectIdentity
ciscoRAISA1783SAD4T0S = _CiscoRAISA1783SAD4T0S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2269)
)
_CiscoRAISA1783SAD2T2S_ObjectIdentity = ObjectIdentity
ciscoRAISA1783SAD2T2S = _CiscoRAISA1783SAD2T2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2270)
)
_CiscoISA4000_ObjectIdentity = ObjectIdentity
ciscoISA4000 = _CiscoISA4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2271)
)
_CiscoC888EAK9_ObjectIdentity = ObjectIdentity
ciscoC888EAK9 = _CiscoC888EAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2272)
)
_CiscoC6816xle_ObjectIdentity = ObjectIdentity
ciscoC6816xle = _CiscoC6816xle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2273)
)
_CiscoC6832xle_ObjectIdentity = ObjectIdentity
ciscoC6832xle = _CiscoC6832xle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2274)
)
_CiscoC6824xle_ObjectIdentity = ObjectIdentity
ciscoC6824xle = _CiscoC6824xle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2275)
)
_CiscoC6840xle_ObjectIdentity = ObjectIdentity
ciscoC6840xle = _CiscoC6840xle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2276)
)
_Cat35xxStack_ObjectIdentity = ObjectIdentity
cat35xxStack = _Cat35xxStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2277)
)
_CatWsC365012X48UR_ObjectIdentity = ObjectIdentity
catWsC365012X48UR = _CatWsC365012X48UR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2278)
)
_CatWsC36508X24UQ_ObjectIdentity = ObjectIdentity
catWsC36508X24UQ = _CatWsC36508X24UQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2279)
)
_CatWsC365012X48UZ_ObjectIdentity = ObjectIdentity
catWsC365012X48UZ = _CatWsC365012X48UZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2280)
)
_CatWsC365012X48UQ_ObjectIdentity = ObjectIdentity
catWsC365012X48UQ = _CatWsC365012X48UQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2281)
)
_CiscoNam2420_ObjectIdentity = ObjectIdentity
ciscoNam2420 = _CiscoNam2420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2282)
)
_CiscoNam2440_ObjectIdentity = ObjectIdentity
ciscoNam2440 = _CiscoNam2440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2283)
)
_CiscoflowAgent3300_ObjectIdentity = ObjectIdentity
ciscoflowAgent3300 = _CiscoflowAgent3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2284)
)
_CiscoFpr9300K9_ObjectIdentity = ObjectIdentity
ciscoFpr9300K9 = _CiscoFpr9300K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2285)
)
_CiscoFpr9000SM24_ObjectIdentity = ObjectIdentity
ciscoFpr9000SM24 = _CiscoFpr9000SM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2286)
)
_CiscoFpr9000SM36_ObjectIdentity = ObjectIdentity
ciscoFpr9000SM36 = _CiscoFpr9000SM36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2288)
)
_CatWsC365048FQM_ObjectIdentity = ObjectIdentity
catWsC365048FQM = _CatWsC365048FQM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2290)
)
_CatWsC365024PDM_ObjectIdentity = ObjectIdentity
catWsC365024PDM = _CatWsC365024PDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2291)
)
_CiscoFpr4150K9_ObjectIdentity = ObjectIdentity
ciscoFpr4150K9 = _CiscoFpr4150K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2292)
)
_CiscoFpr4140K9_ObjectIdentity = ObjectIdentity
ciscoFpr4140K9 = _CiscoFpr4140K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2293)
)
_CiscoFpr4120K9_ObjectIdentity = ObjectIdentity
ciscoFpr4120K9 = _CiscoFpr4120K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2294)
)
_CiscoFpr4110K9_ObjectIdentity = ObjectIdentity
ciscoFpr4110K9 = _CiscoFpr4110K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2295)
)
_CiscoIE500016S12P_ObjectIdentity = ObjectIdentity
ciscoIE500016S12P = _CiscoIE500016S12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2296)
)
_CiscoASA5512td_ObjectIdentity = ObjectIdentity
ciscoASA5512td = _CiscoASA5512td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2297)
)
_CiscoASA5515td_ObjectIdentity = ObjectIdentity
ciscoASA5515td = _CiscoASA5515td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2298)
)
_CiscoASA5525td_ObjectIdentity = ObjectIdentity
ciscoASA5525td = _CiscoASA5525td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2299)
)
_CiscoASA5545td_ObjectIdentity = ObjectIdentity
ciscoASA5545td = _CiscoASA5545td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2300)
)
_CiscoASA5555td_ObjectIdentity = ObjectIdentity
ciscoASA5555td = _CiscoASA5555td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2301)
)
_CiscoASA5506td_ObjectIdentity = ObjectIdentity
ciscoASA5506td = _CiscoASA5506td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2302)
)
_CiscoASA5506Wtd_ObjectIdentity = ObjectIdentity
ciscoASA5506Wtd = _CiscoASA5506Wtd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2303)
)
_CiscoASA5506Htd_ObjectIdentity = ObjectIdentity
ciscoASA5506Htd = _CiscoASA5506Htd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2304)
)
_CiscoASA5508td_ObjectIdentity = ObjectIdentity
ciscoASA5508td = _CiscoASA5508td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2305)
)
_CiscoASA5516td_ObjectIdentity = ObjectIdentity
ciscoASA5516td = _CiscoASA5516td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2306)
)
_CiscoPIUCSAPLK9_ObjectIdentity = ObjectIdentity
ciscoPIUCSAPLK9 = _CiscoPIUCSAPLK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2307)
)
_Cisco899GLTEJPK9_ObjectIdentity = ObjectIdentity
cisco899GLTEJPK9 = _Cisco899GLTEJPK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2308)
)
_Cisco819GLTEMNAK9_ObjectIdentity = ObjectIdentity
cisco819GLTEMNAK9 = _Cisco819GLTEMNAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2309)
)
_CiscoFpr4110SM12_ObjectIdentity = ObjectIdentity
ciscoFpr4110SM12 = _CiscoFpr4110SM12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2313)
)
_CiscoFpr4120SM24_ObjectIdentity = ObjectIdentity
ciscoFpr4120SM24 = _CiscoFpr4120SM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2314)
)
_CiscoFpr4140SM36_ObjectIdentity = ObjectIdentity
ciscoFpr4140SM36 = _CiscoFpr4140SM36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2315)
)
_CiscoFpr4150SM44_ObjectIdentity = ObjectIdentity
ciscoFpr4150SM44 = _CiscoFpr4150SM44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2316)
)
_CiscoNCS5001_ObjectIdentity = ObjectIdentity
ciscoNCS5001 = _CiscoNCS5001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2317)
)
_CiscoNCS5002_ObjectIdentity = ObjectIdentity
ciscoNCS5002 = _CiscoNCS5002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2318)
)
_CiscoFpvK9_ObjectIdentity = ObjectIdentity
ciscoFpvK9 = _CiscoFpvK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2319)
)
_CiscoASR901CC_ObjectIdentity = ObjectIdentity
ciscoASR901CC = _CiscoASR901CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2320)
)
_CiscoASR901ECC_ObjectIdentity = ObjectIdentity
ciscoASR901ECC = _CiscoASR901ECC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2321)
)
_CiscoASR901DC10GCC_ObjectIdentity = ObjectIdentity
ciscoASR901DC10GCC = _CiscoASR901DC10GCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2322)
)
_CiscoASR901EDC10GCC_ObjectIdentity = ObjectIdentity
ciscoASR901EDC10GCC = _CiscoASR901EDC10GCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2323)
)
_CiscoASR901DC10GSCC_ObjectIdentity = ObjectIdentity
ciscoASR901DC10GSCC = _CiscoASR901DC10GSCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2324)
)
_CiscoASR92012SZIMCC_ObjectIdentity = ObjectIdentity
ciscoASR92012SZIMCC = _CiscoASR92012SZIMCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2325)
)
_CiscoNcs4201_ObjectIdentity = ObjectIdentity
ciscoNcs4201 = _CiscoNcs4201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2326)
)
_CiscoNcs4202_ObjectIdentity = ObjectIdentity
ciscoNcs4202 = _CiscoNcs4202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2327)
)
_CiscoNcs4206_ObjectIdentity = ObjectIdentity
ciscoNcs4206 = _CiscoNcs4206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2328)
)
_CiscoNcs4216_ObjectIdentity = ObjectIdentity
ciscoNcs4216 = _CiscoNcs4216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2329)
)
_CiscoIE10004TLM_ObjectIdentity = ObjectIdentity
ciscoIE10004TLM = _CiscoIE10004TLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2330)
)
_CiscoIE10006TLM_ObjectIdentity = ObjectIdentity
ciscoIE10006TLM = _CiscoIE10006TLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2331)
)
_CiscoIE10004PTSLM_ObjectIdentity = ObjectIdentity
ciscoIE10004PTSLM = _CiscoIE10004PTSLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2332)
)
_CiscoIE10008PTSLM_ObjectIdentity = ObjectIdentity
ciscoIE10008PTSLM = _CiscoIE10008PTSLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2333)
)
_CiscoVFTD_ObjectIdentity = ObjectIdentity
ciscoVFTD = _CiscoVFTD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2334)
)
_CiscoISR4451B_ObjectIdentity = ObjectIdentity
ciscoISR4451B = _CiscoISR4451B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2335)
)
_CiscoISR4431B_ObjectIdentity = ObjectIdentity
ciscoISR4431B = _CiscoISR4431B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2336)
)
_CiscoISR4351B_ObjectIdentity = ObjectIdentity
ciscoISR4351B = _CiscoISR4351B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2337)
)
_CiscoISR4331B_ObjectIdentity = ObjectIdentity
ciscoISR4331B = _CiscoISR4331B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2338)
)
_CiscoISR4321B_ObjectIdentity = ObjectIdentity
ciscoISR4321B = _CiscoISR4321B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2339)
)
_CiscoRAIE1783IMS28GNAC_ObjectIdentity = ObjectIdentity
ciscoRAIE1783IMS28GNAC = _CiscoRAIE1783IMS28GNAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2340)
)
_CiscoRAIE1783IMS28GNDC_ObjectIdentity = ObjectIdentity
ciscoRAIE1783IMS28GNDC = _CiscoRAIE1783IMS28GNDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2341)
)
_CiscoRAIE1783IMS28GRAC_ObjectIdentity = ObjectIdentity
ciscoRAIE1783IMS28GRAC = _CiscoRAIE1783IMS28GRAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2342)
)
_CiscoRAIE1783IMS28GRDC_ObjectIdentity = ObjectIdentity
ciscoRAIE1783IMS28GRDC = _CiscoRAIE1783IMS28GRDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2343)
)
_CiscoQSFP100GCWDM4S_ObjectIdentity = ObjectIdentity
ciscoQSFP100GCWDM4S = _CiscoQSFP100GCWDM4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2344)
)
_Cisco897VAGWLTEGAEK9_ObjectIdentity = ObjectIdentity
cisco897VAGWLTEGAEK9 = _Cisco897VAGWLTEGAEK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2345)
)
_Cisco886VAGLTEGAK9_ObjectIdentity = ObjectIdentity
cisco886VAGLTEGAK9 = _Cisco886VAGLTEGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2346)
)
_CiscoNcs1002_ObjectIdentity = ObjectIdentity
ciscoNcs1002 = _CiscoNcs1002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2347)
)
_CiscoASR1001HX_ObjectIdentity = ObjectIdentity
ciscoASR1001HX = _CiscoASR1001HX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2348)
)
_CiscoNCS5508_ObjectIdentity = ObjectIdentity
ciscoNCS5508 = _CiscoNCS5508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2349)
)
_CiscoNCS5501SE_ObjectIdentity = ObjectIdentity
ciscoNCS5501SE = _CiscoNCS5501SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2350)
)
_CiscoNCS5502SE_ObjectIdentity = ObjectIdentity
ciscoNCS5502SE = _CiscoNCS5502SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2351)
)
_CiscoUnifiedSipProxy_ObjectIdentity = ObjectIdentity
ciscoUnifiedSipProxy = _CiscoUnifiedSipProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2352)
)
_Cisco898EAGLTELAK9_ObjectIdentity = ObjectIdentity
cisco898EAGLTELAK9 = _Cisco898EAGLTELAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2355)
)
_Cisco897VAGLTELAK9_ObjectIdentity = ObjectIdentity
cisco897VAGLTELAK9 = _Cisco897VAGLTELAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2356)
)
_Cisco819GWLTELACK9_ObjectIdentity = ObjectIdentity
cisco819GWLTELACK9 = _Cisco819GWLTELACK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2357)
)
_Cisco819GWLTELAQK9_ObjectIdentity = ObjectIdentity
cisco819GWLTELAQK9 = _Cisco819GWLTELAQK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2358)
)
_Cisco819GWLTELANK9_ObjectIdentity = ObjectIdentity
cisco819GWLTELANK9 = _Cisco819GWLTELANK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2359)
)
_CiscoCatWSC2960L8TSLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L8TSLL = _CiscoCatWSC2960L8TSLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2360)
)
_CiscoCatWSC2960L8PSLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L8PSLL = _CiscoCatWSC2960L8PSLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2361)
)
_CiscoCatWSC2960L16TSLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L16TSLL = _CiscoCatWSC2960L16TSLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2362)
)
_CiscoCatWSC2960L16PSLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L16PSLL = _CiscoCatWSC2960L16PSLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2363)
)
_CiscoCatWSC2960L24TSLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L24TSLL = _CiscoCatWSC2960L24TSLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2364)
)
_CiscoCatWSC2960L24PSLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L24PSLL = _CiscoCatWSC2960L24PSLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2365)
)
_CiscoCatWSC2960L48TSLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L48TSLL = _CiscoCatWSC2960L48TSLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2366)
)
_CiscoCatWSC2960L48PSLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L48PSLL = _CiscoCatWSC2960L48PSLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2367)
)
_CiscoIE40104S24P_ObjectIdentity = ObjectIdentity
ciscoIE40104S24P = _CiscoIE40104S24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2368)
)
_CiscoIE401016S12P_ObjectIdentity = ObjectIdentity
ciscoIE401016S12P = _CiscoIE401016S12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2369)
)
_Cisco867VAEK9V2_ObjectIdentity = ObjectIdentity
cisco867VAEK9V2 = _Cisco867VAEK9V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2378)
)
_Cisco866VAEK9V2_ObjectIdentity = ObjectIdentity
cisco866VAEK9V2 = _Cisco866VAEK9V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2379)
)
_Cisco867VAEV2_ObjectIdentity = ObjectIdentity
cisco867VAEV2 = _Cisco867VAEV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2380)
)
_Cisco899GLTELAK9_ObjectIdentity = ObjectIdentity
cisco899GLTELAK9 = _Cisco899GLTELAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2381)
)
_Cisco819GLTELAK9_ObjectIdentity = ObjectIdentity
cisco819GLTELAK9 = _Cisco819GLTELAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2382)
)
_CiscoRAIE1783LMS5_ObjectIdentity = ObjectIdentity
ciscoRAIE1783LMS5 = _CiscoRAIE1783LMS5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2383)
)
_CiscoRAIE1783LMS8_ObjectIdentity = ObjectIdentity
ciscoRAIE1783LMS8 = _CiscoRAIE1783LMS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2384)
)
_CiscoStealthWatch2404_ObjectIdentity = ObjectIdentity
ciscoStealthWatch2404 = _CiscoStealthWatch2404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2385)
)
_CiscoStealthWatch2420_ObjectIdentity = ObjectIdentity
ciscoStealthWatch2420 = _CiscoStealthWatch2420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2386)
)
_CiscoNamApp2404_ObjectIdentity = ObjectIdentity
ciscoNamApp2404 = _CiscoNamApp2404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2387)
)
_CatWsC36508X24PD_ObjectIdentity = ObjectIdentity
catWsC36508X24PD = _CatWsC36508X24PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2388)
)
_CatWsC365012X48FD_ObjectIdentity = ObjectIdentity
catWsC365012X48FD = _CatWsC365012X48FD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2389)
)
_CiscoASR9910_ObjectIdentity = ObjectIdentity
ciscoASR9910 = _CiscoASR9910_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2390)
)
_CiscoC9800CLK9_ObjectIdentity = ObjectIdentity
ciscoC9800CLK9 = _CiscoC9800CLK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2391)
)
_Cisco819HGLTEMNAK9_ObjectIdentity = ObjectIdentity
cisco819HGLTEMNAK9 = _Cisco819HGLTEMNAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2392)
)
_CiscoIR829GWLTEGASK9_ObjectIdentity = ObjectIdentity
ciscoIR829GWLTEGASK9 = _CiscoIR829GWLTEGASK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2393)
)
_CiscoIR829GWLTEGACK9_ObjectIdentity = ObjectIdentity
ciscoIR829GWLTEGACK9 = _CiscoIR829GWLTEGACK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2394)
)
_CiscoISR4221_ObjectIdentity = ObjectIdentity
ciscoISR4221 = _CiscoISR4221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2395)
)
_CiscoISR4221B_ObjectIdentity = ObjectIdentity
ciscoISR4221B = _CiscoISR4221B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2396)
)
_CiscoCSP2100_ObjectIdentity = ObjectIdentity
ciscoCSP2100 = _CiscoCSP2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2397)
)
_CiscoCDB8U_ObjectIdentity = ObjectIdentity
ciscoCDB8U = _CiscoCDB8U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2398)
)
_CiscoCDB8P_ObjectIdentity = ObjectIdentity
ciscoCDB8P = _CiscoCDB8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2399)
)
_CiscoNCS5501_ObjectIdentity = ObjectIdentity
ciscoNCS5501 = _CiscoNCS5501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2400)
)
_CiscoNCS5502_ObjectIdentity = ObjectIdentity
ciscoNCS5502 = _CiscoNCS5502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2401)
)
_CiscoNCS4216F2BSA_ObjectIdentity = ObjectIdentity
ciscoNCS4216F2BSA = _CiscoNCS4216F2BSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2402)
)
_CiscoFpr2110td_ObjectIdentity = ObjectIdentity
ciscoFpr2110td = _CiscoFpr2110td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2404)
)
_CiscoFpr2120td_ObjectIdentity = ObjectIdentity
ciscoFpr2120td = _CiscoFpr2120td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2405)
)
_CiscoFpr2130td_ObjectIdentity = ObjectIdentity
ciscoFpr2130td = _CiscoFpr2130td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2406)
)
_CiscoFpr2140td_ObjectIdentity = ObjectIdentity
ciscoFpr2140td = _CiscoFpr2140td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2407)
)
_CiscoFpr9000SM44_ObjectIdentity = ObjectIdentity
ciscoFpr9000SM44 = _CiscoFpr9000SM44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2409)
)
_CiscoNCS5011_ObjectIdentity = ObjectIdentity
ciscoNCS5011 = _CiscoNCS5011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2411)
)
_CiscoNCS5516_ObjectIdentity = ObjectIdentity
ciscoNCS5516 = _CiscoNCS5516_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2412)
)
_CiscoNCS5504_ObjectIdentity = ObjectIdentity
ciscoNCS5504 = _CiscoNCS5504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2413)
)
_CiscoUCSE160S_ObjectIdentity = ObjectIdentity
ciscoUCSE160S = _CiscoUCSE160S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2415)
)
_CiscoUCSE180DM3_ObjectIdentity = ObjectIdentity
ciscoUCSE180DM3 = _CiscoUCSE180DM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2416)
)
_CiscoUCSE1120DM3_ObjectIdentity = ObjectIdentity
ciscoUCSE1120DM3 = _CiscoUCSE1120DM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2417)
)
_CiscoCat950012Q_ObjectIdentity = ObjectIdentity
ciscoCat950012Q = _CiscoCat950012Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2418)
)
_CiscoCat950024Q_ObjectIdentity = ObjectIdentity
ciscoCat950024Q = _CiscoCat950024Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2419)
)
_CiscoCat950040X_ObjectIdentity = ObjectIdentity
ciscoCat950040X = _CiscoCat950040X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2420)
)
_CiscoNCS1001_ObjectIdentity = ObjectIdentity
ciscoNCS1001 = _CiscoNCS1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2423)
)
_CiscoIR809G3GGAK9_ObjectIdentity = ObjectIdentity
ciscoIR809G3GGAK9 = _CiscoIR809G3GGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2425)
)
_CiscoIR809GLTELAK9_ObjectIdentity = ObjectIdentity
ciscoIR809GLTELAK9 = _CiscoIR809GLTELAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2426)
)
_Cisco3504WLC_ObjectIdentity = ObjectIdentity
cisco3504WLC = _Cisco3504WLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2427)
)
_CiscoNCS55A136HSES_ObjectIdentity = ObjectIdentity
ciscoNCS55A136HSES = _CiscoNCS55A136HSES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2428)
)
_CiscoNCS5501HD_ObjectIdentity = ObjectIdentity
ciscoNCS5501HD = _CiscoNCS5501HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2430)
)
_CiscoNCS5501HDS_ObjectIdentity = ObjectIdentity
ciscoNCS5501HDS = _CiscoNCS5501HDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2431)
)
_CiscoNCS55A124H_ObjectIdentity = ObjectIdentity
ciscoNCS55A124H = _CiscoNCS55A124H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2432)
)
_CiscoCXP2270GSR12_ObjectIdentity = ObjectIdentity
ciscoCXP2270GSR12 = _CiscoCXP2270GSR12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2433)
)
_CiscoNCS4216F2B_ObjectIdentity = ObjectIdentity
ciscoNCS4216F2B = _CiscoNCS4216F2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2434)
)
_CiscoCat930024T_ObjectIdentity = ObjectIdentity
ciscoCat930024T = _CiscoCat930024T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2435)
)
_CiscoCat930024P_ObjectIdentity = ObjectIdentity
ciscoCat930024P = _CiscoCat930024P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2436)
)
_CiscoCat930024U_ObjectIdentity = ObjectIdentity
ciscoCat930024U = _CiscoCat930024U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2437)
)
_CiscoCat930024UX_ObjectIdentity = ObjectIdentity
ciscoCat930024UX = _CiscoCat930024UX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2438)
)
_CiscoCat930048T_ObjectIdentity = ObjectIdentity
ciscoCat930048T = _CiscoCat930048T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2439)
)
_CiscoCat930048P_ObjectIdentity = ObjectIdentity
ciscoCat930048P = _CiscoCat930048P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2440)
)
_CiscoCat930048U_ObjectIdentity = ObjectIdentity
ciscoCat930048U = _CiscoCat930048U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2441)
)
_CiscoCat930048UXM_ObjectIdentity = ObjectIdentity
ciscoCat930048UXM = _CiscoCat930048UXM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2442)
)
_CiscoC11118P_ObjectIdentity = ObjectIdentity
ciscoC11118P = _CiscoC11118P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2443)
)
_CiscoC11118PLteEA_ObjectIdentity = ObjectIdentity
ciscoC11118PLteEA = _CiscoC11118PLteEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2444)
)
_CiscoC11118PLteLA_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLA = _CiscoC11118PLteLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2445)
)
_CiscoC11118PWE_ObjectIdentity = ObjectIdentity
ciscoC11118PWE = _CiscoC11118PWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2446)
)
_CiscoC11118PWB_ObjectIdentity = ObjectIdentity
ciscoC11118PWB = _CiscoC11118PWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2447)
)
_CiscoC11118PWA_ObjectIdentity = ObjectIdentity
ciscoC11118PWA = _CiscoC11118PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2448)
)
_CiscoC11118PWZ_ObjectIdentity = ObjectIdentity
ciscoC11118PWZ = _CiscoC11118PWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2449)
)
_CiscoC11118PWN_ObjectIdentity = ObjectIdentity
ciscoC11118PWN = _CiscoC11118PWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2450)
)
_CiscoC11118PWQ_ObjectIdentity = ObjectIdentity
ciscoC11118PWQ = _CiscoC11118PWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2451)
)
_CiscoC11118PWH_ObjectIdentity = ObjectIdentity
ciscoC11118PWH = _CiscoC11118PWH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2452)
)
_CiscoC11118PWR_ObjectIdentity = ObjectIdentity
ciscoC11118PWR = _CiscoC11118PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2453)
)
_CiscoC11118PWF_ObjectIdentity = ObjectIdentity
ciscoC11118PWF = _CiscoC11118PWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2454)
)
_CiscoC11118PLteEAWE_ObjectIdentity = ObjectIdentity
ciscoC11118PLteEAWE = _CiscoC11118PLteEAWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2455)
)
_CiscoC11118PLteEAWB_ObjectIdentity = ObjectIdentity
ciscoC11118PLteEAWB = _CiscoC11118PLteEAWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2456)
)
_CiscoC11118PLteEAWA_ObjectIdentity = ObjectIdentity
ciscoC11118PLteEAWA = _CiscoC11118PLteEAWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2457)
)
_CiscoC11118PLteEAWR_ObjectIdentity = ObjectIdentity
ciscoC11118PLteEAWR = _CiscoC11118PLteEAWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2458)
)
_CiscoC11118PLteLAWZ_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLAWZ = _CiscoC11118PLteLAWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2459)
)
_CiscoC11118PLteLAWN_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLAWN = _CiscoC11118PLteLAWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2460)
)
_CiscoC11118PLteLAWQ_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLAWQ = _CiscoC11118PLteLAWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2461)
)
_CiscoC11118PLteLAWH_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLAWH = _CiscoC11118PLteLAWH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2462)
)
_CiscoC11118PLteLAWF_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLAWF = _CiscoC11118PLteLAWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2463)
)
_CiscoC11118PLteLAWD_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLAWD = _CiscoC11118PLteLAWD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2464)
)
_CiscoASR914_ObjectIdentity = ObjectIdentity
ciscoASR914 = _CiscoASR914_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2480)
)
_CiscoNCSFFC2_ObjectIdentity = ObjectIdentity
ciscoNCSFFC2 = _CiscoNCSFFC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2481)
)
_CiscoNCS4KF_ObjectIdentity = ObjectIdentity
ciscoNCS4KF = _CiscoNCS4KF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2482)
)
_CiscoFpr1010td_ObjectIdentity = ObjectIdentity
ciscoFpr1010td = _CiscoFpr1010td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2483)
)
_Cisco2911A_ObjectIdentity = ObjectIdentity
cisco2911A = _Cisco2911A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2486)
)
_CiscoUCSS3260_ObjectIdentity = ObjectIdentity
ciscoUCSS3260 = _CiscoUCSS3260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2487)
)
_CiscoWSC365048TSE_ObjectIdentity = ObjectIdentity
ciscoWSC365048TSE = _CiscoWSC365048TSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2491)
)
_CiscoUCSC220M5_ObjectIdentity = ObjectIdentity
ciscoUCSC220M5 = _CiscoUCSC220M5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2492)
)
_CiscoUCSC240M5_ObjectIdentity = ObjectIdentity
ciscoUCSC240M5 = _CiscoUCSC240M5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2493)
)
_CiscoCat9300FixedSwitchStack_ObjectIdentity = ObjectIdentity
ciscoCat9300FixedSwitchStack = _CiscoCat9300FixedSwitchStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2494)
)
_CiscoCatWSC2960L24TQLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L24TQLL = _CiscoCatWSC2960L24TQLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2495)
)
_CiscoCatWSC2960L48TQLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L48TQLL = _CiscoCatWSC2960L48TQLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2496)
)
_CiscoCatWSC2960L24PQLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L24PQLL = _CiscoCatWSC2960L24PQLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2497)
)
_CiscoCatWSC2960L48PQLL_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960L48PQLL = _CiscoCatWSC2960L48PQLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2498)
)
_CiscoCat9404R_ObjectIdentity = ObjectIdentity
ciscoCat9404R = _CiscoCat9404R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2499)
)
_CiscoCat9407R_ObjectIdentity = ObjectIdentity
ciscoCat9407R = _CiscoCat9407R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2500)
)
_CiscoCat9410R_ObjectIdentity = ObjectIdentity
ciscoCat9410R = _CiscoCat9410R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2501)
)
_CiscoASR903U_ObjectIdentity = ObjectIdentity
ciscoASR903U = _CiscoASR903U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2502)
)
_CiscoASR902U_ObjectIdentity = ObjectIdentity
ciscoASR902U = _CiscoASR902U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2503)
)
_CiscoASR920U16SZIM_ObjectIdentity = ObjectIdentity
ciscoASR920U16SZIM = _CiscoASR920U16SZIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2504)
)
_CiscoC11114P_ObjectIdentity = ObjectIdentity
ciscoC11114P = _CiscoC11114P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2505)
)
_CiscoC11114PLteEA_ObjectIdentity = ObjectIdentity
ciscoC11114PLteEA = _CiscoC11114PLteEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2506)
)
_CiscoC11114PLteLA_ObjectIdentity = ObjectIdentity
ciscoC11114PLteLA = _CiscoC11114PLteLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2507)
)
_CiscoC11114PWE_ObjectIdentity = ObjectIdentity
ciscoC11114PWE = _CiscoC11114PWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2508)
)
_CiscoC11114PWB_ObjectIdentity = ObjectIdentity
ciscoC11114PWB = _CiscoC11114PWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2509)
)
_CiscoC11114PWA_ObjectIdentity = ObjectIdentity
ciscoC11114PWA = _CiscoC11114PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2510)
)
_CiscoC11114PWZ_ObjectIdentity = ObjectIdentity
ciscoC11114PWZ = _CiscoC11114PWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2511)
)
_CiscoC11114PWN_ObjectIdentity = ObjectIdentity
ciscoC11114PWN = _CiscoC11114PWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2512)
)
_CiscoC11114PWQ_ObjectIdentity = ObjectIdentity
ciscoC11114PWQ = _CiscoC11114PWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2513)
)
_CiscoC11114PWH_ObjectIdentity = ObjectIdentity
ciscoC11114PWH = _CiscoC11114PWH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2514)
)
_CiscoC11114PWR_ObjectIdentity = ObjectIdentity
ciscoC11114PWR = _CiscoC11114PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2515)
)
_CiscoC11114PWF_ObjectIdentity = ObjectIdentity
ciscoC11114PWF = _CiscoC11114PWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2516)
)
_CiscoC11114PWD_ObjectIdentity = ObjectIdentity
ciscoC11114PWD = _CiscoC11114PWD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2517)
)
_CiscoC11164P_ObjectIdentity = ObjectIdentity
ciscoC11164P = _CiscoC11164P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2518)
)
_CiscoC11164PLteEA_ObjectIdentity = ObjectIdentity
ciscoC11164PLteEA = _CiscoC11164PLteEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2519)
)
_CiscoC11174P_ObjectIdentity = ObjectIdentity
ciscoC11174P = _CiscoC11174P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2520)
)
_CiscoC11164PWE_ObjectIdentity = ObjectIdentity
ciscoC11164PWE = _CiscoC11164PWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2521)
)
_CiscoC11174PLteEA_ObjectIdentity = ObjectIdentity
ciscoC11174PLteEA = _CiscoC11174PLteEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2522)
)
_CiscoC11174PLteLA_ObjectIdentity = ObjectIdentity
ciscoC11174PLteLA = _CiscoC11174PLteLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2523)
)
_CiscoC11174PWE_ObjectIdentity = ObjectIdentity
ciscoC11174PWE = _CiscoC11174PWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2524)
)
_CiscoC11174PWA_ObjectIdentity = ObjectIdentity
ciscoC11174PWA = _CiscoC11174PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2525)
)
_CiscoC11174PWZ_ObjectIdentity = ObjectIdentity
ciscoC11174PWZ = _CiscoC11174PWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2526)
)
_CiscoC11174PM_ObjectIdentity = ObjectIdentity
ciscoC11174PM = _CiscoC11174PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2527)
)
_CiscoC11174PMLteEA_ObjectIdentity = ObjectIdentity
ciscoC11174PMLteEA = _CiscoC11174PMLteEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2528)
)
_CiscoC11174PMWE_ObjectIdentity = ObjectIdentity
ciscoC11174PMWE = _CiscoC11174PMWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2529)
)
_CiscoC980040K9_ObjectIdentity = ObjectIdentity
ciscoC980040K9 = _CiscoC980040K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2530)
)
_CiscoAIRCT9880K9_ObjectIdentity = ObjectIdentity
ciscoAIRCT9880K9 = _CiscoAIRCT9880K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2531)
)
_CiscoC11128P_ObjectIdentity = ObjectIdentity
ciscoC11128P = _CiscoC11128P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2532)
)
_CiscoC11128PLteEA_ObjectIdentity = ObjectIdentity
ciscoC11128PLteEA = _CiscoC11128PLteEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2533)
)
_CiscoC11138P_ObjectIdentity = ObjectIdentity
ciscoC11138P = _CiscoC11138P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2534)
)
_CiscoC11138PM_ObjectIdentity = ObjectIdentity
ciscoC11138PM = _CiscoC11138PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2535)
)
_CiscoC11138PLteEA_ObjectIdentity = ObjectIdentity
ciscoC11138PLteEA = _CiscoC11138PLteEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2536)
)
_CiscoC11138PLteLA_ObjectIdentity = ObjectIdentity
ciscoC11138PLteLA = _CiscoC11138PLteLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2537)
)
_CiscoC11138PMLteEA_ObjectIdentity = ObjectIdentity
ciscoC11138PMLteEA = _CiscoC11138PMLteEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2538)
)
_CiscoC11138PWE_ObjectIdentity = ObjectIdentity
ciscoC11138PWE = _CiscoC11138PWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2539)
)
_CiscoC11138PWA_ObjectIdentity = ObjectIdentity
ciscoC11138PWA = _CiscoC11138PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2540)
)
_CiscoC11138PWZ_ObjectIdentity = ObjectIdentity
ciscoC11138PWZ = _CiscoC11138PWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2541)
)
_CiscoC11138PMWE_ObjectIdentity = ObjectIdentity
ciscoC11138PMWE = _CiscoC11138PMWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2542)
)
_CiscoC11138PLteEAWE_ObjectIdentity = ObjectIdentity
ciscoC11138PLteEAWE = _CiscoC11138PLteEAWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2543)
)
_CiscoC11138PLteLAWE_ObjectIdentity = ObjectIdentity
ciscoC11138PLteLAWE = _CiscoC11138PLteLAWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2544)
)
_CiscoC11138PLteLAWZ_ObjectIdentity = ObjectIdentity
ciscoC11138PLteLAWZ = _CiscoC11138PLteLAWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2545)
)
_CiscoC11188P_ObjectIdentity = ObjectIdentity
ciscoC11188P = _CiscoC11188P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2552)
)
_CiscoC11164PLteEAWE_ObjectIdentity = ObjectIdentity
ciscoC11164PLteEAWE = _CiscoC11164PLteEAWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2554)
)
_CiscoC11174PLteEAWE_ObjectIdentity = ObjectIdentity
ciscoC11174PLteEAWE = _CiscoC11174PLteEAWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2555)
)
_CiscoC11174PLteEAWA_ObjectIdentity = ObjectIdentity
ciscoC11174PLteEAWA = _CiscoC11174PLteEAWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2556)
)
_CiscoC11174PLteLAWZ_ObjectIdentity = ObjectIdentity
ciscoC11174PLteLAWZ = _CiscoC11174PLteLAWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2557)
)
_CiscoC11174PMLteEAWE_ObjectIdentity = ObjectIdentity
ciscoC11174PMLteEAWE = _CiscoC11174PMLteEAWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2558)
)
_CiscoIR807GLTEVZK9_ObjectIdentity = ObjectIdentity
ciscoIR807GLTEVZK9 = _CiscoIR807GLTEVZK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2559)
)
_CiscoIR807GLTEGAK9_ObjectIdentity = ObjectIdentity
ciscoIR807GLTEGAK9 = _CiscoIR807GLTEGAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2560)
)
_CiscoIR807GLTENAK9_ObjectIdentity = ObjectIdentity
ciscoIR807GLTENAK9 = _CiscoIR807GLTENAK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2561)
)
_CiscoUCSE180DM3K9_ObjectIdentity = ObjectIdentity
ciscoUCSE180DM3K9 = _CiscoUCSE180DM3K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2562)
)
_CiscoUCSE1120DM3K9_ObjectIdentity = ObjectIdentity
ciscoUCSE1120DM3K9 = _CiscoUCSE1120DM3K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2563)
)
_CiscoCat930048UN_ObjectIdentity = ObjectIdentity
ciscoCat930048UN = _CiscoCat930048UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2564)
)
_CiscoNFVIS_ObjectIdentity = ObjectIdentity
ciscoNFVIS = _CiscoNFVIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2565)
)
_CiscoCat950032C_ObjectIdentity = ObjectIdentity
ciscoCat950032C = _CiscoCat950032C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2566)
)
_CiscoCat950032QC_ObjectIdentity = ObjectIdentity
ciscoCat950032QC = _CiscoCat950032QC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2567)
)
_CiscoCat950048Y4C_ObjectIdentity = ObjectIdentity
ciscoCat950048Y4C = _CiscoCat950048Y4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2568)
)
_CiscoIR829GWLTEGAxK9_ObjectIdentity = ObjectIdentity
ciscoIR829GWLTEGAxK9 = _CiscoIR829GWLTEGAxK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2569)
)
_CiscoNCS55A2MODSES_ObjectIdentity = ObjectIdentity
ciscoNCS55A2MODSES = _CiscoNCS55A2MODSES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2570)
)
_CiscoNCS55A2MODS_ObjectIdentity = ObjectIdentity
ciscoNCS55A2MODS = _CiscoNCS55A2MODS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2571)
)
_CiscoASR9906_ObjectIdentity = ObjectIdentity
ciscoASR9906 = _CiscoASR9906_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2572)
)
_CiscoCat950024Y4C_ObjectIdentity = ObjectIdentity
ciscoCat950024Y4C = _CiscoCat950024Y4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2573)
)
_CiscoCat9200L24P4X_ObjectIdentity = ObjectIdentity
ciscoCat9200L24P4X = _CiscoCat9200L24P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2574)
)
_CiscoCat9200L48P4X_ObjectIdentity = ObjectIdentity
ciscoCat9200L48P4X = _CiscoCat9200L48P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2575)
)
_CiscoCat9200L24PXG4X_ObjectIdentity = ObjectIdentity
ciscoCat9200L24PXG4X = _CiscoCat9200L24PXG4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2576)
)
_CiscoCat9200L24PXG2Y_ObjectIdentity = ObjectIdentity
ciscoCat9200L24PXG2Y = _CiscoCat9200L24PXG2Y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2577)
)
_CiscoCat9200L48PXG4X_ObjectIdentity = ObjectIdentity
ciscoCat9200L48PXG4X = _CiscoCat9200L48PXG4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2578)
)
_CiscoCat9200L48PXG2Y_ObjectIdentity = ObjectIdentity
ciscoCat9200L48PXG2Y = _CiscoCat9200L48PXG2Y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2579)
)
_CiscoCat920024T_ObjectIdentity = ObjectIdentity
ciscoCat920024T = _CiscoCat920024T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2580)
)
_CiscoCat9200L24T4G_ObjectIdentity = ObjectIdentity
ciscoCat9200L24T4G = _CiscoCat9200L24T4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2581)
)
_CiscoCat9200L48T4G_ObjectIdentity = ObjectIdentity
ciscoCat9200L48T4G = _CiscoCat9200L48T4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2582)
)
_CiscoCat9200L24T4X_ObjectIdentity = ObjectIdentity
ciscoCat9200L24T4X = _CiscoCat9200L24T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2583)
)
_CiscoCat9200L48T4X_ObjectIdentity = ObjectIdentity
ciscoCat9200L48T4X = _CiscoCat9200L48T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2584)
)
_CiscoCat9200L24P4G_ObjectIdentity = ObjectIdentity
ciscoCat9200L24P4G = _CiscoCat9200L24P4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2585)
)
_CiscoCat9200L48P4G_ObjectIdentity = ObjectIdentity
ciscoCat9200L48P4G = _CiscoCat9200L48P4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2586)
)
_CiscoCat920048T_ObjectIdentity = ObjectIdentity
ciscoCat920048T = _CiscoCat920048T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2587)
)
_CiscoCat920024P_ObjectIdentity = ObjectIdentity
ciscoCat920024P = _CiscoCat920024P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2588)
)
_CiscoCat920048P_ObjectIdentity = ObjectIdentity
ciscoCat920048P = _CiscoCat920048P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2589)
)
_CiscoCat920024PXG_ObjectIdentity = ObjectIdentity
ciscoCat920024PXG = _CiscoCat920024PXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2590)
)
_CiscoCat920048PXG_ObjectIdentity = ObjectIdentity
ciscoCat920048PXG = _CiscoCat920048PXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2591)
)
_CiscoCat950016X_ObjectIdentity = ObjectIdentity
ciscoCat950016X = _CiscoCat950016X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2592)
)
_CiscoCat9500FixedSwitchStack_ObjectIdentity = ObjectIdentity
ciscoCat9500FixedSwitchStack = _CiscoCat9500FixedSwitchStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2593)
)
_CiscoN5204GAZA_ObjectIdentity = ObjectIdentity
ciscoN5204GAZA = _CiscoN5204GAZA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2602)
)
_CiscoN52020G4ZA_ObjectIdentity = ObjectIdentity
ciscoN52020G4ZA = _CiscoN52020G4ZA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2603)
)
_CiscoN52020G4ZD_ObjectIdentity = ObjectIdentity
ciscoN52020G4ZD = _CiscoN52020G4ZD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2604)
)
_CiscoN520X4G4ZA_ObjectIdentity = ObjectIdentity
ciscoN520X4G4ZA = _CiscoN520X4G4ZA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2605)
)
_CiscoN520X4G4ZD_ObjectIdentity = ObjectIdentity
ciscoN520X4G4ZD = _CiscoN520X4G4ZD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2606)
)
_CiscoN520X20G4ZA_ObjectIdentity = ObjectIdentity
ciscoN520X20G4ZA = _CiscoN520X20G4ZA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2607)
)
_CiscoN520X20G4ZD_ObjectIdentity = ObjectIdentity
ciscoN520X20G4ZD = _CiscoN520X20G4ZD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2608)
)
_CiscoIR829MLTELAxK9_ObjectIdentity = ObjectIdentity
ciscoIR829MLTELAxK9 = _CiscoIR829MLTELAxK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2609)
)
_CiscoIR829M2LTEEAxK9_ObjectIdentity = ObjectIdentity
ciscoIR829M2LTEEAxK9 = _CiscoIR829M2LTEEAxK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2610)
)
_CiscoISA30004Ctd_ObjectIdentity = ObjectIdentity
ciscoISA30004Ctd = _CiscoISA30004Ctd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2611)
)
_CiscoISA30002C2Ftd_ObjectIdentity = ObjectIdentity
ciscoISA30002C2Ftd = _CiscoISA30002C2Ftd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2612)
)
_CiscoRA1783SAD4T0Std_ObjectIdentity = ObjectIdentity
ciscoRA1783SAD4T0Std = _CiscoRA1783SAD4T0Std_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2613)
)
_CiscoRA1783SAD2T2Std_ObjectIdentity = ObjectIdentity
ciscoRA1783SAD2T2Std = _CiscoRA1783SAD2T2Std_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2614)
)
_Cisco8818_ObjectIdentity = ObjectIdentity
cisco8818 = _Cisco8818_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2615)
)
_Cisco8812_ObjectIdentity = ObjectIdentity
cisco8812 = _Cisco8812_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2616)
)
_Cisco8808_ObjectIdentity = ObjectIdentity
cisco8808 = _Cisco8808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2617)
)
_CiscoC11092PLteGB_ObjectIdentity = ObjectIdentity
ciscoC11092PLteGB = _CiscoC11092PLteGB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2619)
)
_CiscoC11092PLteUS_ObjectIdentity = ObjectIdentity
ciscoC11092PLteUS = _CiscoC11092PLteUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2620)
)
_CiscoC11092PLteVZ_ObjectIdentity = ObjectIdentity
ciscoC11092PLteVZ = _CiscoC11092PLteVZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2621)
)
_CiscoC11092PLteJN_ObjectIdentity = ObjectIdentity
ciscoC11092PLteJN = _CiscoC11092PLteJN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2622)
)
_CiscoC11092PLteAU_ObjectIdentity = ObjectIdentity
ciscoC11092PLteAU = _CiscoC11092PLteAU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2623)
)
_CiscoC11092PLteIN_ObjectIdentity = ObjectIdentity
ciscoC11092PLteIN = _CiscoC11092PLteIN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2624)
)
_CiscoC11014P_ObjectIdentity = ObjectIdentity
ciscoC11014P = _CiscoC11014P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2625)
)
_CiscoC11014PLteP_ObjectIdentity = ObjectIdentity
ciscoC11014PLteP = _CiscoC11014PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2626)
)
_CiscoC11014PLtePWE_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWE = _CiscoC11014PLtePWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2627)
)
_CiscoC11014PLtePWB_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWB = _CiscoC11014PLtePWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2628)
)
_CiscoC11014PLtePWD_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWD = _CiscoC11014PLtePWD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2629)
)
_CiscoC11014PLtePWZ_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWZ = _CiscoC11014PLtePWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2630)
)
_CiscoC11014PLtePWA_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWA = _CiscoC11014PLtePWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2631)
)
_CiscoC11014PLtePWH_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWH = _CiscoC11014PLtePWH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2632)
)
_CiscoC11014PLtePWQ_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWQ = _CiscoC11014PLtePWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2633)
)
_CiscoC11014PLtePWR_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWR = _CiscoC11014PLtePWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2634)
)
_CiscoC11014PLtePWN_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWN = _CiscoC11014PLtePWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2635)
)
_CiscoC11014PLtePWF_ObjectIdentity = ObjectIdentity
ciscoC11014PLtePWF = _CiscoC11014PLtePWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2636)
)
_CiscoC11094PLte2P_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2P = _CiscoC11094PLte2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2637)
)
_CiscoC11094PLte2PWB_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWB = _CiscoC11094PLte2PWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2638)
)
_CiscoC11094PLte2PWE_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWE = _CiscoC11094PLte2PWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2639)
)
_CiscoC11094PLte2PWD_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWD = _CiscoC11094PLte2PWD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2640)
)
_CiscoC11094PLte2PWZ_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWZ = _CiscoC11094PLte2PWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2641)
)
_CiscoC11094PLte2PWA_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWA = _CiscoC11094PLte2PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2642)
)
_CiscoC11094PLte2PWH_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWH = _CiscoC11094PLte2PWH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2643)
)
_CiscoC11094PLte2PWQ_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWQ = _CiscoC11094PLte2PWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2644)
)
_CiscoC11094PLte2PWN_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWN = _CiscoC11094PLte2PWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2645)
)
_CiscoC11094PLte2PWR_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWR = _CiscoC11094PLte2PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2646)
)
_CiscoC11094PLte2PWF_ObjectIdentity = ObjectIdentity
ciscoC11094PLte2PWF = _CiscoC11094PLte2PWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2647)
)
_CiscoC9606R_ObjectIdentity = ObjectIdentity
ciscoC9606R = _CiscoC9606R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2648)
)
_Cisco8201_ObjectIdentity = ObjectIdentity
cisco8201 = _Cisco8201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2649)
)
_Cisco8202_ObjectIdentity = ObjectIdentity
cisco8202 = _Cisco8202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2650)
)
_CiscoC11128PWE_ObjectIdentity = ObjectIdentity
ciscoC11128PWE = _CiscoC11128PWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2652)
)
_CiscoC11128PLteEAWE_ObjectIdentity = ObjectIdentity
ciscoC11128PLteEAWE = _CiscoC11128PLteEAWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2653)
)
_CiscoC11138PWB_ObjectIdentity = ObjectIdentity
ciscoC11138PWB = _CiscoC11138PWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2654)
)
_CiscoC11138PLteEAWB_ObjectIdentity = ObjectIdentity
ciscoC11138PLteEAWB = _CiscoC11138PLteEAWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2655)
)
_CiscoC11138PLteLAWA_ObjectIdentity = ObjectIdentity
ciscoC11138PLteLAWA = _CiscoC11138PLteLAWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2656)
)
_CiscoC11164PLteLA_ObjectIdentity = ObjectIdentity
ciscoC11164PLteLA = _CiscoC11164PLteLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2657)
)
_CiscoASR9901_ObjectIdentity = ObjectIdentity
ciscoASR9901 = _CiscoASR9901_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2658)
)
_CiscoEsxSECPA_ObjectIdentity = ObjectIdentity
ciscoEsxSECPA = _CiscoEsxSECPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2659)
)
_CiscoKvmSECPA_ObjectIdentity = ObjectIdentity
ciscoKvmSECPA = _CiscoKvmSECPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2660)
)
_CiscoIR1101K9_ObjectIdentity = ObjectIdentity
ciscoIR1101K9 = _CiscoIR1101K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2661)
)
_CiscoFpr1140td_ObjectIdentity = ObjectIdentity
ciscoFpr1140td = _CiscoFpr1140td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2662)
)
_CiscoFpr1120td_ObjectIdentity = ObjectIdentity
ciscoFpr1120td = _CiscoFpr1120td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2663)
)
_CiscoCat9400VirtualStack_ObjectIdentity = ObjectIdentity
ciscoCat9400VirtualStack = _CiscoCat9400VirtualStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2664)
)
_CiscoISRAP1100ACME_ObjectIdentity = ObjectIdentity
ciscoISRAP1100ACME = _CiscoISRAP1100ACME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2665)
)
_CiscoISR4221X_ObjectIdentity = ObjectIdentity
ciscoISR4221X = _CiscoISR4221X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2666)
)
_CiscoC1111X8P_ObjectIdentity = ObjectIdentity
ciscoC1111X8P = _CiscoC1111X8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2668)
)
_CiscoC980080K9_ObjectIdentity = ObjectIdentity
ciscoC980080K9 = _CiscoC980080K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2669)
)
_CiscoAP4800_ObjectIdentity = ObjectIdentity
ciscoAP4800 = _CiscoAP4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2670)
)
_CiscoIR829M2LTELAxK9_ObjectIdentity = ObjectIdentity
ciscoIR829M2LTELAxK9 = _CiscoIR829M2LTELAxK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2672)
)
_CiscoIR829MLTEEAxK9_ObjectIdentity = ObjectIdentity
ciscoIR829MLTEEAxK9 = _CiscoIR829MLTEEAxK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2673)
)
_CiscoIR829BLTEEAxK9_ObjectIdentity = ObjectIdentity
ciscoIR829BLTEEAxK9 = _CiscoIR829BLTEEAxK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2674)
)
_CiscoIR829BLTELAxK9_ObjectIdentity = ObjectIdentity
ciscoIR829BLTELAxK9 = _CiscoIR829BLTELAxK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2675)
)
_CiscoIR829B2LTEEAxK9_ObjectIdentity = ObjectIdentity
ciscoIR829B2LTEEAxK9 = _CiscoIR829B2LTEEAxK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2676)
)
_CiscoIR829B2LTELAxK9_ObjectIdentity = ObjectIdentity
ciscoIR829B2LTELAxK9 = _CiscoIR829B2LTELAxK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2677)
)
_CiscoASR92012SZD_ObjectIdentity = ObjectIdentity
ciscoASR92012SZD = _CiscoASR92012SZD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2678)
)
_CiscoASR92012SZA_ObjectIdentity = ObjectIdentity
ciscoASR92012SZA = _CiscoASR92012SZA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2679)
)
_CiscoISR4461_ObjectIdentity = ObjectIdentity
ciscoISR4461 = _CiscoISR4461_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2680)
)
_CiscoESS3300NCP_ObjectIdentity = ObjectIdentity
ciscoESS3300NCP = _CiscoESS3300NCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2681)
)
_CiscoESS3300CON_ObjectIdentity = ObjectIdentity
ciscoESS3300CON = _CiscoESS3300CON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2682)
)
_CiscoIE32008T2S_ObjectIdentity = ObjectIdentity
ciscoIE32008T2S = _CiscoIE32008T2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2683)
)
_CiscoIE32008P2S_ObjectIdentity = ObjectIdentity
ciscoIE32008P2S = _CiscoIE32008P2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2684)
)
_CiscoIE33008T2S_ObjectIdentity = ObjectIdentity
ciscoIE33008T2S = _CiscoIE33008T2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2685)
)
_CiscoIE33008P2S_ObjectIdentity = ObjectIdentity
ciscoIE33008P2S = _CiscoIE33008P2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2686)
)
_CiscoIE34008P2S_ObjectIdentity = ObjectIdentity
ciscoIE34008P2S = _CiscoIE34008P2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2687)
)
_CiscoCat9500VirtualStack_ObjectIdentity = ObjectIdentity
ciscoCat9500VirtualStack = _CiscoCat9500VirtualStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2688)
)
_CiscoNam2520_ObjectIdentity = ObjectIdentity
ciscoNam2520 = _CiscoNam2520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2689)
)
_CiscoNam2540_ObjectIdentity = ObjectIdentity
ciscoNam2540 = _CiscoNam2540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2690)
)
_CiscoCSPA2520_ObjectIdentity = ObjectIdentity
ciscoCSPA2520 = _CiscoCSPA2520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2691)
)
_CiscoIR1101XK9_ObjectIdentity = ObjectIdentity
ciscoIR1101XK9 = _CiscoIR1101XK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2692)
)
_CiscoVG450_ObjectIdentity = ObjectIdentity
ciscoVG450 = _CiscoVG450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2693)
)
_CiscoCat9200LFixedSwitchStack_ObjectIdentity = ObjectIdentity
ciscoCat9200LFixedSwitchStack = _CiscoCat9200LFixedSwitchStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2694)
)
_CiscoCat9200FixedSwitchStack_ObjectIdentity = ObjectIdentity
ciscoCat9200FixedSwitchStack = _CiscoCat9200FixedSwitchStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2695)
)
_CiscoRAIE1783MMS10B_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10B = _CiscoRAIE1783MMS10B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2697)
)
_CiscoRAIE1783MMS10BE_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10BE = _CiscoRAIE1783MMS10BE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2698)
)
_CiscoRAIE1783MMS10_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10 = _CiscoRAIE1783MMS10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2699)
)
_CiscoRAIE1783MMS10R_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10R = _CiscoRAIE1783MMS10R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2700)
)
_CiscoRAIE1783MMS10E_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10E = _CiscoRAIE1783MMS10E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2701)
)
_CiscoRAIE1783MMS10ER_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10ER = _CiscoRAIE1783MMS10ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2702)
)
_CiscoRAIE1783MMS10EA_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10EA = _CiscoRAIE1783MMS10EA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2703)
)
_CiscoRAIE1783MMS10EAR_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10EAR = _CiscoRAIE1783MMS10EAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2704)
)
_CiscoASR92020SZM_ObjectIdentity = ObjectIdentity
ciscoASR92020SZM = _CiscoASR92020SZM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2705)
)
_Cisco9214PK9_ObjectIdentity = ObjectIdentity
cisco9214PK9 = _Cisco9214PK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2708)
)
_Cisco9314PK9_ObjectIdentity = ObjectIdentity
cisco9314PK9 = _Cisco9314PK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2709)
)
_Cisco9214PLTEGBK9_ObjectIdentity = ObjectIdentity
cisco9214PLTEGBK9 = _Cisco9214PLTEGBK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2711)
)
_Cisco9214PLTEASK9_ObjectIdentity = ObjectIdentity
cisco9214PLTEASK9 = _Cisco9214PLTEASK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2712)
)
_Cisco9214PLTEAUK9_ObjectIdentity = ObjectIdentity
cisco9214PLTEAUK9 = _Cisco9214PLTEAUK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2713)
)
_Cisco921J4PK9_ObjectIdentity = ObjectIdentity
cisco921J4PK9 = _Cisco921J4PK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2715)
)
_Cisco9274PK9_ObjectIdentity = ObjectIdentity
cisco9274PK9 = _Cisco9274PK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2716)
)
_Cisco9274PMK9_ObjectIdentity = ObjectIdentity
cisco9274PMK9 = _Cisco9274PMK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2717)
)
_Cisco9264PK9_ObjectIdentity = ObjectIdentity
cisco9264PK9 = _Cisco9264PK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2718)
)
_Cisco9274PLTEAUK9_ObjectIdentity = ObjectIdentity
cisco9274PLTEAUK9 = _Cisco9274PLTEAUK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2719)
)
_Cisco9274PLTEGBK9_ObjectIdentity = ObjectIdentity
cisco9274PLTEGBK9 = _Cisco9274PLTEGBK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2721)
)
_Cisco9274PMLTEGBK9_ObjectIdentity = ObjectIdentity
cisco9274PMLTEGBK9 = _Cisco9274PMLTEGBK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2722)
)
_Cisco9264PLTEGBK9_ObjectIdentity = ObjectIdentity
cisco9264PLTEGBK9 = _Cisco9264PLTEGBK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2723)
)
_CiscoAP1840_ObjectIdentity = ObjectIdentity
ciscoAP1840 = _CiscoAP1840_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2730)
)
_CiscoC11118PWS_ObjectIdentity = ObjectIdentity
ciscoC11118PWS = _CiscoC11118PWS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2731)
)
_CiscoC11118PLteLAWS_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLAWS = _CiscoC11118PLteLAWS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2732)
)
_CiscoC11118PLteLAWA_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLAWA = _CiscoC11118PLteLAWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2733)
)
_CiscoC11118PLteLAWE_ObjectIdentity = ObjectIdentity
ciscoC11118PLteLAWE = _CiscoC11118PLteLAWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2734)
)
_CiscoNCS55A2MODHDS_ObjectIdentity = ObjectIdentity
ciscoNCS55A2MODHDS = _CiscoNCS55A2MODHDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2735)
)
_CiscoUCSC125_ObjectIdentity = ObjectIdentity
ciscoUCSC125 = _CiscoUCSC125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2737)
)
_CiscoWSC6506E_ObjectIdentity = ObjectIdentity
ciscoWSC6506E = _CiscoWSC6506E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2738)
)
_CiscoWSC6509E_ObjectIdentity = ObjectIdentity
ciscoWSC6509E = _CiscoWSC6509E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2739)
)
_CiscoNCS1004_ObjectIdentity = ObjectIdentity
ciscoNCS1004 = _CiscoNCS1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2740)
)
_CiscoN54024Z8Q2CM_ObjectIdentity = ObjectIdentity
ciscoN54024Z8Q2CM = _CiscoN54024Z8Q2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2741)
)
_CiscoN540X24Z8Q2CM_ObjectIdentity = ObjectIdentity
ciscoN540X24Z8Q2CM = _CiscoN540X24Z8Q2CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2742)
)
_CiscoN560RSP4_ObjectIdentity = ObjectIdentity
ciscoN560RSP4 = _CiscoN560RSP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2743)
)
_CiscoN560RSP4E_ObjectIdentity = ObjectIdentity
ciscoN560RSP4E = _CiscoN560RSP4E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2744)
)
_CiscoC11218PLteP_ObjectIdentity = ObjectIdentity
ciscoC11218PLteP = _CiscoC11218PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2745)
)
_CiscoC1121X8PLTEP_ObjectIdentity = ObjectIdentity
ciscoC1121X8PLTEP = _CiscoC1121X8PLTEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2746)
)
_CiscoC11218PLtePWE_ObjectIdentity = ObjectIdentity
ciscoC11218PLtePWE = _CiscoC11218PLtePWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2747)
)
_CiscoC11218PLtePWB_ObjectIdentity = ObjectIdentity
ciscoC11218PLtePWB = _CiscoC11218PLtePWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2748)
)
_CiscoC11218PLtePWZ_ObjectIdentity = ObjectIdentity
ciscoC11218PLtePWZ = _CiscoC11218PLtePWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2749)
)
_CiscoC11218PLtePWQ_ObjectIdentity = ObjectIdentity
ciscoC11218PLtePWQ = _CiscoC11218PLtePWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2750)
)
_CiscoC11218P_ObjectIdentity = ObjectIdentity
ciscoC11218P = _CiscoC11218P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2751)
)
_CiscoC1121X8P_ObjectIdentity = ObjectIdentity
ciscoC1121X8P = _CiscoC1121X8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2752)
)
_CiscoC11618P_ObjectIdentity = ObjectIdentity
ciscoC11618P = _CiscoC11618P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2753)
)
_CiscoC1161X8P_ObjectIdentity = ObjectIdentity
ciscoC1161X8P = _CiscoC1161X8P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2754)
)
_CiscoC11618PLteP_ObjectIdentity = ObjectIdentity
ciscoC11618PLteP = _CiscoC11618PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2755)
)
_CiscoC1161X8PLteP_ObjectIdentity = ObjectIdentity
ciscoC1161X8PLteP = _CiscoC1161X8PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2756)
)
_CiscoFpr9000SM56_ObjectIdentity = ObjectIdentity
ciscoFpr9000SM56 = _CiscoFpr9000SM56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2757)
)
_CiscoC11268PLteP_ObjectIdentity = ObjectIdentity
ciscoC11268PLteP = _CiscoC11268PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2758)
)
_CiscoC11278PLteP_ObjectIdentity = ObjectIdentity
ciscoC11278PLteP = _CiscoC11278PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2759)
)
_CiscoC11278PMLteP_ObjectIdentity = ObjectIdentity
ciscoC11278PMLteP = _CiscoC11278PMLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2760)
)
_CiscoC1126X8PLteP_ObjectIdentity = ObjectIdentity
ciscoC1126X8PLteP = _CiscoC1126X8PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2761)
)
_CiscoC1127X8PLteP_ObjectIdentity = ObjectIdentity
ciscoC1127X8PLteP = _CiscoC1127X8PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2762)
)
_CiscoC1127X8PMLteP_ObjectIdentity = ObjectIdentity
ciscoC1127X8PMLteP = _CiscoC1127X8PMLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2763)
)
_CiscoC11214P_ObjectIdentity = ObjectIdentity
ciscoC11214P = _CiscoC11214P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2764)
)
_CiscoC11214PLteP_ObjectIdentity = ObjectIdentity
ciscoC11214PLteP = _CiscoC11214PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2765)
)
_CiscoC11288PLteP_ObjectIdentity = ObjectIdentity
ciscoC11288PLteP = _CiscoC11288PLteP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2766)
)
_CiscoVG4002FXS2FXO_ObjectIdentity = ObjectIdentity
ciscoVG4002FXS2FXO = _CiscoVG4002FXS2FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2767)
)
_CiscoVG4004FXS4FXO_ObjectIdentity = ObjectIdentity
ciscoVG4004FXS4FXO = _CiscoVG4004FXS4FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2768)
)
_CiscoVG4006FXS6FXO_ObjectIdentity = ObjectIdentity
ciscoVG4006FXS6FXO = _CiscoVG4006FXS6FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2769)
)
_CiscoVG4008FXS_ObjectIdentity = ObjectIdentity
ciscoVG4008FXS = _CiscoVG4008FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2770)
)
_CiscoC891FJK9_ObjectIdentity = ObjectIdentity
ciscoC891FJK9 = _CiscoC891FJK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2771)
)
_CiscoFpr9000SM40_ObjectIdentity = ObjectIdentity
ciscoFpr9000SM40 = _CiscoFpr9000SM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2772)
)
_CiscoFpr9000SM48_ObjectIdentity = ObjectIdentity
ciscoFpr9000SM48 = _CiscoFpr9000SM48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2773)
)
_CiscoFpr4115SM24_ObjectIdentity = ObjectIdentity
ciscoFpr4115SM24 = _CiscoFpr4115SM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2774)
)
_CiscoFpr4125SM32_ObjectIdentity = ObjectIdentity
ciscoFpr4125SM32 = _CiscoFpr4125SM32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2775)
)
_CiscoFpr4145SM44_ObjectIdentity = ObjectIdentity
ciscoFpr4145SM44 = _CiscoFpr4145SM44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2776)
)
_CiscoFpr4145K9_ObjectIdentity = ObjectIdentity
ciscoFpr4145K9 = _CiscoFpr4145K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2777)
)
_CiscoFpr4125K9_ObjectIdentity = ObjectIdentity
ciscoFpr4125K9 = _CiscoFpr4125K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2778)
)
_CiscoFpr4115K9_ObjectIdentity = ObjectIdentity
ciscoFpr4115K9 = _CiscoFpr4115K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2779)
)
_CiscoCat930024S_ObjectIdentity = ObjectIdentity
ciscoCat930024S = _CiscoCat930024S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2780)
)
_CiscoCat930048S_ObjectIdentity = ObjectIdentity
ciscoCat930048S = _CiscoCat930048S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2781)
)
_CiscoIOSXREdgecore591654XKSOACF_ObjectIdentity = ObjectIdentity
ciscoIOSXREdgecore591654XKSOACF = _CiscoIOSXREdgecore591654XKSOACF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2782)
)
_CiscoIOSXREdgecoreAS781664X_ObjectIdentity = ObjectIdentity
ciscoIOSXREdgecoreAS781664X = _CiscoIOSXREdgecoreAS781664X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2783)
)
_CiscoSNS3615K9_ObjectIdentity = ObjectIdentity
ciscoSNS3615K9 = _CiscoSNS3615K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2784)
)
_CiscoSNS3655K9_ObjectIdentity = ObjectIdentity
ciscoSNS3655K9 = _CiscoSNS3655K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2785)
)
_CiscoSNS3695K9_ObjectIdentity = ObjectIdentity
ciscoSNS3695K9 = _CiscoSNS3695K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2786)
)
_CiscoNCS55A2MODHXS_ObjectIdentity = ObjectIdentity
ciscoNCS55A2MODHXS = _CiscoNCS55A2MODHXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2787)
)
_CiscoC1121X8PLtePWE_ObjectIdentity = ObjectIdentity
ciscoC1121X8PLtePWE = _CiscoC1121X8PLtePWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2788)
)
_CiscoC1121X8PLtePWB_ObjectIdentity = ObjectIdentity
ciscoC1121X8PLtePWB = _CiscoC1121X8PLtePWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2789)
)
_CiscoC1121X8PLtePWZ_ObjectIdentity = ObjectIdentity
ciscoC1121X8PLtePWZ = _CiscoC1121X8PLtePWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2790)
)
_CiscoC1121X8PLtePWA_ObjectIdentity = ObjectIdentity
ciscoC1121X8PLtePWA = _CiscoC1121X8PLtePWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2791)
)
_CiscoCat9300L24T4G_ObjectIdentity = ObjectIdentity
ciscoCat9300L24T4G = _CiscoCat9300L24T4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2792)
)
_CiscoCat9300L48T4G_ObjectIdentity = ObjectIdentity
ciscoCat9300L48T4G = _CiscoCat9300L48T4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2793)
)
_CiscoCat9300L24T4X_ObjectIdentity = ObjectIdentity
ciscoCat9300L24T4X = _CiscoCat9300L24T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2794)
)
_CiscoCat9300L48T4X_ObjectIdentity = ObjectIdentity
ciscoCat9300L48T4X = _CiscoCat9300L48T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2795)
)
_CiscoCat9300L24P4G_ObjectIdentity = ObjectIdentity
ciscoCat9300L24P4G = _CiscoCat9300L24P4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2796)
)
_CiscoCat9300L48P4G_ObjectIdentity = ObjectIdentity
ciscoCat9300L48P4G = _CiscoCat9300L48P4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2797)
)
_CiscoCat9300L24P4X_ObjectIdentity = ObjectIdentity
ciscoCat9300L24P4X = _CiscoCat9300L24P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2798)
)
_CiscoCat9300L48P4X_ObjectIdentity = ObjectIdentity
ciscoCat9300L48P4X = _CiscoCat9300L48P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2799)
)
_CiscoCat9300L24UXG4X_ObjectIdentity = ObjectIdentity
ciscoCat9300L24UXG4X = _CiscoCat9300L24UXG4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2800)
)
_CiscoCat9300L48UXG4X_ObjectIdentity = ObjectIdentity
ciscoCat9300L48UXG4X = _CiscoCat9300L48UXG4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2801)
)
_CiscoCat9300L24UXG2Q_ObjectIdentity = ObjectIdentity
ciscoCat9300L24UXG2Q = _CiscoCat9300L24UXG2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2802)
)
_CiscoCat9300L48UXG2Q_ObjectIdentity = ObjectIdentity
ciscoCat9300L48UXG2Q = _CiscoCat9300L48UXG2Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2803)
)
_Ciscocat9300Lstack_ObjectIdentity = ObjectIdentity
ciscocat9300Lstack = _Ciscocat9300Lstack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2804)
)
_CiscoCatWSC2960LSM8TS_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM8TS = _CiscoCatWSC2960LSM8TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2806)
)
_CiscoCatWSC2960LSM8PS_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM8PS = _CiscoCatWSC2960LSM8PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2807)
)
_CiscoCatWSC2960LSM16TS_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM16TS = _CiscoCatWSC2960LSM16TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2808)
)
_CiscoCatWSC2960LSM16PS_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM16PS = _CiscoCatWSC2960LSM16PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2809)
)
_CiscoCatWSC2960LSM24TS_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM24TS = _CiscoCatWSC2960LSM24TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2810)
)
_CiscoCatWSC2960LSM24PS_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM24PS = _CiscoCatWSC2960LSM24PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2811)
)
_CiscoCatWSC2960LSM48TS_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM48TS = _CiscoCatWSC2960LSM48TS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2812)
)
_CiscoCatWSC2960LSM48PS_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM48PS = _CiscoCatWSC2960LSM48PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2813)
)
_CiscoCatWSC2960LSM24TQ_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM24TQ = _CiscoCatWSC2960LSM24TQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2814)
)
_CiscoCatWSC2960LSM48TQ_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM48TQ = _CiscoCatWSC2960LSM48TQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2815)
)
_CiscoCatWSC2960LSM24PQ_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM24PQ = _CiscoCatWSC2960LSM24PQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2816)
)
_CiscoCatWSC2960LSM48PQ_ObjectIdentity = ObjectIdentity
ciscoCatWSC2960LSM48PQ = _CiscoCatWSC2960LSM48PQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2817)
)
_CiscoC850012X4QC_ObjectIdentity = ObjectIdentity
ciscoC850012X4QC = _CiscoC850012X4QC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2818)
)
_CiscoC850012X_ObjectIdentity = ObjectIdentity
ciscoC850012X = _CiscoC850012X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2819)
)
_CiscoC9592PLteGB_ObjectIdentity = ObjectIdentity
ciscoC9592PLteGB = _CiscoC9592PLteGB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2820)
)
_CiscoC9592PLteUS_ObjectIdentity = ObjectIdentity
ciscoC9592PLteUS = _CiscoC9592PLteUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2821)
)
_CiscoC9592PLteVZ_ObjectIdentity = ObjectIdentity
ciscoC9592PLteVZ = _CiscoC9592PLteVZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2822)
)
_CiscoC9592PLteIN_ObjectIdentity = ObjectIdentity
ciscoC9592PLteIN = _CiscoC9592PLteIN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2823)
)
_CiscoC9514P_ObjectIdentity = ObjectIdentity
ciscoC9514P = _CiscoC9514P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2824)
)
_CiscoCMeWlc_ObjectIdentity = ObjectIdentity
ciscoCMeWlc = _CiscoCMeWlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2825)
)
_CiscoIE34008FTMC_ObjectIdentity = ObjectIdentity
ciscoIE34008FTMC = _CiscoIE34008FTMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2826)
)
_CiscoIE340016FTMC_ObjectIdentity = ObjectIdentity
ciscoIE340016FTMC = _CiscoIE340016FTMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2827)
)
_CiscoIE340024FTMC_ObjectIdentity = ObjectIdentity
ciscoIE340024FTMC = _CiscoIE340024FTMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2828)
)
_CiscoIE34008TMC_ObjectIdentity = ObjectIdentity
ciscoIE34008TMC = _CiscoIE34008TMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2829)
)
_CiscoIE340016TMC_ObjectIdentity = ObjectIdentity
ciscoIE340016TMC = _CiscoIE340016TMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2830)
)
_CiscoIE340024TMC_ObjectIdentity = ObjectIdentity
ciscoIE340024TMC = _CiscoIE340024TMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2831)
)
_CiscoCat930024UBX_ObjectIdentity = ObjectIdentity
ciscoCat930024UBX = _CiscoCat930024UBX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2833)
)
_CiscoCat930048UB_ObjectIdentity = ObjectIdentity
ciscoCat930048UB = _CiscoCat930048UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2834)
)
_CiscoCat930024UB_ObjectIdentity = ObjectIdentity
ciscoCat930024UB = _CiscoCat930024UB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2835)
)
_CiscoC9115AXI_ObjectIdentity = ObjectIdentity
ciscoC9115AXI = _CiscoC9115AXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2839)
)
_CiscoC9115AXME_ObjectIdentity = ObjectIdentity
ciscoC9115AXME = _CiscoC9115AXME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2840)
)
_CiscoC9117AXME_ObjectIdentity = ObjectIdentity
ciscoC9117AXME = _CiscoC9117AXME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2841)
)
_CiscoC9117AXI_ObjectIdentity = ObjectIdentity
ciscoC9117AXI = _CiscoC9117AXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2842)
)
_CiscoNCS5064_ObjectIdentity = ObjectIdentity
ciscoNCS5064 = _CiscoNCS5064_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2843)
)
_CiscoESR1115CONK9_ObjectIdentity = ObjectIdentity
ciscoESR1115CONK9 = _CiscoESR1115CONK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2844)
)
_CiscoESR1115NCPK9_ObjectIdentity = ObjectIdentity
ciscoESR1115NCPK9 = _CiscoESR1115NCPK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2845)
)
_CiscoC9115AXE_ObjectIdentity = ObjectIdentity
ciscoC9115AXE = _CiscoC9115AXE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2846)
)
_CiscoC9120AXI_ObjectIdentity = ObjectIdentity
ciscoC9120AXI = _CiscoC9120AXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2849)
)
_CiscoC9120AXME_ObjectIdentity = ObjectIdentity
ciscoC9120AXME = _CiscoC9120AXME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2850)
)
_CiscoC9120AXE_ObjectIdentity = ObjectIdentity
ciscoC9120AXE = _CiscoC9120AXE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2851)
)
_CiscoC9120AXEME_ObjectIdentity = ObjectIdentity
ciscoC9120AXEME = _CiscoC9120AXEME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2852)
)
_CiscoN5604_ObjectIdentity = ObjectIdentity
ciscoN5604 = _CiscoN5604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2853)
)
_CiscoN5604CC_ObjectIdentity = ObjectIdentity
ciscoN5604CC = _CiscoN5604CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2854)
)
_CiscoN5604RSP4_ObjectIdentity = ObjectIdentity
ciscoN5604RSP4 = _CiscoN5604RSP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2855)
)
_CiscoN5604RSP4E_ObjectIdentity = ObjectIdentity
ciscoN5604RSP4E = _CiscoN5604RSP4E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2856)
)
_CiscoN5604RSP4CC_ObjectIdentity = ObjectIdentity
ciscoN5604RSP4CC = _CiscoN5604RSP4CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2857)
)
_CiscoN5604RSP4ECC_ObjectIdentity = ObjectIdentity
ciscoN5604RSP4ECC = _CiscoN5604RSP4ECC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2858)
)
_CiscoC9800LCK9_ObjectIdentity = ObjectIdentity
ciscoC9800LCK9 = _CiscoC9800LCK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2860)
)
_CiscoC9800LFK9_ObjectIdentity = ObjectIdentity
ciscoC9800LFK9 = _CiscoC9800LFK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2861)
)
_CiscoESR6300CONK9_ObjectIdentity = ObjectIdentity
ciscoESR6300CONK9 = _CiscoESR6300CONK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2864)
)
_CiscoESR6300NCPK9_ObjectIdentity = ObjectIdentity
ciscoESR6300NCPK9 = _CiscoESR6300NCPK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2865)
)
_CiscoNCS55A148Q6H_ObjectIdentity = ObjectIdentity
ciscoNCS55A148Q6H = _CiscoNCS55A148Q6H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2866)
)
_CiscoNCS55A148T6H_ObjectIdentity = ObjectIdentity
ciscoNCS55A148T6H = _CiscoNCS55A148T6H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2867)
)
_CiscoCMICR4PS_ObjectIdentity = ObjectIdentity
ciscoCMICR4PS = _CiscoCMICR4PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2868)
)
_CiscoCMICR4PC_ObjectIdentity = ObjectIdentity
ciscoCMICR4PC = _CiscoCMICR4PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2869)
)
_CiscoFpr1150td_ObjectIdentity = ObjectIdentity
ciscoFpr1150td = _CiscoFpr1150td_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2870)
)
_CiscoC9606RVirtualStack_ObjectIdentity = ObjectIdentity
ciscoC9606RVirtualStack = _CiscoC9606RVirtualStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2871)
)
_CiscoIE34008T2S_ObjectIdentity = ObjectIdentity
ciscoIE34008T2S = _CiscoIE34008T2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2872)
)
_CiscoCat930024H_ObjectIdentity = ObjectIdentity
ciscoCat930024H = _CiscoCat930024H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2873)
)
_CiscoCat930048H_ObjectIdentity = ObjectIdentity
ciscoCat930048H = _CiscoCat930048H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2874)
)
_CiscoC9130AXI_ObjectIdentity = ObjectIdentity
ciscoC9130AXI = _CiscoC9130AXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2877)
)
_CiscoC9130AXIME_ObjectIdentity = ObjectIdentity
ciscoC9130AXIME = _CiscoC9130AXIME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2878)
)
_CiscoC9130AXE_ObjectIdentity = ObjectIdentity
ciscoC9130AXE = _CiscoC9130AXE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2879)
)
_CiscoC9130AXEME_ObjectIdentity = ObjectIdentity
ciscoC9130AXEME = _CiscoC9130AXEME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2880)
)
_CiscoIE3400H8FT_ObjectIdentity = ObjectIdentity
ciscoIE3400H8FT = _CiscoIE3400H8FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2881)
)
_CiscoIE3400H16FT_ObjectIdentity = ObjectIdentity
ciscoIE3400H16FT = _CiscoIE3400H16FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2882)
)
_CiscoIE3400H24FT_ObjectIdentity = ObjectIdentity
ciscoIE3400H24FT = _CiscoIE3400H24FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2883)
)
_CiscoIE3400H8T_ObjectIdentity = ObjectIdentity
ciscoIE3400H8T = _CiscoIE3400H8T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2884)
)
_CiscoIE3400H16T_ObjectIdentity = ObjectIdentity
ciscoIE3400H16T = _CiscoIE3400H16T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2885)
)
_CiscoIE3400H24T_ObjectIdentity = ObjectIdentity
ciscoIE3400H24T = _CiscoIE3400H24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2886)
)
_CiscoENCS5104_ObjectIdentity = ObjectIdentity
ciscoENCS5104 = _CiscoENCS5104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2889)
)
_CiscoRAIE1783MMS10A_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10A = _CiscoRAIE1783MMS10A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2891)
)
_CiscoRAIE1783MMS10AR_ObjectIdentity = ObjectIdentity
ciscoRAIE1783MMS10AR = _CiscoRAIE1783MMS10AR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2892)
)
_CiscoENCS510464_ObjectIdentity = ObjectIdentity
ciscoENCS510464 = _CiscoENCS510464_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2893)
)
_CiscoENCS5104200_ObjectIdentity = ObjectIdentity
ciscoENCS5104200 = _CiscoENCS5104200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2894)
)
_CiscoENCS5104400_ObjectIdentity = ObjectIdentity
ciscoENCS5104400 = _CiscoENCS5104400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2895)
)
_CiscoC10008T2GL_ObjectIdentity = ObjectIdentity
ciscoC10008T2GL = _CiscoC10008T2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2896)
)
_CiscoCat100010GbpsStack_ObjectIdentity = ObjectIdentity
ciscoCat100010GbpsStack = _CiscoCat100010GbpsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2897)
)
_CiscoAIRIW6300ME_ObjectIdentity = ObjectIdentity
ciscoAIRIW6300ME = _CiscoAIRIW6300ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2898)
)
_CiscoFpr4112K9_ObjectIdentity = ObjectIdentity
ciscoFpr4112K9 = _CiscoFpr4112K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2899)
)
_CiscoCSP5200_ObjectIdentity = ObjectIdentity
ciscoCSP5200 = _CiscoCSP5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2900)
)
_CiscoCSP5216_ObjectIdentity = ObjectIdentity
ciscoCSP5216 = _CiscoCSP5216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2901)
)
_CiscoCSP5228_ObjectIdentity = ObjectIdentity
ciscoCSP5228 = _CiscoCSP5228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2902)
)
_CiscoCSP5400_ObjectIdentity = ObjectIdentity
ciscoCSP5400 = _CiscoCSP5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2903)
)
_CiscoCSP5436_ObjectIdentity = ObjectIdentity
ciscoCSP5436 = _CiscoCSP5436_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2904)
)
_CiscoCSP5444_ObjectIdentity = ObjectIdentity
ciscoCSP5444 = _CiscoCSP5444_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2905)
)
_CiscoCSP5456_ObjectIdentity = ObjectIdentity
ciscoCSP5456 = _CiscoCSP5456_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2906)
)
_CiscoCat920024PB_ObjectIdentity = ObjectIdentity
ciscoCat920024PB = _CiscoCat920024PB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2907)
)
_CiscoCat920048PB_ObjectIdentity = ObjectIdentity
ciscoCat920048PB = _CiscoCat920048PB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2908)
)
_CiscoC10008TE2GL_ObjectIdentity = ObjectIdentity
ciscoC10008TE2GL = _CiscoC10008TE2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2909)
)
_CiscoC10008P2GL_ObjectIdentity = ObjectIdentity
ciscoC10008P2GL = _CiscoC10008P2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2910)
)
_CiscoC10008PE2GL_ObjectIdentity = ObjectIdentity
ciscoC10008PE2GL = _CiscoC10008PE2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2911)
)
_CiscoC10008FP2GL_ObjectIdentity = ObjectIdentity
ciscoC10008FP2GL = _CiscoC10008FP2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2912)
)
_CiscoC10008FPE2GL_ObjectIdentity = ObjectIdentity
ciscoC10008FPE2GL = _CiscoC10008FPE2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2913)
)
_CiscoC100016T2GL_ObjectIdentity = ObjectIdentity
ciscoC100016T2GL = _CiscoC100016T2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2914)
)
_CiscoC100016TE2GL_ObjectIdentity = ObjectIdentity
ciscoC100016TE2GL = _CiscoC100016TE2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2915)
)
_CiscoC100016P2GL_ObjectIdentity = ObjectIdentity
ciscoC100016P2GL = _CiscoC100016P2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2916)
)
_CiscoC100016PE2GL_ObjectIdentity = ObjectIdentity
ciscoC100016PE2GL = _CiscoC100016PE2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2917)
)
_CiscoC100016FP2GL_ObjectIdentity = ObjectIdentity
ciscoC100016FP2GL = _CiscoC100016FP2GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2918)
)
_CiscoC100024T4GL_ObjectIdentity = ObjectIdentity
ciscoC100024T4GL = _CiscoC100024T4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2919)
)
_CiscoC100024PP4GL_ObjectIdentity = ObjectIdentity
ciscoC100024PP4GL = _CiscoC100024PP4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2920)
)
_CiscoC100024P4GL_ObjectIdentity = ObjectIdentity
ciscoC100024P4GL = _CiscoC100024P4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2921)
)
_CiscoC100024FP4GL_ObjectIdentity = ObjectIdentity
ciscoC100024FP4GL = _CiscoC100024FP4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2922)
)
_CiscoC100048T4GL_ObjectIdentity = ObjectIdentity
ciscoC100048T4GL = _CiscoC100048T4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2923)
)
_CiscoC100048PP4GL_ObjectIdentity = ObjectIdentity
ciscoC100048PP4GL = _CiscoC100048PP4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2924)
)
_CiscoC100048P4GL_ObjectIdentity = ObjectIdentity
ciscoC100048P4GL = _CiscoC100048P4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2925)
)
_CiscoC100048FP4GL_ObjectIdentity = ObjectIdentity
ciscoC100048FP4GL = _CiscoC100048FP4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2926)
)
_CiscoC100024T4XL_ObjectIdentity = ObjectIdentity
ciscoC100024T4XL = _CiscoC100024T4XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2927)
)
_CiscoC100024P4XL_ObjectIdentity = ObjectIdentity
ciscoC100024P4XL = _CiscoC100024P4XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2928)
)
_CiscoC100024FP4XL_ObjectIdentity = ObjectIdentity
ciscoC100024FP4XL = _CiscoC100024FP4XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2929)
)
_CiscoC100048T4XL_ObjectIdentity = ObjectIdentity
ciscoC100048T4XL = _CiscoC100048T4XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2930)
)
_CiscoC100048P4XL_ObjectIdentity = ObjectIdentity
ciscoC100048P4XL = _CiscoC100048P4XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2931)
)
_CiscoC100048FP4XL_ObjectIdentity = ObjectIdentity
ciscoC100048FP4XL = _CiscoC100048FP4XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2932)
)
_CiscoMobilityExpress_ObjectIdentity = ObjectIdentity
ciscoMobilityExpress = _CiscoMobilityExpress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2958)
)
_CiscoCat10001GbpsStack_ObjectIdentity = ObjectIdentity
ciscoCat10001GbpsStack = _CiscoCat10001GbpsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2959)
)
_CiscoC82001N4T_ObjectIdentity = ObjectIdentity
ciscoC82001N4T = _CiscoC82001N4T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2961)
)
_CiscoC8200L4G_ObjectIdentity = ObjectIdentity
ciscoC8200L4G = _CiscoC8200L4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2962)
)
_CiscoC83002N2S4T2X_ObjectIdentity = ObjectIdentity
ciscoC83002N2S4T2X = _CiscoC83002N2S4T2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2963)
)
_CiscoC83002N2S6T_ObjectIdentity = ObjectIdentity
ciscoC83002N2S6T = _CiscoC83002N2S6T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2964)
)
_CiscoCat9200BFixedSwitchStack_ObjectIdentity = ObjectIdentity
ciscoCat9200BFixedSwitchStack = _CiscoCat9200BFixedSwitchStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2965)
)
_CiscoESW6300ME_ObjectIdentity = ObjectIdentity
ciscoESW6300ME = _CiscoESW6300ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2966)
)
_CiscoC8500L8G4X_ObjectIdentity = ObjectIdentity
ciscoC8500L8G4X = _CiscoC8500L8G4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2968)
)
_CiscoC1100TG1N32A_ObjectIdentity = ObjectIdentity
ciscoC1100TG1N32A = _CiscoC1100TG1N32A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2971)
)
_CiscoC1100TG1N24P32A_ObjectIdentity = ObjectIdentity
ciscoC1100TG1N24P32A = _CiscoC1100TG1N24P32A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2972)
)
_CiscoC1100TGX1N24P32A_ObjectIdentity = ObjectIdentity
ciscoC1100TGX1N24P32A = _CiscoC1100TGX1N24P32A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2973)
)
_CiscoCMICR4PT_ObjectIdentity = ObjectIdentity
ciscoCMICR4PT = _CiscoCMICR4PT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2978)
)
_CiscoNCS540L28Z4SysA_ObjectIdentity = ObjectIdentity
ciscoNCS540L28Z4SysA = _CiscoNCS540L28Z4SysA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2981)
)
_CiscoNCS540L28Z4SysD_ObjectIdentity = ObjectIdentity
ciscoNCS540L28Z4SysD = _CiscoNCS540L28Z4SysD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2982)
)
_CiscoNCS540L16Z4G8Q2CA_ObjectIdentity = ObjectIdentity
ciscoNCS540L16Z4G8Q2CA = _CiscoNCS540L16Z4G8Q2CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2983)
)
_CiscoNCS540L16Z4G8Q2CD_ObjectIdentity = ObjectIdentity
ciscoNCS540L16Z4G8Q2CD = _CiscoNCS540L16Z4G8Q2CD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2984)
)
_CiscoNCS540L12Z20GSysA_ObjectIdentity = ObjectIdentity
ciscoNCS540L12Z20GSysA = _CiscoNCS540L12Z20GSysA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2985)
)
_CiscoNCS540L12Z20GSysD_ObjectIdentity = ObjectIdentity
ciscoNCS540L12Z20GSysD = _CiscoNCS540L12Z20GSysD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2986)
)
_CiscoNCS540L12Z16GSysA_ObjectIdentity = ObjectIdentity
ciscoNCS540L12Z16GSysA = _CiscoNCS540L12Z16GSysA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2987)
)
_CiscoNCS540L12Z16GSysD_ObjectIdentity = ObjectIdentity
ciscoNCS540L12Z16GSysD = _CiscoNCS540L12Z16GSysD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2988)
)
_CiscoC83001N1S6T_ObjectIdentity = ObjectIdentity
ciscoC83001N1S6T = _CiscoC83001N1S6T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2989)
)
_CiscoC83001N1S4T2X_ObjectIdentity = ObjectIdentity
ciscoC83001N1S4T2X = _CiscoC83001N1S4T2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2990)
)
_CiscoFpr4112SM12_ObjectIdentity = ObjectIdentity
ciscoFpr4112SM12 = _CiscoFpr4112SM12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2991)
)
_CiscoCat9300L48PF4X_ObjectIdentity = ObjectIdentity
ciscoCat9300L48PF4X = _CiscoCat9300L48PF4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2992)
)
_CiscoCat9300L48PF4G_ObjectIdentity = ObjectIdentity
ciscoCat9300L48PF4G = _CiscoCat9300L48PF4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2993)
)
_CiscoNCS540LFHCSRSys_ObjectIdentity = ObjectIdentity
ciscoNCS540LFHCSRSys = _CiscoNCS540LFHCSRSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3001)
)
_CiscoNCS540LFHAGGSys_ObjectIdentity = ObjectIdentity
ciscoNCS540LFHAGGSys = _CiscoNCS540LFHAGGSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3002)
)
_CiscoNCS540LFHIP65Sys_ObjectIdentity = ObjectIdentity
ciscoNCS540LFHIP65Sys = _CiscoNCS540LFHIP65Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3003)
)
_CiscoC8000V_ObjectIdentity = ObjectIdentity
ciscoC8000V = _CiscoC8000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3004)
)
_CiscoIE33008T2X_ObjectIdentity = ObjectIdentity
ciscoIE33008T2X = _CiscoIE33008T2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3007)
)
_CiscoIE33008U2X_ObjectIdentity = ObjectIdentity
ciscoIE33008U2X = _CiscoIE33008U2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3008)
)
_CiscoNCS54016G_ObjectIdentity = ObjectIdentity
ciscoNCS54016G = _CiscoNCS54016G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3009)
)
_CiscoNCS540X16G_ObjectIdentity = ObjectIdentity
ciscoNCS540X16G = _CiscoNCS540X16G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3010)
)
_CiscoCat920048PL_ObjectIdentity = ObjectIdentity
ciscoCat920048PL = _CiscoCat920048PL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3011)
)
_CiscoC9200L48PL4G_ObjectIdentity = ObjectIdentity
ciscoC9200L48PL4G = _CiscoC9200L48PL4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3012)
)
_CiscoC9200L48PL4X_ObjectIdentity = ObjectIdentity
ciscoC9200L48PL4X = _CiscoC9200L48PL4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3013)
)
_CiscoISR11004G_ObjectIdentity = ObjectIdentity
ciscoISR11004G = _CiscoISR11004G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3016)
)
_CiscoISR11006G_ObjectIdentity = ObjectIdentity
ciscoISR11006G = _CiscoISR11006G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3017)
)
_CiscoISR11004GLTEGB_ObjectIdentity = ObjectIdentity
ciscoISR11004GLTEGB = _CiscoISR11004GLTEGB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3018)
)
_CiscoISR11004GLTENA_ObjectIdentity = ObjectIdentity
ciscoISR11004GLTENA = _CiscoISR11004GLTENA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3019)
)
_CiscoC1000FE24T4GL_ObjectIdentity = ObjectIdentity
ciscoC1000FE24T4GL = _CiscoC1000FE24T4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3021)
)
_CiscoC1000FE24P4GL_ObjectIdentity = ObjectIdentity
ciscoC1000FE24P4GL = _CiscoC1000FE24P4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3022)
)
_CiscoC1000FE48T4GL_ObjectIdentity = ObjectIdentity
ciscoC1000FE48T4GL = _CiscoC1000FE48T4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3023)
)
_CiscoC1000FE48P4GL_ObjectIdentity = ObjectIdentity
ciscoC1000FE48P4GL = _CiscoC1000FE48P4GL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3024)
)
_CiscoDNAPLTTA1X_ObjectIdentity = ObjectIdentity
ciscoDNAPLTTA1X = _CiscoDNAPLTTA1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3025)
)
_CiscoIR1821K9_ObjectIdentity = ObjectIdentity
ciscoIR1821K9 = _CiscoIR1821K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3026)
)
_CiscoIR1831K9_ObjectIdentity = ObjectIdentity
ciscoIR1831K9 = _CiscoIR1831K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3027)
)
_CiscoIR1833K9_ObjectIdentity = ObjectIdentity
ciscoIR1833K9 = _CiscoIR1833K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3028)
)
_CiscoIR1835K9_ObjectIdentity = ObjectIdentity
ciscoIR1835K9 = _CiscoIR1835K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3029)
)
_CiscoNCS540L6Z18GSysA_ObjectIdentity = ObjectIdentity
ciscoNCS540L6Z18GSysA = _CiscoNCS540L6Z18GSysA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3030)
)
_CiscoNCS540L6Z18GSysD_ObjectIdentity = ObjectIdentity
ciscoNCS540L6Z18GSysD = _CiscoNCS540L6Z18GSysD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3031)
)
_CiscoNCS540L8Z16GSysD_ObjectIdentity = ObjectIdentity
ciscoNCS540L8Z16GSysD = _CiscoNCS540L8Z16GSysD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3032)
)
_CiscoNCS540L8Z16GSysA_ObjectIdentity = ObjectIdentity
ciscoNCS540L8Z16GSysA = _CiscoNCS540L8Z16GSysA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3033)
)
_CiscoNCS540L4Z14G2QA_ObjectIdentity = ObjectIdentity
ciscoNCS540L4Z14G2QA = _CiscoNCS540L4Z14G2QA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3034)
)
_CiscoNCS540L4Z14G2QD_ObjectIdentity = ObjectIdentity
ciscoNCS540L4Z14G2QD = _CiscoNCS540L4Z14G2QD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3035)
)
_CiscoC9300X12Y_ObjectIdentity = ObjectIdentity
ciscoC9300X12Y = _CiscoC9300X12Y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3037)
)
_CiscoC9300X24Y_ObjectIdentity = ObjectIdentity
ciscoC9300X24Y = _CiscoC9300X24Y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3038)
)
_CiscoC9300X48HX_ObjectIdentity = ObjectIdentity
ciscoC9300X48HX = _CiscoC9300X48HX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3039)
)
_CiscoC9300X48TX_ObjectIdentity = ObjectIdentity
ciscoC9300X48TX = _CiscoC9300X48TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3040)
)
_CiscoISR1100X4G_ObjectIdentity = ObjectIdentity
ciscoISR1100X4G = _CiscoISR1100X4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3045)
)
_CiscoISR1100X6G_ObjectIdentity = ObjectIdentity
ciscoISR1100X6G = _CiscoISR1100X6G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3046)
)
_CiscoESS930010XE_ObjectIdentity = ObjectIdentity
ciscoESS930010XE = _CiscoESS930010XE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3047)
)
_CiscoIR8140HK9_ObjectIdentity = ObjectIdentity
ciscoIR8140HK9 = _CiscoIR8140HK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3048)
)
_CiscoIR8140HPK9_ObjectIdentity = ObjectIdentity
ciscoIR8140HPK9 = _CiscoIR8140HPK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3049)
)
_CiscoC9115AXEME_ObjectIdentity = ObjectIdentity
ciscoC9115AXEME = _CiscoC9115AXEME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3050)
)
_CiscoC9120AXPME_ObjectIdentity = ObjectIdentity
ciscoC9120AXPME = _CiscoC9120AXPME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3051)
)
_CiscoIR8340K9_ObjectIdentity = ObjectIdentity
ciscoIR8340K9 = _CiscoIR8340K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3052)
)
_CiscoFpr3110K9_ObjectIdentity = ObjectIdentity
ciscoFpr3110K9 = _CiscoFpr3110K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3053)
)
_CiscoFpr3120K9_ObjectIdentity = ObjectIdentity
ciscoFpr3120K9 = _CiscoFpr3120K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3054)
)
_CiscoFpr3130K9_ObjectIdentity = ObjectIdentity
ciscoFpr3130K9 = _CiscoFpr3130K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3055)
)
_CiscoFpr3140K9_ObjectIdentity = ObjectIdentity
ciscoFpr3140K9 = _CiscoFpr3140K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3056)
)
_CiscoC9KF1SSD960G_ObjectIdentity = ObjectIdentity
ciscoC9KF1SSD960G = _CiscoC9KF1SSD960G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3062)
)
_CiscoC9KF1SSD480G_ObjectIdentity = ObjectIdentity
ciscoC9KF1SSD480G = _CiscoC9KF1SSD480G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3063)
)
_CiscoC9KF1SSD240G_ObjectIdentity = ObjectIdentity
ciscoC9KF1SSD240G = _CiscoC9KF1SSD240G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3064)
)
_CiscoC8500L8S4X_ObjectIdentity = ObjectIdentity
ciscoC8500L8S4X = _CiscoC8500L8S4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3069)
)
_CiscoC11138PLteEAWA_ObjectIdentity = ObjectIdentity
ciscoC11138PLteEAWA = _CiscoC11138PLteEAWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3070)
)
_CiscoVG420144FXS_ObjectIdentity = ObjectIdentity
ciscoVG420144FXS = _CiscoVG420144FXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3071)
)
_CiscoVG420132FXS6FXO_ObjectIdentity = ObjectIdentity
ciscoVG420132FXS6FXO = _CiscoVG420132FXS6FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3072)
)
_CiscoVG42084FXS6FXO_ObjectIdentity = ObjectIdentity
ciscoVG42084FXS6FXO = _CiscoVG42084FXS6FXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3073)
)
_CiscoC8200L1N4T_ObjectIdentity = ObjectIdentity
ciscoC8200L1N4T = _CiscoC8200L1N4T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3074)
)
_CiscoASR9903_ObjectIdentity = ObjectIdentity
ciscoASR9903 = _CiscoASR9903_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3075)
)
_CiscoNCS57B15DSESys_ObjectIdentity = ObjectIdentity
ciscoNCS57B15DSESys = _CiscoNCS57B15DSESys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3076)
)
_CiscoNCS57B16D24Sys_ObjectIdentity = ObjectIdentity
ciscoNCS57B16D24Sys = _CiscoNCS57B16D24Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3077)
)
_CiscoCat9200CX12T2X2G_ObjectIdentity = ObjectIdentity
ciscoCat9200CX12T2X2G = _CiscoCat9200CX12T2X2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3078)
)
_CiscoCat9200CX12P2X2G_ObjectIdentity = ObjectIdentity
ciscoCat9200CX12P2X2G = _CiscoCat9200CX12P2X2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3079)
)
_CiscoCat9500X28C8D_ObjectIdentity = ObjectIdentity
ciscoCat9500X28C8D = _CiscoCat9500X28C8D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3084)
)
_CiscoC850020X6C_ObjectIdentity = ObjectIdentity
ciscoC850020X6C = _CiscoC850020X6C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3085)
)
_CiscoC9300X48HXN_ObjectIdentity = ObjectIdentity
ciscoC9300X48HXN = _CiscoC9300X48HXN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3086)
)
_CiscoC9300X24HX_ObjectIdentity = ObjectIdentity
ciscoC9300X24HX = _CiscoC9300X24HX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3087)
)
_CiscoXRdControlPlaneC1_ObjectIdentity = ObjectIdentity
ciscoXRdControlPlaneC1 = _CiscoXRdControlPlaneC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3089)
)
_CiscoASR9902_ObjectIdentity = ObjectIdentity
ciscoASR9902 = _CiscoASR9902_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3090)
)
_CiscoCat9200CX8P2X2G_ObjectIdentity = ObjectIdentity
ciscoCat9200CX8P2X2G = _CiscoCat9200CX8P2X2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3097)
)
_CiscoCat9200CX8PT2G_ObjectIdentity = ObjectIdentity
ciscoCat9200CX8PT2G = _CiscoCat9200CX8PT2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3098)
)
_CiscoCat9200CX8UXG2X_ObjectIdentity = ObjectIdentity
ciscoCat9200CX8UXG2X = _CiscoCat9200CX8UXG2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3099)
)
_CiscoUCSC220M6_ObjectIdentity = ObjectIdentity
ciscoUCSC220M6 = _CiscoUCSC220M6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3100)
)
_CiscoUCSC240M6_ObjectIdentity = ObjectIdentity
ciscoUCSC240M6 = _CiscoUCSC240M6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3101)
)
_CiscoUCSB200M5_ObjectIdentity = ObjectIdentity
ciscoUCSB200M5 = _CiscoUCSB200M5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3103)
)
_CiscoUCSB480M5_ObjectIdentity = ObjectIdentity
ciscoUCSB480M5 = _CiscoUCSB480M5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3104)
)
_CiscoC11318PWE_ObjectIdentity = ObjectIdentity
ciscoC11318PWE = _CiscoC11318PWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3105)
)
_CiscoC11318PWA_ObjectIdentity = ObjectIdentity
ciscoC11318PWA = _CiscoC11318PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3106)
)
_CiscoC11318PWB_ObjectIdentity = ObjectIdentity
ciscoC11318PWB = _CiscoC11318PWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3107)
)
_CiscoC11318PWZ_ObjectIdentity = ObjectIdentity
ciscoC11318PWZ = _CiscoC11318PWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3108)
)
_CiscoC11318PWQ_ObjectIdentity = ObjectIdentity
ciscoC11318PWQ = _CiscoC11318PWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3109)
)
_CiscoC1131X8PWE_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWE = _CiscoC1131X8PWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3110)
)
_CiscoC1131X8PWA_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWA = _CiscoC1131X8PWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3111)
)
_CiscoC1131X8PWB_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWB = _CiscoC1131X8PWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3112)
)
_CiscoC1131X8PWZ_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWZ = _CiscoC1131X8PWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3113)
)
_CiscoC1131X8PWQ_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWQ = _CiscoC1131X8PWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3114)
)
_CiscoC11318PLTEPWB_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWB = _CiscoC11318PLTEPWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3115)
)
_CiscoC1131X8PLTEPWE_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWE = _CiscoC1131X8PLTEPWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3116)
)
_CiscoC1131X8PLTEPWA_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWA = _CiscoC1131X8PLTEPWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3117)
)
_CiscoC11318PLTEPWA_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWA = _CiscoC11318PLTEPWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3118)
)
_CiscoC11318PLTEPWZ_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWZ = _CiscoC11318PLTEPWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3119)
)
_CiscoC11318PLTEPWQ_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWQ = _CiscoC11318PLTEPWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3120)
)
_CiscoC11318PLTEPWE_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWE = _CiscoC11318PLTEPWE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3121)
)
_CiscoC1131X8PLTEPWZ_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWZ = _CiscoC1131X8PLTEPWZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3122)
)
_CiscoC1131X8PLTEPWB_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWB = _CiscoC1131X8PLTEPWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3123)
)
_CiscoC1131X8PLTEPWQ_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWQ = _CiscoC1131X8PLTEPWQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3124)
)
_CiscoIE931026S2C_ObjectIdentity = ObjectIdentity
ciscoIE931026S2C = _CiscoIE931026S2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3129)
)
_CiscoIE9320stack_ObjectIdentity = ObjectIdentity
ciscoIE9320stack = _CiscoIE9320stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3130)
)
_CiscoIC30002C2FK9_ObjectIdentity = ObjectIdentity
ciscoIC30002C2FK9 = _CiscoIC30002C2FK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3135)
)
_CiscoUCSIOM2208_ObjectIdentity = ObjectIdentity
ciscoUCSIOM2208 = _CiscoUCSIOM2208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3138)
)
_CiscoUCSIOM2304_ObjectIdentity = ObjectIdentity
ciscoUCSIOM2304 = _CiscoUCSIOM2304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3139)
)
_CiscoUCSIOM2408_ObjectIdentity = ObjectIdentity
ciscoUCSIOM2408 = _CiscoUCSIOM2408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3140)
)
_CiscoUCSBXI910825G_ObjectIdentity = ObjectIdentity
ciscoUCSBXI910825G = _CiscoUCSBXI910825G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3141)
)
_CiscoUCSBXI9108100G_ObjectIdentity = ObjectIdentity
ciscoUCSBXI9108100G = _CiscoUCSBXI9108100G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3142)
)
_CiscoNCS540L24Q8L2DDSys_ObjectIdentity = ObjectIdentity
ciscoNCS540L24Q8L2DDSys = _CiscoNCS540L24Q8L2DDSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3143)
)
_Cisco810132FH_ObjectIdentity = ObjectIdentity
cisco810132FH = _Cisco810132FH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3144)
)
_CiscoISRAP1101AX_ObjectIdentity = ObjectIdentity
ciscoISRAP1101AX = _CiscoISRAP1101AX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3145)
)
_CiscoNCS55A124Q6HSS_ObjectIdentity = ObjectIdentity
ciscoNCS55A124Q6HSS = _CiscoNCS55A124Q6HSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3146)
)
_CiscoNCS57C3MODSSYS_ObjectIdentity = ObjectIdentity
ciscoNCS57C3MODSSYS = _CiscoNCS57C3MODSSYS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3147)
)
_CiscoNCS57C3MODSYS_ObjectIdentity = ObjectIdentity
ciscoNCS57C3MODSYS = _CiscoNCS57C3MODSYS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3148)
)
_Cisco811132EH_ObjectIdentity = ObjectIdentity
cisco811132EH = _Cisco811132EH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3149)
)
_Cisco820232FHM_ObjectIdentity = ObjectIdentity
cisco820232FHM = _Cisco820232FHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3150)
)
_Cisco820232FHMO_ObjectIdentity = ObjectIdentity
cisco820232FHMO = _Cisco820232FHMO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3151)
)
_CiscoNCS1010_ObjectIdentity = ObjectIdentity
ciscoNCS1010 = _CiscoNCS1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3153)
)
_CiscoNCS57C148Q6Sys_ObjectIdentity = ObjectIdentity
ciscoNCS57C148Q6Sys = _CiscoNCS57C148Q6Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3154)
)
_CiscoNCS55A124Q6HS_ObjectIdentity = ObjectIdentity
ciscoNCS55A124Q6HS = _CiscoNCS55A124Q6HS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3158)
)
_CiscoNCS540L6Z14GSysD_ObjectIdentity = ObjectIdentity
ciscoNCS540L6Z14GSysD = _CiscoNCS540L6Z14GSysD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3163)
)
_CiscoC9200CX12P2XGH_ObjectIdentity = ObjectIdentity
ciscoC9200CX12P2XGH = _CiscoC9200CX12P2XGH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3164)
)
_CiscoIE932026S2C_ObjectIdentity = ObjectIdentity
ciscoIE932026S2C = _CiscoIE932026S2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3165)
)
_CiscoFpr3105K9_ObjectIdentity = ObjectIdentity
ciscoFpr3105K9 = _CiscoFpr3105K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3166)
)
_CiscoUCSC225M6_ObjectIdentity = ObjectIdentity
ciscoUCSC225M6 = _CiscoUCSC225M6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3168)
)
_CiscoIE31004T2S_ObjectIdentity = ObjectIdentity
ciscoIE31004T2S = _CiscoIE31004T2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3169)
)
_CiscoIE31008T2C_ObjectIdentity = ObjectIdentity
ciscoIE31008T2C = _CiscoIE31008T2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3170)
)
_CiscoIE310018T2C_ObjectIdentity = ObjectIdentity
ciscoIE310018T2C = _CiscoIE310018T2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3171)
)
_CiscoIE31058T2C_ObjectIdentity = ObjectIdentity
ciscoIE31058T2C = _CiscoIE31058T2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3172)
)
_CiscoIE310518T2C_ObjectIdentity = ObjectIdentity
ciscoIE310518T2C = _CiscoIE310518T2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3173)
)
_CiscoRAIE1783CMS6B_ObjectIdentity = ObjectIdentity
ciscoRAIE1783CMS6B = _CiscoRAIE1783CMS6B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3174)
)
_CiscoRAIE1783CMS6P_ObjectIdentity = ObjectIdentity
ciscoRAIE1783CMS6P = _CiscoRAIE1783CMS6P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3175)
)
_CiscoRAIE1783CMS10B_ObjectIdentity = ObjectIdentity
ciscoRAIE1783CMS10B = _CiscoRAIE1783CMS10B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3176)
)
_CiscoRAIE1783CMS10P_ObjectIdentity = ObjectIdentity
ciscoRAIE1783CMS10P = _CiscoRAIE1783CMS10P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3177)
)
_CiscoRAIE1783CMS10DP_ObjectIdentity = ObjectIdentity
ciscoRAIE1783CMS10DP = _CiscoRAIE1783CMS10DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3178)
)
_CiscoRAIE1783CMS10DN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783CMS10DN = _CiscoRAIE1783CMS10DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3179)
)
_CiscoRAIE1783CMS20DB_ObjectIdentity = ObjectIdentity
ciscoRAIE1783CMS20DB = _CiscoRAIE1783CMS20DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3180)
)
_CiscoRAIE1783CMS20DP_ObjectIdentity = ObjectIdentity
ciscoRAIE1783CMS20DP = _CiscoRAIE1783CMS20DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3181)
)
_CiscoRAIE1783CMS20DN_ObjectIdentity = ObjectIdentity
ciscoRAIE1783CMS20DN = _CiscoRAIE1783CMS20DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3182)
)
_CiscoXRdvRouterC1_ObjectIdentity = ObjectIdentity
ciscoXRdvRouterC1 = _CiscoXRdvRouterC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3191)
)
_Cisco810132H_ObjectIdentity = ObjectIdentity
cisco810132H = _Cisco810132H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3192)
)
_Cisco810264H_ObjectIdentity = ObjectIdentity
cisco810264H = _Cisco810264H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3193)
)
_CiscoC9200CX8P2XGH_ObjectIdentity = ObjectIdentity
ciscoC9200CX8P2XGH = _CiscoC9200CX8P2XGH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3195)
)
_CiscoC9200CX8UXG2XH_ObjectIdentity = ObjectIdentity
ciscoC9200CX8UXG2XH = _CiscoC9200CX8UXG2XH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3196)
)
_CiscoESR6300LICK9_ObjectIdentity = ObjectIdentity
ciscoESR6300LICK9 = _CiscoESR6300LICK9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3197)
)
_CiscoDP01QSDDZF1_ObjectIdentity = ObjectIdentity
ciscoDP01QSDDZF1 = _CiscoDP01QSDDZF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3198)
)
_CiscoIE932022S2C4X_ObjectIdentity = ObjectIdentity
ciscoIE932022S2C4X = _CiscoIE932022S2C4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3199)
)
_CiscoIE932024T4X_ObjectIdentity = ObjectIdentity
ciscoIE932024T4X = _CiscoIE932024T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3200)
)
_CiscoIE932024P4X_ObjectIdentity = ObjectIdentity
ciscoIE932024P4X = _CiscoIE932024P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3201)
)
_CiscoIE932016P8U4X_ObjectIdentity = ObjectIdentity
ciscoIE932016P8U4X = _CiscoIE932016P8U4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3202)
)
_CiscoIE932024P4S_ObjectIdentity = ObjectIdentity
ciscoIE932024P4S = _CiscoIE932024P4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3203)
)
_CiscoIE31008T4S_ObjectIdentity = ObjectIdentity
ciscoIE31008T4S = _CiscoIE31008T4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3204)
)
_CiscoC8500L8S2X2Y_ObjectIdentity = ObjectIdentity
ciscoC8500L8S2X2Y = _CiscoC8500L8S2X2Y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3205)
)
_CiscoC8500L8S8X4Y_ObjectIdentity = ObjectIdentity
ciscoC8500L8S8X4Y = _CiscoC8500L8S8X4Y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3206)
)
_CiscoC8300UCPE1N20_ObjectIdentity = ObjectIdentity
ciscoC8300UCPE1N20 = _CiscoC8300UCPE1N20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3207)
)
_CiscoUCSC220M7_ObjectIdentity = ObjectIdentity
ciscoUCSC220M7 = _CiscoUCSC220M7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3208)
)
_CiscoUCSC240M7_ObjectIdentity = ObjectIdentity
ciscoUCSC240M7 = _CiscoUCSC240M7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3209)
)
_CiscoC12008TD_ObjectIdentity = ObjectIdentity
ciscoC12008TD = _CiscoC12008TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3210)
)
_CiscoC12008TE2G_ObjectIdentity = ObjectIdentity
ciscoC12008TE2G = _CiscoC12008TE2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3211)
)
_CiscoC12008PE2G_ObjectIdentity = ObjectIdentity
ciscoC12008PE2G = _CiscoC12008PE2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3212)
)
_CiscoC12008FP2G_ObjectIdentity = ObjectIdentity
ciscoC12008FP2G = _CiscoC12008FP2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3213)
)
_CiscoC120016T2G_ObjectIdentity = ObjectIdentity
ciscoC120016T2G = _CiscoC120016T2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3214)
)
_CiscoC120016P2G_ObjectIdentity = ObjectIdentity
ciscoC120016P2G = _CiscoC120016P2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3215)
)
_CiscoC120024T4G_ObjectIdentity = ObjectIdentity
ciscoC120024T4G = _CiscoC120024T4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3216)
)
_CiscoC120024P4G_ObjectIdentity = ObjectIdentity
ciscoC120024P4G = _CiscoC120024P4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3217)
)
_CiscoC120024FP4G_ObjectIdentity = ObjectIdentity
ciscoC120024FP4G = _CiscoC120024FP4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3218)
)
_CiscoC120048T4G_ObjectIdentity = ObjectIdentity
ciscoC120048T4G = _CiscoC120048T4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3219)
)
_CiscoC120048P4G_ObjectIdentity = ObjectIdentity
ciscoC120048P4G = _CiscoC120048P4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3220)
)
_CiscoC120024T4X_ObjectIdentity = ObjectIdentity
ciscoC120024T4X = _CiscoC120024T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3221)
)
_CiscoC120024P4X_ObjectIdentity = ObjectIdentity
ciscoC120024P4X = _CiscoC120024P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3222)
)
_CiscoC120024FP4X_ObjectIdentity = ObjectIdentity
ciscoC120024FP4X = _CiscoC120024FP4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3223)
)
_CiscoC120048T4X_ObjectIdentity = ObjectIdentity
ciscoC120048T4X = _CiscoC120048T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3224)
)
_CiscoC120048P4X_ObjectIdentity = ObjectIdentity
ciscoC120048P4X = _CiscoC120048P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3225)
)
_CiscoC13008TE2G_ObjectIdentity = ObjectIdentity
ciscoC13008TE2G = _CiscoC13008TE2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3226)
)
_CiscoC13008PE2G_ObjectIdentity = ObjectIdentity
ciscoC13008PE2G = _CiscoC13008PE2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3227)
)
_CiscoC13008FP2G_ObjectIdentity = ObjectIdentity
ciscoC13008FP2G = _CiscoC13008FP2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3228)
)
_CiscoC130016T2G_ObjectIdentity = ObjectIdentity
ciscoC130016T2G = _CiscoC130016T2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3229)
)
_CiscoC130016P2G_ObjectIdentity = ObjectIdentity
ciscoC130016P2G = _CiscoC130016P2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3230)
)
_CiscoC130016FP2G_ObjectIdentity = ObjectIdentity
ciscoC130016FP2G = _CiscoC130016FP2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3231)
)
_CiscoC130024T4G_ObjectIdentity = ObjectIdentity
ciscoC130024T4G = _CiscoC130024T4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3232)
)
_CiscoC130024P4G_ObjectIdentity = ObjectIdentity
ciscoC130024P4G = _CiscoC130024P4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3233)
)
_CiscoC130024FP4G_ObjectIdentity = ObjectIdentity
ciscoC130024FP4G = _CiscoC130024FP4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3234)
)
_CiscoC130048T4G_ObjectIdentity = ObjectIdentity
ciscoC130048T4G = _CiscoC130048T4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3235)
)
_CiscoC130048P4G_ObjectIdentity = ObjectIdentity
ciscoC130048P4G = _CiscoC130048P4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3236)
)
_CiscoC130048FP4G_ObjectIdentity = ObjectIdentity
ciscoC130048FP4G = _CiscoC130048FP4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3237)
)
_CiscoC130016P4X_ObjectIdentity = ObjectIdentity
ciscoC130016P4X = _CiscoC130016P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3238)
)
_CiscoC130024T4X_ObjectIdentity = ObjectIdentity
ciscoC130024T4X = _CiscoC130024T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3239)
)
_CiscoC130024P4X_ObjectIdentity = ObjectIdentity
ciscoC130024P4X = _CiscoC130024P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3240)
)
_CiscoC130024FP4X_ObjectIdentity = ObjectIdentity
ciscoC130024FP4X = _CiscoC130024FP4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3241)
)
_CiscoC130048T4X_ObjectIdentity = ObjectIdentity
ciscoC130048T4X = _CiscoC130048T4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3242)
)
_CiscoC130048P4X_ObjectIdentity = ObjectIdentity
ciscoC130048P4X = _CiscoC130048P4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3243)
)
_CiscoC130048FP4X_ObjectIdentity = ObjectIdentity
ciscoC130048FP4X = _CiscoC130048FP4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3244)
)
_CiscoC13008MGP2X_ObjectIdentity = ObjectIdentity
ciscoC13008MGP2X = _CiscoC13008MGP2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3245)
)
_CiscoC130024MGP4X_ObjectIdentity = ObjectIdentity
ciscoC130024MGP4X = _CiscoC130024MGP4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3246)
)
_CiscoC130048MGP4X_ObjectIdentity = ObjectIdentity
ciscoC130048MGP4X = _CiscoC130048MGP4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3247)
)
_CiscoC130012XT2X_ObjectIdentity = ObjectIdentity
ciscoC130012XT2X = _CiscoC130012XT2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3248)
)
_CiscoC130012XS_ObjectIdentity = ObjectIdentity
ciscoC130012XS = _CiscoC130012XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3249)
)
_CiscoC130024XT_ObjectIdentity = ObjectIdentity
ciscoC130024XT = _CiscoC130024XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3250)
)
_CiscoC130024XS_ObjectIdentity = ObjectIdentity
ciscoC130024XS = _CiscoC130024XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3251)
)
_CiscoC130016XTS_ObjectIdentity = ObjectIdentity
ciscoC130016XTS = _CiscoC130016XTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3252)
)
_CiscoC130024XTS_ObjectIdentity = ObjectIdentity
ciscoC130024XTS = _CiscoC130024XTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3253)
)
_CiscoNCS57D218DDSYS_ObjectIdentity = ObjectIdentity
ciscoNCS57D218DDSYS = _CiscoNCS57D218DDSYS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3254)
)
_CiscoUCSX410CM7_ObjectIdentity = ObjectIdentity
ciscoUCSX410CM7 = _CiscoUCSX410CM7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3256)
)
_CiscoFpr1010Etd_ObjectIdentity = ObjectIdentity
ciscoFpr1010Etd = _CiscoFpr1010Etd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3257)
)
_CiscoSNS3715K9_ObjectIdentity = ObjectIdentity
ciscoSNS3715K9 = _CiscoSNS3715K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3270)
)
_CiscoSNS3755K9_ObjectIdentity = ObjectIdentity
ciscoSNS3755K9 = _CiscoSNS3755K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3271)
)
_CiscoSNS3795K9_ObjectIdentity = ObjectIdentity
ciscoSNS3795K9 = _CiscoSNS3795K9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3272)
)
_CiscoIW9165DHURWB_ObjectIdentity = ObjectIdentity
ciscoIW9165DHURWB = _CiscoIW9165DHURWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3280)
)
_CiscoIW9165EURWB_ObjectIdentity = ObjectIdentity
ciscoIW9165EURWB = _CiscoIW9165EURWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3281)
)
_CiscoIW9167EHURWB_ObjectIdentity = ObjectIdentity
ciscoIW9167EHURWB = _CiscoIW9167EHURWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3282)
)
_CiscoCG522E_ObjectIdentity = ObjectIdentity
ciscoCG522E = _CiscoCG522E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3283)
)
_CiscoCG418E_ObjectIdentity = ObjectIdentity
ciscoCG418E = _CiscoCG418E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3284)
)
_CiscoCG1134GW6_ObjectIdentity = ObjectIdentity
ciscoCG1134GW6 = _CiscoCG1134GW6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3285)
)
_CiscoCG113W6_ObjectIdentity = ObjectIdentity
ciscoCG113W6 = _CiscoCG113W6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3286)
)
_CiscoC11318PWN_ObjectIdentity = ObjectIdentity
ciscoC11318PWN = _CiscoC11318PWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3328)
)
_CiscoC11318PWH_ObjectIdentity = ObjectIdentity
ciscoC11318PWH = _CiscoC11318PWH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3329)
)
_CiscoC11318PWK_ObjectIdentity = ObjectIdentity
ciscoC11318PWK = _CiscoC11318PWK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3330)
)
_CiscoC11318PWF_ObjectIdentity = ObjectIdentity
ciscoC11318PWF = _CiscoC11318PWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3331)
)
_CiscoC11318PWD_ObjectIdentity = ObjectIdentity
ciscoC11318PWD = _CiscoC11318PWD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3332)
)
_CiscoC11318PWR_ObjectIdentity = ObjectIdentity
ciscoC11318PWR = _CiscoC11318PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3333)
)
_CiscoC1131X8PWN_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWN = _CiscoC1131X8PWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3334)
)
_CiscoC1131X8PWH_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWH = _CiscoC1131X8PWH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3335)
)
_CiscoC1131X8PWK_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWK = _CiscoC1131X8PWK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3336)
)
_CiscoC1131X8PWF_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWF = _CiscoC1131X8PWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3337)
)
_CiscoC1131X8PWD_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWD = _CiscoC1131X8PWD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3338)
)
_CiscoC1131X8PWR_ObjectIdentity = ObjectIdentity
ciscoC1131X8PWR = _CiscoC1131X8PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3339)
)
_CiscoC11318PLTEPWN_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWN = _CiscoC11318PLTEPWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3340)
)
_CiscoC11318PLTEPWH_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWH = _CiscoC11318PLTEPWH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3341)
)
_CiscoC11318PLTEPWK_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWK = _CiscoC11318PLTEPWK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3342)
)
_CiscoC11318PLTEPWF_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWF = _CiscoC11318PLTEPWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3343)
)
_CiscoC11318PLTEPWD_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWD = _CiscoC11318PLTEPWD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3344)
)
_CiscoC11318PLTEPWR_ObjectIdentity = ObjectIdentity
ciscoC11318PLTEPWR = _CiscoC11318PLTEPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3345)
)
_CiscoC1131X8PLTEPWN_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWN = _CiscoC1131X8PLTEPWN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3346)
)
_CiscoC1131X8PLTEPWH_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWH = _CiscoC1131X8PLTEPWH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3347)
)
_CiscoC1131X8PLTEPWK_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWK = _CiscoC1131X8PLTEPWK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3348)
)
_CiscoC1131X8PLTEPWF_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWF = _CiscoC1131X8PLTEPWF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3349)
)
_CiscoC1131X8PLTEPWD_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWD = _CiscoC1131X8PLTEPWD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3350)
)
_CiscoC1131X8PLTEPWR_ObjectIdentity = ObjectIdentity
ciscoC1131X8PLTEPWR = _CiscoC1131X8PLTEPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3351)
)
_CiscoNCS1014_ObjectIdentity = ObjectIdentity
ciscoNCS1014 = _CiscoNCS1014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3366)
)
_CiscoNCS1012_ObjectIdentity = ObjectIdentity
ciscoNCS1012 = _CiscoNCS1012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3367)
)
_CiscoNCS1020_ObjectIdentity = ObjectIdentity
ciscoNCS1020 = _CiscoNCS1020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3368)
)
_CiscoC9610R_ObjectIdentity = ObjectIdentity
ciscoC9610R = _CiscoC9610R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3383)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PRODUCTS-MIB",
    **{"ciscoGatewayServer": ciscoGatewayServer,
       "ciscoTerminalServer": ciscoTerminalServer,
       "ciscoTrouter": ciscoTrouter,
       "ciscoProtocolTranslator": ciscoProtocolTranslator,
       "ciscoIGS": ciscoIGS,
       "cisco3000": cisco3000,
       "cisco4000": cisco4000,
       "cisco7000": cisco7000,
       "ciscoCS500": ciscoCS500,
       "cisco2000": cisco2000,
       "ciscoAGSplus": ciscoAGSplus,
       "cisco7010": cisco7010,
       "cisco2500": cisco2500,
       "cisco4500": cisco4500,
       "cisco2102": cisco2102,
       "cisco2202": cisco2202,
       "cisco2501": cisco2501,
       "cisco2502": cisco2502,
       "cisco2503": cisco2503,
       "cisco2504": cisco2504,
       "cisco2505": cisco2505,
       "cisco2506": cisco2506,
       "cisco2507": cisco2507,
       "cisco2508": cisco2508,
       "cisco2509": cisco2509,
       "cisco2510": cisco2510,
       "cisco2511": cisco2511,
       "cisco2512": cisco2512,
       "cisco2513": cisco2513,
       "cisco2514": cisco2514,
       "cisco2515": cisco2515,
       "cisco3101": cisco3101,
       "cisco3102": cisco3102,
       "cisco3103": cisco3103,
       "cisco3104": cisco3104,
       "cisco3202": cisco3202,
       "cisco3204": cisco3204,
       "ciscoAccessProRC": ciscoAccessProRC,
       "ciscoAccessProEC": ciscoAccessProEC,
       "cisco1000": cisco1000,
       "cisco1003": cisco1003,
       "cisco2516": cisco2516,
       "cisco1020": cisco1020,
       "cisco1004": cisco1004,
       "cisco7507": cisco7507,
       "cisco7513": cisco7513,
       "cisco7506": cisco7506,
       "cisco7505": cisco7505,
       "cisco1005": cisco1005,
       "cisco4700": cisco4700,
       "ciscoPro1003": ciscoPro1003,
       "ciscoPro1004": ciscoPro1004,
       "ciscoPro1005": ciscoPro1005,
       "ciscoPro1020": ciscoPro1020,
       "ciscoPro2500PCE": ciscoPro2500PCE,
       "ciscoPro2501": ciscoPro2501,
       "ciscoPro2503": ciscoPro2503,
       "ciscoPro2505": ciscoPro2505,
       "ciscoPro2507": ciscoPro2507,
       "ciscoPro2509": ciscoPro2509,
       "ciscoPro2511": ciscoPro2511,
       "ciscoPro2514": ciscoPro2514,
       "ciscoPro2516": ciscoPro2516,
       "ciscoPro2519": ciscoPro2519,
       "ciscoPro2521": ciscoPro2521,
       "ciscoPro4500": ciscoPro4500,
       "cisco2517": cisco2517,
       "cisco2518": cisco2518,
       "cisco2519": cisco2519,
       "cisco2520": cisco2520,
       "cisco2521": cisco2521,
       "cisco2522": cisco2522,
       "cisco2523": cisco2523,
       "cisco2524": cisco2524,
       "cisco2525": cisco2525,
       "ciscoPro751": ciscoPro751,
       "ciscoPro752": ciscoPro752,
       "ciscoPro753": ciscoPro753,
       "ciscoPro901": ciscoPro901,
       "ciscoPro902": ciscoPro902,
       "cisco751": cisco751,
       "cisco752": cisco752,
       "cisco753": cisco753,
       "ciscoPro741": ciscoPro741,
       "ciscoPro742": ciscoPro742,
       "ciscoPro743": ciscoPro743,
       "ciscoPro744": ciscoPro744,
       "ciscoPro761": ciscoPro761,
       "ciscoPro762": ciscoPro762,
       "ciscoPro763": ciscoPro763,
       "ciscoPro764": ciscoPro764,
       "ciscoPro765": ciscoPro765,
       "ciscoPro766": ciscoPro766,
       "cisco741": cisco741,
       "cisco742": cisco742,
       "cisco743": cisco743,
       "cisco744": cisco744,
       "cisco761": cisco761,
       "cisco762": cisco762,
       "cisco763": cisco763,
       "cisco764": cisco764,
       "cisco765": cisco765,
       "cisco766": cisco766,
       "ciscoPro2520": ciscoPro2520,
       "ciscoPro2522": ciscoPro2522,
       "ciscoPro2524": ciscoPro2524,
       "ciscoLS1010": ciscoLS1010,
       "cisco7206": cisco7206,
       "ciscoAS5200": ciscoAS5200,
       "cisco3640": cisco3640,
       "ciscoCatalyst3500": ciscoCatalyst3500,
       "ciscoWSX3011": ciscoWSX3011,
       "cisco1601": cisco1601,
       "cisco1602": cisco1602,
       "cisco1603": cisco1603,
       "cisco1604": cisco1604,
       "ciscoPro1601": ciscoPro1601,
       "ciscoPro1602": ciscoPro1602,
       "ciscoPro1603": ciscoPro1603,
       "ciscoPro1604": ciscoPro1604,
       "ciscoWSX5301": ciscoWSX5301,
       "cisco3620": cisco3620,
       "ciscoPro3620": ciscoPro3620,
       "ciscoPro3640": ciscoPro3640,
       "cisco7204": cisco7204,
       "cisco771": cisco771,
       "cisco772": cisco772,
       "cisco775": cisco775,
       "cisco776": cisco776,
       "ciscoPro2502": ciscoPro2502,
       "ciscoPro2504": ciscoPro2504,
       "ciscoPro2506": ciscoPro2506,
       "ciscoPro2508": ciscoPro2508,
       "ciscoPro2510": ciscoPro2510,
       "ciscoPro2512": ciscoPro2512,
       "ciscoPro2513": ciscoPro2513,
       "ciscoPro2515": ciscoPro2515,
       "ciscoPro2517": ciscoPro2517,
       "ciscoPro2518": ciscoPro2518,
       "ciscoPro2523": ciscoPro2523,
       "ciscoPro2525": ciscoPro2525,
       "ciscoPro4700": ciscoPro4700,
       "ciscoPro316T": ciscoPro316T,
       "ciscoPro316C": ciscoPro316C,
       "ciscoPro3116": ciscoPro3116,
       "catalyst116T": catalyst116T,
       "catalyst116C": catalyst116C,
       "catalyst1116": catalyst1116,
       "ciscoAS2509RJ": ciscoAS2509RJ,
       "ciscoAS2511RJ": ciscoAS2511RJ,
       "ciscoMC3810": ciscoMC3810,
       "cisco1503": cisco1503,
       "cisco1502": cisco1502,
       "ciscoAS5300": ciscoAS5300,
       "ciscoLS1015": ciscoLS1015,
       "cisco2501FRADFX": cisco2501FRADFX,
       "cisco2501LANFRADFX": cisco2501LANFRADFX,
       "cisco2502LANFRADFX": cisco2502LANFRADFX,
       "ciscoWSX5302": ciscoWSX5302,
       "ciscoFastHub216T": ciscoFastHub216T,
       "catalyst2908xl": catalyst2908xl,
       "catalyst2916mxl": catalyst2916mxl,
       "cisco1605": cisco1605,
       "cisco12012": cisco12012,
       "catalyst1912C": catalyst1912C,
       "ciscoMicroWebServer2": ciscoMicroWebServer2,
       "ciscoFastHubBMMTX": ciscoFastHubBMMTX,
       "ciscoFastHubBMMFX": ciscoFastHubBMMFX,
       "ciscoUBR7246": ciscoUBR7246,
       "cisco6400": cisco6400,
       "cisco12004": cisco12004,
       "cisco12008": cisco12008,
       "catalyst2924XL": catalyst2924XL,
       "catalyst2924CXL": catalyst2924CXL,
       "cisco2610": cisco2610,
       "cisco2611": cisco2611,
       "cisco2612": cisco2612,
       "ciscoAS5800": ciscoAS5800,
       "ciscoSC3640": ciscoSC3640,
       "cisco8510": cisco8510,
       "ciscoUBR904": ciscoUBR904,
       "cisco6200": cisco6200,
       "cisco7202": cisco7202,
       "cisco2613": cisco2613,
       "cisco8515": cisco8515,
       "catalyst9006": catalyst9006,
       "catalyst9009": catalyst9009,
       "ciscoRPM": ciscoRPM,
       "cisco1710": cisco1710,
       "cisco1720": cisco1720,
       "catalyst8540msr": catalyst8540msr,
       "catalyst8540csr": catalyst8540csr,
       "cisco7576": cisco7576,
       "cisco3660": cisco3660,
       "cisco1401": cisco1401,
       "cisco2620": cisco2620,
       "cisco2621": cisco2621,
       "ciscoUBR7223": ciscoUBR7223,
       "cisco6400Nrp": cisco6400Nrp,
       "cisco801": cisco801,
       "cisco802": cisco802,
       "cisco803": cisco803,
       "cisco804": cisco804,
       "cisco1750": cisco1750,
       "catalyst2924XLv": catalyst2924XLv,
       "catalyst2924CXLv": catalyst2924CXLv,
       "catalyst2912XL": catalyst2912XL,
       "catalyst2924MXL": catalyst2924MXL,
       "catalyst2912MfXL": catalyst2912MfXL,
       "cisco7206VXR": cisco7206VXR,
       "cisco7204VXR": cisco7204VXR,
       "cisco1538M": cisco1538M,
       "cisco1548M": cisco1548M,
       "ciscoFasthub100": ciscoFasthub100,
       "ciscoPIXFirewall": ciscoPIXFirewall,
       "ciscoMGX8850": ciscoMGX8850,
       "ciscoMGX8830": ciscoMGX8830,
       "catalyst8510msr": catalyst8510msr,
       "catalyst8515msr": catalyst8515msr,
       "ciscoIGX8410": ciscoIGX8410,
       "ciscoIGX8420": ciscoIGX8420,
       "ciscoIGX8430": ciscoIGX8430,
       "ciscoIGX8450": ciscoIGX8450,
       "ciscoBPX8620": ciscoBPX8620,
       "ciscoBPX8650": ciscoBPX8650,
       "ciscoBPX8680": ciscoBPX8680,
       "ciscoCacheEngine": ciscoCacheEngine,
       "ciscoCat6000": ciscoCat6000,
       "ciscoBPXSes": ciscoBPXSes,
       "ciscoIGXSes": ciscoIGXSes,
       "ciscoLocalDirector": ciscoLocalDirector,
       "cisco805": cisco805,
       "catalyst3508GXL": catalyst3508GXL,
       "catalyst3512XL": catalyst3512XL,
       "catalyst3524XL": catalyst3524XL,
       "cisco1407": cisco1407,
       "cisco1417": cisco1417,
       "cisco6100": cisco6100,
       "cisco6130": cisco6130,
       "cisco6260": cisco6260,
       "ciscoOpticalRegenerator": ciscoOpticalRegenerator,
       "ciscoUBR924": ciscoUBR924,
       "ciscoWSX6302Msm": ciscoWSX6302Msm,
       "catalyst5kRsfc": catalyst5kRsfc,
       "catalyst6kMsfc": catalyst6kMsfc,
       "cisco7120Quadt1": cisco7120Quadt1,
       "cisco7120T3": cisco7120T3,
       "cisco7120E3": cisco7120E3,
       "cisco7120At3": cisco7120At3,
       "cisco7120Ae3": cisco7120Ae3,
       "cisco7120Smi3": cisco7120Smi3,
       "cisco7140Dualt3": cisco7140Dualt3,
       "cisco7140Duale3": cisco7140Duale3,
       "cisco7140Dualat3": cisco7140Dualat3,
       "cisco7140Dualae3": cisco7140Dualae3,
       "cisco7140Dualmm3": cisco7140Dualmm3,
       "cisco827QuadV": cisco827QuadV,
       "ciscoUBR7246VXR": ciscoUBR7246VXR,
       "cisco10400": cisco10400,
       "cisco12016": cisco12016,
       "ciscoAs5400": ciscoAs5400,
       "cat2948gL3": cat2948gL3,
       "cisco7140Octt1": cisco7140Octt1,
       "cisco7140Dualfe": cisco7140Dualfe,
       "cat3548XL": cat3548XL,
       "ciscoVG200": ciscoVG200,
       "cat6006": cat6006,
       "cat6009": cat6009,
       "cat6506": cat6506,
       "cat6509": cat6509,
       "cisco827": cisco827,
       "ciscoManagementEngine1100": ciscoManagementEngine1100,
       "ciscoMc3810V3": ciscoMc3810V3,
       "cat3524tXLEn": cat3524tXLEn,
       "cisco7507z": cisco7507z,
       "cisco7513z": cisco7513z,
       "cisco7507mx": cisco7507mx,
       "cisco7513mx": cisco7513mx,
       "ciscoUBR912C": ciscoUBR912C,
       "ciscoUBR912S": ciscoUBR912S,
       "ciscoUBR914": ciscoUBR914,
       "cisco802J": cisco802J,
       "cisco804J": cisco804J,
       "cisco6160": cisco6160,
       "cat4908gL3": cat4908gL3,
       "cisco6015": cisco6015,
       "cat4232L3": cat4232L3,
       "catalyst6kMsfc2": catalyst6kMsfc2,
       "cisco7750Mrp200": cisco7750Mrp200,
       "cisco7750Ssp80": cisco7750Ssp80,
       "ciscoMGX8230": ciscoMGX8230,
       "ciscoMGX8250": ciscoMGX8250,
       "ciscoCVA122": ciscoCVA122,
       "ciscoCVA124": ciscoCVA124,
       "ciscoAs5850": ciscoAs5850,
       "cat6509Sp": cat6509Sp,
       "ciscoMGX8240": ciscoMGX8240,
       "cat4840gL3": cat4840gL3,
       "ciscoAS5350": ciscoAS5350,
       "cisco7750": cisco7750,
       "ciscoMGX8950": ciscoMGX8950,
       "ciscoUBR925": ciscoUBR925,
       "ciscoUBR10012": ciscoUBR10012,
       "catalyst4kGateway": catalyst4kGateway,
       "cisco2650": cisco2650,
       "cisco2651": cisco2651,
       "cisco826QuadV": cisco826QuadV,
       "cisco826": cisco826,
       "catalyst295012": catalyst295012,
       "catalyst295024": catalyst295024,
       "catalyst295024C": catalyst295024C,
       "cisco1751": cisco1751,
       "cisco1730Iad8Fxs": cisco1730Iad8Fxs,
       "cisco1730Iad16Fxs": cisco1730Iad16Fxs,
       "cisco626": cisco626,
       "cisco627": cisco627,
       "cisco633": cisco633,
       "cisco673": cisco673,
       "cisco675": cisco675,
       "cisco675e": cisco675e,
       "cisco676": cisco676,
       "cisco677": cisco677,
       "cisco678": cisco678,
       "cisco3661Ac": cisco3661Ac,
       "cisco3661Dc": cisco3661Dc,
       "cisco3662Ac": cisco3662Ac,
       "cisco3662Dc": cisco3662Dc,
       "cisco3662AcCo": cisco3662AcCo,
       "cisco3662DcCo": cisco3662DcCo,
       "ciscoUBR7111": ciscoUBR7111,
       "ciscoUBR7111E": ciscoUBR7111E,
       "ciscoUBR7114": ciscoUBR7114,
       "ciscoUBR7114E": ciscoUBR7114E,
       "cisco12010": cisco12010,
       "cisco8110": cisco8110,
       "cisco8120": cisco8120,
       "ciscoUBR905": ciscoUBR905,
       "ciscoIDS": ciscoIDS,
       "ciscoSOHO77": ciscoSOHO77,
       "ciscoSOHO76": ciscoSOHO76,
       "cisco7150Dualfe": cisco7150Dualfe,
       "cisco7150Octt1": cisco7150Octt1,
       "cisco7150Dualt3": cisco7150Dualt3,
       "ciscoOlympus": ciscoOlympus,
       "catalyst2950t24": catalyst2950t24,
       "ciscoVPS1110": ciscoVPS1110,
       "ciscoContentEngine": ciscoContentEngine,
       "ciscoIAD2420": ciscoIAD2420,
       "cisco677i": cisco677i,
       "cisco674": cisco674,
       "ciscoDPA7630": ciscoDPA7630,
       "catalyst355024": catalyst355024,
       "catalyst355048": catalyst355048,
       "catalyst355012T": catalyst355012T,
       "catalyst2924LREXL": catalyst2924LREXL,
       "catalyst2912LREXL": catalyst2912LREXL,
       "ciscoCVA122E": ciscoCVA122E,
       "ciscoCVA124E": ciscoCVA124E,
       "ciscoURM": ciscoURM,
       "ciscoURM2FE": ciscoURM2FE,
       "ciscoURM2FE2V": ciscoURM2FE2V,
       "cisco7401VXR": cisco7401VXR,
       "cisco951": cisco951,
       "cisco952": cisco952,
       "ciscoCAP340": ciscoCAP340,
       "ciscoCAP350": ciscoCAP350,
       "ciscoDPA7610": ciscoDPA7610,
       "cisco828": cisco828,
       "ciscoSOHO78": ciscoSOHO78,
       "cisco806": cisco806,
       "cisco12416": cisco12416,
       "cat2948gL3Dc": cat2948gL3Dc,
       "cat4908gL3Dc": cat4908gL3Dc,
       "cisco12406": cisco12406,
       "ciscoPIXFirewall506": ciscoPIXFirewall506,
       "ciscoPIXFirewall515": ciscoPIXFirewall515,
       "ciscoPIXFirewall520": ciscoPIXFirewall520,
       "ciscoPIXFirewall525": ciscoPIXFirewall525,
       "ciscoPIXFirewall535": ciscoPIXFirewall535,
       "cisco12410": cisco12410,
       "cisco811": cisco811,
       "cisco813": cisco813,
       "cisco10720": cisco10720,
       "ciscoMWR1900": ciscoMWR1900,
       "cisco4224": cisco4224,
       "ciscoWSC6513": ciscoWSC6513,
       "cisco7603": cisco7603,
       "cisco7606": cisco7606,
       "cisco7401ASR": cisco7401ASR,
       "ciscoVG248": ciscoVG248,
       "ciscoHSE": ciscoHSE,
       "ciscoONS15540ESP": ciscoONS15540ESP,
       "ciscoSN5420": ciscoSN5420,
       "ciscoIcs7750Ce300": ciscoIcs7750Ce300,
       "ciscoCe507": ciscoCe507,
       "ciscoCe560": ciscoCe560,
       "ciscoCe590": ciscoCe590,
       "ciscoCe7320": ciscoCe7320,
       "cisco2691": cisco2691,
       "cisco3725": cisco3725,
       "cisco3640A": cisco3640A,
       "cisco1760": cisco1760,
       "ciscoPIXFirewall501": ciscoPIXFirewall501,
       "cisco2610M": cisco2610M,
       "cisco2611M": cisco2611M,
       "ciscoGP10": ciscoGP10,
       "ciscoMC21": ciscoMC21,
       "ciscoSN51": ciscoSN51,
       "cisco12404": cisco12404,
       "cisco9004": cisco9004,
       "cisco3631Co": cisco3631Co,
       "catalyst295012G": catalyst295012G,
       "catalyst295024G": catalyst295024G,
       "catalyst295048G": catalyst295048G,
       "catalyst295024S": catalyst295024S,
       "catalyst355012G": catalyst355012G,
       "ciscoCE507AV": ciscoCE507AV,
       "ciscoCE560AV": ciscoCE560AV,
       "ciscoIE2105": ciscoIE2105,
       "ciscoMGX8850Pxm1E": ciscoMGX8850Pxm1E,
       "cisco3745": cisco3745,
       "cisco10005": cisco10005,
       "cisco10008": cisco10008,
       "cisco7304": cisco7304,
       "ciscoRpmXf": ciscoRpmXf,
       "ciscoOsm4oc3PosSmIr": ciscoOsm4oc3PosSmIr,
       "ciscoOsm4oc3PosMmSr": ciscoOsm4oc3PosMmSr,
       "ciscoOsm4oc3PosSmLr": ciscoOsm4oc3PosSmLr,
       "cisco1721": cisco1721,
       "cat4000Sup3": cat4000Sup3,
       "cisco827H": cisco827H,
       "ciscoSOHO77H": ciscoSOHO77H,
       "cat4006": cat4006,
       "ciscoWSC6503": ciscoWSC6503,
       "ciscoPIXFirewall506E": ciscoPIXFirewall506E,
       "ciscoPIXFirewall515E": ciscoPIXFirewall515E,
       "cat355024Dc": cat355024Dc,
       "cat355024Mmf": cat355024Mmf,
       "ciscoCE2636": ciscoCE2636,
       "ciscoDwCE": ciscoDwCE,
       "cisco7750Mrp300": cisco7750Mrp300,
       "ciscoRPMPR": ciscoRPMPR,
       "cisco14MGX8830Pxm1E": cisco14MGX8830Pxm1E,
       "ciscoWlse": ciscoWlse,
       "ciscoONS15530": ciscoONS15530,
       "ciscoONS15530NEBS": ciscoONS15530NEBS,
       "ciscoONS15530ETSI": ciscoONS15530ETSI,
       "ciscoSOHO71": ciscoSOHO71,
       "cisco6400UAC": cisco6400UAC,
       "cisco2610XM": cisco2610XM,
       "cisco2611XM": cisco2611XM,
       "cisco2620XM": cisco2620XM,
       "cisco2621XM": cisco2621XM,
       "cisco2650XM": cisco2650XM,
       "cisco2651XM": cisco2651XM,
       "catalyst295024GDC": catalyst295024GDC,
       "ciscoAIRAP1200": ciscoAIRAP1200,
       "ciscoSN5428": ciscoSN5428,
       "cisco7301": cisco7301,
       "cisco12816": cisco12816,
       "cisco12810": cisco12810,
       "cisco3250": cisco3250,
       "catalyst295024SX": catalyst295024SX,
       "ciscoONS15540ESPx": ciscoONS15540ESPx,
       "catalyst295024LRESt": catalyst295024LRESt,
       "catalyst29508LRESt": catalyst29508LRESt,
       "catalyst295024LREG": catalyst295024LREG,
       "catalyst355024PWR": catalyst355024PWR,
       "ciscoCDM4630": ciscoCDM4630,
       "ciscoCDM4650": ciscoCDM4650,
       "catalyst2955T12": catalyst2955T12,
       "catalyst2955C12": catalyst2955C12,
       "ciscoCE508": ciscoCE508,
       "ciscoCE565": ciscoCE565,
       "ciscoCE7325": ciscoCE7325,
       "ciscoONS15454": ciscoONS15454,
       "ciscoONS15327": ciscoONS15327,
       "cisco837": cisco837,
       "ciscoSOHO97": ciscoSOHO97,
       "cisco831": cisco831,
       "ciscoSOHO91": ciscoSOHO91,
       "cisco836": cisco836,
       "ciscoSOHO96": ciscoSOHO96,
       "cat4507": cat4507,
       "cat4506": cat4506,
       "cat4503": cat4503,
       "ciscoCE7305": ciscoCE7305,
       "ciscoCE510": ciscoCE510,
       "ciscoAIRAP1100": ciscoAIRAP1100,
       "catalyst2955S12": catalyst2955S12,
       "cisco7609": cisco7609,
       "ciscoWSC65509": ciscoWSC65509,
       "catalyst375024": catalyst375024,
       "catalyst375048": catalyst375048,
       "catalyst375024TS": catalyst375024TS,
       "catalyst375024T": catalyst375024T,
       "catalyst37xxStack": catalyst37xxStack,
       "ciscoGSS": ciscoGSS,
       "ciscoPrimaryGSSM": ciscoPrimaryGSSM,
       "ciscoStandbyGSSM": ciscoStandbyGSSM,
       "ciscoMWR1941DC": ciscoMWR1941DC,
       "ciscoDSC9216K9": ciscoDSC9216K9,
       "cat6500FirewallSm": cat6500FirewallSm,
       "ciscoSCA11000": ciscoSCA11000,
       "ciscoCSM": ciscoCSM,
       "ciscoAIRAP1210": ciscoAIRAP1210,
       "ciscoSCA211000": ciscoSCA211000,
       "catalyst297024": catalyst297024,
       "cisco7613": cisco7613,
       "ciscoSN54282": ciscoSN54282,
       "catalyst3750Ge12Sfp": catalyst3750Ge12Sfp,
       "ciscoCR4430": ciscoCR4430,
       "ciscoCR4450": ciscoCR4450,
       "ciscoAIRBR1410": ciscoAIRBR1410,
       "ciscoWSC6509neba": ciscoWSC6509neba,
       "catalyst375048PS": catalyst375048PS,
       "catalyst375024PS": catalyst375024PS,
       "catalyst4510": catalyst4510,
       "cisco1711": cisco1711,
       "cisco1712": cisco1712,
       "catalyst29408TT": catalyst29408TT,
       "catalyst29408TF": catalyst29408TF,
       "cisco3825": cisco3825,
       "cisco3845": cisco3845,
       "cisco2430Iad24Fxs": cisco2430Iad24Fxs,
       "cisco2431Iad8Fxs": cisco2431Iad8Fxs,
       "cisco2431Iad16Fxs": cisco2431Iad16Fxs,
       "cisco2431Iad1T1E1": cisco2431Iad1T1E1,
       "cisco2432Iad24Fxs": cisco2432Iad24Fxs,
       "cisco1701ADSLBRI": cisco1701ADSLBRI,
       "catalyst2950St24LRE997": catalyst2950St24LRE997,
       "ciscoAirAp350IOS": ciscoAirAp350IOS,
       "cisco3220": cisco3220,
       "cat6500SslSm": cat6500SslSm,
       "ciscoSIMSE": ciscoSIMSE,
       "ciscoESSE": ciscoESSE,
       "catalyst6kSup720": catalyst6kSup720,
       "ciscoVG224": ciscoVG224,
       "catalyst295048T": catalyst295048T,
       "catalyst295048SX": catalyst295048SX,
       "catalyst297024TS": catalyst297024TS,
       "ciscoNmNam": ciscoNmNam,
       "catalyst356024PS": catalyst356024PS,
       "catalyst356048PS": catalyst356048PS,
       "ciscoAIRBR1300": ciscoAIRBR1300,
       "cisco851": cisco851,
       "cisco857": cisco857,
       "cisco876": cisco876,
       "cisco877": cisco877,
       "cisco878": cisco878,
       "cisco871": cisco871,
       "uMG9820": uMG9820,
       "catalyst6kGateway": catalyst6kGateway,
       "catalyst375024ME": catalyst375024ME,
       "catalyst4000NAM": catalyst4000NAM,
       "cisco2811": cisco2811,
       "cisco2821": cisco2821,
       "cisco2851": cisco2851,
       "cisco3201WMIC": cisco3201WMIC,
       "ciscoMCS7815I": ciscoMCS7815I,
       "ciscoMCS7825H": ciscoMCS7825H,
       "ciscoMCS7835H": ciscoMCS7835H,
       "ciscoMCS7835I": ciscoMCS7835I,
       "ciscoMCS7845H": ciscoMCS7845H,
       "ciscoMCS7845I": ciscoMCS7845I,
       "ciscoMCS7855I": ciscoMCS7855I,
       "ciscoMCS7865I": ciscoMCS7865I,
       "cisco12006": cisco12006,
       "catalyst3750G16TD": catalyst3750G16TD,
       "ciscoIGESM": ciscoIGESM,
       "ciscoCCM": ciscoCCM,
       "cisco1718": cisco1718,
       "ciscoCe511K9": ciscoCe511K9,
       "ciscoCe566K9": ciscoCe566K9,
       "ciscoMGX8830Pxm45": ciscoMGX8830Pxm45,
       "ciscoMGX8880": ciscoMGX8880,
       "ciscoWsSvcWLAN1K9": ciscoWsSvcWLAN1K9,
       "ciscoCe7306K9": ciscoCe7306K9,
       "ciscoCe7326K9": ciscoCe7326K9,
       "catalyst3750G24PS": catalyst3750G24PS,
       "catalyst3750G48PS": catalyst3750G48PS,
       "catalyst3750G48TS": catalyst3750G48TS,
       "ciscoBMGX8830Pxm45": ciscoBMGX8830Pxm45,
       "ciscoBMGX8830Pxm1E": ciscoBMGX8830Pxm1E,
       "ciscoBMGX8850Pxm45": ciscoBMGX8850Pxm45,
       "ciscoBMGX8850Pxm1E": ciscoBMGX8850Pxm1E,
       "ciscoSSLCSM": ciscoSSLCSM,
       "ciscoNetworkRegistrar": ciscoNetworkRegistrar,
       "ciscoCe501K9": ciscoCe501K9,
       "ciscoCRS16S": ciscoCRS16S,
       "catalyst3560G24PS": catalyst3560G24PS,
       "catalyst3560G24TS": catalyst3560G24TS,
       "catalyst3560G48PS": catalyst3560G48PS,
       "catalyst3560G48TS": catalyst3560G48TS,
       "ciscoAIRAP1130": ciscoAIRAP1130,
       "cisco2801": cisco2801,
       "cisco1841": cisco1841,
       "ciscoWsSvcMWAM1": ciscoWsSvcMWAM1,
       "ciscoNMCUE": ciscoNMCUE,
       "ciscoAIMCUE": ciscoAIMCUE,
       "catalyst3750G24TS1U": catalyst3750G24TS1U,
       "cisco371098HP001": cisco371098HP001,
       "catalyst4948": catalyst4948,
       "ciscoSB101": ciscoSB101,
       "ciscoSB106": ciscoSB106,
       "ciscoSB107": ciscoSB107,
       "ciscoWLSE1130": ciscoWLSE1130,
       "ciscoWLSE1030": ciscoWLSE1030,
       "ciscoHSE1140": ciscoHSE1140,
       "catalyst356024TS": catalyst356024TS,
       "catalyst356048TS": catalyst356048TS,
       "ciscoWsSvcadsm1K9": ciscoWsSvcadsm1K9,
       "ciscoWsSvcagsm1K9": ciscoWsSvcagsm1K9,
       "ciscoONS15310": ciscoONS15310,
       "cisco1801": cisco1801,
       "cisco1802": cisco1802,
       "cisco1803": cisco1803,
       "cisco1811": cisco1811,
       "cisco1812": cisco1812,
       "ciscoCRS8S": ciscoCRS8S,
       "ciscoIDS4210": ciscoIDS4210,
       "ciscoIDS4215": ciscoIDS4215,
       "ciscoIDS4235": ciscoIDS4235,
       "ciscoIPS4240": ciscoIPS4240,
       "ciscoIDS4250": ciscoIDS4250,
       "ciscoIDS4250SX": ciscoIDS4250SX,
       "ciscoIDS4250XL": ciscoIDS4250XL,
       "ciscoIPS4255": ciscoIPS4255,
       "ciscoIDSIDSM2": ciscoIDSIDSM2,
       "ciscoIDSNMCIDS": ciscoIDSNMCIDS,
       "ciscoIPSSSM20": ciscoIPSSSM20,
       "catalyst375024FS": catalyst375024FS,
       "ciscoWSC6504E": ciscoWSC6504E,
       "cisco7604": cisco7604,
       "catalyst494810GE": catalyst494810GE,
       "ciscoIGESMSFP": ciscoIGESMSFP,
       "ciscoFE6326K9": ciscoFE6326K9,
       "ciscoIPSSSM10": ciscoIPSSSM10,
       "ciscoNme16Es1Ge": ciscoNme16Es1Ge,
       "ciscoNmeX24Es1Ge": ciscoNmeX24Es1Ge,
       "ciscoNmeXd24Es2St": ciscoNmeXd24Es2St,
       "ciscoNmeXd48Es2Ge": ciscoNmeXd48Es2Ge,
       "cisco3202WMIC": cisco3202WMIC,
       "ciscoAs5400XM": ciscoAs5400XM,
       "ciscoASA5510": ciscoASA5510,
       "ciscoASA5520": ciscoASA5520,
       "ciscoASA5520sc": ciscoASA5520sc,
       "ciscoASA5540": ciscoASA5540,
       "ciscoASA5540sc": ciscoASA5540sc,
       "ciscoWsSvcFwm1sc": ciscoWsSvcFwm1sc,
       "ciscoPIXFirewall535sc": ciscoPIXFirewall535sc,
       "ciscoPIXFirewall525sc": ciscoPIXFirewall525sc,
       "ciscoPIXFirewall515Esc": ciscoPIXFirewall515Esc,
       "ciscoPIXFirewall515sc": ciscoPIXFirewall515sc,
       "ciscoAs5350XM": ciscoAs5350XM,
       "ciscoFe7326K9": ciscoFe7326K9,
       "ciscoFe511K9": ciscoFe511K9,
       "ciscoSCEDispatcher": ciscoSCEDispatcher,
       "ciscoSCE1000": ciscoSCE1000,
       "ciscoSCE2000": ciscoSCE2000,
       "ciscoAIRAP1240": ciscoAIRAP1240,
       "ciscoDSC9120CLK9": ciscoDSC9120CLK9,
       "ciscoFe611K9": ciscoFe611K9,
       "catalyst3750Ge12SfpDc": catalyst3750Ge12SfpDc,
       "cisco3271": cisco3271,
       "cisco3272": cisco3272,
       "cisco3241": cisco3241,
       "cisco3242": cisco3242,
       "ciscoICM": ciscoICM,
       "catalyst296024": catalyst296024,
       "catalyst296048": catalyst296048,
       "catalyst2960G24": catalyst2960G24,
       "catalyst2960G48": catalyst2960G48,
       "catalyst45503": catalyst45503,
       "catalyst45506": catalyst45506,
       "catalyst45507": catalyst45507,
       "catalyst455010": catalyst455010,
       "ciscoNme16Es1GeNoPwr": ciscoNme16Es1GeNoPwr,
       "ciscoNmeX24Es1GeNoPwr": ciscoNmeX24Es1GeNoPwr,
       "ciscoNmeXd24Es2StNoPwr": ciscoNmeXd24Es2StNoPwr,
       "ciscoNmeXd48Es2GeNoPwr": ciscoNmeXd48Es2GeNoPwr,
       "catalyst6kMsfc2a": catalyst6kMsfc2a,
       "ciscoEDI": ciscoEDI,
       "ciscoCe611K9": ciscoCe611K9,
       "ciscoWLSEs20": ciscoWLSEs20,
       "ciscoMPX": ciscoMPX,
       "ciscoNMCUEEC": ciscoNMCUEEC,
       "ciscoWLSE1132": ciscoWLSE1132,
       "ciscoME6340ACA": ciscoME6340ACA,
       "ciscoME6340DCA": ciscoME6340DCA,
       "ciscoME6340DCB": ciscoME6340DCB,
       "catalyst296024TT": catalyst296024TT,
       "catalyst296048TT": catalyst296048TT,
       "ciscoIGESMSFPT": ciscoIGESMSFPT,
       "ciscoMEC6524gs8s": ciscoMEC6524gs8s,
       "ciscoMEC6524gt8s": ciscoMEC6524gt8s,
       "ciscoMEC6724s10x2": ciscoMEC6724s10x2,
       "ciscoMEC6724t10x2": ciscoMEC6724t10x2,
       "ciscoPaldron": ciscoPaldron,
       "catalystsExpress50024TT": catalystsExpress50024TT,
       "catalystsExpress50024LC": catalystsExpress50024LC,
       "catalystsExpress50024PC": catalystsExpress50024PC,
       "catalystsExpress50012TC": catalystsExpress50012TC,
       "ciscoIGESMT": ciscoIGESMT,
       "ciscoACE04G": ciscoACE04G,
       "ciscoACE10K9": ciscoACE10K9,
       "cisco5750": cisco5750,
       "ciscoMWR1941DCA": ciscoMWR1941DCA,
       "cisco815": cisco815,
       "cisco240024TSA": cisco240024TSA,
       "cisco240024TSD": cisco240024TSD,
       "cisco340024TSA": cisco340024TSA,
       "cisco340024TSD": cisco340024TSD,
       "ciscoCrs18Linecard": ciscoCrs18Linecard,
       "ciscoCrs1Fabric": ciscoCrs1Fabric,
       "ciscoFE2636": ciscoFE2636,
       "ciscoIDS4220": ciscoIDS4220,
       "ciscoIDS4230": ciscoIDS4230,
       "ciscoIPS4260": ciscoIPS4260,
       "ciscoWsSvcSAMIBB": ciscoWsSvcSAMIBB,
       "ciscoASA5505": ciscoASA5505,
       "ciscoMCS7825I": ciscoMCS7825I,
       "ciscoWsC3750g24ps": ciscoWsC3750g24ps,
       "ciscoWs3020Hpq": ciscoWs3020Hpq,
       "ciscoWs3030Del": ciscoWs3030Del,
       "ciscoSpaOc48posSfp": ciscoSpaOc48posSfp,
       "catalyst6kEnhancedGateway": catalyst6kEnhancedGateway,
       "ciscoWLSE1133": ciscoWLSE1133,
       "ciscoASA5550": ciscoASA5550,
       "ciscoNMAONK9": ciscoNMAONK9,
       "ciscoNMAONWS": ciscoNMAONWS,
       "ciscoNMAONAPS": ciscoNMAONAPS,
       "ciscoWae612K9": ciscoWae612K9,
       "ciscoAIRAP1250": ciscoAIRAP1250,
       "ciscoCe512K9": ciscoCe512K9,
       "ciscoFe512K9": ciscoFe512K9,
       "ciscoCe612K9": ciscoCe612K9,
       "ciscoFe612K9": ciscoFe612K9,
       "ciscoASA5550sc": ciscoASA5550sc,
       "ciscoASA5520sy": ciscoASA5520sy,
       "ciscoASA5540sy": ciscoASA5540sy,
       "ciscoASA5550sy": ciscoASA5550sy,
       "ciscoWsSvcFwm1sy": ciscoWsSvcFwm1sy,
       "ciscoPIXFirewall515sy": ciscoPIXFirewall515sy,
       "ciscoPIXFirewall515Esy": ciscoPIXFirewall515Esy,
       "ciscoPIXFirewall525sy": ciscoPIXFirewall525sy,
       "ciscoPIXFirewall535sy": ciscoPIXFirewall535sy,
       "ciscoIpRanOpt4p": ciscoIpRanOpt4p,
       "ciscoASA5510sc": ciscoASA5510sc,
       "ciscoASA5510sy": ciscoASA5510sy,
       "ciscoJumpgate": ciscoJumpgate,
       "ciscoOe512K9": ciscoOe512K9,
       "ciscoOe612K9": ciscoOe612K9,
       "catalyst3750G24WS25": catalyst3750G24WS25,
       "catalyst3750G24WS50": catalyst3750G24WS50,
       "ciscoMe3400g12CsA": ciscoMe3400g12CsA,
       "ciscoMe3400g12CsD": ciscoMe3400g12CsD,
       "cisco877M": cisco877M,
       "cisco1801M": cisco1801M,
       "catalystWsCBS3040FSC": catalystWsCBS3040FSC,
       "ciscoOe511K9": ciscoOe511K9,
       "ciscoOe611K9": ciscoOe611K9,
       "ciscoOe7326K9": ciscoOe7326K9,
       "ciscoMe492410GE": ciscoMe492410GE,
       "catalyst3750E24TD": catalyst3750E24TD,
       "catalyst3750E48TD": catalyst3750E48TD,
       "catalyst3750E48PD": catalyst3750E48PD,
       "catalyst3750E24PD": catalyst3750E24PD,
       "catalyst3560E24TD": catalyst3560E24TD,
       "catalyst3560E48TD": catalyst3560E48TD,
       "catalyst3560E24PD": catalyst3560E24PD,
       "catalyst3560E48PD": catalyst3560E48PD,
       "catalyst35608PC": catalyst35608PC,
       "catalyst29608TC": catalyst29608TC,
       "catalyst2960G8TC": catalyst2960G8TC,
       "ciscoTSPri": ciscoTSPri,
       "ciscoTSSec": ciscoTSSec,
       "ciscoUWIpPhone7921G": ciscoUWIpPhone7921G,
       "ciscoUWIpPhone7920": ciscoUWIpPhone7920,
       "cisco3200WirelessMic": cisco3200WirelessMic,
       "ciscoISRWireless": ciscoISRWireless,
       "ciscoIPSVirtual": ciscoIPSVirtual,
       "ciscoIDS4215Virtual": ciscoIDS4215Virtual,
       "ciscoIDS4235Virtual": ciscoIDS4235Virtual,
       "ciscoIDS4250Virtual": ciscoIDS4250Virtual,
       "ciscoIDS4250SXVirtual": ciscoIDS4250SXVirtual,
       "ciscoIDS4250XLVirtual": ciscoIDS4250XLVirtual,
       "ciscoIDS4240Virtual": ciscoIDS4240Virtual,
       "ciscoIDS4255Virtual": ciscoIDS4255Virtual,
       "ciscoIDS4260Virtual": ciscoIDS4260Virtual,
       "ciscoIDSIDSM2Virtual": ciscoIDSIDSM2Virtual,
       "ciscoIPSSSM20Virtual": ciscoIPSSSM20Virtual,
       "ciscoIPSSSM10Virtual": ciscoIPSSSM10Virtual,
       "ciscoNMWLCE": ciscoNMWLCE,
       "cisco3205WirelessMic": cisco3205WirelessMic,
       "cisco5720": cisco5720,
       "cisco7201": cisco7201,
       "ciscoCrs14S": ciscoCrs14S,
       "ciscoNmWae": ciscoNmWae,
       "ciscoACE4710K9": ciscoACE4710K9,
       "ciscoMe3400g2csA": ciscoMe3400g2csA,
       "ciscoNmeNam": ciscoNmeNam,
       "ciscoUbr7225Vxr": ciscoUbr7225Vxr,
       "ciscoAirWlc2106K9": ciscoAirWlc2106K9,
       "ciscoMwr1951DC": ciscoMwr1951DC,
       "ciscoIPS4270": ciscoIPS4270,
       "ciscoIPS4270Virtual": ciscoIPS4270Virtual,
       "ciscoWSC6509ve": ciscoWSC6509ve,
       "cisco5740": cisco5740,
       "cisco861": cisco861,
       "cisco866": cisco866,
       "cisco867": cisco867,
       "cisco881": cisco881,
       "cisco881G": cisco881G,
       "ciscoIad881F": ciscoIad881F,
       "cisco881Srst": cisco881Srst,
       "ciscoIad881B": ciscoIad881B,
       "cisco886": cisco886,
       "cisco886G": cisco886G,
       "ciscoIad886F": ciscoIad886F,
       "ciscoIad886B": ciscoIad886B,
       "cisco886Srst": cisco886Srst,
       "cisco887": cisco887,
       "cisco887G": cisco887G,
       "ciscoIad887F": ciscoIad887F,
       "ciscoIad887B": ciscoIad887B,
       "cisco887Srst": cisco887Srst,
       "cisco888": cisco888,
       "cisco888G": cisco888G,
       "ciscoIad888F": ciscoIad888F,
       "ciscoIad888B": ciscoIad888B,
       "cisco888Srst": cisco888Srst,
       "cisco891": cisco891,
       "cisco892": cisco892,
       "cisco885D3": cisco885D3,
       "ciscoIad885FD3": ciscoIad885FD3,
       "cisco885EJ3": cisco885EJ3,
       "cisco7603s": cisco7603s,
       "cisco7606s": cisco7606s,
       "cisco7609s": cisco7609s,
       "cisco7600Seb": cisco7600Seb,
       "ciscoNMECUE": ciscoNMECUE,
       "ciscoAIM2CUE": ciscoAIM2CUE,
       "ciscoUC500": ciscoUC500,
       "cisco860Ap": cisco860Ap,
       "cisco880Ap": cisco880Ap,
       "cisco890Ap": cisco890Ap,
       "cisco1900Ap": cisco1900Ap,
       "cisco340024FSA": cisco340024FSA,
       "catalyst4503e": catalyst4503e,
       "catalyst4506e": catalyst4506e,
       "catalyst4507re": catalyst4507re,
       "catalyst4510re": catalyst4510re,
       "ciscoUC520s8U4FXOK9": ciscoUC520s8U4FXOK9,
       "ciscoUC520s8U4FXOWK9": ciscoUC520s8U4FXOWK9,
       "ciscoUC520s8U2BRIK9": ciscoUC520s8U2BRIK9,
       "ciscoUC520s8U2BRIWK9": ciscoUC520s8U2BRIWK9,
       "ciscoUC520s16U4FXOK9": ciscoUC520s16U4FXOK9,
       "ciscoUC520s16U4FXOWK9": ciscoUC520s16U4FXOWK9,
       "ciscoUC520s16U2BRIK9": ciscoUC520s16U2BRIK9,
       "ciscoUC520s16U2BRIWK9": ciscoUC520s16U2BRIWK9,
       "ciscoUC520m32U8FXOK9": ciscoUC520m32U8FXOK9,
       "ciscoUC520m32U8FXOWK9": ciscoUC520m32U8FXOWK9,
       "ciscoUC520m32U4BRIK9": ciscoUC520m32U4BRIK9,
       "ciscoUC520m32U4BRIWK9": ciscoUC520m32U4BRIWK9,
       "ciscoUC520m48U12FXOK9": ciscoUC520m48U12FXOK9,
       "ciscoUC520m48U12FXOWK9": ciscoUC520m48U12FXOWK9,
       "ciscoUC520m48U6BRIK9": ciscoUC520m48U6BRIK9,
       "ciscoUC520m48U6BRIWK9": ciscoUC520m48U6BRIWK9,
       "ciscoUC520m48U1T1E1FK9": ciscoUC520m48U1T1E1FK9,
       "ciscoUC520m48U1T1E1BK9": ciscoUC520m48U1T1E1BK9,
       "catalyst65xxVirtualSwitch": catalyst65xxVirtualSwitch,
       "catalystExpress5208PC": catalystExpress5208PC,
       "ciscoMCS7816I": ciscoMCS7816I,
       "ciscoMCS7828I": ciscoMCS7828I,
       "ciscoMCS7816H": ciscoMCS7816H,
       "ciscoMCS7828H": ciscoMCS7828H,
       "cisco1861Uc2BK9": cisco1861Uc2BK9,
       "cisco1861Uc4FK9": cisco1861Uc4FK9,
       "cisco1861Srst2BK9": cisco1861Srst2BK9,
       "cisco1861Srst4FK9": cisco1861Srst4FK9,
       "ciscoNmeApa": ciscoNmeApa,
       "ciscoOe7330K9": ciscoOe7330K9,
       "ciscoOe7350K9": ciscoOe7350K9,
       "ciscoWsCbs3110gS": ciscoWsCbs3110gS,
       "ciscoWsCbs3110gSt": ciscoWsCbs3110gSt,
       "ciscoWsCbs3110xS": ciscoWsCbs3110xS,
       "ciscoWsCbs3110xSt": ciscoWsCbs3110xSt,
       "ciscoSce8000": ciscoSce8000,
       "ciscoASA5580": ciscoASA5580,
       "ciscoASA5580sc": ciscoASA5580sc,
       "ciscoASA5580sy": ciscoASA5580sy,
       "cat4900M": cat4900M,
       "catWsCbs3120gS": catWsCbs3120gS,
       "catWsCbs3120xS": catWsCbs3120xS,
       "catWsCbs3032Del": catWsCbs3032Del,
       "catWsCbs3130gS": catWsCbs3130gS,
       "catWsCbs3130xS": catWsCbs3130xS,
       "ciscoASR1002": ciscoASR1002,
       "ciscoASR1004": ciscoASR1004,
       "ciscoASR1006": ciscoASR1006,
       "cisco520WirelessController": cisco520WirelessController,
       "cat296048TCS": cat296048TCS,
       "cat296024TCS": cat296024TCS,
       "cat296024S": cat296024S,
       "cat3560e12d": cat3560e12d,
       "ciscoCatRfgw": ciscoCatRfgw,
       "catExpress52024TT": catExpress52024TT,
       "catExpress52024LC": catExpress52024LC,
       "catExpress52024PC": catExpress52024PC,
       "catExpress520G24TC": catExpress520G24TC,
       "ciscoCDScde100": ciscoCDScde100,
       "ciscoCDScde200": ciscoCDScde200,
       "ciscoCDScde300": ciscoCDScde300,
       "cisco1861SrstCue2BK9": cisco1861SrstCue2BK9,
       "cisco1861SrstCue4FK9": cisco1861SrstCue4FK9,
       "ciscoVFrameDataCenter": ciscoVFrameDataCenter,
       "ciscoVQEServer": ciscoVQEServer,
       "ciscoIPSSSM40Virtual": ciscoIPSSSM40Virtual,
       "ciscoIPSSSM40": ciscoIPSSSM40,
       "ciscoVgd1t3": ciscoVgd1t3,
       "ciscoCBS3100": ciscoCBS3100,
       "ciscoCBS3110": ciscoCBS3110,
       "ciscoCBS3120": ciscoCBS3120,
       "ciscoCBS3130": ciscoCBS3130,
       "catalyst296024PC": catalyst296024PC,
       "catalyst296024LT": catalyst296024LT,
       "catalyst2960PD8TT": catalyst2960PD8TT,
       "ciscoSpa2x1geSynce": ciscoSpa2x1geSynce,
       "ciscoN5kC5020pBa": ciscoN5kC5020pBa,
       "ciscoN5kC5020pBd": ciscoN5kC5020pBd,
       "catalyst3560E12SD": catalyst3560E12SD,
       "ciscoOe674": ciscoOe674,
       "ciscoIE30004TC": ciscoIE30004TC,
       "ciscoIE30008TC": ciscoIE30008TC,
       "ciscoRAIE1783MS06T": ciscoRAIE1783MS06T,
       "ciscoRAIE1783MS10T": ciscoRAIE1783MS10T,
       "cisco2435Iad8fxs": cisco2435Iad8fxs,
       "ciscoVG204": ciscoVG204,
       "ciscoVG202": ciscoVG202,
       "catalyst291824TT": catalyst291824TT,
       "catalyst291824TC": catalyst291824TC,
       "catalyst291848TT": catalyst291848TT,
       "catalyst291848TC": catalyst291848TC,
       "ciscoVQETools": ciscoVQETools,
       "ciscoUC520m24U4BRIK9": ciscoUC520m24U4BRIK9,
       "ciscoUC520m24U8FXOK9": ciscoUC520m24U8FXOK9,
       "ciscoUC520s16U2BRIWK9J": ciscoUC520s16U2BRIWK9J,
       "ciscoUC520s8U2BRIWK9J": ciscoUC520s8U2BRIWK9J,
       "ciscoVSIntSp": ciscoVSIntSp,
       "ciscoVSSP": ciscoVSSP,
       "ciscoVSHydecoder": ciscoVSHydecoder,
       "ciscoVSDecoder": ciscoVSDecoder,
       "ciscoVSEncoder4P": ciscoVSEncoder4P,
       "ciscoVSEncoder1P": ciscoVSEncoder1P,
       "ciscoSCS1000K9": ciscoSCS1000K9,
       "cisco1805": cisco1805,
       "ciscoCe7341": ciscoCe7341,
       "ciscoCe7371": ciscoCe7371,
       "cisco7613s": cisco7613s,
       "ciscoOe574": ciscoOe574,
       "ciscoOe474": ciscoOe474,
       "ciscoOe274": ciscoOe274,
       "ciscoAp801agn": ciscoAp801agn,
       "ciscoAp801gn": ciscoAp801gn,
       "cisco1861WSrstCue4FK9": cisco1861WSrstCue4FK9,
       "cisco1861WSrstCue2BK9": cisco1861WSrstCue2BK9,
       "cisco1861WSrst4FK9": cisco1861WSrst4FK9,
       "cisco1861WSrst2BK9": cisco1861WSrst2BK9,
       "cisco1861WUc4FK9": cisco1861WUc4FK9,
       "cisco1861WUc2BK9": cisco1861WUc2BK9,
       "ciscoCe674": ciscoCe674,
       "ciscoVQEIST": ciscoVQEIST,
       "ciscoAIRAP1160": ciscoAIRAP1160,
       "ciscoWsCbs3012Ibm": ciscoWsCbs3012Ibm,
       "ciscoWsCbs3012IbmI": ciscoWsCbs3012IbmI,
       "ciscoWsCbs3125gS": ciscoWsCbs3125gS,
       "ciscoWsCbs3125xS": ciscoWsCbs3125xS,
       "ciscoTSPriG2": ciscoTSPriG2,
       "catalyst492810GE": catalyst492810GE,
       "catalyst296048TTS": catalyst296048TTS,
       "catalyst29608TCS": catalyst29608TCS,
       "ciscoMe3400eg2csA": ciscoMe3400eg2csA,
       "ciscoMe3400eg12csM": ciscoMe3400eg12csM,
       "ciscoMe3400e24tsM": ciscoMe3400e24tsM,
       "ciscoIPSSSC5Virtual": ciscoIPSSSC5Virtual,
       "ciscoSR520FE": ciscoSR520FE,
       "ciscoSR520ADSL": ciscoSR520ADSL,
       "ciscoSR520ADSLi": ciscoSR520ADSLi,
       "ciscoMwr2941DC": ciscoMwr2941DC,
       "catalyst356012PCS": catalyst356012PCS,
       "catalyst296048PSTL": catalyst296048PSTL,
       "ciscoASR9010": ciscoASR9010,
       "ciscoASR9006": ciscoASR9006,
       "catalyst3560v224tsD": catalyst3560v224tsD,
       "catalyst3560v224ts": catalyst3560v224ts,
       "catalyst3560v224ps": catalyst3560v224ps,
       "catalyst3750v224ts": catalyst3750v224ts,
       "catalyst3750v224ps": catalyst3750v224ps,
       "catalyst3560v248ts": catalyst3560v248ts,
       "catalyst3560v248ps": catalyst3560v248ps,
       "catalyst3750v248ts": catalyst3750v248ts,
       "catalyst3750v248ps": catalyst3750v248ps,
       "ciscoHwicCableD2": ciscoHwicCableD2,
       "ciscoHwicCableEJ2": ciscoHwicCableEJ2,
       "ciscoBr1430": ciscoBr1430,
       "ciscoAIRBR1430": ciscoAIRBR1430,
       "ciscoNamApp2204": ciscoNamApp2204,
       "ciscoNamApp2220": ciscoNamApp2220,
       "ciscoAIRAP1141": ciscoAIRAP1141,
       "ciscoAIRAP1142": ciscoAIRAP1142,
       "ciscoASR14K4S": ciscoASR14K4S,
       "ciscoASR14K8S": ciscoASR14K8S,
       "cisco18xxx": cisco18xxx,
       "ciscoIPSSSC5": ciscoIPSSSC5,
       "cisco887Vdsl2": cisco887Vdsl2,
       "cisco3945": cisco3945,
       "cisco3925": cisco3925,
       "cisco2951": cisco2951,
       "cisco2921": cisco2921,
       "cisco2911": cisco2911,
       "cisco2901": cisco2901,
       "cisco1941": cisco1941,
       "ciscoSm2k15Es1GePoe": ciscoSm2k15Es1GePoe,
       "ciscoSm3k15Es1GePoe": ciscoSm3k15Es1GePoe,
       "ciscoSm3k16GePoe": ciscoSm3k16GePoe,
       "ciscoSm2k23Es1Ge": ciscoSm2k23Es1Ge,
       "ciscoSm2k23Es1GePoe": ciscoSm2k23Es1GePoe,
       "ciscoSm3k23Es1GePoe": ciscoSm3k23Es1GePoe,
       "ciscoSm3k24GePoe": ciscoSm3k24GePoe,
       "ciscoSmXd2k48Es2SFP": ciscoSmXd2k48Es2SFP,
       "ciscoSmXd3k48Es2SFPPoe": ciscoSmXd3k48Es2SFPPoe,
       "ciscoSmXd3k48Ge2SFPPoe": ciscoSmXd3k48Ge2SFPPoe,
       "ciscoEsw52024pK9": ciscoEsw52024pK9,
       "ciscoEsw54024pK9": ciscoEsw54024pK9,
       "ciscoEsw52048pK9": ciscoEsw52048pK9,
       "ciscoEsw52024K9": ciscoEsw52024K9,
       "ciscoEsw54024K9": ciscoEsw54024K9,
       "ciscoEsw52048K9": ciscoEsw52048K9,
       "ciscoEsw54048K9": ciscoEsw54048K9,
       "cisco1861": cisco1861,
       "ciscoUC520": ciscoUC520,
       "catalystWSC2975GS48PSL": catalystWSC2975GS48PSL,
       "catalystC2975Stack": catalystC2975Stack,
       "cisco5500Wlc": cisco5500Wlc,
       "ciscoSR520T1": ciscoSR520T1,
       "ciscoPwrC3900Poe": ciscoPwrC3900Poe,
       "ciscoPwrC3900AC": ciscoPwrC3900AC,
       "ciscoPwrC2921C2951Poe": ciscoPwrC2921C2951Poe,
       "ciscoPwrC2921C2951AC": ciscoPwrC2921C2951AC,
       "ciscoPwrC2911Poe": ciscoPwrC2911Poe,
       "ciscoPwrC2911AC": ciscoPwrC2911AC,
       "ciscoPwrC2901Poe": ciscoPwrC2901Poe,
       "ciscoPwrC1941C2901AC": ciscoPwrC1941C2901AC,
       "ciscoPwrC1941Poe": ciscoPwrC1941Poe,
       "ciscoPwrC3900DC": ciscoPwrC3900DC,
       "ciscoPwrC2921C2951DC": ciscoPwrC2921C2951DC,
       "ciscoPwrC2911DC": ciscoPwrC2911DC,
       "ciscoRpsAdptrC2921C2951": ciscoRpsAdptrC2921C2951,
       "ciscoRpsAdptrC2911": ciscoRpsAdptrC2911,
       "ciscoIPSSSC2": ciscoIPSSSC2,
       "ciscoIPSSSC2Virtual": ciscoIPSSSC2Virtual,
       "catalystWSCBS3140XS": catalystWSCBS3140XS,
       "catalystWSCBS3140GS": catalystWSCBS3140GS,
       "catalystWSCBS3042FSC": catalystWSCBS3042FSC,
       "catalystWSCBS3150XS": catalystWSCBS3150XS,
       "catalystWSCBS3150GS": catalystWSCBS3150GS,
       "catalystWSCBS3052NEC": catalystWSCBS3052NEC,
       "ciscoCBS3140Stack": ciscoCBS3140Stack,
       "ciscoCBS3150Stack": ciscoCBS3150Stack,
       "cisco1941W": cisco1941W,
       "ciscoC888E": ciscoC888E,
       "ciscoC888EG": ciscoC888EG,
       "ciscoIad888EB": ciscoIad888EB,
       "ciscoIad888EF": ciscoIad888EF,
       "ciscoC888ESRST": ciscoC888ESRST,
       "ciscoASA5505W": ciscoASA5505W,
       "cisco3845nv": cisco3845nv,
       "cisco3825nv": cisco3825nv,
       "catalystWSC235048TD": catalystWSC235048TD,
       "cisco887M": cisco887M,
       "ciscoVg250": ciscoVg250,
       "ciscoVg226e": ciscoVg226e,
       "ciscoDsIbm8GfcK9": ciscoDsIbm8GfcK9,
       "ciscoDsHp8GfcK9": ciscoDsHp8GfcK9,
       "ciscoDsDell8GfcK9": ciscoDsDell8GfcK9,
       "ciscoDsC9148K9": ciscoDsC9148K9,
       "ciscoCeVirtualBlade": ciscoCeVirtualBlade,
       "ciscoCDScde420": ciscoCDScde420,
       "ciscoCDScde220": ciscoCDScde220,
       "ciscoCDScde110": ciscoCDScde110,
       "ciscoASR1002F": ciscoASR1002F,
       "ciscoSecureAccessControlSystem": ciscoSecureAccessControlSystem,
       "cisco861Npe": cisco861Npe,
       "cisco881Npe": cisco881Npe,
       "cisco881GNpe": cisco881GNpe,
       "cisco887Npe": cisco887Npe,
       "cisco888GNpe": cisco888GNpe,
       "cisco891Npe": cisco891Npe,
       "ciscoAIRAP3501": ciscoAIRAP3501,
       "ciscoAIRAP3502": ciscoAIRAP3502,
       "ciscoCDScde400": ciscoCDScde400,
       "ciscoSA520K9": ciscoSA520K9,
       "ciscoSA520WK9": ciscoSA520WK9,
       "ciscoSA540K9": ciscoSA540K9,
       "ciscoSps2004B": ciscoSps2004B,
       "ciscoSps204B": ciscoSps204B,
       "ciscoUC560T1E1K9": ciscoUC560T1E1K9,
       "ciscoUC560BRIK9": ciscoUC560BRIK9,
       "ciscoUC560FXOK9": ciscoUC560FXOK9,
       "ciscoAp541nAK9": ciscoAp541nAK9,
       "ciscoAp541nEK9": ciscoAp541nEK9,
       "ciscoAp541nNK9": ciscoAp541nNK9,
       "cisco887GVdsl2": cisco887GVdsl2,
       "cisco887SrstVdsl2": cisco887SrstVdsl2,
       "ciscoUc540wFxoK9": ciscoUc540wFxoK9,
       "ciscoUc540wBriK9": ciscoUc540wBriK9,
       "ciscoCaServer": ciscoCaServer,
       "ciscoCaManager": ciscoCaManager,
       "cisco3925SPE200": cisco3925SPE200,
       "cisco3945SPE250": cisco3945SPE250,
       "catalyst296024LCS": catalyst296024LCS,
       "catalyst296024PCS": catalyst296024PCS,
       "catalyst296048PSTS": catalyst296048PSTS,
       "ciscoISM": ciscoISM,
       "ciscoSM": ciscoSM,
       "ciscoNMEAXP": ciscoNMEAXP,
       "ciscoAIMAXP": ciscoAIMAXP,
       "ciscoAIM2AXP": ciscoAIM2AXP,
       "ciscoSRP521": ciscoSRP521,
       "ciscoSRP526": ciscoSRP526,
       "ciscoSRP527": ciscoSRP527,
       "ciscoSRP541": ciscoSRP541,
       "ciscoSRP546": ciscoSRP546,
       "ciscoSRP547": ciscoSRP547,
       "ciscoVS510FXO": ciscoVS510FXO,
       "ciscoNmWae900": ciscoNmWae900,
       "ciscoNmWae700": ciscoNmWae700,
       "cisco5940RA": cisco5940RA,
       "cisco5940RC": cisco5940RC,
       "ciscoASR1001": ciscoASR1001,
       "ciscoASR1013": ciscoASR1013,
       "ciscoCDScde205": ciscoCDScde205,
       "ciscoPwr1941AC": ciscoPwr1941AC,
       "ciscoNamWaasVirtualBlade": ciscoNamWaasVirtualBlade,
       "ciscoRaie1783Rms06t": ciscoRaie1783Rms06t,
       "ciscoRaie1783Rms10t": ciscoRaie1783Rms10t,
       "cisco1941WEK9": cisco1941WEK9,
       "cisco1941WPK9": cisco1941WPK9,
       "cisco1941WNK9": cisco1941WNK9,
       "ciscoMXE5600": ciscoMXE5600,
       "ciscoEsw5408pK9": ciscoEsw5408pK9,
       "ciscoEsw5208pK9": ciscoEsw5208pK9,
       "catalyst4948e10GE": catalyst4948e10GE,
       "cat2960x48tsS": cat2960x48tsS,
       "cat2960x24tsS": cat2960x24tsS,
       "cat2960xs48fpdL": cat2960xs48fpdL,
       "cat2960xs48lpdL": cat2960xs48lpdL,
       "cat2960xs48ltdL": cat2960xs48ltdL,
       "cat2960xs24pdL": cat2960xs24pdL,
       "cat2960xs24tdL": cat2960xs24tdL,
       "cat2960xs48fpsL": cat2960xs48fpsL,
       "cat2960xs48lpsL": cat2960xs48lpsL,
       "cat2960xs24psL": cat2960xs24psL,
       "cat2960xs48tsL": cat2960xs48tsL,
       "cat2960xs24tsL": cat2960xs24tsL,
       "cisco1921k9": cisco1921k9,
       "cisco1905k9": cisco1905k9,
       "ciscoPwrC1921C1905AC": ciscoPwrC1921C1905AC,
       "ciscoASA5585Ssp10": ciscoASA5585Ssp10,
       "ciscoASA5585Ssp20": ciscoASA5585Ssp20,
       "ciscoASA5585Ssp40": ciscoASA5585Ssp40,
       "ciscoASA5585Ssp60": ciscoASA5585Ssp60,
       "ciscoASA5585Ssp10sc": ciscoASA5585Ssp10sc,
       "ciscoASA5585Ssp20sc": ciscoASA5585Ssp20sc,
       "ciscoASA5585Ssp40sc": ciscoASA5585Ssp40sc,
       "ciscoASA5585Ssp60sc": ciscoASA5585Ssp60sc,
       "ciscoASA5585Ssp10sy": ciscoASA5585Ssp10sy,
       "ciscoASA5585Ssp20sy": ciscoASA5585Ssp20sy,
       "ciscoASA5585Ssp40sy": ciscoASA5585Ssp40sy,
       "ciscoASA5585Ssp60sy": ciscoASA5585Ssp60sy,
       "cisco3925SPE250": cisco3925SPE250,
       "cisco3945SPE200": cisco3945SPE200,
       "cat29xxStack": cat29xxStack,
       "ciscoOeNm302": ciscoOeNm302,
       "ciscoOeNm502": ciscoOeNm502,
       "ciscoOeNm522": ciscoOeNm522,
       "ciscoOeSmSre700": ciscoOeSmSre700,
       "ciscoOeSmSre900": ciscoOeSmSre900,
       "ciscoVsaNam": ciscoVsaNam,
       "ciscoMwr2941DCA": ciscoMwr2941DCA,
       "ciscoN7KC7018IOS": ciscoN7KC7018IOS,
       "ciscoN7KC7010IOS": ciscoN7KC7010IOS,
       "ciscoN4KDellEth": ciscoN4KDellEth,
       "ciscoN4KDellCiscoEth": ciscoN4KDellCiscoEth,
       "cisco1941WCK9": cisco1941WCK9,
       "ciscoCDScde2202s3": ciscoCDScde2202s3,
       "cat3750x24": cat3750x24,
       "cat3750x48": cat3750x48,
       "cat3750x24P": cat3750x24P,
       "cat3750x48P": cat3750x48P,
       "cat3560x24": cat3560x24,
       "cat3560x48": cat3560x48,
       "cat3560x24P": cat3560x24P,
       "cat3560x48P": cat3560x48P,
       "ciscoNMEAIR": ciscoNMEAIR,
       "ciscoACE30K9": ciscoACE30K9,
       "ciscoASA5585SspIps10": ciscoASA5585SspIps10,
       "ciscoASA5585SspIps20": ciscoASA5585SspIps20,
       "ciscoASA5585SspIps40": ciscoASA5585SspIps40,
       "ciscoASA5585SspIps60": ciscoASA5585SspIps60,
       "cisco1841CK9": cisco1841CK9,
       "cisco2801CK9": cisco2801CK9,
       "cisco2811CK9": cisco2811CK9,
       "cisco2821CK9": cisco2821CK9,
       "cisco2851CK9": cisco2851CK9,
       "cisco3825CK9": cisco3825CK9,
       "cisco3845CK9": cisco3845CK9,
       "cisco3825CnvK9": cisco3825CnvK9,
       "cisco3845CnvK9": cisco3845CnvK9,
       "ciscoCGS252024TC": ciscoCGS252024TC,
       "ciscoCGS252016S8PC": ciscoCGS252016S8PC,
       "ciscoAIRAP1262": ciscoAIRAP1262,
       "ciscoAIRAP1261": ciscoAIRAP1261,
       "cisco892F": cisco892F,
       "ciscoMe3600x24fsM": ciscoMe3600x24fsM,
       "ciscoMe3600x24tsM": ciscoMe3600x24tsM,
       "ciscoMe3800x24fsM": ciscoMe3800x24fsM,
       "ciscoCGR2010": ciscoCGR2010,
       "ciscoPwrCGR20xxCGS25xxPoeAC": ciscoPwrCGR20xxCGS25xxPoeAC,
       "ciscoPwrCGR20xxCGS25xxPoeDC": ciscoPwrCGR20xxCGS25xxPoeDC,
       "catWsC2960s48tsS": catWsC2960s48tsS,
       "catWsC2960s24tsS": catWsC2960s24tsS,
       "catWsC2960s48fpdL": catWsC2960s48fpdL,
       "catWsC2960s48ldpL": catWsC2960s48ldpL,
       "catWsC2960s48tdL": catWsC2960s48tdL,
       "catWsC2960s24pdL": catWsC2960s24pdL,
       "catWsC2960s24tdL": catWsC2960s24tdL,
       "catWsC2960s48fpsL": catWsC2960s48fpsL,
       "catWsC2960s48lpsL": catWsC2960s48lpsL,
       "catWsC2960s24psL": catWsC2960s24psL,
       "catWsC2960s48tsL": catWsC2960s48tsL,
       "catWsC2960s24tsL": catWsC2960s24tsL,
       "cisco1906CK9": cisco1906CK9,
       "ciscoAIRAP1042": ciscoAIRAP1042,
       "ciscoAIRAP1041": ciscoAIRAP1041,
       "cisco887VaM": cisco887VaM,
       "cisco867Va": cisco867Va,
       "cisco886Va": cisco886Va,
       "cisco887Va": cisco887Va,
       "ciscoASASm1sc": ciscoASASm1sc,
       "ciscoASASm1sy": ciscoASASm1sy,
       "ciscoASASm1": ciscoASASm1,
       "cat2960cPD8TT": cat2960cPD8TT,
       "ciscoAirCt2504K9": ciscoAirCt2504K9,
       "ciscoISMAXP": ciscoISMAXP,
       "ciscoSMAXP": ciscoSMAXP,
       "ciscoAxpSmSre900": ciscoAxpSmSre900,
       "ciscoAxpSmSre700": ciscoAxpSmSre700,
       "ciscoAxpIsmSre300": ciscoAxpIsmSre300,
       "ciscoCDSISM": ciscoCDSISM,
       "cat4507rpluse": cat4507rpluse,
       "cat4510rpluse": cat4510rpluse,
       "ciscoAxpNme302": ciscoAxpNme302,
       "ciscoAxpNme502": ciscoAxpNme502,
       "ciscoAxpNme522": ciscoAxpNme522,
       "ciscoACE20K9": ciscoACE20K9,
       "ciscoWsC236048tdS": ciscoWsC236048tdS,
       "ciscoWiSM2": ciscoWiSM2,
       "ciscoCDScde250": ciscoCDScde250,
       "cisco7500Wlc": cisco7500Wlc,
       "ciscoAnmVirtualApp": ciscoAnmVirtualApp,
       "ciscoECDS3100": ciscoECDS3100,
       "ciscoECDS1100": ciscoECDS1100,
       "cisco881G2": cisco881G2,
       "catWsC3750v224fsS": catWsC3750v224fsS,
       "ciscoOeVWaas": ciscoOeVWaas,
       "ciscoASA5585Ssp10K7": ciscoASA5585Ssp10K7,
       "ciscoASA5585Ssp20K7": ciscoASA5585Ssp20K7,
       "ciscoASA5585Ssp40K7": ciscoASA5585Ssp40K7,
       "ciscoASA5585Ssp60K7": ciscoASA5585Ssp60K7,
       "ciscoASA5585Ssp10K7sc": ciscoASA5585Ssp10K7sc,
       "ciscoASA5585Ssp20K7sc": ciscoASA5585Ssp20K7sc,
       "ciscoASA5585Ssp40K7sc": ciscoASA5585Ssp40K7sc,
       "ciscoASA5585Ssp60K7sc": ciscoASA5585Ssp60K7sc,
       "ciscoASA5585Ssp10K7sy": ciscoASA5585Ssp10K7sy,
       "ciscoASA5585Ssp20K7sy": ciscoASA5585Ssp20K7sy,
       "ciscoASA5585Ssp40K7sy": ciscoASA5585Ssp40K7sy,
       "ciscoASA5585Ssp60K7sy": ciscoASA5585Ssp60K7sy,
       "ciscoSreSmNam": ciscoSreSmNam,
       "cat2960cPD8PT": cat2960cPD8PT,
       "cat2960cG8TC": cat2960cG8TC,
       "cat3560cG8PC": cat3560cG8PC,
       "cat3560cG8TC": cat3560cG8TC,
       "ciscoIE301016S8PC": ciscoIE301016S8PC,
       "ciscoIE301024TC": ciscoIE301024TC,
       "ciscoRAIE1783RMSB10T": ciscoRAIE1783RMSB10T,
       "ciscoRAIE1783RMSB06T": ciscoRAIE1783RMSB06T,
       "ciscoASA5585SspIps10K7": ciscoASA5585SspIps10K7,
       "ciscoASA5585SspIps20K7": ciscoASA5585SspIps20K7,
       "ciscoASA5585SspIps40K7": ciscoASA5585SspIps40K7,
       "ciscoASA5585SspIps60K7": ciscoASA5585SspIps60K7,
       "catalyst4948ef10GE": catalyst4948ef10GE,
       "cat292824TCC": cat292824TCC,
       "cat292848TCC": cat292848TCC,
       "cat292824LTC": cat292824LTC,
       "ciscoCrs16SB": ciscoCrs16SB,
       "ciscoQuad": ciscoQuad,
       "ciscoASASm1K7sc": ciscoASASm1K7sc,
       "ciscoASASm1K7sy": ciscoASASm1K7sy,
       "ciscoASASm1K7": ciscoASASm1K7,
       "ciscoPwrCGR2010PoeAC": ciscoPwrCGR2010PoeAC,
       "ciscoPwrCGR2010PoeDC": ciscoPwrCGR2010PoeDC,
       "cisco1861eUc2BK9": cisco1861eUc2BK9,
       "cisco1861eUc4FK9": cisco1861eUc4FK9,
       "ciscoC1861eSrstFK9": ciscoC1861eSrstFK9,
       "ciscoC1861eSrstBK9": ciscoC1861eSrstBK9,
       "ciscoC1861eSrstCFK9": ciscoC1861eSrstCFK9,
       "ciscoC1861eSrstCBK9": ciscoC1861eSrstCBK9,
       "ciscoGrwicDes6s": ciscoGrwicDes6s,
       "ciscoGrwicDes2s8pc": ciscoGrwicDes2s8pc,
       "ciscoUCVirtualMachine": ciscoUCVirtualMachine,
       "ciscoWave8541": ciscoWave8541,
       "ciscoWave7571": ciscoWave7571,
       "ciscoWave7541": ciscoWave7541,
       "ciscoWave694": ciscoWave694,
       "ciscoWave594": ciscoWave594,
       "ciscoWave294": ciscoWave294,
       "cisco5915RC": cisco5915RC,
       "cisco5915RA": cisco5915RA,
       "cisco867VAEK9": cisco867VAEK9,
       "cisco866VAEK9": cisco866VAEK9,
       "cisco867VAE": cisco867VAE,
       "cisco866VAE": cisco866VAE,
       "ciscoAp802gn": ciscoAp802gn,
       "ciscoAp802agn": ciscoAp802agn,
       "catwsC2960C8tcS": catwsC2960C8tcS,
       "catwsC2960C8tcL": catwsC2960C8tcL,
       "catwsC2960C8pcL": catwsC2960C8pcL,
       "catwsC2960C12pcL": catwsC2960C12pcL,
       "catwsC3560CPD8ptS": catwsC3560CPD8ptS,
       "cisco1841ve": cisco1841ve,
       "cisco2811ve": cisco2811ve,
       "cisco881WAK9": cisco881WAK9,
       "cisco881WEK9": cisco881WEK9,
       "cisco881WPK9": cisco881WPK9,
       "cisco886VaWEK9": cisco886VaWEK9,
       "cisco887VamWEK9": cisco887VamWEK9,
       "cisco887VaWAK9": cisco887VaWAK9,
       "cisco887VaWEK9": cisco887VaWEK9,
       "cisco819GUK9": cisco819GUK9,
       "cisco819GSK9": cisco819GSK9,
       "cisco819GVK9": cisco819GVK9,
       "cisco819GBK9": cisco819GBK9,
       "cisco819G7AK9": cisco819G7AK9,
       "cisco819G7K9": cisco819G7K9,
       "cisco819HGUK9": cisco819HGUK9,
       "cisco819HGSK9": cisco819HGSK9,
       "cisco819HGVK9": cisco819HGVK9,
       "cisco819HGBK9": cisco819HGBK9,
       "cisco819HG7AK9": cisco819HG7AK9,
       "cisco819HG7K9": cisco819HG7K9,
       "cisco886Vag7K9": cisco886Vag7K9,
       "cisco887VagSK9": cisco887VagSK9,
       "cisco887Vag7K9": cisco887Vag7K9,
       "cisco887Vamg7K9": cisco887Vamg7K9,
       "cisco888Eg7K9": cisco888Eg7K9,
       "cisco881GUK9": cisco881GUK9,
       "cisco881GSK9": cisco881GSK9,
       "cisco881GVK9": cisco881GVK9,
       "cisco881GBK9": cisco881GBK9,
       "cisco881G7K9": cisco881G7K9,
       "cisco881G7AK9": cisco881G7AK9,
       "cat3750x24s": cat3750x24s,
       "cat3750x12s": cat3750x12s,
       "ciscoNME": ciscoNME,
       "ciscoASA5512": ciscoASA5512,
       "ciscoASA5525": ciscoASA5525,
       "ciscoASA5545": ciscoASA5545,
       "ciscoASA5555": ciscoASA5555,
       "ciscoASA5512sc": ciscoASA5512sc,
       "ciscoASA5525sc": ciscoASA5525sc,
       "ciscoASA5545sc": ciscoASA5545sc,
       "ciscoASA5555sc": ciscoASA5555sc,
       "ciscoASA5512sy": ciscoASA5512sy,
       "ciscoASA5515sy": ciscoASA5515sy,
       "ciscoASA5525sy": ciscoASA5525sy,
       "ciscoASA5545sy": ciscoASA5545sy,
       "ciscoASA5555sy": ciscoASA5555sy,
       "ciscoASA5515sc": ciscoASA5515sc,
       "ciscoASA5515": ciscoASA5515,
       "ciscoPCM": ciscoPCM,
       "ciscoIse3315K9": ciscoIse3315K9,
       "ciscoIse3395K9": ciscoIse3395K9,
       "ciscoIse3355K9": ciscoIse3355K9,
       "ciscoIseVmK9": ciscoIseVmK9,
       "ciscoIPS4345": ciscoIPS4345,
       "ciscoIPS4360": ciscoIPS4360,
       "ciscoEcdsVB": ciscoEcdsVB,
       "ciscoTsCodecG2": ciscoTsCodecG2,
       "ciscoTsCodecG2C": ciscoTsCodecG2C,
       "ciscoTSCodecG2RC": ciscoTSCodecG2RC,
       "ciscoTSCodecG2R": ciscoTSCodecG2R,
       "ciscoASA5585SspIps10Virtual": ciscoASA5585SspIps10Virtual,
       "ciscoASA5585SspIps20Virtual": ciscoASA5585SspIps20Virtual,
       "ciscoASA5585SspIps40Virtual": ciscoASA5585SspIps40Virtual,
       "ciscoASA5585SspIps60Virtual": ciscoASA5585SspIps60Virtual,
       "ciscoASR903": ciscoASR903,
       "ciscoASA5512K7": ciscoASA5512K7,
       "ciscoASA5515K7": ciscoASA5515K7,
       "ciscoASA5525K7": ciscoASA5525K7,
       "ciscoASA5545K7": ciscoASA5545K7,
       "ciscoASA5555K7": ciscoASA5555K7,
       "ciscoASA5512K7sc": ciscoASA5512K7sc,
       "ciscoASA5515K7sc": ciscoASA5515K7sc,
       "ciscoASA5525K7sc": ciscoASA5525K7sc,
       "ciscoASA5545K7sc": ciscoASA5545K7sc,
       "ciscoASA5555K7sc": ciscoASA5555K7sc,
       "ciscoASA5512K7sy": ciscoASA5512K7sy,
       "ciscoASA5515K7sy": ciscoASA5515K7sy,
       "ciscoASA5525K7sy": ciscoASA5525K7sy,
       "ciscoASA5545K7sy": ciscoASA5545K7sy,
       "ciscoASA5555K7sy": ciscoASA5555K7sy,
       "ciscoASR5500": ciscoASR5500,
       "ciscoXfp10Ger192IrL": ciscoXfp10Ger192IrL,
       "ciscoXfp10Glr192SrL": ciscoXfp10Glr192SrL,
       "ciscoXfp10Gzr192LrL": ciscoXfp10Gzr192LrL,
       "catwsC3560C12pcS": catwsC3560C12pcS,
       "catwsC3560C8pcS": catwsC3560C8pcS,
       "ciscoCRSFabBP": ciscoCRSFabBP,
       "ciscoIE20004TS": ciscoIE20004TS,
       "ciscoIE20004T": ciscoIE20004T,
       "ciscoIE20004TSG": ciscoIE20004TSG,
       "ciscoIE20004TG": ciscoIE20004TG,
       "ciscoIE20008TC": ciscoIE20008TC,
       "ciscoIE20008TCG": ciscoIE20008TCG,
       "ciscoIE200016TC": ciscoIE200016TC,
       "ciscoIE200016TCG": ciscoIE200016TCG,
       "ciscoRAIE1783BMS06SL": ciscoRAIE1783BMS06SL,
       "ciscoRAIE1783BMS06TL": ciscoRAIE1783BMS06TL,
       "ciscoRAIE1783BMS06TA": ciscoRAIE1783BMS06TA,
       "ciscoRAIE1783BMS06SGL": ciscoRAIE1783BMS06SGL,
       "ciscoRAIE1783BMS06SGA": ciscoRAIE1783BMS06SGA,
       "ciscoRAIE1783BMS06TGL": ciscoRAIE1783BMS06TGL,
       "ciscoRAIE1783BMS06TGA": ciscoRAIE1783BMS06TGA,
       "ciscoRAIE1783BMS10CL": ciscoRAIE1783BMS10CL,
       "ciscoRAIE1783BMS10CA": ciscoRAIE1783BMS10CA,
       "ciscoRAIE1783BMS10CGL": ciscoRAIE1783BMS10CGL,
       "ciscoRAIE1783BMS10CGA": ciscoRAIE1783BMS10CGA,
       "ciscoRAIE1783BMS10CGP": ciscoRAIE1783BMS10CGP,
       "ciscoRAIE1783BMS10CGN": ciscoRAIE1783BMS10CGN,
       "ciscoRAIE1783BMS20CL": ciscoRAIE1783BMS20CL,
       "ciscoRAIE1783BMS20CA": ciscoRAIE1783BMS20CA,
       "ciscoRAIE1783BMS20CGL": ciscoRAIE1783BMS20CGL,
       "ciscoRAIE1783BMS20CGP": ciscoRAIE1783BMS20CGP,
       "ciscoRAIE1783BMS20CGPK": ciscoRAIE1783BMS20CGPK,
       "cisco819HG4GGK9": cisco819HG4GGK9,
       "cisco819G4GAK9": cisco819G4GAK9,
       "cisco819G4GVK9": cisco819G4GVK9,
       "cisco819G4GGK9": cisco819G4GGK9,
       "ciscoUcsC200": ciscoUcsC200,
       "ciscoUcsC210": ciscoUcsC210,
       "ciscoUcsC250": ciscoUcsC250,
       "ciscoUcsC260": ciscoUcsC260,
       "ciscoUcsC460": ciscoUcsC460,
       "ciscoRAIE1783BMS06SA": ciscoRAIE1783BMS06SA,
       "ciscoIE200016TCGX": ciscoIE200016TCGX,
       "ciscoASR901": ciscoASR901,
       "ciscoASR901E": ciscoASR901E,
       "ciscoOeSmSre910": ciscoOeSmSre910,
       "ciscoOeSmSre710": ciscoOeSmSre710,
       "ciscoASR1002X": ciscoASR1002X,
       "ciscoNam2304": ciscoNam2304,
       "ciscoNam2320": ciscoNam2320,
       "ciscoNam3": ciscoNam3,
       "cisco819HG4GAK9": cisco819HG4GAK9,
       "ciscoECDS50IVB": ciscoECDS50IVB,
       "ciscoCSR1000v": ciscoCSR1000v,
       "ciscoASR5000": ciscoASR5000,
       "ciscoflowAgent3000": ciscoflowAgent3000,
       "ciscoTelePresenceMCU5310": ciscoTelePresenceMCU5310,
       "ciscoTelePresenceMCU5320": ciscoTelePresenceMCU5320,
       "cisco888ea": cisco888ea,
       "ciscoVG350": ciscoVG350,
       "cisco881GW7AK9": cisco881GW7AK9,
       "cisco881GW7EK9": cisco881GW7EK9,
       "cisco881GWSAK9": cisco881GWSAK9,
       "cisco881GWVAK9": cisco881GWVAK9,
       "cisco887Vagw7AK9": cisco887Vagw7AK9,
       "cisco887Vagw7EK9": cisco887Vagw7EK9,
       "cisco881WDAK9": cisco881WDAK9,
       "cisco881WDEK9": cisco881WDEK9,
       "cisco887VaWDAK9": cisco887VaWDAK9,
       "cisco887VaWDEK9": cisco887VaWDEK9,
       "cisco819HGW7EK9": cisco819HGW7EK9,
       "cisco819HGW7NK9": cisco819HGW7NK9,
       "cisco819HGW7AAK9": cisco819HGW7AAK9,
       "cisco819HGWVAK9": cisco819HGWVAK9,
       "cisco819HGWSAK9": cisco819HGWSAK9,
       "cisco819HK9": cisco819HK9,
       "cisco819HWDEK9": cisco819HWDEK9,
       "cisco819HWDAK9": cisco819HWDAK9,
       "cisco812G7K9": cisco812G7K9,
       "cisco812GCIFI7EK9": cisco812GCIFI7EK9,
       "cisco812GCIFI7NK9": cisco812GCIFI7NK9,
       "cisco812GCIFIVAK9": cisco812GCIFIVAK9,
       "cisco812GCIFISAK9": cisco812GCIFISAK9,
       "cisco819GUMK9": cisco819GUMK9,
       "cisco819GSMK9": cisco819GSMK9,
       "cisco819GVMK9": cisco819GVMK9,
       "cisco819GBMK9": cisco819GBMK9,
       "cisco819G7AMK9": cisco819G7AMK9,
       "cisco819G7MK9": cisco819G7MK9,
       "cisco819HGUMK9": cisco819HGUMK9,
       "cisco819HGSMK9": cisco819HGSMK9,
       "cisco819HGVMK9": cisco819HGVMK9,
       "cisco819HGBMK9": cisco819HGBMK9,
       "cisco819HG7AMK9": cisco819HG7AMK9,
       "cisco819HG7MK9": cisco819HG7MK9,
       "ciscoCDScde2502s6": ciscoCDScde2502s6,
       "ciscoCDScde2502m0": ciscoCDScde2502m0,
       "ciscoCDScde2502s8": ciscoCDScde2502s8,
       "cisco881V": cisco881V,
       "cisco887vaV": cisco887vaV,
       "cisco887vaVW": cisco887vaVW,
       "ciscoMDE10XVB": ciscoMDE10XVB,
       "cat4500X16": cat4500X16,
       "cat4500X32": cat4500X32,
       "ciscoCDScde2502s9": ciscoCDScde2502s9,
       "ciscoCDScde2502s10": ciscoCDScde2502s10,
       "ciscoASA5585Nm20x1GE": ciscoASA5585Nm20x1GE,
       "ciscoCDScdeGeneric": ciscoCDScdeGeneric,
       "ciscoASA1000Vsy": ciscoASA1000Vsy,
       "ciscoASA1000Vsc": ciscoASA1000Vsc,
       "ciscoASA1000V": ciscoASA1000V,
       "cisco8500WLC": cisco8500WLC,
       "ciscoASA5585Nm8x10GE": ciscoASA5585Nm8x10GE,
       "ciscoASA5585Nm4x10GE": ciscoASA5585Nm4x10GE,
       "ciscoISR4400": ciscoISR4400,
       "cisco892FspK9": cisco892FspK9,
       "cisco897VaMK9": cisco897VaMK9,
       "cisco897VawEK9": cisco897VawEK9,
       "cisco897VawAK9": cisco897VawAK9,
       "cisco897VaK9": cisco897VaK9,
       "cisco896VaK9": cisco896VaK9,
       "ciscoVirtualWlc": ciscoVirtualWlc,
       "ciscoAIRAP802agn": ciscoAIRAP802agn,
       "ciscoAp802Hagn": ciscoAp802Hagn,
       "ciscoE160DP": ciscoE160DP,
       "ciscoE160D": ciscoE160D,
       "ciscoE140DP": ciscoE140DP,
       "ciscoE140D": ciscoE140D,
       "ciscoE140S": ciscoE140S,
       "ciscoASR9001": ciscoASR9001,
       "ciscoASR9922": ciscoASR9922,
       "cat385048P": cat385048P,
       "cat385024P": cat385024P,
       "cat385048": cat385048,
       "cat385024": cat385024,
       "cisco5760wlc": cisco5760wlc,
       "ciscoVSGateway": ciscoVSGateway,
       "ciscoIbiza": ciscoIbiza,
       "ciscoSkyros": ciscoSkyros,
       "ciscoAIRAP1601": ciscoAIRAP1601,
       "ciscoAIRAP2600": ciscoAIRAP2600,
       "ciscoCRS8SB": ciscoCRS8SB,
       "ciscoAIRAP2602": ciscoAIRAP2602,
       "ciscoAIRAP1602": ciscoAIRAP1602,
       "ciscoAIRAP3602": ciscoAIRAP3602,
       "ciscoAIRAP3601": ciscoAIRAP3601,
       "ciscoAIRAP1552": ciscoAIRAP1552,
       "ciscoAIRAP1553": ciscoAIRAP1553,
       "ciscoNgsm3k16gepoeplus": ciscoNgsm3k16gepoeplus,
       "ciscoNexus1010X": ciscoNexus1010X,
       "ciscoNexus1110S": ciscoNexus1110S,
       "ciscoNexus1110X": ciscoNexus1110X,
       "ciscoNexus1110XL": ciscoNexus1110XL,
       "ciscoHsE300K9": ciscoHsE300K9,
       "cisco866VAEWEK9": cisco866VAEWEK9,
       "cisco867VAEWAK9": cisco867VAEWAK9,
       "cisco867VAEWEK9": cisco867VAEWEK9,
       "cisco867VAEPOEWAK9": cisco867VAEPOEWAK9,
       "ciscoSmES3x24P": ciscoSmES3x24P,
       "ciscoSmDES3x48P": ciscoSmDES3x48P,
       "ciscoOeKWaas": ciscoOeKWaas,
       "ciscoUcsC220": ciscoUcsC220,
       "ciscoUcsC240": ciscoUcsC240,
       "ciscoUcsC22": ciscoUcsC22,
       "ciscoUcsC24": ciscoUcsC24,
       "ciscoCDScde2202s4": ciscoCDScde2202s4,
       "ciscoCDScde4604r1": ciscoCDScde4604r1,
       "ciscoASR1002XC": ciscoASR1002XC,
       "catWsC2960x48fpdL": catWsC2960x48fpdL,
       "catWsC2960x48lpdL": catWsC2960x48lpdL,
       "catWsC2960x48tdL": catWsC2960x48tdL,
       "catWsC2960x24pdL": catWsC2960x24pdL,
       "catWsC2960x24tdL": catWsC2960x24tdL,
       "catWsC2960x48fpsL": catWsC2960x48fpsL,
       "catWsC2960x48lpsL": catWsC2960x48lpsL,
       "catWsC2960x24psL": catWsC2960x24psL,
       "catWsC2960x48tsL": catWsC2960x48tsL,
       "catWsC2960x24tsL": catWsC2960x24tsL,
       "catWsC2960x24psqL": catWsC2960x24psqL,
       "catWsC2960x48lpsS": catWsC2960x48lpsS,
       "catWsC2960x24psS": catWsC2960x24psS,
       "catWsC2960x48tsLL": catWsC2960x48tsLL,
       "catWsC2960x24tsLL": catWsC2960x24tsLL,
       "ciscoISR4441": ciscoISR4441,
       "ciscoISR4442": ciscoISR4442,
       "ciscoISR4451": ciscoISR4451,
       "ciscoISR4452": ciscoISR4452,
       "ciscoASR9912": ciscoASR9912,
       "cat3560x48U": cat3560x48U,
       "cat3560x24U": cat3560x24U,
       "cat3750x48U": cat3750x48U,
       "cat3750x24U": cat3750x24U,
       "ciscoIE20008TCGN": ciscoIE20008TCGN,
       "ciscoIE200016TCGN": ciscoIE200016TCGN,
       "ciscoIem30004SM": ciscoIem30004SM,
       "ciscoIem30008SM": ciscoIem30008SM,
       "cisco1783MX04S": cisco1783MX04S,
       "cisco1783MX08S": cisco1783MX08S,
       "ciscoASR901TenGigDCE": ciscoASR901TenGigDCE,
       "ciscoASR901TenGigACE": ciscoASR901TenGigACE,
       "ciscoASR901TenGigDC": ciscoASR901TenGigDC,
       "ciscoASR901TenGigAC": ciscoASR901TenGigAC,
       "ciscoIE200016TCGP": ciscoIE200016TCGP,
       "ciscoIE200016TCGEP": ciscoIE200016TCGEP,
       "ciscoIE200016TCGNXP": ciscoIE200016TCGNXP,
       "cat4xxxVirtualSwitch": cat4xxxVirtualSwitch,
       "ciscoRAIE1783BMS20CGN": ciscoRAIE1783BMS20CGN,
       "ciscoRAIE1783BMS12T4E2CGP": ciscoRAIE1783BMS12T4E2CGP,
       "ciscoRAIE1783BMS12T4E2CGNK": ciscoRAIE1783BMS12T4E2CGNK,
       "ciscoMds9848512K9SM": ciscoMds9848512K9SM,
       "ciscoMds9710SM": ciscoMds9710SM,
       "ciscoMds9710FM": ciscoMds9710FM,
       "ciscoMds9710FCS": ciscoMds9710FCS,
       "ciscoMDS9250iIFSPS": ciscoMDS9250iIFSPS,
       "ciscoMDS9250iIFSDC": ciscoMDS9250iIFSDC,
       "ciscoMDS9250iIFS": ciscoMDS9250iIFS,
       "ciscoNexus1000VH": ciscoNexus1000VH,
       "cat38xxstack": cat38xxstack,
       "ciscoVG202XM": ciscoVG202XM,
       "ciscoVG204XM": ciscoVG204XM,
       "ciscoWsC2960P48PstL": ciscoWsC2960P48PstL,
       "ciscoWsC2960P24PcL": ciscoWsC2960P24PcL,
       "ciscoWsC2960P24LcL": ciscoWsC2960P24LcL,
       "ciscoWsC2960P48TcL": ciscoWsC2960P48TcL,
       "ciscoWsC2960P24TcL": ciscoWsC2960P24TcL,
       "ciscoWsC2960P48PstS": ciscoWsC2960P48PstS,
       "ciscoWsC2960P24PcS": ciscoWsC2960P24PcS,
       "ciscoWsC2960P24LcS": ciscoWsC2960P24LcS,
       "ciscoWsC2960P48TcS": ciscoWsC2960P48TcS,
       "ciscoWsC2960P24TcS": ciscoWsC2960P24TcS,
       "ciscoASR9904": ciscoASR9904,
       "ciscoME2600X": ciscoME2600X,
       "ciscoPanini": ciscoPanini,
       "ciscoC6807xl": ciscoC6807xl,
       "cat385024U": cat385024U,
       "cat385048U": cat385048U,
       "ciscoVG310": ciscoVG310,
       "ciscoVG320": ciscoVG320,
       "ciscoC6880xle": ciscoC6880xle,
       "cat45Sup8e": cat45Sup8e,
       "ciscoWsC2960XR48FpdI": ciscoWsC2960XR48FpdI,
       "ciscoWsC2960XR48LpdI": ciscoWsC2960XR48LpdI,
       "ciscoWsC2960XR48TdI": ciscoWsC2960XR48TdI,
       "ciscoWsC2960XR24PdI": ciscoWsC2960XR24PdI,
       "ciscoWsC2960XR24TdI": ciscoWsC2960XR24TdI,
       "ciscoWsC2960XR48FpsI": ciscoWsC2960XR48FpsI,
       "ciscoWsC2960XR48LpsI": ciscoWsC2960XR48LpsI,
       "ciscoWsC2960XR48TsI": ciscoWsC2960XR48TsI,
       "ciscoWsC2960XR24PsI": ciscoWsC2960XR24PsI,
       "ciscoWsC2960XR24TsI": ciscoWsC2960XR24TsI,
       "ciscoUCSC460M4Rackserver": ciscoUCSC460M4Rackserver,
       "ciscoA901S4SGFD": ciscoA901S4SGFD,
       "ciscoA901S3SGFD": ciscoA901S3SGFD,
       "ciscoA901S2SGFD": ciscoA901S2SGFD,
       "ciscoA901S3SGFAH": ciscoA901S3SGFAH,
       "ciscoA901S2SGFAH": ciscoA901S2SGFAH,
       "ciscoC365024TS": ciscoC365024TS,
       "ciscoC365048TS": ciscoC365048TS,
       "ciscoC365024PS": ciscoC365024PS,
       "ciscoC365048PS": ciscoC365048PS,
       "ciscoC365024TD": ciscoC365024TD,
       "ciscoC365048TD": ciscoC365048TD,
       "ciscoC365024PD": ciscoC365024PD,
       "ciscoC365048PD": ciscoC365048PD,
       "ciscoIE2000U4STSG": ciscoIE2000U4STSG,
       "ciscoIE2000U16TCGP": ciscoIE2000U16TCGP,
       "ciscoIE20008T67B": ciscoIE20008T67B,
       "ciscoIE200016T67B": ciscoIE200016T67B,
       "ciscoIE200024T67B": ciscoIE200024T67B,
       "ciscoIE20008T67PGE": ciscoIE20008T67PGE,
       "ciscoIE200016T67PGE": ciscoIE200016T67PGE,
       "ciscoRAIE1783ZMS8TA": ciscoRAIE1783ZMS8TA,
       "ciscoRAIE1783ZMS16TA": ciscoRAIE1783ZMS16TA,
       "ciscoRAIE1783ZMS24TA": ciscoRAIE1783ZMS24TA,
       "ciscoRAIE1783ZMS4T4E2TGP": ciscoRAIE1783ZMS4T4E2TGP,
       "ciscoRAIE1783ZMS8T8E2TGP": ciscoRAIE1783ZMS8T8E2TGP,
       "ciscoNcs6008": ciscoNcs6008,
       "ciscoC881K9": ciscoC881K9,
       "ciscoC886VaK9": ciscoC886VaK9,
       "ciscoC886VaJK9": ciscoC886VaJK9,
       "ciscoC887VaK9": ciscoC887VaK9,
       "ciscoC887VaMK9": ciscoC887VaMK9,
       "ciscoC888K9": ciscoC888K9,
       "ciscoC891FK9": ciscoC891FK9,
       "ciscoC891FwAK9": ciscoC891FwAK9,
       "ciscoC891FwEK9": ciscoC891FwEK9,
       "ciscoASR1001X": ciscoASR1001X,
       "cisco1783WAP5100xK9": cisco1783WAP5100xK9,
       "ciscoCDScde2502s5": ciscoCDScde2502s5,
       "ciscoUcsE140S": ciscoUcsE140S,
       "ciscoNXNAM1": ciscoNXNAM1,
       "ciscoC6800ia48fpdL": ciscoC6800ia48fpdL,
       "ciscoC6800ia48tdL": ciscoC6800ia48tdL,
       "ciscoIE2000U4TG": ciscoIE2000U4TG,
       "ciscoIE2000U4TSG": ciscoIE2000U4TSG,
       "ciscoIE2000U8TCG": ciscoIE2000U8TCG,
       "ciscoIE2000U16TCG": ciscoIE2000U16TCG,
       "ciscoIE2000U16TCGX": ciscoIE2000U16TCGX,
       "ciscoAIRAP3702": ciscoAIRAP3702,
       "ciscoAIRAP702": ciscoAIRAP702,
       "ciscoAIRAP1532": ciscoAIRAP1532,
       "ciscoEsxNAM": ciscoEsxNAM,
       "ciscoKvmNAM": ciscoKvmNAM,
       "ciscoHyperNAM": ciscoHyperNAM,
       "ciscoC385024S": ciscoC385024S,
       "ciscoC385012S": ciscoC385012S,
       "ciscoC365048PQ": ciscoC365048PQ,
       "ciscoC365048TQ": ciscoC365048TQ,
       "ciscoASR902": ciscoASR902,
       "ciscoME1200": ciscoME1200,
       "ciscoVASA": ciscoVASA,
       "ciscoVASASy": ciscoVASASy,
       "ciscoVASASc": ciscoVASASc,
       "ciscoN9Kc9508": ciscoN9Kc9508,
       "ciscoWapAP702": ciscoWapAP702,
       "ciscoWapAP2602": ciscoWapAP2602,
       "ciscoWapAP1602": ciscoWapAP1602,
       "ciscoN9KC93128TX": ciscoN9KC93128TX,
       "ciscoN9KC9396TX": ciscoN9KC9396TX,
       "ciscoN9KC9396PX": ciscoN9KC9396PX,
       "ciscoWlcCt5508K9": ciscoWlcCt5508K9,
       "ciscoWlcCt2504K9": ciscoWlcCt2504K9,
       "ciscoUcsEN120S": ciscoUcsEN120S,
       "ciscoUcsEN140N": ciscoUcsEN140N,
       "ciscoUcsEN120E": ciscoUcsEN120E,
       "ciscoC68xxVirtualSwitch": ciscoC68xxVirtualSwitch,
       "ciscoISR4431": ciscoISR4431,
       "ciscoC6880x": ciscoC6880x,
       "ciscoCPT50": ciscoCPT50,
       "ciscoAIRAP2702": ciscoAIRAP2702,
       "ciscoNCS4016": ciscoNCS4016,
       "ciscoCSE340WG32K9": ciscoCSE340WG32K9,
       "ciscoCSE340WG32AK9": ciscoCSE340WG32AK9,
       "ciscoCSE340WG32CK9": ciscoCSE340WG32CK9,
       "ciscoCSE340WG32EK9": ciscoCSE340WG32EK9,
       "ciscoCSE340WG32NK9": ciscoCSE340WG32NK9,
       "ciscoCSE340WM32K9": ciscoCSE340WM32K9,
       "ciscoCSE340WM32AK9": ciscoCSE340WM32AK9,
       "ciscoCSE340WM32CK9": ciscoCSE340WM32CK9,
       "ciscoCSE340WM32EK9": ciscoCSE340WM32EK9,
       "ciscoCSE340WM32NK9": ciscoCSE340WM32NK9,
       "ciscoitpRT1081K9": ciscoitpRT1081K9,
       "ciscoitpRT1091FK9": ciscoitpRT1091FK9,
       "ciscoitpPwr30WAC": ciscoitpPwr30WAC,
       "ciscoitpPwr60WAC": ciscoitpPwr60WAC,
       "ciscoitpPwr60WACV2": ciscoitpPwr60WACV2,
       "ciscoitpPwr125WAC": ciscoitpPwr125WAC,
       "ciscoitpRT2241K9": ciscoitpRT2241K9,
       "ciscoitpRT2221K9": ciscoitpRT2221K9,
       "ciscoitpRT2241WCK9": ciscoitpRT2241WCK9,
       "ciscoitpAxpIsmSre300": ciscoitpAxpIsmSre300,
       "ciscoitpPwr2241AC": ciscoitpPwr2241AC,
       "ciscoitpRT3211K9": ciscoitpRT3211K9,
       "ciscoitpRT3221K9": ciscoitpRT3221K9,
       "ciscoitpRT3201K9": ciscoitpRT3201K9,
       "ciscoitpPwrRT3201AC": ciscoitpPwrRT3201AC,
       "ciscoitpPwrRT3211AC": ciscoitpPwrRT3211AC,
       "ciscoitpPwrRT3211DC": ciscoitpPwrRT3211DC,
       "ciscoitpPwrRT32AC": ciscoitpPwrRT32AC,
       "ciscoitpRpsAdptrRT3211": ciscoitpRpsAdptrRT3211,
       "ciscoitpRpsAdptrRT32": ciscoitpRpsAdptrRT32,
       "ciscoitpAxpSmSre710": ciscoitpAxpSmSre710,
       "ciscoitpAxpSmSre910": ciscoitpAxpSmSre910,
       "ciscoN9Kc9516": ciscoN9Kc9516,
       "ciscoN9Kc9504": ciscoN9Kc9504,
       "ciscoDoorCGR1240": ciscoDoorCGR1240,
       "ciscoISR4351": ciscoISR4351,
       "ciscoWRP500": ciscoWRP500,
       "cisco897VABK9": cisco897VABK9,
       "cisco819HWDCK9": cisco819HWDCK9,
       "catAIRCT57006": catAIRCT57006,
       "cisco897VAMGLTEGAK9": cisco897VAMGLTEGAK9,
       "cisco899GLTESTK9": cisco899GLTESTK9,
       "cisco899GLTENAK9": cisco899GLTENAK9,
       "cisco899GLTEVZK9": cisco899GLTEVZK9,
       "cisco819G4GNAK9": cisco819G4GNAK9,
       "cisco819G4GSTK9": cisco819G4GSTK9,
       "cisco898EAGLTEGAK9": cisco898EAGLTEGAK9,
       "cisco897VAGLTEGAK9": cisco897VAGLTEGAK9,
       "cisco896VAGLTEGAK9": cisco896VAGLTEGAK9,
       "cisco899GLTEGAK9": cisco899GLTEGAK9,
       "cisco881G4GGAK9": cisco881G4GGAK9,
       "cisco887VAG4GGAK9": cisco887VAG4GGAK9,
       "cisco819G4GGAK9": cisco819G4GGAK9,
       "cisco819G4GVZK9": cisco819G4GVZK9,
       "ciscoIOG910WK9": ciscoIOG910WK9,
       "ciscoIOG910GK9": ciscoIOG910GK9,
       "ciscoIOG910K9": ciscoIOG910K9,
       "cat36xxstack": cat36xxstack,
       "cat57xxstack": cat57xxstack,
       "ciscoISR4331": ciscoISR4331,
       "ciscoIE40004TC4GE": ciscoIE40004TC4GE,
       "ciscoIE40008T4GE": ciscoIE40008T4GE,
       "ciscoIE40008S4GE": ciscoIE40008S4GE,
       "ciscoIE40004T4P4GE": ciscoIE40004T4P4GE,
       "ciscoIE400016T4GE": ciscoIE400016T4GE,
       "ciscoIE40004S8P4GE": ciscoIE40004S8P4GE,
       "ciscoIE40008GT4GE": ciscoIE40008GT4GE,
       "ciscoIE40008GS4GE": ciscoIE40008GS4GE,
       "ciscoIE40004GC4GP4GE": ciscoIE40004GC4GP4GE,
       "ciscoIE400016GT4GE": ciscoIE400016GT4GE,
       "ciscoIE40008GT8GP4GE": ciscoIE40008GT8GP4GE,
       "ciscoIE40004GS8GP4GE": ciscoIE40004GS8GP4GE,
       "ciscoRAIE1783HMS4C4CGN": ciscoRAIE1783HMS4C4CGN,
       "ciscoRAIE1783HMS8T4CGN": ciscoRAIE1783HMS8T4CGN,
       "ciscoRAIE1783HMS8S4CGN": ciscoRAIE1783HMS8S4CGN,
       "ciscoRAIE1783HMS4T4E4CGN": ciscoRAIE1783HMS4T4E4CGN,
       "ciscoRAIE1783HMS16T4CGN": ciscoRAIE1783HMS16T4CGN,
       "ciscoRAIE1783HMS4S8E4CGN": ciscoRAIE1783HMS4S8E4CGN,
       "ciscoRAIE1783HMS8TG4CGN": ciscoRAIE1783HMS8TG4CGN,
       "ciscoRAIE1783HMS8SG4CGN": ciscoRAIE1783HMS8SG4CGN,
       "ciscoRAIE1783HMS4EG8CGN": ciscoRAIE1783HMS4EG8CGN,
       "ciscoRAIE1783HMS16TG4CGN": ciscoRAIE1783HMS16TG4CGN,
       "ciscoRAIE1783HMS8TG8EG4CGN": ciscoRAIE1783HMS8TG8EG4CGN,
       "ciscoRAIE1783HMS4SG8EG4CGN": ciscoRAIE1783HMS4SG8EG4CGN,
       "ciscoISR4321": ciscoISR4321,
       "ciscoCSE340G32K9": ciscoCSE340G32K9,
       "ciscoCSE340M32K9": ciscoCSE340M32K9,
       "ciscoSCE10000": ciscoSCE10000,
       "ciscoVirtualSCE": ciscoVirtualSCE,
       "ciscoASR901AC10GS": ciscoASR901AC10GS,
       "ciscoASR901DC10GS": ciscoASR901DC10GS,
       "ciscoASR92024SZIM": ciscoASR92024SZIM,
       "ciscoASR92024TZM": ciscoASR92024TZM,
       "ciscoASR92024SZM": ciscoASR92024SZM,
       "ciscoIR809GLTESTK9": ciscoIR809GLTESTK9,
       "ciscoIR809GLTEVZK9": ciscoIR809GLTEVZK9,
       "ciscoIR809GLTEGAK9": ciscoIR809GLTEGAK9,
       "ciscoIR809GLTENAK9": ciscoIR809GLTENAK9,
       "ciscoIR829GWLTESTAK9": ciscoIR829GWLTESTAK9,
       "ciscoIR829GWLTEVZAK9": ciscoIR829GWLTEVZAK9,
       "ciscoIR829GWLTEGAZK9": ciscoIR829GWLTEGAZK9,
       "ciscoIR829GWLTEGAEK9": ciscoIR829GWLTEGAEK9,
       "ciscoIR829GWLTENAAK9": ciscoIR829GWLTENAAK9,
       "ciscoWallander1x1GESKU": ciscoWallander1x1GESKU,
       "ciscoWallander2x1GESKU": ciscoWallander2x1GESKU,
       "ciscoASA5506": ciscoASA5506,
       "ciscoASA5506sc": ciscoASA5506sc,
       "ciscoASA5506sy": ciscoASA5506sy,
       "ciscoASA5506W": ciscoASA5506W,
       "ciscoASA5506Wsc": ciscoASA5506Wsc,
       "ciscoASA5506Wsy": ciscoASA5506Wsy,
       "ciscoASA5508": ciscoASA5508,
       "ciscoASA5508sc": ciscoASA5508sc,
       "ciscoASA5508sy": ciscoASA5508sy,
       "ciscoASA5506K7": ciscoASA5506K7,
       "ciscoASA5506K7sc": ciscoASA5506K7sc,
       "ciscoASA5506K7sy": ciscoASA5506K7sy,
       "ciscoASA5508K7": ciscoASA5508K7,
       "ciscoASA5508K7sc": ciscoASA5508K7sc,
       "ciscoASA5508K7sy": ciscoASA5508K7sy,
       "ciscoAIRAP1702": ciscoAIRAP1702,
       "catwsC3560CX8ptS": catwsC3560CX8ptS,
       "catwsC3560CX8XpdS": catwsC3560CX8XpdS,
       "catwsC3560CX12pdS": catwsC3560CX12pdS,
       "catwsC3560CX12tcS": catwsC3560CX12tcS,
       "catwsC3560CX12pcS": catwsC3560CX12pcS,
       "catwsC3560CX8tcS": catwsC3560CX8tcS,
       "catwsC3560CX8pcS": catwsC3560CX8pcS,
       "catwsC2960CX8tcL": catwsC2960CX8tcL,
       "cisco2911TK9": cisco2911TK9,
       "ciscoSNS3495K9": ciscoSNS3495K9,
       "ciscoSNS3415K9": ciscoSNS3415K9,
       "ciscocBR8": ciscocBR8,
       "ciscoPwrC2911DCPOE": ciscoPwrC2911DCPOE,
       "ciscoASR1006X": ciscoASR1006X,
       "ciscoASR1009X": ciscoASR1009X,
       "ciscoAIRAP702w": ciscoAIRAP702w,
       "ciscoAIRAP1572": ciscoAIRAP1572,
       "cisco891x24XK9": cisco891x24XK9,
       "ciscoUCSEN120E54": ciscoUCSEN120E54,
       "ciscoUCSEN120E108": ciscoUCSEN120E108,
       "ciscoUCSEN120E208": ciscoUCSEN120E208,
       "ciscoASR9204SZD": ciscoASR9204SZD,
       "ciscoASR9208SZ0A": ciscoASR9208SZ0A,
       "ciscoASR92012CZA": ciscoASR92012CZA,
       "ciscoASR92012CZD": ciscoASR92012CZD,
       "ciscoASR9204SZA": ciscoASR9204SZA,
       "ciscoASR92010SZ0D": ciscoASR92010SZ0D,
       "ciscoTSCodecG3": ciscoTSCodecG3,
       "ciscoC385012XS": ciscoC385012XS,
       "ciscoC385024XS": ciscoC385024XS,
       "ciscoC385048XS": ciscoC385048XS,
       "ciscoC385012X48U": ciscoC385012X48U,
       "ciscoC385024XU": ciscoC385024XU,
       "ciscoRAIE1783ZMS4T4E2TGN": ciscoRAIE1783ZMS4T4E2TGN,
       "ciscoRAIE1783ZMS8T8E2TGN": ciscoRAIE1783ZMS8T8E2TGN,
       "cisco5520WLC": cisco5520WLC,
       "cisco8540Wlc": cisco8540Wlc,
       "ciscoRAIE1783HMS8TG4CGR": ciscoRAIE1783HMS8TG4CGR,
       "ciscoRAIE1783HMS8SG4CGR": ciscoRAIE1783HMS8SG4CGR,
       "ciscoRAIE1783HMS4EG8CGR": ciscoRAIE1783HMS4EG8CGR,
       "ciscoRAIE1783HMS16TG4CGR": ciscoRAIE1783HMS16TG4CGR,
       "ciscoRAIE1783HMS8TG8EG4CGR": ciscoRAIE1783HMS8TG8EG4CGR,
       "ciscoRAIE1783HMS4SG8EG4CGR": ciscoRAIE1783HMS4SG8EG4CGR,
       "ciscoUCSC220M4": ciscoUCSC220M4,
       "ciscoUCSC240M4": ciscoUCSC240M4,
       "ciscoUCSC3160": ciscoUCSC3160,
       "cisco1941WTK9": cisco1941WTK9,
       "ciscoUCSC3260": ciscoUCSC3260,
       "ciscoUCSE160DM2K9": ciscoUCSE160DM2K9,
       "ciscoUCSE180DM2K9": ciscoUCSE180DM2K9,
       "ciscoCDScde2802s5": ciscoCDScde2802s5,
       "ciscoCDScde2802s10": ciscoCDScde2802s10,
       "ciscoCDScde2802s21": ciscoCDScde2802s21,
       "ciscoCDScde2802h0": ciscoCDScde2802h0,
       "ciscoCDScde2802h13": ciscoCDScde2802h13,
       "ciscoCDScde2802h26": ciscoCDScde2802h26,
       "ciscoWSC2960CX8PCL": ciscoWSC2960CX8PCL,
       "cisco1941WIK9": cisco1941WIK9,
       "ciscoFp7030K9": ciscoFp7030K9,
       "ciscoFp7050K9": ciscoFp7050K9,
       "ciscoFp7110K9": ciscoFp7110K9,
       "ciscoFp7110FiK9": ciscoFp7110FiK9,
       "ciscoFp7115K9": ciscoFp7115K9,
       "ciscoFp7120K9": ciscoFp7120K9,
       "ciscoFp7120FiK9": ciscoFp7120FiK9,
       "ciscoFp7125K9": ciscoFp7125K9,
       "ciscoFp8120K9": ciscoFp8120K9,
       "ciscoFp8130K9": ciscoFp8130K9,
       "ciscoFp8140K9": ciscoFp8140K9,
       "ciscoFp8250K9": ciscoFp8250K9,
       "ciscoFp8260K9": ciscoFp8260K9,
       "ciscoFp8270K9": ciscoFp8270K9,
       "ciscoFp8290K9": ciscoFp8290K9,
       "ciscoFp8350K9": ciscoFp8350K9,
       "ciscoFp8360K9": ciscoFp8360K9,
       "ciscoFp8370K9": ciscoFp8370K9,
       "ciscoFp8390K9": ciscoFp8390K9,
       "ciscoFs750K9": ciscoFs750K9,
       "ciscoFs1500K9": ciscoFs1500K9,
       "ciscoFs3500K9": ciscoFs3500K9,
       "ciscoFs4000K9": ciscoFs4000K9,
       "ciscoAmp7150K9": ciscoAmp7150K9,
       "ciscoAmp8050K9": ciscoAmp8050K9,
       "ciscoAmp8150K9": ciscoAmp8150K9,
       "ciscoAmp8350K9": ciscoAmp8350K9,
       "ciscoAmp8360K9": ciscoAmp8360K9,
       "ciscoAmp8370K9": ciscoAmp8370K9,
       "ciscoAmp8390K9": ciscoAmp8390K9,
       "ciscoFpSsl1500K9": ciscoFpSsl1500K9,
       "ciscoFpSsl1500FiK9": ciscoFpSsl1500FiK9,
       "ciscoFpSsl2000K9": ciscoFpSsl2000K9,
       "ciscoFpSsl8200K9": ciscoFpSsl8200K9,
       "ciscoFp7010K9": ciscoFp7010K9,
       "ciscoFp7020K9": ciscoFp7020K9,
       "cisco841Mx4XK9": cisco841Mx4XK9,
       "cisco841Mx8XK9": cisco841Mx8XK9,
       "ciscoC819GWLTEMNAAK9": ciscoC819GWLTEMNAAK9,
       "ciscoC819GWLTEGAEK9": ciscoC819GWLTEGAEK9,
       "ciscoIE500012S12P10G": ciscoIE500012S12P10G,
       "ciscoRAIE1783IMS28NAC": ciscoRAIE1783IMS28NAC,
       "ciscoRAIE1783IMS28NDC": ciscoRAIE1783IMS28NDC,
       "ciscoRAIE1783IMS28RAC": ciscoRAIE1783IMS28RAC,
       "ciscoRAIE1783IMS28RDC": ciscoRAIE1783IMS28RDC,
       "ciscoACIController": ciscoACIController,
       "ciscoAIRAPIW3702": ciscoAIRAPIW3702,
       "ciscoASA5506H": ciscoASA5506H,
       "ciscoASA5516": ciscoASA5516,
       "ciscoASA5506Hsc": ciscoASA5506Hsc,
       "ciscoASA5516sc": ciscoASA5516sc,
       "ciscoASA5506Hsy": ciscoASA5506Hsy,
       "ciscoASA5516sy": ciscoASA5516sy,
       "ciscoASR92016SZIM": ciscoASR92016SZIM,
       "ciscoIR829GWLTEMAAK9": ciscoIR829GWLTEMAAK9,
       "ciscoPwsX474812X48uE": ciscoPwsX474812X48uE,
       "ciscoASR1002HX": ciscoASR1002HX,
       "ciscoNCS4009": ciscoNCS4009,
       "ciscoRAISA1783SAD2T2Ssy": ciscoRAISA1783SAD2T2Ssy,
       "ciscoRAISA1783SAD4T0Ssy": ciscoRAISA1783SAD4T0Ssy,
       "ciscoISA30002C2Fsy": ciscoISA30002C2Fsy,
       "ciscoISA30004Csy": ciscoISA30004Csy,
       "ciscoISA4000sy": ciscoISA4000sy,
       "ciscoISA4000sc": ciscoISA4000sc,
       "ciscoRAISA1783SAD2T2Ssc": ciscoRAISA1783SAD2T2Ssc,
       "ciscoRAISA1783SAD4T0Ssc": ciscoRAISA1783SAD4T0Ssc,
       "ciscoISA30002C2Fsc": ciscoISA30002C2Fsc,
       "ciscoISA30004Csc": ciscoISA30004Csc,
       "ciscoIOSXRv9000": ciscoIOSXRv9000,
       "ciscoSNS3515K9": ciscoSNS3515K9,
       "ciscoSNS3595K9": ciscoSNS3595K9,
       "ciscoISA30002C2F": ciscoISA30002C2F,
       "ciscoISA30004C": ciscoISA30004C,
       "ciscoRAISA1783SAD4T0S": ciscoRAISA1783SAD4T0S,
       "ciscoRAISA1783SAD2T2S": ciscoRAISA1783SAD2T2S,
       "ciscoISA4000": ciscoISA4000,
       "ciscoC888EAK9": ciscoC888EAK9,
       "ciscoC6816xle": ciscoC6816xle,
       "ciscoC6832xle": ciscoC6832xle,
       "ciscoC6824xle": ciscoC6824xle,
       "ciscoC6840xle": ciscoC6840xle,
       "cat35xxStack": cat35xxStack,
       "catWsC365012X48UR": catWsC365012X48UR,
       "catWsC36508X24UQ": catWsC36508X24UQ,
       "catWsC365012X48UZ": catWsC365012X48UZ,
       "catWsC365012X48UQ": catWsC365012X48UQ,
       "ciscoNam2420": ciscoNam2420,
       "ciscoNam2440": ciscoNam2440,
       "ciscoflowAgent3300": ciscoflowAgent3300,
       "ciscoFpr9300K9": ciscoFpr9300K9,
       "ciscoFpr9000SM24": ciscoFpr9000SM24,
       "ciscoFpr9000SM36": ciscoFpr9000SM36,
       "catWsC365048FQM": catWsC365048FQM,
       "catWsC365024PDM": catWsC365024PDM,
       "ciscoFpr4150K9": ciscoFpr4150K9,
       "ciscoFpr4140K9": ciscoFpr4140K9,
       "ciscoFpr4120K9": ciscoFpr4120K9,
       "ciscoFpr4110K9": ciscoFpr4110K9,
       "ciscoIE500016S12P": ciscoIE500016S12P,
       "ciscoASA5512td": ciscoASA5512td,
       "ciscoASA5515td": ciscoASA5515td,
       "ciscoASA5525td": ciscoASA5525td,
       "ciscoASA5545td": ciscoASA5545td,
       "ciscoASA5555td": ciscoASA5555td,
       "ciscoASA5506td": ciscoASA5506td,
       "ciscoASA5506Wtd": ciscoASA5506Wtd,
       "ciscoASA5506Htd": ciscoASA5506Htd,
       "ciscoASA5508td": ciscoASA5508td,
       "ciscoASA5516td": ciscoASA5516td,
       "ciscoPIUCSAPLK9": ciscoPIUCSAPLK9,
       "cisco899GLTEJPK9": cisco899GLTEJPK9,
       "cisco819GLTEMNAK9": cisco819GLTEMNAK9,
       "ciscoFpr4110SM12": ciscoFpr4110SM12,
       "ciscoFpr4120SM24": ciscoFpr4120SM24,
       "ciscoFpr4140SM36": ciscoFpr4140SM36,
       "ciscoFpr4150SM44": ciscoFpr4150SM44,
       "ciscoNCS5001": ciscoNCS5001,
       "ciscoNCS5002": ciscoNCS5002,
       "ciscoFpvK9": ciscoFpvK9,
       "ciscoASR901CC": ciscoASR901CC,
       "ciscoASR901ECC": ciscoASR901ECC,
       "ciscoASR901DC10GCC": ciscoASR901DC10GCC,
       "ciscoASR901EDC10GCC": ciscoASR901EDC10GCC,
       "ciscoASR901DC10GSCC": ciscoASR901DC10GSCC,
       "ciscoASR92012SZIMCC": ciscoASR92012SZIMCC,
       "ciscoNcs4201": ciscoNcs4201,
       "ciscoNcs4202": ciscoNcs4202,
       "ciscoNcs4206": ciscoNcs4206,
       "ciscoNcs4216": ciscoNcs4216,
       "ciscoIE10004TLM": ciscoIE10004TLM,
       "ciscoIE10006TLM": ciscoIE10006TLM,
       "ciscoIE10004PTSLM": ciscoIE10004PTSLM,
       "ciscoIE10008PTSLM": ciscoIE10008PTSLM,
       "ciscoVFTD": ciscoVFTD,
       "ciscoISR4451B": ciscoISR4451B,
       "ciscoISR4431B": ciscoISR4431B,
       "ciscoISR4351B": ciscoISR4351B,
       "ciscoISR4331B": ciscoISR4331B,
       "ciscoISR4321B": ciscoISR4321B,
       "ciscoRAIE1783IMS28GNAC": ciscoRAIE1783IMS28GNAC,
       "ciscoRAIE1783IMS28GNDC": ciscoRAIE1783IMS28GNDC,
       "ciscoRAIE1783IMS28GRAC": ciscoRAIE1783IMS28GRAC,
       "ciscoRAIE1783IMS28GRDC": ciscoRAIE1783IMS28GRDC,
       "ciscoQSFP100GCWDM4S": ciscoQSFP100GCWDM4S,
       "cisco897VAGWLTEGAEK9": cisco897VAGWLTEGAEK9,
       "cisco886VAGLTEGAK9": cisco886VAGLTEGAK9,
       "ciscoNcs1002": ciscoNcs1002,
       "ciscoASR1001HX": ciscoASR1001HX,
       "ciscoNCS5508": ciscoNCS5508,
       "ciscoNCS5501SE": ciscoNCS5501SE,
       "ciscoNCS5502SE": ciscoNCS5502SE,
       "ciscoUnifiedSipProxy": ciscoUnifiedSipProxy,
       "cisco898EAGLTELAK9": cisco898EAGLTELAK9,
       "cisco897VAGLTELAK9": cisco897VAGLTELAK9,
       "cisco819GWLTELACK9": cisco819GWLTELACK9,
       "cisco819GWLTELAQK9": cisco819GWLTELAQK9,
       "cisco819GWLTELANK9": cisco819GWLTELANK9,
       "ciscoCatWSC2960L8TSLL": ciscoCatWSC2960L8TSLL,
       "ciscoCatWSC2960L8PSLL": ciscoCatWSC2960L8PSLL,
       "ciscoCatWSC2960L16TSLL": ciscoCatWSC2960L16TSLL,
       "ciscoCatWSC2960L16PSLL": ciscoCatWSC2960L16PSLL,
       "ciscoCatWSC2960L24TSLL": ciscoCatWSC2960L24TSLL,
       "ciscoCatWSC2960L24PSLL": ciscoCatWSC2960L24PSLL,
       "ciscoCatWSC2960L48TSLL": ciscoCatWSC2960L48TSLL,
       "ciscoCatWSC2960L48PSLL": ciscoCatWSC2960L48PSLL,
       "ciscoIE40104S24P": ciscoIE40104S24P,
       "ciscoIE401016S12P": ciscoIE401016S12P,
       "cisco867VAEK9V2": cisco867VAEK9V2,
       "cisco866VAEK9V2": cisco866VAEK9V2,
       "cisco867VAEV2": cisco867VAEV2,
       "cisco899GLTELAK9": cisco899GLTELAK9,
       "cisco819GLTELAK9": cisco819GLTELAK9,
       "ciscoRAIE1783LMS5": ciscoRAIE1783LMS5,
       "ciscoRAIE1783LMS8": ciscoRAIE1783LMS8,
       "ciscoStealthWatch2404": ciscoStealthWatch2404,
       "ciscoStealthWatch2420": ciscoStealthWatch2420,
       "ciscoNamApp2404": ciscoNamApp2404,
       "catWsC36508X24PD": catWsC36508X24PD,
       "catWsC365012X48FD": catWsC365012X48FD,
       "ciscoASR9910": ciscoASR9910,
       "ciscoC9800CLK9": ciscoC9800CLK9,
       "cisco819HGLTEMNAK9": cisco819HGLTEMNAK9,
       "ciscoIR829GWLTEGASK9": ciscoIR829GWLTEGASK9,
       "ciscoIR829GWLTEGACK9": ciscoIR829GWLTEGACK9,
       "ciscoISR4221": ciscoISR4221,
       "ciscoISR4221B": ciscoISR4221B,
       "ciscoCSP2100": ciscoCSP2100,
       "ciscoCDB8U": ciscoCDB8U,
       "ciscoCDB8P": ciscoCDB8P,
       "ciscoNCS5501": ciscoNCS5501,
       "ciscoNCS5502": ciscoNCS5502,
       "ciscoNCS4216F2BSA": ciscoNCS4216F2BSA,
       "ciscoFpr2110td": ciscoFpr2110td,
       "ciscoFpr2120td": ciscoFpr2120td,
       "ciscoFpr2130td": ciscoFpr2130td,
       "ciscoFpr2140td": ciscoFpr2140td,
       "ciscoFpr9000SM44": ciscoFpr9000SM44,
       "ciscoNCS5011": ciscoNCS5011,
       "ciscoNCS5516": ciscoNCS5516,
       "ciscoNCS5504": ciscoNCS5504,
       "ciscoUCSE160S": ciscoUCSE160S,
       "ciscoUCSE180DM3": ciscoUCSE180DM3,
       "ciscoUCSE1120DM3": ciscoUCSE1120DM3,
       "ciscoCat950012Q": ciscoCat950012Q,
       "ciscoCat950024Q": ciscoCat950024Q,
       "ciscoCat950040X": ciscoCat950040X,
       "ciscoNCS1001": ciscoNCS1001,
       "ciscoIR809G3GGAK9": ciscoIR809G3GGAK9,
       "ciscoIR809GLTELAK9": ciscoIR809GLTELAK9,
       "cisco3504WLC": cisco3504WLC,
       "ciscoNCS55A136HSES": ciscoNCS55A136HSES,
       "ciscoNCS5501HD": ciscoNCS5501HD,
       "ciscoNCS5501HDS": ciscoNCS5501HDS,
       "ciscoNCS55A124H": ciscoNCS55A124H,
       "ciscoCXP2270GSR12": ciscoCXP2270GSR12,
       "ciscoNCS4216F2B": ciscoNCS4216F2B,
       "ciscoCat930024T": ciscoCat930024T,
       "ciscoCat930024P": ciscoCat930024P,
       "ciscoCat930024U": ciscoCat930024U,
       "ciscoCat930024UX": ciscoCat930024UX,
       "ciscoCat930048T": ciscoCat930048T,
       "ciscoCat930048P": ciscoCat930048P,
       "ciscoCat930048U": ciscoCat930048U,
       "ciscoCat930048UXM": ciscoCat930048UXM,
       "ciscoC11118P": ciscoC11118P,
       "ciscoC11118PLteEA": ciscoC11118PLteEA,
       "ciscoC11118PLteLA": ciscoC11118PLteLA,
       "ciscoC11118PWE": ciscoC11118PWE,
       "ciscoC11118PWB": ciscoC11118PWB,
       "ciscoC11118PWA": ciscoC11118PWA,
       "ciscoC11118PWZ": ciscoC11118PWZ,
       "ciscoC11118PWN": ciscoC11118PWN,
       "ciscoC11118PWQ": ciscoC11118PWQ,
       "ciscoC11118PWH": ciscoC11118PWH,
       "ciscoC11118PWR": ciscoC11118PWR,
       "ciscoC11118PWF": ciscoC11118PWF,
       "ciscoC11118PLteEAWE": ciscoC11118PLteEAWE,
       "ciscoC11118PLteEAWB": ciscoC11118PLteEAWB,
       "ciscoC11118PLteEAWA": ciscoC11118PLteEAWA,
       "ciscoC11118PLteEAWR": ciscoC11118PLteEAWR,
       "ciscoC11118PLteLAWZ": ciscoC11118PLteLAWZ,
       "ciscoC11118PLteLAWN": ciscoC11118PLteLAWN,
       "ciscoC11118PLteLAWQ": ciscoC11118PLteLAWQ,
       "ciscoC11118PLteLAWH": ciscoC11118PLteLAWH,
       "ciscoC11118PLteLAWF": ciscoC11118PLteLAWF,
       "ciscoC11118PLteLAWD": ciscoC11118PLteLAWD,
       "ciscoASR914": ciscoASR914,
       "ciscoNCSFFC2": ciscoNCSFFC2,
       "ciscoNCS4KF": ciscoNCS4KF,
       "ciscoFpr1010td": ciscoFpr1010td,
       "cisco2911A": cisco2911A,
       "ciscoUCSS3260": ciscoUCSS3260,
       "ciscoWSC365048TSE": ciscoWSC365048TSE,
       "ciscoUCSC220M5": ciscoUCSC220M5,
       "ciscoUCSC240M5": ciscoUCSC240M5,
       "ciscoCat9300FixedSwitchStack": ciscoCat9300FixedSwitchStack,
       "ciscoCatWSC2960L24TQLL": ciscoCatWSC2960L24TQLL,
       "ciscoCatWSC2960L48TQLL": ciscoCatWSC2960L48TQLL,
       "ciscoCatWSC2960L24PQLL": ciscoCatWSC2960L24PQLL,
       "ciscoCatWSC2960L48PQLL": ciscoCatWSC2960L48PQLL,
       "ciscoCat9404R": ciscoCat9404R,
       "ciscoCat9407R": ciscoCat9407R,
       "ciscoCat9410R": ciscoCat9410R,
       "ciscoASR903U": ciscoASR903U,
       "ciscoASR902U": ciscoASR902U,
       "ciscoASR920U16SZIM": ciscoASR920U16SZIM,
       "ciscoC11114P": ciscoC11114P,
       "ciscoC11114PLteEA": ciscoC11114PLteEA,
       "ciscoC11114PLteLA": ciscoC11114PLteLA,
       "ciscoC11114PWE": ciscoC11114PWE,
       "ciscoC11114PWB": ciscoC11114PWB,
       "ciscoC11114PWA": ciscoC11114PWA,
       "ciscoC11114PWZ": ciscoC11114PWZ,
       "ciscoC11114PWN": ciscoC11114PWN,
       "ciscoC11114PWQ": ciscoC11114PWQ,
       "ciscoC11114PWH": ciscoC11114PWH,
       "ciscoC11114PWR": ciscoC11114PWR,
       "ciscoC11114PWF": ciscoC11114PWF,
       "ciscoC11114PWD": ciscoC11114PWD,
       "ciscoC11164P": ciscoC11164P,
       "ciscoC11164PLteEA": ciscoC11164PLteEA,
       "ciscoC11174P": ciscoC11174P,
       "ciscoC11164PWE": ciscoC11164PWE,
       "ciscoC11174PLteEA": ciscoC11174PLteEA,
       "ciscoC11174PLteLA": ciscoC11174PLteLA,
       "ciscoC11174PWE": ciscoC11174PWE,
       "ciscoC11174PWA": ciscoC11174PWA,
       "ciscoC11174PWZ": ciscoC11174PWZ,
       "ciscoC11174PM": ciscoC11174PM,
       "ciscoC11174PMLteEA": ciscoC11174PMLteEA,
       "ciscoC11174PMWE": ciscoC11174PMWE,
       "ciscoC980040K9": ciscoC980040K9,
       "ciscoAIRCT9880K9": ciscoAIRCT9880K9,
       "ciscoC11128P": ciscoC11128P,
       "ciscoC11128PLteEA": ciscoC11128PLteEA,
       "ciscoC11138P": ciscoC11138P,
       "ciscoC11138PM": ciscoC11138PM,
       "ciscoC11138PLteEA": ciscoC11138PLteEA,
       "ciscoC11138PLteLA": ciscoC11138PLteLA,
       "ciscoC11138PMLteEA": ciscoC11138PMLteEA,
       "ciscoC11138PWE": ciscoC11138PWE,
       "ciscoC11138PWA": ciscoC11138PWA,
       "ciscoC11138PWZ": ciscoC11138PWZ,
       "ciscoC11138PMWE": ciscoC11138PMWE,
       "ciscoC11138PLteEAWE": ciscoC11138PLteEAWE,
       "ciscoC11138PLteLAWE": ciscoC11138PLteLAWE,
       "ciscoC11138PLteLAWZ": ciscoC11138PLteLAWZ,
       "ciscoC11188P": ciscoC11188P,
       "ciscoC11164PLteEAWE": ciscoC11164PLteEAWE,
       "ciscoC11174PLteEAWE": ciscoC11174PLteEAWE,
       "ciscoC11174PLteEAWA": ciscoC11174PLteEAWA,
       "ciscoC11174PLteLAWZ": ciscoC11174PLteLAWZ,
       "ciscoC11174PMLteEAWE": ciscoC11174PMLteEAWE,
       "ciscoIR807GLTEVZK9": ciscoIR807GLTEVZK9,
       "ciscoIR807GLTEGAK9": ciscoIR807GLTEGAK9,
       "ciscoIR807GLTENAK9": ciscoIR807GLTENAK9,
       "ciscoUCSE180DM3K9": ciscoUCSE180DM3K9,
       "ciscoUCSE1120DM3K9": ciscoUCSE1120DM3K9,
       "ciscoCat930048UN": ciscoCat930048UN,
       "ciscoNFVIS": ciscoNFVIS,
       "ciscoCat950032C": ciscoCat950032C,
       "ciscoCat950032QC": ciscoCat950032QC,
       "ciscoCat950048Y4C": ciscoCat950048Y4C,
       "ciscoIR829GWLTEGAxK9": ciscoIR829GWLTEGAxK9,
       "ciscoNCS55A2MODSES": ciscoNCS55A2MODSES,
       "ciscoNCS55A2MODS": ciscoNCS55A2MODS,
       "ciscoASR9906": ciscoASR9906,
       "ciscoCat950024Y4C": ciscoCat950024Y4C,
       "ciscoCat9200L24P4X": ciscoCat9200L24P4X,
       "ciscoCat9200L48P4X": ciscoCat9200L48P4X,
       "ciscoCat9200L24PXG4X": ciscoCat9200L24PXG4X,
       "ciscoCat9200L24PXG2Y": ciscoCat9200L24PXG2Y,
       "ciscoCat9200L48PXG4X": ciscoCat9200L48PXG4X,
       "ciscoCat9200L48PXG2Y": ciscoCat9200L48PXG2Y,
       "ciscoCat920024T": ciscoCat920024T,
       "ciscoCat9200L24T4G": ciscoCat9200L24T4G,
       "ciscoCat9200L48T4G": ciscoCat9200L48T4G,
       "ciscoCat9200L24T4X": ciscoCat9200L24T4X,
       "ciscoCat9200L48T4X": ciscoCat9200L48T4X,
       "ciscoCat9200L24P4G": ciscoCat9200L24P4G,
       "ciscoCat9200L48P4G": ciscoCat9200L48P4G,
       "ciscoCat920048T": ciscoCat920048T,
       "ciscoCat920024P": ciscoCat920024P,
       "ciscoCat920048P": ciscoCat920048P,
       "ciscoCat920024PXG": ciscoCat920024PXG,
       "ciscoCat920048PXG": ciscoCat920048PXG,
       "ciscoCat950016X": ciscoCat950016X,
       "ciscoCat9500FixedSwitchStack": ciscoCat9500FixedSwitchStack,
       "ciscoN5204GAZA": ciscoN5204GAZA,
       "ciscoN52020G4ZA": ciscoN52020G4ZA,
       "ciscoN52020G4ZD": ciscoN52020G4ZD,
       "ciscoN520X4G4ZA": ciscoN520X4G4ZA,
       "ciscoN520X4G4ZD": ciscoN520X4G4ZD,
       "ciscoN520X20G4ZA": ciscoN520X20G4ZA,
       "ciscoN520X20G4ZD": ciscoN520X20G4ZD,
       "ciscoIR829MLTELAxK9": ciscoIR829MLTELAxK9,
       "ciscoIR829M2LTEEAxK9": ciscoIR829M2LTEEAxK9,
       "ciscoISA30004Ctd": ciscoISA30004Ctd,
       "ciscoISA30002C2Ftd": ciscoISA30002C2Ftd,
       "ciscoRA1783SAD4T0Std": ciscoRA1783SAD4T0Std,
       "ciscoRA1783SAD2T2Std": ciscoRA1783SAD2T2Std,
       "cisco8818": cisco8818,
       "cisco8812": cisco8812,
       "cisco8808": cisco8808,
       "ciscoC11092PLteGB": ciscoC11092PLteGB,
       "ciscoC11092PLteUS": ciscoC11092PLteUS,
       "ciscoC11092PLteVZ": ciscoC11092PLteVZ,
       "ciscoC11092PLteJN": ciscoC11092PLteJN,
       "ciscoC11092PLteAU": ciscoC11092PLteAU,
       "ciscoC11092PLteIN": ciscoC11092PLteIN,
       "ciscoC11014P": ciscoC11014P,
       "ciscoC11014PLteP": ciscoC11014PLteP,
       "ciscoC11014PLtePWE": ciscoC11014PLtePWE,
       "ciscoC11014PLtePWB": ciscoC11014PLtePWB,
       "ciscoC11014PLtePWD": ciscoC11014PLtePWD,
       "ciscoC11014PLtePWZ": ciscoC11014PLtePWZ,
       "ciscoC11014PLtePWA": ciscoC11014PLtePWA,
       "ciscoC11014PLtePWH": ciscoC11014PLtePWH,
       "ciscoC11014PLtePWQ": ciscoC11014PLtePWQ,
       "ciscoC11014PLtePWR": ciscoC11014PLtePWR,
       "ciscoC11014PLtePWN": ciscoC11014PLtePWN,
       "ciscoC11014PLtePWF": ciscoC11014PLtePWF,
       "ciscoC11094PLte2P": ciscoC11094PLte2P,
       "ciscoC11094PLte2PWB": ciscoC11094PLte2PWB,
       "ciscoC11094PLte2PWE": ciscoC11094PLte2PWE,
       "ciscoC11094PLte2PWD": ciscoC11094PLte2PWD,
       "ciscoC11094PLte2PWZ": ciscoC11094PLte2PWZ,
       "ciscoC11094PLte2PWA": ciscoC11094PLte2PWA,
       "ciscoC11094PLte2PWH": ciscoC11094PLte2PWH,
       "ciscoC11094PLte2PWQ": ciscoC11094PLte2PWQ,
       "ciscoC11094PLte2PWN": ciscoC11094PLte2PWN,
       "ciscoC11094PLte2PWR": ciscoC11094PLte2PWR,
       "ciscoC11094PLte2PWF": ciscoC11094PLte2PWF,
       "ciscoC9606R": ciscoC9606R,
       "cisco8201": cisco8201,
       "cisco8202": cisco8202,
       "ciscoC11128PWE": ciscoC11128PWE,
       "ciscoC11128PLteEAWE": ciscoC11128PLteEAWE,
       "ciscoC11138PWB": ciscoC11138PWB,
       "ciscoC11138PLteEAWB": ciscoC11138PLteEAWB,
       "ciscoC11138PLteLAWA": ciscoC11138PLteLAWA,
       "ciscoC11164PLteLA": ciscoC11164PLteLA,
       "ciscoASR9901": ciscoASR9901,
       "ciscoEsxSECPA": ciscoEsxSECPA,
       "ciscoKvmSECPA": ciscoKvmSECPA,
       "ciscoIR1101K9": ciscoIR1101K9,
       "ciscoFpr1140td": ciscoFpr1140td,
       "ciscoFpr1120td": ciscoFpr1120td,
       "ciscoCat9400VirtualStack": ciscoCat9400VirtualStack,
       "ciscoISRAP1100ACME": ciscoISRAP1100ACME,
       "ciscoISR4221X": ciscoISR4221X,
       "ciscoC1111X8P": ciscoC1111X8P,
       "ciscoC980080K9": ciscoC980080K9,
       "ciscoAP4800": ciscoAP4800,
       "ciscoIR829M2LTELAxK9": ciscoIR829M2LTELAxK9,
       "ciscoIR829MLTEEAxK9": ciscoIR829MLTEEAxK9,
       "ciscoIR829BLTEEAxK9": ciscoIR829BLTEEAxK9,
       "ciscoIR829BLTELAxK9": ciscoIR829BLTELAxK9,
       "ciscoIR829B2LTEEAxK9": ciscoIR829B2LTEEAxK9,
       "ciscoIR829B2LTELAxK9": ciscoIR829B2LTELAxK9,
       "ciscoASR92012SZD": ciscoASR92012SZD,
       "ciscoASR92012SZA": ciscoASR92012SZA,
       "ciscoISR4461": ciscoISR4461,
       "ciscoESS3300NCP": ciscoESS3300NCP,
       "ciscoESS3300CON": ciscoESS3300CON,
       "ciscoIE32008T2S": ciscoIE32008T2S,
       "ciscoIE32008P2S": ciscoIE32008P2S,
       "ciscoIE33008T2S": ciscoIE33008T2S,
       "ciscoIE33008P2S": ciscoIE33008P2S,
       "ciscoIE34008P2S": ciscoIE34008P2S,
       "ciscoCat9500VirtualStack": ciscoCat9500VirtualStack,
       "ciscoNam2520": ciscoNam2520,
       "ciscoNam2540": ciscoNam2540,
       "ciscoCSPA2520": ciscoCSPA2520,
       "ciscoIR1101XK9": ciscoIR1101XK9,
       "ciscoVG450": ciscoVG450,
       "ciscoCat9200LFixedSwitchStack": ciscoCat9200LFixedSwitchStack,
       "ciscoCat9200FixedSwitchStack": ciscoCat9200FixedSwitchStack,
       "ciscoRAIE1783MMS10B": ciscoRAIE1783MMS10B,
       "ciscoRAIE1783MMS10BE": ciscoRAIE1783MMS10BE,
       "ciscoRAIE1783MMS10": ciscoRAIE1783MMS10,
       "ciscoRAIE1783MMS10R": ciscoRAIE1783MMS10R,
       "ciscoRAIE1783MMS10E": ciscoRAIE1783MMS10E,
       "ciscoRAIE1783MMS10ER": ciscoRAIE1783MMS10ER,
       "ciscoRAIE1783MMS10EA": ciscoRAIE1783MMS10EA,
       "ciscoRAIE1783MMS10EAR": ciscoRAIE1783MMS10EAR,
       "ciscoASR92020SZM": ciscoASR92020SZM,
       "cisco9214PK9": cisco9214PK9,
       "cisco9314PK9": cisco9314PK9,
       "cisco9214PLTEGBK9": cisco9214PLTEGBK9,
       "cisco9214PLTEASK9": cisco9214PLTEASK9,
       "cisco9214PLTEAUK9": cisco9214PLTEAUK9,
       "cisco921J4PK9": cisco921J4PK9,
       "cisco9274PK9": cisco9274PK9,
       "cisco9274PMK9": cisco9274PMK9,
       "cisco9264PK9": cisco9264PK9,
       "cisco9274PLTEAUK9": cisco9274PLTEAUK9,
       "cisco9274PLTEGBK9": cisco9274PLTEGBK9,
       "cisco9274PMLTEGBK9": cisco9274PMLTEGBK9,
       "cisco9264PLTEGBK9": cisco9264PLTEGBK9,
       "ciscoAP1840": ciscoAP1840,
       "ciscoC11118PWS": ciscoC11118PWS,
       "ciscoC11118PLteLAWS": ciscoC11118PLteLAWS,
       "ciscoC11118PLteLAWA": ciscoC11118PLteLAWA,
       "ciscoC11118PLteLAWE": ciscoC11118PLteLAWE,
       "ciscoNCS55A2MODHDS": ciscoNCS55A2MODHDS,
       "ciscoUCSC125": ciscoUCSC125,
       "ciscoWSC6506E": ciscoWSC6506E,
       "ciscoWSC6509E": ciscoWSC6509E,
       "ciscoNCS1004": ciscoNCS1004,
       "ciscoN54024Z8Q2CM": ciscoN54024Z8Q2CM,
       "ciscoN540X24Z8Q2CM": ciscoN540X24Z8Q2CM,
       "ciscoN560RSP4": ciscoN560RSP4,
       "ciscoN560RSP4E": ciscoN560RSP4E,
       "ciscoC11218PLteP": ciscoC11218PLteP,
       "ciscoC1121X8PLTEP": ciscoC1121X8PLTEP,
       "ciscoC11218PLtePWE": ciscoC11218PLtePWE,
       "ciscoC11218PLtePWB": ciscoC11218PLtePWB,
       "ciscoC11218PLtePWZ": ciscoC11218PLtePWZ,
       "ciscoC11218PLtePWQ": ciscoC11218PLtePWQ,
       "ciscoC11218P": ciscoC11218P,
       "ciscoC1121X8P": ciscoC1121X8P,
       "ciscoC11618P": ciscoC11618P,
       "ciscoC1161X8P": ciscoC1161X8P,
       "ciscoC11618PLteP": ciscoC11618PLteP,
       "ciscoC1161X8PLteP": ciscoC1161X8PLteP,
       "ciscoFpr9000SM56": ciscoFpr9000SM56,
       "ciscoC11268PLteP": ciscoC11268PLteP,
       "ciscoC11278PLteP": ciscoC11278PLteP,
       "ciscoC11278PMLteP": ciscoC11278PMLteP,
       "ciscoC1126X8PLteP": ciscoC1126X8PLteP,
       "ciscoC1127X8PLteP": ciscoC1127X8PLteP,
       "ciscoC1127X8PMLteP": ciscoC1127X8PMLteP,
       "ciscoC11214P": ciscoC11214P,
       "ciscoC11214PLteP": ciscoC11214PLteP,
       "ciscoC11288PLteP": ciscoC11288PLteP,
       "ciscoVG4002FXS2FXO": ciscoVG4002FXS2FXO,
       "ciscoVG4004FXS4FXO": ciscoVG4004FXS4FXO,
       "ciscoVG4006FXS6FXO": ciscoVG4006FXS6FXO,
       "ciscoVG4008FXS": ciscoVG4008FXS,
       "ciscoC891FJK9": ciscoC891FJK9,
       "ciscoFpr9000SM40": ciscoFpr9000SM40,
       "ciscoFpr9000SM48": ciscoFpr9000SM48,
       "ciscoFpr4115SM24": ciscoFpr4115SM24,
       "ciscoFpr4125SM32": ciscoFpr4125SM32,
       "ciscoFpr4145SM44": ciscoFpr4145SM44,
       "ciscoFpr4145K9": ciscoFpr4145K9,
       "ciscoFpr4125K9": ciscoFpr4125K9,
       "ciscoFpr4115K9": ciscoFpr4115K9,
       "ciscoCat930024S": ciscoCat930024S,
       "ciscoCat930048S": ciscoCat930048S,
       "ciscoIOSXREdgecore591654XKSOACF": ciscoIOSXREdgecore591654XKSOACF,
       "ciscoIOSXREdgecoreAS781664X": ciscoIOSXREdgecoreAS781664X,
       "ciscoSNS3615K9": ciscoSNS3615K9,
       "ciscoSNS3655K9": ciscoSNS3655K9,
       "ciscoSNS3695K9": ciscoSNS3695K9,
       "ciscoNCS55A2MODHXS": ciscoNCS55A2MODHXS,
       "ciscoC1121X8PLtePWE": ciscoC1121X8PLtePWE,
       "ciscoC1121X8PLtePWB": ciscoC1121X8PLtePWB,
       "ciscoC1121X8PLtePWZ": ciscoC1121X8PLtePWZ,
       "ciscoC1121X8PLtePWA": ciscoC1121X8PLtePWA,
       "ciscoCat9300L24T4G": ciscoCat9300L24T4G,
       "ciscoCat9300L48T4G": ciscoCat9300L48T4G,
       "ciscoCat9300L24T4X": ciscoCat9300L24T4X,
       "ciscoCat9300L48T4X": ciscoCat9300L48T4X,
       "ciscoCat9300L24P4G": ciscoCat9300L24P4G,
       "ciscoCat9300L48P4G": ciscoCat9300L48P4G,
       "ciscoCat9300L24P4X": ciscoCat9300L24P4X,
       "ciscoCat9300L48P4X": ciscoCat9300L48P4X,
       "ciscoCat9300L24UXG4X": ciscoCat9300L24UXG4X,
       "ciscoCat9300L48UXG4X": ciscoCat9300L48UXG4X,
       "ciscoCat9300L24UXG2Q": ciscoCat9300L24UXG2Q,
       "ciscoCat9300L48UXG2Q": ciscoCat9300L48UXG2Q,
       "ciscocat9300Lstack": ciscocat9300Lstack,
       "ciscoCatWSC2960LSM8TS": ciscoCatWSC2960LSM8TS,
       "ciscoCatWSC2960LSM8PS": ciscoCatWSC2960LSM8PS,
       "ciscoCatWSC2960LSM16TS": ciscoCatWSC2960LSM16TS,
       "ciscoCatWSC2960LSM16PS": ciscoCatWSC2960LSM16PS,
       "ciscoCatWSC2960LSM24TS": ciscoCatWSC2960LSM24TS,
       "ciscoCatWSC2960LSM24PS": ciscoCatWSC2960LSM24PS,
       "ciscoCatWSC2960LSM48TS": ciscoCatWSC2960LSM48TS,
       "ciscoCatWSC2960LSM48PS": ciscoCatWSC2960LSM48PS,
       "ciscoCatWSC2960LSM24TQ": ciscoCatWSC2960LSM24TQ,
       "ciscoCatWSC2960LSM48TQ": ciscoCatWSC2960LSM48TQ,
       "ciscoCatWSC2960LSM24PQ": ciscoCatWSC2960LSM24PQ,
       "ciscoCatWSC2960LSM48PQ": ciscoCatWSC2960LSM48PQ,
       "ciscoC850012X4QC": ciscoC850012X4QC,
       "ciscoC850012X": ciscoC850012X,
       "ciscoC9592PLteGB": ciscoC9592PLteGB,
       "ciscoC9592PLteUS": ciscoC9592PLteUS,
       "ciscoC9592PLteVZ": ciscoC9592PLteVZ,
       "ciscoC9592PLteIN": ciscoC9592PLteIN,
       "ciscoC9514P": ciscoC9514P,
       "ciscoCMeWlc": ciscoCMeWlc,
       "ciscoIE34008FTMC": ciscoIE34008FTMC,
       "ciscoIE340016FTMC": ciscoIE340016FTMC,
       "ciscoIE340024FTMC": ciscoIE340024FTMC,
       "ciscoIE34008TMC": ciscoIE34008TMC,
       "ciscoIE340016TMC": ciscoIE340016TMC,
       "ciscoIE340024TMC": ciscoIE340024TMC,
       "ciscoCat930024UBX": ciscoCat930024UBX,
       "ciscoCat930048UB": ciscoCat930048UB,
       "ciscoCat930024UB": ciscoCat930024UB,
       "ciscoC9115AXI": ciscoC9115AXI,
       "ciscoC9115AXME": ciscoC9115AXME,
       "ciscoC9117AXME": ciscoC9117AXME,
       "ciscoC9117AXI": ciscoC9117AXI,
       "ciscoNCS5064": ciscoNCS5064,
       "ciscoESR1115CONK9": ciscoESR1115CONK9,
       "ciscoESR1115NCPK9": ciscoESR1115NCPK9,
       "ciscoC9115AXE": ciscoC9115AXE,
       "ciscoC9120AXI": ciscoC9120AXI,
       "ciscoC9120AXME": ciscoC9120AXME,
       "ciscoC9120AXE": ciscoC9120AXE,
       "ciscoC9120AXEME": ciscoC9120AXEME,
       "ciscoN5604": ciscoN5604,
       "ciscoN5604CC": ciscoN5604CC,
       "ciscoN5604RSP4": ciscoN5604RSP4,
       "ciscoN5604RSP4E": ciscoN5604RSP4E,
       "ciscoN5604RSP4CC": ciscoN5604RSP4CC,
       "ciscoN5604RSP4ECC": ciscoN5604RSP4ECC,
       "ciscoC9800LCK9": ciscoC9800LCK9,
       "ciscoC9800LFK9": ciscoC9800LFK9,
       "ciscoESR6300CONK9": ciscoESR6300CONK9,
       "ciscoESR6300NCPK9": ciscoESR6300NCPK9,
       "ciscoNCS55A148Q6H": ciscoNCS55A148Q6H,
       "ciscoNCS55A148T6H": ciscoNCS55A148T6H,
       "ciscoCMICR4PS": ciscoCMICR4PS,
       "ciscoCMICR4PC": ciscoCMICR4PC,
       "ciscoFpr1150td": ciscoFpr1150td,
       "ciscoC9606RVirtualStack": ciscoC9606RVirtualStack,
       "ciscoIE34008T2S": ciscoIE34008T2S,
       "ciscoCat930024H": ciscoCat930024H,
       "ciscoCat930048H": ciscoCat930048H,
       "ciscoC9130AXI": ciscoC9130AXI,
       "ciscoC9130AXIME": ciscoC9130AXIME,
       "ciscoC9130AXE": ciscoC9130AXE,
       "ciscoC9130AXEME": ciscoC9130AXEME,
       "ciscoIE3400H8FT": ciscoIE3400H8FT,
       "ciscoIE3400H16FT": ciscoIE3400H16FT,
       "ciscoIE3400H24FT": ciscoIE3400H24FT,
       "ciscoIE3400H8T": ciscoIE3400H8T,
       "ciscoIE3400H16T": ciscoIE3400H16T,
       "ciscoIE3400H24T": ciscoIE3400H24T,
       "ciscoENCS5104": ciscoENCS5104,
       "ciscoRAIE1783MMS10A": ciscoRAIE1783MMS10A,
       "ciscoRAIE1783MMS10AR": ciscoRAIE1783MMS10AR,
       "ciscoENCS510464": ciscoENCS510464,
       "ciscoENCS5104200": ciscoENCS5104200,
       "ciscoENCS5104400": ciscoENCS5104400,
       "ciscoC10008T2GL": ciscoC10008T2GL,
       "ciscoCat100010GbpsStack": ciscoCat100010GbpsStack,
       "ciscoAIRIW6300ME": ciscoAIRIW6300ME,
       "ciscoFpr4112K9": ciscoFpr4112K9,
       "ciscoCSP5200": ciscoCSP5200,
       "ciscoCSP5216": ciscoCSP5216,
       "ciscoCSP5228": ciscoCSP5228,
       "ciscoCSP5400": ciscoCSP5400,
       "ciscoCSP5436": ciscoCSP5436,
       "ciscoCSP5444": ciscoCSP5444,
       "ciscoCSP5456": ciscoCSP5456,
       "ciscoCat920024PB": ciscoCat920024PB,
       "ciscoCat920048PB": ciscoCat920048PB,
       "ciscoC10008TE2GL": ciscoC10008TE2GL,
       "ciscoC10008P2GL": ciscoC10008P2GL,
       "ciscoC10008PE2GL": ciscoC10008PE2GL,
       "ciscoC10008FP2GL": ciscoC10008FP2GL,
       "ciscoC10008FPE2GL": ciscoC10008FPE2GL,
       "ciscoC100016T2GL": ciscoC100016T2GL,
       "ciscoC100016TE2GL": ciscoC100016TE2GL,
       "ciscoC100016P2GL": ciscoC100016P2GL,
       "ciscoC100016PE2GL": ciscoC100016PE2GL,
       "ciscoC100016FP2GL": ciscoC100016FP2GL,
       "ciscoC100024T4GL": ciscoC100024T4GL,
       "ciscoC100024PP4GL": ciscoC100024PP4GL,
       "ciscoC100024P4GL": ciscoC100024P4GL,
       "ciscoC100024FP4GL": ciscoC100024FP4GL,
       "ciscoC100048T4GL": ciscoC100048T4GL,
       "ciscoC100048PP4GL": ciscoC100048PP4GL,
       "ciscoC100048P4GL": ciscoC100048P4GL,
       "ciscoC100048FP4GL": ciscoC100048FP4GL,
       "ciscoC100024T4XL": ciscoC100024T4XL,
       "ciscoC100024P4XL": ciscoC100024P4XL,
       "ciscoC100024FP4XL": ciscoC100024FP4XL,
       "ciscoC100048T4XL": ciscoC100048T4XL,
       "ciscoC100048P4XL": ciscoC100048P4XL,
       "ciscoC100048FP4XL": ciscoC100048FP4XL,
       "ciscoMobilityExpress": ciscoMobilityExpress,
       "ciscoCat10001GbpsStack": ciscoCat10001GbpsStack,
       "ciscoC82001N4T": ciscoC82001N4T,
       "ciscoC8200L4G": ciscoC8200L4G,
       "ciscoC83002N2S4T2X": ciscoC83002N2S4T2X,
       "ciscoC83002N2S6T": ciscoC83002N2S6T,
       "ciscoCat9200BFixedSwitchStack": ciscoCat9200BFixedSwitchStack,
       "ciscoESW6300ME": ciscoESW6300ME,
       "ciscoC8500L8G4X": ciscoC8500L8G4X,
       "ciscoC1100TG1N32A": ciscoC1100TG1N32A,
       "ciscoC1100TG1N24P32A": ciscoC1100TG1N24P32A,
       "ciscoC1100TGX1N24P32A": ciscoC1100TGX1N24P32A,
       "ciscoCMICR4PT": ciscoCMICR4PT,
       "ciscoNCS540L28Z4SysA": ciscoNCS540L28Z4SysA,
       "ciscoNCS540L28Z4SysD": ciscoNCS540L28Z4SysD,
       "ciscoNCS540L16Z4G8Q2CA": ciscoNCS540L16Z4G8Q2CA,
       "ciscoNCS540L16Z4G8Q2CD": ciscoNCS540L16Z4G8Q2CD,
       "ciscoNCS540L12Z20GSysA": ciscoNCS540L12Z20GSysA,
       "ciscoNCS540L12Z20GSysD": ciscoNCS540L12Z20GSysD,
       "ciscoNCS540L12Z16GSysA": ciscoNCS540L12Z16GSysA,
       "ciscoNCS540L12Z16GSysD": ciscoNCS540L12Z16GSysD,
       "ciscoC83001N1S6T": ciscoC83001N1S6T,
       "ciscoC83001N1S4T2X": ciscoC83001N1S4T2X,
       "ciscoFpr4112SM12": ciscoFpr4112SM12,
       "ciscoCat9300L48PF4X": ciscoCat9300L48PF4X,
       "ciscoCat9300L48PF4G": ciscoCat9300L48PF4G,
       "ciscoNCS540LFHCSRSys": ciscoNCS540LFHCSRSys,
       "ciscoNCS540LFHAGGSys": ciscoNCS540LFHAGGSys,
       "ciscoNCS540LFHIP65Sys": ciscoNCS540LFHIP65Sys,
       "ciscoC8000V": ciscoC8000V,
       "ciscoIE33008T2X": ciscoIE33008T2X,
       "ciscoIE33008U2X": ciscoIE33008U2X,
       "ciscoNCS54016G": ciscoNCS54016G,
       "ciscoNCS540X16G": ciscoNCS540X16G,
       "ciscoCat920048PL": ciscoCat920048PL,
       "ciscoC9200L48PL4G": ciscoC9200L48PL4G,
       "ciscoC9200L48PL4X": ciscoC9200L48PL4X,
       "ciscoISR11004G": ciscoISR11004G,
       "ciscoISR11006G": ciscoISR11006G,
       "ciscoISR11004GLTEGB": ciscoISR11004GLTEGB,
       "ciscoISR11004GLTENA": ciscoISR11004GLTENA,
       "ciscoC1000FE24T4GL": ciscoC1000FE24T4GL,
       "ciscoC1000FE24P4GL": ciscoC1000FE24P4GL,
       "ciscoC1000FE48T4GL": ciscoC1000FE48T4GL,
       "ciscoC1000FE48P4GL": ciscoC1000FE48P4GL,
       "ciscoDNAPLTTA1X": ciscoDNAPLTTA1X,
       "ciscoIR1821K9": ciscoIR1821K9,
       "ciscoIR1831K9": ciscoIR1831K9,
       "ciscoIR1833K9": ciscoIR1833K9,
       "ciscoIR1835K9": ciscoIR1835K9,
       "ciscoNCS540L6Z18GSysA": ciscoNCS540L6Z18GSysA,
       "ciscoNCS540L6Z18GSysD": ciscoNCS540L6Z18GSysD,
       "ciscoNCS540L8Z16GSysD": ciscoNCS540L8Z16GSysD,
       "ciscoNCS540L8Z16GSysA": ciscoNCS540L8Z16GSysA,
       "ciscoNCS540L4Z14G2QA": ciscoNCS540L4Z14G2QA,
       "ciscoNCS540L4Z14G2QD": ciscoNCS540L4Z14G2QD,
       "ciscoC9300X12Y": ciscoC9300X12Y,
       "ciscoC9300X24Y": ciscoC9300X24Y,
       "ciscoC9300X48HX": ciscoC9300X48HX,
       "ciscoC9300X48TX": ciscoC9300X48TX,
       "ciscoISR1100X4G": ciscoISR1100X4G,
       "ciscoISR1100X6G": ciscoISR1100X6G,
       "ciscoESS930010XE": ciscoESS930010XE,
       "ciscoIR8140HK9": ciscoIR8140HK9,
       "ciscoIR8140HPK9": ciscoIR8140HPK9,
       "ciscoC9115AXEME": ciscoC9115AXEME,
       "ciscoC9120AXPME": ciscoC9120AXPME,
       "ciscoIR8340K9": ciscoIR8340K9,
       "ciscoFpr3110K9": ciscoFpr3110K9,
       "ciscoFpr3120K9": ciscoFpr3120K9,
       "ciscoFpr3130K9": ciscoFpr3130K9,
       "ciscoFpr3140K9": ciscoFpr3140K9,
       "ciscoC9KF1SSD960G": ciscoC9KF1SSD960G,
       "ciscoC9KF1SSD480G": ciscoC9KF1SSD480G,
       "ciscoC9KF1SSD240G": ciscoC9KF1SSD240G,
       "ciscoC8500L8S4X": ciscoC8500L8S4X,
       "ciscoC11138PLteEAWA": ciscoC11138PLteEAWA,
       "ciscoVG420144FXS": ciscoVG420144FXS,
       "ciscoVG420132FXS6FXO": ciscoVG420132FXS6FXO,
       "ciscoVG42084FXS6FXO": ciscoVG42084FXS6FXO,
       "ciscoC8200L1N4T": ciscoC8200L1N4T,
       "ciscoASR9903": ciscoASR9903,
       "ciscoNCS57B15DSESys": ciscoNCS57B15DSESys,
       "ciscoNCS57B16D24Sys": ciscoNCS57B16D24Sys,
       "ciscoCat9200CX12T2X2G": ciscoCat9200CX12T2X2G,
       "ciscoCat9200CX12P2X2G": ciscoCat9200CX12P2X2G,
       "ciscoCat9500X28C8D": ciscoCat9500X28C8D,
       "ciscoC850020X6C": ciscoC850020X6C,
       "ciscoC9300X48HXN": ciscoC9300X48HXN,
       "ciscoC9300X24HX": ciscoC9300X24HX,
       "ciscoXRdControlPlaneC1": ciscoXRdControlPlaneC1,
       "ciscoASR9902": ciscoASR9902,
       "ciscoCat9200CX8P2X2G": ciscoCat9200CX8P2X2G,
       "ciscoCat9200CX8PT2G": ciscoCat9200CX8PT2G,
       "ciscoCat9200CX8UXG2X": ciscoCat9200CX8UXG2X,
       "ciscoUCSC220M6": ciscoUCSC220M6,
       "ciscoUCSC240M6": ciscoUCSC240M6,
       "ciscoUCSB200M5": ciscoUCSB200M5,
       "ciscoUCSB480M5": ciscoUCSB480M5,
       "ciscoC11318PWE": ciscoC11318PWE,
       "ciscoC11318PWA": ciscoC11318PWA,
       "ciscoC11318PWB": ciscoC11318PWB,
       "ciscoC11318PWZ": ciscoC11318PWZ,
       "ciscoC11318PWQ": ciscoC11318PWQ,
       "ciscoC1131X8PWE": ciscoC1131X8PWE,
       "ciscoC1131X8PWA": ciscoC1131X8PWA,
       "ciscoC1131X8PWB": ciscoC1131X8PWB,
       "ciscoC1131X8PWZ": ciscoC1131X8PWZ,
       "ciscoC1131X8PWQ": ciscoC1131X8PWQ,
       "ciscoC11318PLTEPWB": ciscoC11318PLTEPWB,
       "ciscoC1131X8PLTEPWE": ciscoC1131X8PLTEPWE,
       "ciscoC1131X8PLTEPWA": ciscoC1131X8PLTEPWA,
       "ciscoC11318PLTEPWA": ciscoC11318PLTEPWA,
       "ciscoC11318PLTEPWZ": ciscoC11318PLTEPWZ,
       "ciscoC11318PLTEPWQ": ciscoC11318PLTEPWQ,
       "ciscoC11318PLTEPWE": ciscoC11318PLTEPWE,
       "ciscoC1131X8PLTEPWZ": ciscoC1131X8PLTEPWZ,
       "ciscoC1131X8PLTEPWB": ciscoC1131X8PLTEPWB,
       "ciscoC1131X8PLTEPWQ": ciscoC1131X8PLTEPWQ,
       "ciscoIE931026S2C": ciscoIE931026S2C,
       "ciscoIE9320stack": ciscoIE9320stack,
       "ciscoIC30002C2FK9": ciscoIC30002C2FK9,
       "ciscoUCSIOM2208": ciscoUCSIOM2208,
       "ciscoUCSIOM2304": ciscoUCSIOM2304,
       "ciscoUCSIOM2408": ciscoUCSIOM2408,
       "ciscoUCSBXI910825G": ciscoUCSBXI910825G,
       "ciscoUCSBXI9108100G": ciscoUCSBXI9108100G,
       "ciscoNCS540L24Q8L2DDSys": ciscoNCS540L24Q8L2DDSys,
       "cisco810132FH": cisco810132FH,
       "ciscoISRAP1101AX": ciscoISRAP1101AX,
       "ciscoNCS55A124Q6HSS": ciscoNCS55A124Q6HSS,
       "ciscoNCS57C3MODSSYS": ciscoNCS57C3MODSSYS,
       "ciscoNCS57C3MODSYS": ciscoNCS57C3MODSYS,
       "cisco811132EH": cisco811132EH,
       "cisco820232FHM": cisco820232FHM,
       "cisco820232FHMO": cisco820232FHMO,
       "ciscoNCS1010": ciscoNCS1010,
       "ciscoNCS57C148Q6Sys": ciscoNCS57C148Q6Sys,
       "ciscoNCS55A124Q6HS": ciscoNCS55A124Q6HS,
       "ciscoNCS540L6Z14GSysD": ciscoNCS540L6Z14GSysD,
       "ciscoC9200CX12P2XGH": ciscoC9200CX12P2XGH,
       "ciscoIE932026S2C": ciscoIE932026S2C,
       "ciscoFpr3105K9": ciscoFpr3105K9,
       "ciscoUCSC225M6": ciscoUCSC225M6,
       "ciscoIE31004T2S": ciscoIE31004T2S,
       "ciscoIE31008T2C": ciscoIE31008T2C,
       "ciscoIE310018T2C": ciscoIE310018T2C,
       "ciscoIE31058T2C": ciscoIE31058T2C,
       "ciscoIE310518T2C": ciscoIE310518T2C,
       "ciscoRAIE1783CMS6B": ciscoRAIE1783CMS6B,
       "ciscoRAIE1783CMS6P": ciscoRAIE1783CMS6P,
       "ciscoRAIE1783CMS10B": ciscoRAIE1783CMS10B,
       "ciscoRAIE1783CMS10P": ciscoRAIE1783CMS10P,
       "ciscoRAIE1783CMS10DP": ciscoRAIE1783CMS10DP,
       "ciscoRAIE1783CMS10DN": ciscoRAIE1783CMS10DN,
       "ciscoRAIE1783CMS20DB": ciscoRAIE1783CMS20DB,
       "ciscoRAIE1783CMS20DP": ciscoRAIE1783CMS20DP,
       "ciscoRAIE1783CMS20DN": ciscoRAIE1783CMS20DN,
       "ciscoXRdvRouterC1": ciscoXRdvRouterC1,
       "cisco810132H": cisco810132H,
       "cisco810264H": cisco810264H,
       "ciscoC9200CX8P2XGH": ciscoC9200CX8P2XGH,
       "ciscoC9200CX8UXG2XH": ciscoC9200CX8UXG2XH,
       "ciscoESR6300LICK9": ciscoESR6300LICK9,
       "ciscoDP01QSDDZF1": ciscoDP01QSDDZF1,
       "ciscoIE932022S2C4X": ciscoIE932022S2C4X,
       "ciscoIE932024T4X": ciscoIE932024T4X,
       "ciscoIE932024P4X": ciscoIE932024P4X,
       "ciscoIE932016P8U4X": ciscoIE932016P8U4X,
       "ciscoIE932024P4S": ciscoIE932024P4S,
       "ciscoIE31008T4S": ciscoIE31008T4S,
       "ciscoC8500L8S2X2Y": ciscoC8500L8S2X2Y,
       "ciscoC8500L8S8X4Y": ciscoC8500L8S8X4Y,
       "ciscoC8300UCPE1N20": ciscoC8300UCPE1N20,
       "ciscoUCSC220M7": ciscoUCSC220M7,
       "ciscoUCSC240M7": ciscoUCSC240M7,
       "ciscoC12008TD": ciscoC12008TD,
       "ciscoC12008TE2G": ciscoC12008TE2G,
       "ciscoC12008PE2G": ciscoC12008PE2G,
       "ciscoC12008FP2G": ciscoC12008FP2G,
       "ciscoC120016T2G": ciscoC120016T2G,
       "ciscoC120016P2G": ciscoC120016P2G,
       "ciscoC120024T4G": ciscoC120024T4G,
       "ciscoC120024P4G": ciscoC120024P4G,
       "ciscoC120024FP4G": ciscoC120024FP4G,
       "ciscoC120048T4G": ciscoC120048T4G,
       "ciscoC120048P4G": ciscoC120048P4G,
       "ciscoC120024T4X": ciscoC120024T4X,
       "ciscoC120024P4X": ciscoC120024P4X,
       "ciscoC120024FP4X": ciscoC120024FP4X,
       "ciscoC120048T4X": ciscoC120048T4X,
       "ciscoC120048P4X": ciscoC120048P4X,
       "ciscoC13008TE2G": ciscoC13008TE2G,
       "ciscoC13008PE2G": ciscoC13008PE2G,
       "ciscoC13008FP2G": ciscoC13008FP2G,
       "ciscoC130016T2G": ciscoC130016T2G,
       "ciscoC130016P2G": ciscoC130016P2G,
       "ciscoC130016FP2G": ciscoC130016FP2G,
       "ciscoC130024T4G": ciscoC130024T4G,
       "ciscoC130024P4G": ciscoC130024P4G,
       "ciscoC130024FP4G": ciscoC130024FP4G,
       "ciscoC130048T4G": ciscoC130048T4G,
       "ciscoC130048P4G": ciscoC130048P4G,
       "ciscoC130048FP4G": ciscoC130048FP4G,
       "ciscoC130016P4X": ciscoC130016P4X,
       "ciscoC130024T4X": ciscoC130024T4X,
       "ciscoC130024P4X": ciscoC130024P4X,
       "ciscoC130024FP4X": ciscoC130024FP4X,
       "ciscoC130048T4X": ciscoC130048T4X,
       "ciscoC130048P4X": ciscoC130048P4X,
       "ciscoC130048FP4X": ciscoC130048FP4X,
       "ciscoC13008MGP2X": ciscoC13008MGP2X,
       "ciscoC130024MGP4X": ciscoC130024MGP4X,
       "ciscoC130048MGP4X": ciscoC130048MGP4X,
       "ciscoC130012XT2X": ciscoC130012XT2X,
       "ciscoC130012XS": ciscoC130012XS,
       "ciscoC130024XT": ciscoC130024XT,
       "ciscoC130024XS": ciscoC130024XS,
       "ciscoC130016XTS": ciscoC130016XTS,
       "ciscoC130024XTS": ciscoC130024XTS,
       "ciscoNCS57D218DDSYS": ciscoNCS57D218DDSYS,
       "ciscoUCSX410CM7": ciscoUCSX410CM7,
       "ciscoFpr1010Etd": ciscoFpr1010Etd,
       "ciscoSNS3715K9": ciscoSNS3715K9,
       "ciscoSNS3755K9": ciscoSNS3755K9,
       "ciscoSNS3795K9": ciscoSNS3795K9,
       "ciscoIW9165DHURWB": ciscoIW9165DHURWB,
       "ciscoIW9165EURWB": ciscoIW9165EURWB,
       "ciscoIW9167EHURWB": ciscoIW9167EHURWB,
       "ciscoCG522E": ciscoCG522E,
       "ciscoCG418E": ciscoCG418E,
       "ciscoCG1134GW6": ciscoCG1134GW6,
       "ciscoCG113W6": ciscoCG113W6,
       "ciscoC11318PWN": ciscoC11318PWN,
       "ciscoC11318PWH": ciscoC11318PWH,
       "ciscoC11318PWK": ciscoC11318PWK,
       "ciscoC11318PWF": ciscoC11318PWF,
       "ciscoC11318PWD": ciscoC11318PWD,
       "ciscoC11318PWR": ciscoC11318PWR,
       "ciscoC1131X8PWN": ciscoC1131X8PWN,
       "ciscoC1131X8PWH": ciscoC1131X8PWH,
       "ciscoC1131X8PWK": ciscoC1131X8PWK,
       "ciscoC1131X8PWF": ciscoC1131X8PWF,
       "ciscoC1131X8PWD": ciscoC1131X8PWD,
       "ciscoC1131X8PWR": ciscoC1131X8PWR,
       "ciscoC11318PLTEPWN": ciscoC11318PLTEPWN,
       "ciscoC11318PLTEPWH": ciscoC11318PLTEPWH,
       "ciscoC11318PLTEPWK": ciscoC11318PLTEPWK,
       "ciscoC11318PLTEPWF": ciscoC11318PLTEPWF,
       "ciscoC11318PLTEPWD": ciscoC11318PLTEPWD,
       "ciscoC11318PLTEPWR": ciscoC11318PLTEPWR,
       "ciscoC1131X8PLTEPWN": ciscoC1131X8PLTEPWN,
       "ciscoC1131X8PLTEPWH": ciscoC1131X8PLTEPWH,
       "ciscoC1131X8PLTEPWK": ciscoC1131X8PLTEPWK,
       "ciscoC1131X8PLTEPWF": ciscoC1131X8PLTEPWF,
       "ciscoC1131X8PLTEPWD": ciscoC1131X8PLTEPWD,
       "ciscoC1131X8PLTEPWR": ciscoC1131X8PLTEPWR,
       "ciscoNCS1014": ciscoNCS1014,
       "ciscoNCS1012": ciscoNCS1012,
       "ciscoNCS1020": ciscoNCS1020,
       "ciscoC9610R": ciscoC9610R,
       "ciscoProductsMIB": ciscoProductsMIB}
)
