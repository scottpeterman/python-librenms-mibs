# SNMP MIB module (PRIMEKEY-APPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\primekey\PRIMEKEY-APPLIANCE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:57 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

primekey = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22408)
)
if mibBuilder.loadTexts:
    primekey.setRevisions(
        ("2021-07-17 00:00",
         "2021-02-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrimeKeyAppliancePrefixOne_ObjectIdentity = ObjectIdentity
primeKeyAppliancePrefixOne = _PrimeKeyAppliancePrefixOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1)
)
_PrimeKeyAppliancePrefixAnotherOne_ObjectIdentity = ObjectIdentity
primeKeyAppliancePrefixAnotherOne = _PrimeKeyAppliancePrefixAnotherOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1)
)
_PkAppliance_ObjectIdentity = ObjectIdentity
pkAppliance = _PkAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2)
)
_PkSfp_ObjectIdentity = ObjectIdentity
pkSfp = _PkSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1)
)
_PkSfpTwo_ObjectIdentity = ObjectIdentity
pkSfpTwo = _PkSfpTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 2)
)
_PkSfpTwoV_ObjectIdentity = ObjectIdentity
pkSfpTwoV = _PkSfpTwoV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 2, 118)
)
_PkASfpVmStatusX_ObjectIdentity = ObjectIdentity
pkASfpVmStatusX = _PkASfpVmStatusX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 2, 118, 109)
)
_PkASfpVmStatus_Type = OctetString
_PkASfpVmStatus_Object = MibScalar
pkASfpVmStatus = _PkASfpVmStatus_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 2, 118, 109, 1),
    _PkASfpVmStatus_Type()
)
pkASfpVmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpVmStatus.setStatus("current")
_PkSfpThree_ObjectIdentity = ObjectIdentity
pkSfpThree = _PkSfpThree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 3)
)
_PkSfpThreeC_ObjectIdentity = ObjectIdentity
pkSfpThreeC = _PkSfpThreeC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 3, 99)
)
_PkSfpThreeP_ObjectIdentity = ObjectIdentity
pkSfpThreeP = _PkSfpThreeP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 3, 99, 112)
)
_PkASfpCpuTempX_ObjectIdentity = ObjectIdentity
pkASfpCpuTempX = _PkASfpCpuTempX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 3, 99, 112, 117)
)
_PkASfpCpuTemp_Type = OctetString
_PkASfpCpuTemp_Object = MibScalar
pkASfpCpuTemp = _PkASfpCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 3, 99, 112, 117, 1),
    _PkASfpCpuTemp_Type()
)
pkASfpCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpCpuTemp.setStatus("current")
_PkSfpFour_ObjectIdentity = ObjectIdentity
pkSfpFour = _PkSfpFour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4)
)
_PkSfpFourF_ObjectIdentity = ObjectIdentity
pkSfpFourF = _PkSfpFourF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102)
)
_PkSfpFourA_ObjectIdentity = ObjectIdentity
pkSfpFourA = _PkSfpFourA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97)
)
_PkSfpFourN_ObjectIdentity = ObjectIdentity
pkSfpFourN = _PkSfpFourN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110)
)
_PkASfpCpuFanX_ObjectIdentity = ObjectIdentity
pkASfpCpuFanX = _PkASfpCpuFanX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 49)
)
_PkASfpCpuFan_Type = OctetString
_PkASfpCpuFan_Object = MibScalar
pkASfpCpuFan = _PkASfpCpuFan_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 49, 1),
    _PkASfpCpuFan_Type()
)
pkASfpCpuFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpCpuFan.setStatus("current")
_PkASfpSysFan1X_ObjectIdentity = ObjectIdentity
pkASfpSysFan1X = _PkASfpSysFan1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 50)
)
_PkASfpSysFan1_Type = OctetString
_PkASfpSysFan1_Object = MibScalar
pkASfpSysFan1 = _PkASfpSysFan1_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 50, 1),
    _PkASfpSysFan1_Type()
)
pkASfpSysFan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpSysFan1.setStatus("current")
_PkASfpSysFan2X_ObjectIdentity = ObjectIdentity
pkASfpSysFan2X = _PkASfpSysFan2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 51)
)
_PkASfpSysFan2_Type = OctetString
_PkASfpSysFan2_Object = MibScalar
pkASfpSysFan2 = _PkASfpSysFan2_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 51, 1),
    _PkASfpSysFan2_Type()
)
pkASfpSysFan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpSysFan2.setStatus("current")
_PkASfpSysFan3X_ObjectIdentity = ObjectIdentity
pkASfpSysFan3X = _PkASfpSysFan3X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 52)
)
_PkASfpSysFan3_Type = OctetString
_PkASfpSysFan3_Object = MibScalar
pkASfpSysFan3 = _PkASfpSysFan3_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 52, 1),
    _PkASfpSysFan3_Type()
)
pkASfpSysFan3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpSysFan3.setStatus("current")
_PkASfpCpuFanStatusX_ObjectIdentity = ObjectIdentity
pkASfpCpuFanStatusX = _PkASfpCpuFanStatusX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 53)
)
_PkASfpCpuFanStatus_Type = OctetString
_PkASfpCpuFanStatus_Object = MibScalar
pkASfpCpuFanStatus = _PkASfpCpuFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 53, 1),
    _PkASfpCpuFanStatus_Type()
)
pkASfpCpuFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpCpuFanStatus.setStatus("current")
_PkASfpSysFansStatusX_ObjectIdentity = ObjectIdentity
pkASfpSysFansStatusX = _PkASfpSysFansStatusX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 54)
)
_PkASfpSysFansStatus_Type = OctetString
_PkASfpSysFansStatus_Object = MibScalar
pkASfpSysFansStatus = _PkASfpSysFansStatus_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 102, 97, 110, 54, 1),
    _PkASfpSysFansStatus_Type()
)
pkASfpSysFansStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpSysFansStatus.setStatus("current")
_PkSfpFourV_ObjectIdentity = ObjectIdentity
pkSfpFourV = _PkSfpFourV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 118)
)
_PkSfpFourD_ObjectIdentity = ObjectIdentity
pkSfpFourD = _PkSfpFourD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 118, 100)
)
_PkSfpFourB_ObjectIdentity = ObjectIdentity
pkSfpFourB = _PkSfpFourB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 118, 100, 98)
)
_PkAVdbUsagePercentX_ObjectIdentity = ObjectIdentity
pkAVdbUsagePercentX = _PkAVdbUsagePercentX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 118, 100, 98, 49)
)
_PkAVdbUsagePercent_Type = OctetString
_PkAVdbUsagePercent_Object = MibScalar
pkAVdbUsagePercent = _PkAVdbUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 118, 100, 98, 49, 1),
    _PkAVdbUsagePercent_Type()
)
pkAVdbUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAVdbUsagePercent.setStatus("current")
_PkAVdbStatusX_ObjectIdentity = ObjectIdentity
pkAVdbStatusX = _PkAVdbStatusX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 118, 100, 98, 50)
)
_PkAVdbStatus_Type = OctetString
_PkAVdbStatus_Object = MibScalar
pkAVdbStatus = _PkAVdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 4, 118, 100, 98, 50, 1),
    _PkAVdbStatus_Type()
)
pkAVdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAVdbStatus.setStatus("current")
_PkSfpFive_ObjectIdentity = ObjectIdentity
pkSfpFive = _PkSfpFive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5)
)
_PkSfpFiveL_ObjectIdentity = ObjectIdentity
pkSfpFiveL = _PkSfpFiveL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108)
)
_PkSfpFiveO_ObjectIdentity = ObjectIdentity
pkSfpFiveO = _PkSfpFiveO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111)
)
_PkSfpFiveA_ObjectIdentity = ObjectIdentity
pkSfpFiveA = _PkSfpFiveA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97)
)
_PkSfpFiveD_ObjectIdentity = ObjectIdentity
pkSfpFiveD = _PkSfpFiveD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97, 100)
)
_PkASfpLoadX_ObjectIdentity = ObjectIdentity
pkASfpLoadX = _PkASfpLoadX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97, 100, 49)
)
_PkASfpLoad_Type = OctetString
_PkASfpLoad_Object = MibScalar
pkASfpLoad = _PkASfpLoad_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97, 100, 49, 1),
    _PkASfpLoad_Type()
)
pkASfpLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpLoad.setStatus("current")
_PkASfpLoad1mX_ObjectIdentity = ObjectIdentity
pkASfpLoad1mX = _PkASfpLoad1mX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97, 100, 50)
)
_PkASfpLoad1m_Type = OctetString
_PkASfpLoad1m_Object = MibScalar
pkASfpLoad1m = _PkASfpLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97, 100, 50, 1),
    _PkASfpLoad1m_Type()
)
pkASfpLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpLoad1m.setStatus("current")
_PkASfpLoad5mX_ObjectIdentity = ObjectIdentity
pkASfpLoad5mX = _PkASfpLoad5mX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97, 100, 51)
)
_PkASfpLoad5m_Type = OctetString
_PkASfpLoad5m_Object = MibScalar
pkASfpLoad5m = _PkASfpLoad5m_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97, 100, 51, 1),
    _PkASfpLoad5m_Type()
)
pkASfpLoad5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpLoad5m.setStatus("current")
_PkASfpLoad15mX_ObjectIdentity = ObjectIdentity
pkASfpLoad15mX = _PkASfpLoad15mX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97, 100, 52)
)
_PkASfpLoad15m_Type = OctetString
_PkASfpLoad15m_Object = MibScalar
pkASfpLoad15m = _PkASfpLoad15m_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 108, 111, 97, 100, 52, 1),
    _PkASfpLoad15m_Type()
)
pkASfpLoad15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpLoad15m.setStatus("current")
_PkSfpFiveR_ObjectIdentity = ObjectIdentity
pkSfpFiveR = _PkSfpFiveR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114)
)
_PkSfpFiveRA_ObjectIdentity = ObjectIdentity
pkSfpFiveRA = _PkSfpFiveRA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97)
)
_PkSfpFiveRAI_ObjectIdentity = ObjectIdentity
pkSfpFiveRAI = _PkSfpFiveRAI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105)
)
_PkSfpFiveRAID_ObjectIdentity = ObjectIdentity
pkSfpFiveRAID = _PkSfpFiveRAID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100)
)
_PkASfpRaidStatusX_ObjectIdentity = ObjectIdentity
pkASfpRaidStatusX = _PkASfpRaidStatusX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 49)
)
_PkASfpRaidStatus_Type = OctetString
_PkASfpRaidStatus_Object = MibScalar
pkASfpRaidStatus = _PkASfpRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 49, 1),
    _PkASfpRaidStatus_Type()
)
pkASfpRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpRaidStatus.setStatus("current")
_PkASfpRaidStatusStringX_ObjectIdentity = ObjectIdentity
pkASfpRaidStatusStringX = _PkASfpRaidStatusStringX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 50)
)
_PkASfpRaidStatusString_Type = OctetString
_PkASfpRaidStatusString_Object = MibScalar
pkASfpRaidStatusString = _PkASfpRaidStatusString_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 50, 1),
    _PkASfpRaidStatusString_Type()
)
pkASfpRaidStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpRaidStatusString.setStatus("current")
_PkASfpRaidTotalDevicesStringX_ObjectIdentity = ObjectIdentity
pkASfpRaidTotalDevicesStringX = _PkASfpRaidTotalDevicesStringX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 51)
)
_PkASfpRaidTotalDevicesString_Type = OctetString
_PkASfpRaidTotalDevicesString_Object = MibScalar
pkASfpRaidTotalDevicesString = _PkASfpRaidTotalDevicesString_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 51, 1),
    _PkASfpRaidTotalDevicesString_Type()
)
pkASfpRaidTotalDevicesString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpRaidTotalDevicesString.setStatus("current")
_PkASfpRaidTotalDevicesX_ObjectIdentity = ObjectIdentity
pkASfpRaidTotalDevicesX = _PkASfpRaidTotalDevicesX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 52)
)
_PkASfpRaidTotalDevices_Type = OctetString
_PkASfpRaidTotalDevices_Object = MibScalar
pkASfpRaidTotalDevices = _PkASfpRaidTotalDevices_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 52, 1),
    _PkASfpRaidTotalDevices_Type()
)
pkASfpRaidTotalDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpRaidTotalDevices.setStatus("current")
_PkASfpRaidActiveDevicesStringX_ObjectIdentity = ObjectIdentity
pkASfpRaidActiveDevicesStringX = _PkASfpRaidActiveDevicesStringX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 53)
)
_PkASfpRaidActiveDevicesString_Type = OctetString
_PkASfpRaidActiveDevicesString_Object = MibScalar
pkASfpRaidActiveDevicesString = _PkASfpRaidActiveDevicesString_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 53, 1),
    _PkASfpRaidActiveDevicesString_Type()
)
pkASfpRaidActiveDevicesString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpRaidActiveDevicesString.setStatus("current")
_PkASfpRaidActiveDevicesX_ObjectIdentity = ObjectIdentity
pkASfpRaidActiveDevicesX = _PkASfpRaidActiveDevicesX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 54)
)
_PkASfpRaidActiveDevices_Type = OctetString
_PkASfpRaidActiveDevices_Object = MibScalar
pkASfpRaidActiveDevices = _PkASfpRaidActiveDevices_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 5, 114, 97, 105, 100, 54, 1),
    _PkASfpRaidActiveDevices_Type()
)
pkASfpRaidActiveDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpRaidActiveDevices.setStatus("current")
_PkSfpSix_ObjectIdentity = ObjectIdentity
pkSfpSix = _PkSfpSix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6)
)
_PkSfpSixM_ObjectIdentity = ObjectIdentity
pkSfpSixM = _PkSfpSixM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6, 109)
)
_PkSfpSixA_ObjectIdentity = ObjectIdentity
pkSfpSixA = _PkSfpSixA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6, 109, 97)
)
_PkSfpSixI_ObjectIdentity = ObjectIdentity
pkSfpSixI = _PkSfpSixI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6, 109, 97, 105)
)
_PkSfpSixN_ObjectIdentity = ObjectIdentity
pkSfpSixN = _PkSfpSixN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6, 109, 97, 105, 110)
)
_PkSfpSixT_ObjectIdentity = ObjectIdentity
pkSfpSixT = _PkSfpSixT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6, 109, 97, 105, 110, 116)
)
_PkASfpMaintenanceStateX_ObjectIdentity = ObjectIdentity
pkASfpMaintenanceStateX = _PkASfpMaintenanceStateX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6, 109, 97, 105, 110, 116, 49)
)
_PkASfpMaintenanceState_Type = OctetString
_PkASfpMaintenanceState_Object = MibScalar
pkASfpMaintenanceState = _PkASfpMaintenanceState_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6, 109, 97, 105, 110, 116, 49, 1),
    _PkASfpMaintenanceState_Type()
)
pkASfpMaintenanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpMaintenanceState.setStatus("current")
_PkASfpMaintenanceStateStringX_ObjectIdentity = ObjectIdentity
pkASfpMaintenanceStateStringX = _PkASfpMaintenanceStateStringX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6, 109, 97, 105, 110, 116, 50)
)
_PkASfpMaintenanceStateString_Type = OctetString
_PkASfpMaintenanceStateString_Object = MibScalar
pkASfpMaintenanceStateString = _PkASfpMaintenanceStateString_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 6, 109, 97, 105, 110, 116, 50, 1),
    _PkASfpMaintenanceStateString_Type()
)
pkASfpMaintenanceStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASfpMaintenanceStateString.setStatus("current")
_PkSfpSeven_ObjectIdentity = ObjectIdentity
pkSfpSeven = _PkSfpSeven_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 7)
)
_PkSfpSevenV_ObjectIdentity = ObjectIdentity
pkSfpSevenV = _PkSfpSevenV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 7, 118)
)
_PkSfpSevenE_ObjectIdentity = ObjectIdentity
pkSfpSevenE = _PkSfpSevenE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 7, 118, 101)
)
_PkSfpSevenR_ObjectIdentity = ObjectIdentity
pkSfpSevenR = _PkSfpSevenR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 7, 118, 101, 114)
)
_PkSfpSevenS_ObjectIdentity = ObjectIdentity
pkSfpSevenS = _PkSfpSevenS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 7, 118, 101, 114, 115)
)
_PkSfpSevenI_ObjectIdentity = ObjectIdentity
pkSfpSevenI = _PkSfpSevenI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 7, 118, 101, 114, 115, 105)
)
_PkSfpSevenO_ObjectIdentity = ObjectIdentity
pkSfpSevenO = _PkSfpSevenO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 7, 118, 101, 114, 115, 105, 111)
)
_PkAVersionX_ObjectIdentity = ObjectIdentity
pkAVersionX = _PkAVersionX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 7, 118, 101, 114, 115, 105, 111, 110)
)
_PkAVersion_Type = OctetString
_PkAVersion_Object = MibScalar
pkAVersion = _PkAVersion_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 7, 118, 101, 114, 115, 105, 111, 110, 1),
    _PkAVersion_Type()
)
pkAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAVersion.setStatus("current")
_PkSfpEight_ObjectIdentity = ObjectIdentity
pkSfpEight = _PkSfpEight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8)
)
_PkSfpEightC_ObjectIdentity = ObjectIdentity
pkSfpEightC = _PkSfpEightC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99)
)
_PkSfpEightL_ObjectIdentity = ObjectIdentity
pkSfpEightL = _PkSfpEightL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108)
)
_PkSfpEightU_ObjectIdentity = ObjectIdentity
pkSfpEightU = _PkSfpEightU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117)
)
_PkSfpEightS_ObjectIdentity = ObjectIdentity
pkSfpEightS = _PkSfpEightS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115)
)
_PkSfpEightT_ObjectIdentity = ObjectIdentity
pkSfpEightT = _PkSfpEightT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116)
)
_PkSfpEightE_ObjectIdentity = ObjectIdentity
pkSfpEightE = _PkSfpEightE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101)
)
_PkSfpEightR_ObjectIdentity = ObjectIdentity
pkSfpEightR = _PkSfpEightR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114)
)
_PkAClusterLocalNodeIDX_ObjectIdentity = ObjectIdentity
pkAClusterLocalNodeIDX = _PkAClusterLocalNodeIDX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 49)
)
_PkAClusterLocalNodeID_Type = OctetString
_PkAClusterLocalNodeID_Object = MibScalar
pkAClusterLocalNodeID = _PkAClusterLocalNodeID_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 49, 1),
    _PkAClusterLocalNodeID_Type()
)
pkAClusterLocalNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAClusterLocalNodeID.setStatus("current")
_PkAClusterSizeX_ObjectIdentity = ObjectIdentity
pkAClusterSizeX = _PkAClusterSizeX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 50)
)
_PkAClusterSize_Type = OctetString
_PkAClusterSize_Object = MibScalar
pkAClusterSize = _PkAClusterSize_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 50, 1),
    _PkAClusterSize_Type()
)
pkAClusterSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAClusterSize.setStatus("current")
_PkAClusterActiveNodesX_ObjectIdentity = ObjectIdentity
pkAClusterActiveNodesX = _PkAClusterActiveNodesX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 51)
)
_PkAClusterActiveNodes_Type = OctetString
_PkAClusterActiveNodes_Object = MibScalar
pkAClusterActiveNodes = _PkAClusterActiveNodes_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 51, 1),
    _PkAClusterActiveNodes_Type()
)
pkAClusterActiveNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAClusterActiveNodes.setStatus("current")
_PkAClusterLocalGaleraStateX_ObjectIdentity = ObjectIdentity
pkAClusterLocalGaleraStateX = _PkAClusterLocalGaleraStateX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 52)
)
_PkAClusterLocalGaleraState_Type = OctetString
_PkAClusterLocalGaleraState_Object = MibScalar
pkAClusterLocalGaleraState = _PkAClusterLocalGaleraState_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 52, 1),
    _PkAClusterLocalGaleraState_Type()
)
pkAClusterLocalGaleraState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAClusterLocalGaleraState.setStatus("current")
_PkAClusterLocalGaleraStateStringX_ObjectIdentity = ObjectIdentity
pkAClusterLocalGaleraStateStringX = _PkAClusterLocalGaleraStateStringX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 53)
)
_PkAClusterLocalGaleraStateString_Type = OctetString
_PkAClusterLocalGaleraStateString_Object = MibScalar
pkAClusterLocalGaleraStateString = _PkAClusterLocalGaleraStateString_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 53, 1),
    _PkAClusterLocalGaleraStateString_Type()
)
pkAClusterLocalGaleraStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAClusterLocalGaleraStateString.setStatus("current")
_PkAClusterLTIDX_ObjectIdentity = ObjectIdentity
pkAClusterLTIDX = _PkAClusterLTIDX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 54)
)
_PkAClusterLTID_Type = OctetString
_PkAClusterLTID_Object = MibScalar
pkAClusterLTID = _PkAClusterLTID_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 99, 108, 117, 115, 116, 101, 114, 54, 1),
    _PkAClusterLTID_Type()
)
pkAClusterLTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAClusterLTID.setStatus("current")
_PkSfpEightH_ObjectIdentity = ObjectIdentity
pkSfpEightH = _PkSfpEightH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104)
)
_PkSfpEightHE_ObjectIdentity = ObjectIdentity
pkSfpEightHE = _PkSfpEightHE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101)
)
_PkSfpEightHEA_ObjectIdentity = ObjectIdentity
pkSfpEightHEA = _PkSfpEightHEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97)
)
_PkSfpEightHEAL_ObjectIdentity = ObjectIdentity
pkSfpEightHEAL = _PkSfpEightHEAL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108)
)
_PkSfpEightHEALT_ObjectIdentity = ObjectIdentity
pkSfpEightHEALT = _PkSfpEightHEALT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116)
)
_PkSfpEightHEALTH_ObjectIdentity = ObjectIdentity
pkSfpEightHEALTH = _PkSfpEightHEALTH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104)
)
_PkEjbca_ObjectIdentity = ObjectIdentity
pkEjbca = _PkEjbca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 101)
)
_PkAEJBCAHealthStringX_ObjectIdentity = ObjectIdentity
pkAEJBCAHealthStringX = _PkAEJBCAHealthStringX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 101, 49)
)
_PkAEJBCAHealthString_Type = OctetString
_PkAEJBCAHealthString_Object = MibScalar
pkAEJBCAHealthString = _PkAEJBCAHealthString_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 101, 49, 1),
    _PkAEJBCAHealthString_Type()
)
pkAEJBCAHealthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAEJBCAHealthString.setStatus("current")
_PkAEJBCAHealthX_ObjectIdentity = ObjectIdentity
pkAEJBCAHealthX = _PkAEJBCAHealthX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 101, 50)
)
_PkAEJBCAHealth_Type = OctetString
_PkAEJBCAHealth_Object = MibScalar
pkAEJBCAHealth = _PkAEJBCAHealth_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 101, 50, 1),
    _PkAEJBCAHealth_Type()
)
pkAEJBCAHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAEJBCAHealth.setStatus("current")
_PkSignServer_ObjectIdentity = ObjectIdentity
pkSignServer = _PkSignServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 115)
)
_PkASignServerHealthStringX_ObjectIdentity = ObjectIdentity
pkASignServerHealthStringX = _PkASignServerHealthStringX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 115, 49)
)
_PkASignServerHealthString_Type = OctetString
_PkASignServerHealthString_Object = MibScalar
pkASignServerHealthString = _PkASignServerHealthString_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 115, 49, 1),
    _PkASignServerHealthString_Type()
)
pkASignServerHealthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASignServerHealthString.setStatus("current")
_PkASignServerHealthX_ObjectIdentity = ObjectIdentity
pkASignServerHealthX = _PkASignServerHealthX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 115, 50)
)
_PkASignServerHealth_Type = OctetString
_PkASignServerHealth_Object = MibScalar
pkASignServerHealth = _PkASignServerHealth_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 1, 8, 104, 101, 97, 108, 116, 104, 115, 50, 1),
    _PkASignServerHealth_Type()
)
pkASignServerHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkASignServerHealth.setStatus("current")
_PkVhsm_ObjectIdentity = ObjectIdentity
pkVhsm = _PkVhsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2)
)
_PkVhsmX_ObjectIdentity = ObjectIdentity
pkVhsmX = _PkVhsmX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4)
)
_PkVhsmh_ObjectIdentity = ObjectIdentity
pkVhsmh = _PkVhsmh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104)
)
_PkVhsms_ObjectIdentity = ObjectIdentity
pkVhsms = _PkVhsms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115)
)
_PkVhsmm_ObjectIdentity = ObjectIdentity
pkVhsmm = _PkVhsmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109)
)
_PkAHsmStatusStringX_ObjectIdentity = ObjectIdentity
pkAHsmStatusStringX = _PkAHsmStatusStringX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 49)
)
_PkAHsmStatusString_Type = OctetString
_PkAHsmStatusString_Object = MibScalar
pkAHsmStatusString = _PkAHsmStatusString_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 49, 1),
    _PkAHsmStatusString_Type()
)
pkAHsmStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAHsmStatusString.setStatus("current")
_PkAHsmStatusEnumX_ObjectIdentity = ObjectIdentity
pkAHsmStatusEnumX = _PkAHsmStatusEnumX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 50)
)
_PkAHsmStatusEnum_Type = OctetString
_PkAHsmStatusEnum_Object = MibScalar
pkAHsmStatusEnum = _PkAHsmStatusEnum_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 50, 1),
    _PkAHsmStatusEnum_Type()
)
pkAHsmStatusEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAHsmStatusEnum.setStatus("current")
_PkAHsmStatusBoolX_ObjectIdentity = ObjectIdentity
pkAHsmStatusBoolX = _PkAHsmStatusBoolX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 51)
)
_PkAHsmStatusBool_Type = OctetString
_PkAHsmStatusBool_Object = MibScalar
pkAHsmStatusBool = _PkAHsmStatusBool_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 51, 1),
    _PkAHsmStatusBool_Type()
)
pkAHsmStatusBool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAHsmStatusBool.setStatus("current")
_PkAHsmBatteryIntX_ObjectIdentity = ObjectIdentity
pkAHsmBatteryIntX = _PkAHsmBatteryIntX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 52)
)
_PkAHsmBatteryInt_Type = OctetString
_PkAHsmBatteryInt_Object = MibScalar
pkAHsmBatteryInt = _PkAHsmBatteryInt_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 52, 1),
    _PkAHsmBatteryInt_Type()
)
pkAHsmBatteryInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAHsmBatteryInt.setStatus("current")
_PkAHsmBatteryIntStatusX_ObjectIdentity = ObjectIdentity
pkAHsmBatteryIntStatusX = _PkAHsmBatteryIntStatusX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 53)
)
_PkAHsmBatteryIntStatus_Type = OctetString
_PkAHsmBatteryIntStatus_Object = MibScalar
pkAHsmBatteryIntStatus = _PkAHsmBatteryIntStatus_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 53, 1),
    _PkAHsmBatteryIntStatus_Type()
)
pkAHsmBatteryIntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAHsmBatteryIntStatus.setStatus("current")
_PkAHsmSerialNumberX_ObjectIdentity = ObjectIdentity
pkAHsmSerialNumberX = _PkAHsmSerialNumberX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 54)
)
_PkAHsmSerialNumber_Type = OctetString
_PkAHsmSerialNumber_Object = MibScalar
pkAHsmSerialNumber = _PkAHsmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 54, 1),
    _PkAHsmSerialNumber_Type()
)
pkAHsmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAHsmSerialNumber.setStatus("current")
_PkAHsmBatteryExtX_ObjectIdentity = ObjectIdentity
pkAHsmBatteryExtX = _PkAHsmBatteryExtX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 55)
)
_PkAHsmBatteryExt_Type = OctetString
_PkAHsmBatteryExt_Object = MibScalar
pkAHsmBatteryExt = _PkAHsmBatteryExt_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 55, 1),
    _PkAHsmBatteryExt_Type()
)
pkAHsmBatteryExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAHsmBatteryExt.setStatus("current")
_PkAHsmBatteryExtStatusX_ObjectIdentity = ObjectIdentity
pkAHsmBatteryExtStatusX = _PkAHsmBatteryExtStatusX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 56)
)
_PkAHsmBatteryExtStatus_Type = OctetString
_PkAHsmBatteryExtStatus_Object = MibScalar
pkAHsmBatteryExtStatus = _PkAHsmBatteryExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 56, 1),
    _PkAHsmBatteryExtStatus_Type()
)
pkAHsmBatteryExtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAHsmBatteryExtStatus.setStatus("current")
_PkAHsmEidasAuditLogSizeX_ObjectIdentity = ObjectIdentity
pkAHsmEidasAuditLogSizeX = _PkAHsmEidasAuditLogSizeX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 57)
)
_PkAHsmEidasAuditLogSize_Type = OctetString
_PkAHsmEidasAuditLogSize_Object = MibScalar
pkAHsmEidasAuditLogSize = _PkAHsmEidasAuditLogSize_Object(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 2, 2, 4, 104, 115, 109, 57, 1),
    _PkAHsmEidasAuditLogSize_Type()
)
pkAHsmEidasAuditLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkAHsmEidasAuditLogSize.setStatus("current")

# Managed Objects groups

pkAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 4)
)
pkAGroup.setObjects(
      *(("PRIMEKEY-APPLIANCE-MIB", "pkASfpVmStatus"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpCpuTemp"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpCpuFan"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpSysFan1"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpSysFan2"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpSysFan3"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpCpuFanStatus"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpSysFansStatus"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAVdbUsagePercent"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAVdbStatus"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpLoad"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpLoad1m"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpLoad5m"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpLoad15m"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpRaidStatus"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpRaidStatusString"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpRaidTotalDevicesString"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpRaidTotalDevices"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpRaidActiveDevicesString"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpRaidActiveDevices"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpMaintenanceState"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASfpMaintenanceStateString"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAVersion"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAClusterLocalNodeID"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAClusterSize"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAClusterActiveNodes"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAClusterLocalGaleraState"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAClusterLocalGaleraStateString"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAClusterLTID"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAEJBCAHealthString"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAEJBCAHealth"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASignServerHealthString"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkASignServerHealth"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAHsmStatusString"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAHsmStatusEnum"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAHsmStatusBool"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAHsmBatteryInt"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAHsmBatteryIntStatus"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAHsmSerialNumber"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAHsmBatteryExt"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAHsmBatteryExtStatus"),
        ("PRIMEKEY-APPLIANCE-MIB", "pkAHsmEidasAuditLogSize"))
)
if mibBuilder.loadTexts:
    pkAGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pkACompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22408, 1, 1, 3)
)
pkACompliance.setObjects(
    ("PRIMEKEY-APPLIANCE-MIB", "pkAGroup")
)
if mibBuilder.loadTexts:
    pkACompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIMEKEY-APPLIANCE-MIB",
    **{"primekey": primekey,
       "primeKeyAppliancePrefixOne": primeKeyAppliancePrefixOne,
       "primeKeyAppliancePrefixAnotherOne": primeKeyAppliancePrefixAnotherOne,
       "pkAppliance": pkAppliance,
       "pkSfp": pkSfp,
       "pkSfpTwo": pkSfpTwo,
       "pkSfpTwoV": pkSfpTwoV,
       "pkASfpVmStatusX": pkASfpVmStatusX,
       "pkASfpVmStatus": pkASfpVmStatus,
       "pkSfpThree": pkSfpThree,
       "pkSfpThreeC": pkSfpThreeC,
       "pkSfpThreeP": pkSfpThreeP,
       "pkASfpCpuTempX": pkASfpCpuTempX,
       "pkASfpCpuTemp": pkASfpCpuTemp,
       "pkSfpFour": pkSfpFour,
       "pkSfpFourF": pkSfpFourF,
       "pkSfpFourA": pkSfpFourA,
       "pkSfpFourN": pkSfpFourN,
       "pkASfpCpuFanX": pkASfpCpuFanX,
       "pkASfpCpuFan": pkASfpCpuFan,
       "pkASfpSysFan1X": pkASfpSysFan1X,
       "pkASfpSysFan1": pkASfpSysFan1,
       "pkASfpSysFan2X": pkASfpSysFan2X,
       "pkASfpSysFan2": pkASfpSysFan2,
       "pkASfpSysFan3X": pkASfpSysFan3X,
       "pkASfpSysFan3": pkASfpSysFan3,
       "pkASfpCpuFanStatusX": pkASfpCpuFanStatusX,
       "pkASfpCpuFanStatus": pkASfpCpuFanStatus,
       "pkASfpSysFansStatusX": pkASfpSysFansStatusX,
       "pkASfpSysFansStatus": pkASfpSysFansStatus,
       "pkSfpFourV": pkSfpFourV,
       "pkSfpFourD": pkSfpFourD,
       "pkSfpFourB": pkSfpFourB,
       "pkAVdbUsagePercentX": pkAVdbUsagePercentX,
       "pkAVdbUsagePercent": pkAVdbUsagePercent,
       "pkAVdbStatusX": pkAVdbStatusX,
       "pkAVdbStatus": pkAVdbStatus,
       "pkSfpFive": pkSfpFive,
       "pkSfpFiveL": pkSfpFiveL,
       "pkSfpFiveO": pkSfpFiveO,
       "pkSfpFiveA": pkSfpFiveA,
       "pkSfpFiveD": pkSfpFiveD,
       "pkASfpLoadX": pkASfpLoadX,
       "pkASfpLoad": pkASfpLoad,
       "pkASfpLoad1mX": pkASfpLoad1mX,
       "pkASfpLoad1m": pkASfpLoad1m,
       "pkASfpLoad5mX": pkASfpLoad5mX,
       "pkASfpLoad5m": pkASfpLoad5m,
       "pkASfpLoad15mX": pkASfpLoad15mX,
       "pkASfpLoad15m": pkASfpLoad15m,
       "pkSfpFiveR": pkSfpFiveR,
       "pkSfpFiveRA": pkSfpFiveRA,
       "pkSfpFiveRAI": pkSfpFiveRAI,
       "pkSfpFiveRAID": pkSfpFiveRAID,
       "pkASfpRaidStatusX": pkASfpRaidStatusX,
       "pkASfpRaidStatus": pkASfpRaidStatus,
       "pkASfpRaidStatusStringX": pkASfpRaidStatusStringX,
       "pkASfpRaidStatusString": pkASfpRaidStatusString,
       "pkASfpRaidTotalDevicesStringX": pkASfpRaidTotalDevicesStringX,
       "pkASfpRaidTotalDevicesString": pkASfpRaidTotalDevicesString,
       "pkASfpRaidTotalDevicesX": pkASfpRaidTotalDevicesX,
       "pkASfpRaidTotalDevices": pkASfpRaidTotalDevices,
       "pkASfpRaidActiveDevicesStringX": pkASfpRaidActiveDevicesStringX,
       "pkASfpRaidActiveDevicesString": pkASfpRaidActiveDevicesString,
       "pkASfpRaidActiveDevicesX": pkASfpRaidActiveDevicesX,
       "pkASfpRaidActiveDevices": pkASfpRaidActiveDevices,
       "pkSfpSix": pkSfpSix,
       "pkSfpSixM": pkSfpSixM,
       "pkSfpSixA": pkSfpSixA,
       "pkSfpSixI": pkSfpSixI,
       "pkSfpSixN": pkSfpSixN,
       "pkSfpSixT": pkSfpSixT,
       "pkASfpMaintenanceStateX": pkASfpMaintenanceStateX,
       "pkASfpMaintenanceState": pkASfpMaintenanceState,
       "pkASfpMaintenanceStateStringX": pkASfpMaintenanceStateStringX,
       "pkASfpMaintenanceStateString": pkASfpMaintenanceStateString,
       "pkSfpSeven": pkSfpSeven,
       "pkSfpSevenV": pkSfpSevenV,
       "pkSfpSevenE": pkSfpSevenE,
       "pkSfpSevenR": pkSfpSevenR,
       "pkSfpSevenS": pkSfpSevenS,
       "pkSfpSevenI": pkSfpSevenI,
       "pkSfpSevenO": pkSfpSevenO,
       "pkAVersionX": pkAVersionX,
       "pkAVersion": pkAVersion,
       "pkSfpEight": pkSfpEight,
       "pkSfpEightC": pkSfpEightC,
       "pkSfpEightL": pkSfpEightL,
       "pkSfpEightU": pkSfpEightU,
       "pkSfpEightS": pkSfpEightS,
       "pkSfpEightT": pkSfpEightT,
       "pkSfpEightE": pkSfpEightE,
       "pkSfpEightR": pkSfpEightR,
       "pkAClusterLocalNodeIDX": pkAClusterLocalNodeIDX,
       "pkAClusterLocalNodeID": pkAClusterLocalNodeID,
       "pkAClusterSizeX": pkAClusterSizeX,
       "pkAClusterSize": pkAClusterSize,
       "pkAClusterActiveNodesX": pkAClusterActiveNodesX,
       "pkAClusterActiveNodes": pkAClusterActiveNodes,
       "pkAClusterLocalGaleraStateX": pkAClusterLocalGaleraStateX,
       "pkAClusterLocalGaleraState": pkAClusterLocalGaleraState,
       "pkAClusterLocalGaleraStateStringX": pkAClusterLocalGaleraStateStringX,
       "pkAClusterLocalGaleraStateString": pkAClusterLocalGaleraStateString,
       "pkAClusterLTIDX": pkAClusterLTIDX,
       "pkAClusterLTID": pkAClusterLTID,
       "pkSfpEightH": pkSfpEightH,
       "pkSfpEightHE": pkSfpEightHE,
       "pkSfpEightHEA": pkSfpEightHEA,
       "pkSfpEightHEAL": pkSfpEightHEAL,
       "pkSfpEightHEALT": pkSfpEightHEALT,
       "pkSfpEightHEALTH": pkSfpEightHEALTH,
       "pkEjbca": pkEjbca,
       "pkAEJBCAHealthStringX": pkAEJBCAHealthStringX,
       "pkAEJBCAHealthString": pkAEJBCAHealthString,
       "pkAEJBCAHealthX": pkAEJBCAHealthX,
       "pkAEJBCAHealth": pkAEJBCAHealth,
       "pkSignServer": pkSignServer,
       "pkASignServerHealthStringX": pkASignServerHealthStringX,
       "pkASignServerHealthString": pkASignServerHealthString,
       "pkASignServerHealthX": pkASignServerHealthX,
       "pkASignServerHealth": pkASignServerHealth,
       "pkVhsm": pkVhsm,
       "pkVhsmX": pkVhsmX,
       "pkVhsmh": pkVhsmh,
       "pkVhsms": pkVhsms,
       "pkVhsmm": pkVhsmm,
       "pkAHsmStatusStringX": pkAHsmStatusStringX,
       "pkAHsmStatusString": pkAHsmStatusString,
       "pkAHsmStatusEnumX": pkAHsmStatusEnumX,
       "pkAHsmStatusEnum": pkAHsmStatusEnum,
       "pkAHsmStatusBoolX": pkAHsmStatusBoolX,
       "pkAHsmStatusBool": pkAHsmStatusBool,
       "pkAHsmBatteryIntX": pkAHsmBatteryIntX,
       "pkAHsmBatteryInt": pkAHsmBatteryInt,
       "pkAHsmBatteryIntStatusX": pkAHsmBatteryIntStatusX,
       "pkAHsmBatteryIntStatus": pkAHsmBatteryIntStatus,
       "pkAHsmSerialNumberX": pkAHsmSerialNumberX,
       "pkAHsmSerialNumber": pkAHsmSerialNumber,
       "pkAHsmBatteryExtX": pkAHsmBatteryExtX,
       "pkAHsmBatteryExt": pkAHsmBatteryExt,
       "pkAHsmBatteryExtStatusX": pkAHsmBatteryExtStatusX,
       "pkAHsmBatteryExtStatus": pkAHsmBatteryExtStatus,
       "pkAHsmEidasAuditLogSizeX": pkAHsmEidasAuditLogSizeX,
       "pkAHsmEidasAuditLogSize": pkAHsmEidasAuditLogSize,
       "pkACompliance": pkACompliance,
       "pkAGroup": pkAGroup}
)
