# SNMP MIB module (LUM-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\infinera\LUM-REG
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:42 2025
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

lumRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lumRegModule.setRevisions(
        ("2019-08-30 00:00",
         "2019-06-28 00:00",
         "2018-06-29 00:00",
         "2017-09-01 00:00",
         "2017-06-15 00:00",
         "2016-11-30 00:00",
         "2016-01-14 00:00",
         "2015-09-30 00:00",
         "2015-09-15 00:00",
         "2015-01-13 00:00",
         "2014-09-30 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2013-05-01 00:00",
         "2012-12-20 00:00",
         "2012-12-10 00:00",
         "2012-01-20 00:00",
         "2011-12-20 00:00",
         "2011-10-12 00:00",
         "2011-04-13 00:00",
         "2007-04-16 00:00",
         "2006-12-15 00:00",
         "2002-11-26 00:00",
         "2002-11-15 00:00",
         "2002-11-11 00:00",
         "2002-11-08 00:00",
         "2002-10-21 00:00",
         "2002-05-30 00:00",
         "2002-05-16 00:00",
         "2002-04-05 00:00",
         "2002-03-08 00:00",
         "2001-11-20 00:00",
         "2001-10-10 00:00",
         "2001-09-05 00:00",
         "2001-08-09 00:00",
         "2001-08-01 00:00",
         "2001-04-26 00:00",
         "2001-03-12 00:00",
         "2001-03-09 00:00",
         "2001-03-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lumentis_ObjectIdentity = ObjectIdentity
lumentis = _Lumentis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708)
)
if mibBuilder.loadTexts:
    lumentis.setStatus("current")
_LumReg_ObjectIdentity = ObjectIdentity
lumReg = _LumReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1)
)
if mibBuilder.loadTexts:
    lumReg.setStatus("current")
_LumModules_ObjectIdentity = ObjectIdentity
lumModules = _LumModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1)
)
if mibBuilder.loadTexts:
    lumModules.setStatus("current")
_LumGeneric_ObjectIdentity = ObjectIdentity
lumGeneric = _LumGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2)
)
if mibBuilder.loadTexts:
    lumGeneric.setStatus("current")
_LumAlarmMIB_ObjectIdentity = ObjectIdentity
lumAlarmMIB = _LumAlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 1)
)
if mibBuilder.loadTexts:
    lumAlarmMIB.setStatus("current")
_LumSystemMIB_ObjectIdentity = ObjectIdentity
lumSystemMIB = _LumSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2)
)
if mibBuilder.loadTexts:
    lumSystemMIB.setStatus("current")
_LumInventoryMIB_ObjectIdentity = ObjectIdentity
lumInventoryMIB = _LumInventoryMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3)
)
if mibBuilder.loadTexts:
    lumInventoryMIB.setStatus("current")
_LumWdmMIB_ObjectIdentity = ObjectIdentity
lumWdmMIB = _LumWdmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4)
)
if mibBuilder.loadTexts:
    lumWdmMIB.setStatus("current")
_LumBackupMIB_ObjectIdentity = ObjectIdentity
lumBackupMIB = _LumBackupMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 5)
)
if mibBuilder.loadTexts:
    lumBackupMIB.setStatus("current")
_LumLambdaMIB_ObjectIdentity = ObjectIdentity
lumLambdaMIB = _LumLambdaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 6)
)
if mibBuilder.loadTexts:
    lumLambdaMIB.setStatus("current")
_LumTransponderMIB_ObjectIdentity = ObjectIdentity
lumTransponderMIB = _LumTransponderMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 7)
)
if mibBuilder.loadTexts:
    lumTransponderMIB.setStatus("deprecated")
_LumTopologyMIB_ObjectIdentity = ObjectIdentity
lumTopologyMIB = _LumTopologyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 8)
)
if mibBuilder.loadTexts:
    lumTopologyMIB.setStatus("current")
_LumPowerMIB_ObjectIdentity = ObjectIdentity
lumPowerMIB = _LumPowerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 9)
)
if mibBuilder.loadTexts:
    lumPowerMIB.setStatus("deprecated")
_LumOxcMIB_ObjectIdentity = ObjectIdentity
lumOxcMIB = _LumOxcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 10)
)
if mibBuilder.loadTexts:
    lumOxcMIB.setStatus("current")
_LumEquipmentMIB_ObjectIdentity = ObjectIdentity
lumEquipmentMIB = _LumEquipmentMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11)
)
if mibBuilder.loadTexts:
    lumEquipmentMIB.setStatus("current")
_LumMultirateMIB_ObjectIdentity = ObjectIdentity
lumMultirateMIB = _LumMultirateMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 12)
)
if mibBuilder.loadTexts:
    lumMultirateMIB.setStatus("current")
_LumMuxMIB_ObjectIdentity = ObjectIdentity
lumMuxMIB = _LumMuxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 13)
)
if mibBuilder.loadTexts:
    lumMuxMIB.setStatus("current")
_LumIpMIB_ObjectIdentity = ObjectIdentity
lumIpMIB = _LumIpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14)
)
if mibBuilder.loadTexts:
    lumIpMIB.setStatus("current")
_LumPmMIB_ObjectIdentity = ObjectIdentity
lumPmMIB = _LumPmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15)
)
if mibBuilder.loadTexts:
    lumPmMIB.setStatus("current")
_LumSyncMIB_ObjectIdentity = ObjectIdentity
lumSyncMIB = _LumSyncMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16)
)
if mibBuilder.loadTexts:
    lumSyncMIB.setStatus("current")
_LumSnmpMIB_ObjectIdentity = ObjectIdentity
lumSnmpMIB = _LumSnmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17)
)
if mibBuilder.loadTexts:
    lumSnmpMIB.setStatus("current")
_LumEthMIB_ObjectIdentity = ObjectIdentity
lumEthMIB = _LumEthMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 18)
)
if mibBuilder.loadTexts:
    lumEthMIB.setStatus("current")
_LumOaMIB_ObjectIdentity = ObjectIdentity
lumOaMIB = _LumOaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 19)
)
if mibBuilder.loadTexts:
    lumOaMIB.setStatus("current")
_LumDcnMIB_ObjectIdentity = ObjectIdentity
lumDcnMIB = _LumDcnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 20)
)
if mibBuilder.loadTexts:
    lumDcnMIB.setStatus("current")
_LumMemMIB_ObjectIdentity = ObjectIdentity
lumMemMIB = _LumMemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 21)
)
if mibBuilder.loadTexts:
    lumMemMIB.setStatus("current")
_LumFcMIB_ObjectIdentity = ObjectIdentity
lumFcMIB = _LumFcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22)
)
if mibBuilder.loadTexts:
    lumFcMIB.setStatus("obsolete")
_LumSwuMIB_ObjectIdentity = ObjectIdentity
lumSwuMIB = _LumSwuMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 23)
)
if mibBuilder.loadTexts:
    lumSwuMIB.setStatus("current")
_LumGmplsMIB_ObjectIdentity = ObjectIdentity
lumGmplsMIB = _LumGmplsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 24)
)
if mibBuilder.loadTexts:
    lumGmplsMIB.setStatus("current")
_LumGmplsStdMIB_ObjectIdentity = ObjectIdentity
lumGmplsStdMIB = _LumGmplsStdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 25)
)
if mibBuilder.loadTexts:
    lumGmplsStdMIB.setStatus("current")
_LumConnMIB_ObjectIdentity = ObjectIdentity
lumConnMIB = _LumConnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 26)
)
if mibBuilder.loadTexts:
    lumConnMIB.setStatus("current")
_LumClientMIB_ObjectIdentity = ObjectIdentity
lumClientMIB = _LumClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27)
)
if mibBuilder.loadTexts:
    lumClientMIB.setStatus("current")
_LumSoftwareMIB_ObjectIdentity = ObjectIdentity
lumSoftwareMIB = _LumSoftwareMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 28)
)
if mibBuilder.loadTexts:
    lumSoftwareMIB.setStatus("current")
_LumAuxMIB_ObjectIdentity = ObjectIdentity
lumAuxMIB = _LumAuxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29)
)
if mibBuilder.loadTexts:
    lumAuxMIB.setStatus("current")
_LumCircuitMIB_ObjectIdentity = ObjectIdentity
lumCircuitMIB = _LumCircuitMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 30)
)
if mibBuilder.loadTexts:
    lumCircuitMIB.setStatus("current")
_LumRoadmMIB_ObjectIdentity = ObjectIdentity
lumRoadmMIB = _LumRoadmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 31)
)
if mibBuilder.loadTexts:
    lumRoadmMIB.setStatus("current")
_LumMesMIB_ObjectIdentity = ObjectIdentity
lumMesMIB = _LumMesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32)
)
if mibBuilder.loadTexts:
    lumMesMIB.setStatus("current")
_LumOcmMIB_ObjectIdentity = ObjectIdentity
lumOcmMIB = _LumOcmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 33)
)
if mibBuilder.loadTexts:
    lumOcmMIB.setStatus("current")
_LumOtnMIB_ObjectIdentity = ObjectIdentity
lumOtnMIB = _LumOtnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34)
)
if mibBuilder.loadTexts:
    lumOtnMIB.setStatus("current")
_LumSdhpdhMIB_ObjectIdentity = ObjectIdentity
lumSdhpdhMIB = _LumSdhpdhMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35)
)
if mibBuilder.loadTexts:
    lumSdhpdhMIB.setStatus("current")
_LumSatelliteMIB_ObjectIdentity = ObjectIdentity
lumSatelliteMIB = _LumSatelliteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36)
)
if mibBuilder.loadTexts:
    lumSatelliteMIB.setStatus("current")
_LumMulticastMIB_ObjectIdentity = ObjectIdentity
lumMulticastMIB = _LumMulticastMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37)
)
if mibBuilder.loadTexts:
    lumMulticastMIB.setStatus("current")
_LumTrailMIB_ObjectIdentity = ObjectIdentity
lumTrailMIB = _LumTrailMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38)
)
if mibBuilder.loadTexts:
    lumTrailMIB.setStatus("current")
_LumNcMIB_ObjectIdentity = ObjectIdentity
lumNcMIB = _LumNcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39)
)
if mibBuilder.loadTexts:
    lumNcMIB.setStatus("current")
_LumMplsMIB_ObjectIdentity = ObjectIdentity
lumMplsMIB = _LumMplsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 40)
)
if mibBuilder.loadTexts:
    lumMplsMIB.setStatus("current")
_LumPwMIB_ObjectIdentity = ObjectIdentity
lumPwMIB = _LumPwMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 41)
)
if mibBuilder.loadTexts:
    lumPwMIB.setStatus("current")
_LumSiteMIB_ObjectIdentity = ObjectIdentity
lumSiteMIB = _LumSiteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42)
)
if mibBuilder.loadTexts:
    lumSiteMIB.setStatus("current")
_LumPsrMIB_ObjectIdentity = ObjectIdentity
lumPsrMIB = _LumPsrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43)
)
if mibBuilder.loadTexts:
    lumPsrMIB.setStatus("current")
_LumMplsOamMIB_ObjectIdentity = ObjectIdentity
lumMplsOamMIB = _LumMplsOamMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44)
)
if mibBuilder.loadTexts:
    lumMplsOamMIB.setStatus("current")
_LumLinkLossMIB_ObjectIdentity = ObjectIdentity
lumLinkLossMIB = _LumLinkLossMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 45)
)
if mibBuilder.loadTexts:
    lumLinkLossMIB.setStatus("current")
_LumIfBasicMIB_ObjectIdentity = ObjectIdentity
lumIfBasicMIB = _LumIfBasicMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 46)
)
if mibBuilder.loadTexts:
    lumIfBasicMIB.setStatus("current")
_LumIfPhysicalMIB_ObjectIdentity = ObjectIdentity
lumIfPhysicalMIB = _LumIfPhysicalMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47)
)
if mibBuilder.loadTexts:
    lumIfPhysicalMIB.setStatus("current")
_LumIfOpticalMIB_ObjectIdentity = ObjectIdentity
lumIfOpticalMIB = _LumIfOpticalMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48)
)
if mibBuilder.loadTexts:
    lumIfOpticalMIB.setStatus("current")
_LumPmServerMIB_ObjectIdentity = ObjectIdentity
lumPmServerMIB = _LumPmServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 49)
)
if mibBuilder.loadTexts:
    lumPmServerMIB.setStatus("current")
_LumIfOtnMIB_ObjectIdentity = ObjectIdentity
lumIfOtnMIB = _LumIfOtnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 50)
)
if mibBuilder.loadTexts:
    lumIfOtnMIB.setStatus("current")
_LumIfXcMIB_ObjectIdentity = ObjectIdentity
lumIfXcMIB = _LumIfXcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51)
)
if mibBuilder.loadTexts:
    lumIfXcMIB.setStatus("current")
_LumIfSdhMIB_ObjectIdentity = ObjectIdentity
lumIfSdhMIB = _LumIfSdhMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52)
)
if mibBuilder.loadTexts:
    lumIfSdhMIB.setStatus("current")
_LumIfSonetMIB_ObjectIdentity = ObjectIdentity
lumIfSonetMIB = _LumIfSonetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53)
)
if mibBuilder.loadTexts:
    lumIfSonetMIB.setStatus("current")
_LumIfEthMIB_ObjectIdentity = ObjectIdentity
lumIfEthMIB = _LumIfEthMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54)
)
if mibBuilder.loadTexts:
    lumIfEthMIB.setStatus("current")
_LumIfOtnMonMIB_ObjectIdentity = ObjectIdentity
lumIfOtnMonMIB = _LumIfOtnMonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 55)
)
if mibBuilder.loadTexts:
    lumIfOtnMonMIB.setStatus("current")
_LumIfPerfMIB_ObjectIdentity = ObjectIdentity
lumIfPerfMIB = _LumIfPerfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 56)
)
if mibBuilder.loadTexts:
    lumIfPerfMIB.setStatus("current")
_LumPortdeviceMIB_ObjectIdentity = ObjectIdentity
lumPortdeviceMIB = _LumPortdeviceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57)
)
if mibBuilder.loadTexts:
    lumPortdeviceMIB.setStatus("current")
_LumPortdeviceIfMIB_ObjectIdentity = ObjectIdentity
lumPortdeviceIfMIB = _LumPortdeviceIfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58)
)
if mibBuilder.loadTexts:
    lumPortdeviceIfMIB.setStatus("current")
_LumIfFcMIB_ObjectIdentity = ObjectIdentity
lumIfFcMIB = _LumIfFcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 59)
)
if mibBuilder.loadTexts:
    lumIfFcMIB.setStatus("current")
_LumSoamPmMIB_ObjectIdentity = ObjectIdentity
lumSoamPmMIB = _LumSoamPmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60)
)
if mibBuilder.loadTexts:
    lumSoamPmMIB.setStatus("current")
_LumIccpMIB_ObjectIdentity = ObjectIdentity
lumIccpMIB = _LumIccpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 61)
)
if mibBuilder.loadTexts:
    lumIccpMIB.setStatus("current")
_LumMclagMIB_ObjectIdentity = ObjectIdentity
lumMclagMIB = _LumMclagMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62)
)
if mibBuilder.loadTexts:
    lumMclagMIB.setStatus("current")
_LumIfIwdmMIB_ObjectIdentity = ObjectIdentity
lumIfIwdmMIB = _LumIfIwdmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 63)
)
if mibBuilder.loadTexts:
    lumIfIwdmMIB.setStatus("current")
_LumIfMcMIB_ObjectIdentity = ObjectIdentity
lumIfMcMIB = _LumIfMcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64)
)
if mibBuilder.loadTexts:
    lumIfMcMIB.setStatus("current")
_LumIfAmplifierMIB_ObjectIdentity = ObjectIdentity
lumIfAmplifierMIB = _LumIfAmplifierMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 65)
)
if mibBuilder.loadTexts:
    lumIfAmplifierMIB.setStatus("current")
_LumFpuMIB_ObjectIdentity = ObjectIdentity
lumFpuMIB = _LumFpuMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66)
)
if mibBuilder.loadTexts:
    lumFpuMIB.setStatus("current")
_LumLldpV2MIB_ObjectIdentity = ObjectIdentity
lumLldpV2MIB = _LumLldpV2MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67)
)
if mibBuilder.loadTexts:
    lumLldpV2MIB.setStatus("current")
_LumIfFhMIB_ObjectIdentity = ObjectIdentity
lumIfFhMIB = _LumIfFhMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68)
)
if mibBuilder.loadTexts:
    lumIfFhMIB.setStatus("current")
_LumOpenflowMIB_ObjectIdentity = ObjectIdentity
lumOpenflowMIB = _LumOpenflowMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 69)
)
if mibBuilder.loadTexts:
    lumOpenflowMIB.setStatus("current")
_LumIfXcFlexMIB_ObjectIdentity = ObjectIdentity
lumIfXcFlexMIB = _LumIfXcFlexMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70)
)
if mibBuilder.loadTexts:
    lumIfXcFlexMIB.setStatus("current")
_LumSysinfoMIB_ObjectIdentity = ObjectIdentity
lumSysinfoMIB = _LumSysinfoMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71)
)
if mibBuilder.loadTexts:
    lumSysinfoMIB.setStatus("current")
_LumIfOtdrMIB_ObjectIdentity = ObjectIdentity
lumIfOtdrMIB = _LumIfOtdrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72)
)
if mibBuilder.loadTexts:
    lumIfOtdrMIB.setStatus("current")
_LumCryptoMIB_ObjectIdentity = ObjectIdentity
lumCryptoMIB = _LumCryptoMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73)
)
if mibBuilder.loadTexts:
    lumCryptoMIB.setStatus("current")
_LumCommlinkMIB_ObjectIdentity = ObjectIdentity
lumCommlinkMIB = _LumCommlinkMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74)
)
if mibBuilder.loadTexts:
    lumCommlinkMIB.setStatus("current")
_LumAcfMIB_ObjectIdentity = ObjectIdentity
lumAcfMIB = _LumAcfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 75)
)
if mibBuilder.loadTexts:
    lumAcfMIB.setStatus("current")
_LumProducts_ObjectIdentity = ObjectIdentity
lumProducts = _LumProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3)
)
if mibBuilder.loadTexts:
    lumProducts.setStatus("current")
_LumProductsGeneric_ObjectIdentity = ObjectIdentity
lumProductsGeneric = _LumProductsGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1)
)
if mibBuilder.loadTexts:
    lumProductsGeneric.setStatus("current")
_Mentis_ObjectIdentity = ObjectIdentity
mentis = _Mentis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mentis.setStatus("current")
_MentisControlSlot_ObjectIdentity = ObjectIdentity
mentisControlSlot = _MentisControlSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mentisControlSlot.setStatus("current")
_MentisTrafficSlot_ObjectIdentity = ObjectIdentity
mentisTrafficSlot = _MentisTrafficSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mentisTrafficSlot.setStatus("current")
_MentisControlUnit_ObjectIdentity = ObjectIdentity
mentisControlUnit = _MentisControlUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mentisControlUnit.setStatus("current")
_MentisMultirate2500TransponderUnit_ObjectIdentity = ObjectIdentity
mentisMultirate2500TransponderUnit = _MentisMultirate2500TransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mentisMultirate2500TransponderUnit.setStatus("current")
_MentisMuxponder028Unit_ObjectIdentity = ObjectIdentity
mentisMuxponder028Unit = _MentisMuxponder028Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mentisMuxponder028Unit.setStatus("current")
_MentisOpticalCrossConnect8Unit_ObjectIdentity = ObjectIdentity
mentisOpticalCrossConnect8Unit = _MentisOpticalCrossConnect8Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    mentisOpticalCrossConnect8Unit.setStatus("current")
_MentisOpticalCrossConnect16Unit_ObjectIdentity = ObjectIdentity
mentisOpticalCrossConnect16Unit = _MentisOpticalCrossConnect16Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    mentisOpticalCrossConnect16Unit.setStatus("current")
_MentisSingleAddDropABUnit_ObjectIdentity = ObjectIdentity
mentisSingleAddDropABUnit = _MentisSingleAddDropABUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    mentisSingleAddDropABUnit.setStatus("current")
_MentisSingleAddDropBAUnit_ObjectIdentity = ObjectIdentity
mentisSingleAddDropBAUnit = _MentisSingleAddDropBAUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    mentisSingleAddDropBAUnit.setStatus("current")
_MentisDualAddDropABUnit_ObjectIdentity = ObjectIdentity
mentisDualAddDropABUnit = _MentisDualAddDropABUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 12)
)
if mibBuilder.loadTexts:
    mentisDualAddDropABUnit.setStatus("current")
_MentisDualAddDropBAUnit_ObjectIdentity = ObjectIdentity
mentisDualAddDropBAUnit = _MentisDualAddDropBAUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 13)
)
if mibBuilder.loadTexts:
    mentisDualAddDropBAUnit.setStatus("current")
_MentisDualOpticalCirculationUnit_ObjectIdentity = ObjectIdentity
mentisDualOpticalCirculationUnit = _MentisDualOpticalCirculationUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 14)
)
if mibBuilder.loadTexts:
    mentisDualOpticalCirculationUnit.setStatus("current")
_Mentis4ChAddDropABUnit_ObjectIdentity = ObjectIdentity
mentis4ChAddDropABUnit = _Mentis4ChAddDropABUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 15)
)
if mibBuilder.loadTexts:
    mentis4ChAddDropABUnit.setStatus("current")
_Mentis4ChAddDropBAUnit_ObjectIdentity = ObjectIdentity
mentis4ChAddDropBAUnit = _Mentis4ChAddDropBAUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 16)
)
if mibBuilder.loadTexts:
    mentis4ChAddDropBAUnit.setStatus("current")
_MentisDualGbETransponderUnit_ObjectIdentity = ObjectIdentity
mentisDualGbETransponderUnit = _MentisDualGbETransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 17)
)
if mibBuilder.loadTexts:
    mentisDualGbETransponderUnit.setStatus("current")
_MentisOpticalAmplifierUnit_ObjectIdentity = ObjectIdentity
mentisOpticalAmplifierUnit = _MentisOpticalAmplifierUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 18)
)
if mibBuilder.loadTexts:
    mentisOpticalAmplifierUnit.setStatus("current")
_Mentis8chMuxDemuxExtensionUnit_ObjectIdentity = ObjectIdentity
mentis8chMuxDemuxExtensionUnit = _Mentis8chMuxDemuxExtensionUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 19)
)
if mibBuilder.loadTexts:
    mentis8chMuxDemuxExtensionUnit.setStatus("current")
_Mentis8chMuxDemuxTerminalUnit_ObjectIdentity = ObjectIdentity
mentis8chMuxDemuxTerminalUnit = _Mentis8chMuxDemuxTerminalUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 20)
)
if mibBuilder.loadTexts:
    mentis8chMuxDemuxTerminalUnit.setStatus("current")
_MentisQuadOpticalCouplerUnit_ObjectIdentity = ObjectIdentity
mentisQuadOpticalCouplerUnit = _MentisQuadOpticalCouplerUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 21)
)
if mibBuilder.loadTexts:
    mentisQuadOpticalCouplerUnit.setStatus("current")
_MentisMuxponder004Unit_ObjectIdentity = ObjectIdentity
mentisMuxponder004Unit = _MentisMuxponder004Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 22)
)
if mibBuilder.loadTexts:
    mentisMuxponder004Unit.setStatus("current")
_Mentis2chOpticalAmplifierAddDropABUnit_ObjectIdentity = ObjectIdentity
mentis2chOpticalAmplifierAddDropABUnit = _Mentis2chOpticalAmplifierAddDropABUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 23)
)
if mibBuilder.loadTexts:
    mentis2chOpticalAmplifierAddDropABUnit.setStatus("current")
_Mentis2chOpticalAmplifierAddDropBAUnit_ObjectIdentity = ObjectIdentity
mentis2chOpticalAmplifierAddDropBAUnit = _Mentis2chOpticalAmplifierAddDropBAUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 24)
)
if mibBuilder.loadTexts:
    mentis2chOpticalAmplifierAddDropBAUnit.setStatus("current")
_MentisDualOpticalAmplifierUnit_ObjectIdentity = ObjectIdentity
mentisDualOpticalAmplifierUnit = _MentisDualOpticalAmplifierUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 25)
)
if mibBuilder.loadTexts:
    mentisDualOpticalAmplifierUnit.setStatus("current")
_MentisCwdmAddDropUnit_ObjectIdentity = ObjectIdentity
mentisCwdmAddDropUnit = _MentisCwdmAddDropUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 26)
)
if mibBuilder.loadTexts:
    mentisCwdmAddDropUnit.setStatus("current")
_MentisSingleSpurAddDropUnit_ObjectIdentity = ObjectIdentity
mentisSingleSpurAddDropUnit = _MentisSingleSpurAddDropUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 27)
)
if mibBuilder.loadTexts:
    mentisSingleSpurAddDropUnit.setStatus("current")
_Mentis10GTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GTransponderUnit = _Mentis10GTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 28)
)
if mibBuilder.loadTexts:
    mentis10GTransponderUnit.setStatus("current")
_MentisLiteMr2500TransponderUnit_ObjectIdentity = ObjectIdentity
mentisLiteMr2500TransponderUnit = _MentisLiteMr2500TransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 29)
)
if mibBuilder.loadTexts:
    mentisLiteMr2500TransponderUnit.setStatus("current")
_MentisControlOscUnit_ObjectIdentity = ObjectIdentity
mentisControlOscUnit = _MentisControlOscUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 30)
)
if mibBuilder.loadTexts:
    mentisControlOscUnit.setStatus("current")
_MentisControlDualOscUnit_ObjectIdentity = ObjectIdentity
mentisControlDualOscUnit = _MentisControlDualOscUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 31)
)
if mibBuilder.loadTexts:
    mentisControlDualOscUnit.setStatus("current")
_MentisOpticalBandUnit_ObjectIdentity = ObjectIdentity
mentisOpticalBandUnit = _MentisOpticalBandUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 32)
)
if mibBuilder.loadTexts:
    mentisOpticalBandUnit.setStatus("current")
_MentisSync2MHzUnit_ObjectIdentity = ObjectIdentity
mentisSync2MHzUnit = _MentisSync2MHzUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 33)
)
if mibBuilder.loadTexts:
    mentisSync2MHzUnit.setStatus("current")
_MentisMxp8Unit_ObjectIdentity = ObjectIdentity
mentisMxp8Unit = _MentisMxp8Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 34)
)
if mibBuilder.loadTexts:
    mentisMxp8Unit.setStatus("current")
_MentisMxp16Unit_ObjectIdentity = ObjectIdentity
mentisMxp16Unit = _MentisMxp16Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 35)
)
if mibBuilder.loadTexts:
    mentisMxp16Unit.setStatus("current")
_MentisDualGbEDwdmUnit_ObjectIdentity = ObjectIdentity
mentisDualGbEDwdmUnit = _MentisDualGbEDwdmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 36)
)
if mibBuilder.loadTexts:
    mentisDualGbEDwdmUnit.setStatus("current")
_MentisDualGbECwdmUnit_ObjectIdentity = ObjectIdentity
mentisDualGbECwdmUnit = _MentisDualGbECwdmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 37)
)
if mibBuilder.loadTexts:
    mentisDualGbECwdmUnit.setStatus("current")
_MentisDualFiberChannelDwdmUnit_ObjectIdentity = ObjectIdentity
mentisDualFiberChannelDwdmUnit = _MentisDualFiberChannelDwdmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 38)
)
if mibBuilder.loadTexts:
    mentisDualFiberChannelDwdmUnit.setStatus("current")
_MentisDualFiberChannelCwdmUnit_ObjectIdentity = ObjectIdentity
mentisDualFiberChannelCwdmUnit = _MentisDualFiberChannelCwdmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 39)
)
if mibBuilder.loadTexts:
    mentisDualFiberChannelCwdmUnit.setStatus("current")
_MentisFiberChannelGbEDwdmUnit_ObjectIdentity = ObjectIdentity
mentisFiberChannelGbEDwdmUnit = _MentisFiberChannelGbEDwdmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 40)
)
if mibBuilder.loadTexts:
    mentisFiberChannelGbEDwdmUnit.setStatus("current")
_MentisFiberChannelGbECwdmUnit_ObjectIdentity = ObjectIdentity
mentisFiberChannelGbECwdmUnit = _MentisFiberChannelGbECwdmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 41)
)
if mibBuilder.loadTexts:
    mentisFiberChannelGbECwdmUnit.setStatus("current")
_MentisTrippleFiberChannelDwdmUnit_ObjectIdentity = ObjectIdentity
mentisTrippleFiberChannelDwdmUnit = _MentisTrippleFiberChannelDwdmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 42)
)
if mibBuilder.loadTexts:
    mentisTrippleFiberChannelDwdmUnit.setStatus("current")
_MentisQuadMultirateTransponderUnit_ObjectIdentity = ObjectIdentity
mentisQuadMultirateTransponderUnit = _MentisQuadMultirateTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 43)
)
if mibBuilder.loadTexts:
    mentisQuadMultirateTransponderUnit.setStatus("current")
_Mentis4chMuxDemuxTerminalABUnit_ObjectIdentity = ObjectIdentity
mentis4chMuxDemuxTerminalABUnit = _Mentis4chMuxDemuxTerminalABUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 44)
)
if mibBuilder.loadTexts:
    mentis4chMuxDemuxTerminalABUnit.setStatus("current")
_Mentis4chMuxDemuxTerminalBAUnit_ObjectIdentity = ObjectIdentity
mentis4chMuxDemuxTerminalBAUnit = _Mentis4chMuxDemuxTerminalBAUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 45)
)
if mibBuilder.loadTexts:
    mentis4chMuxDemuxTerminalBAUnit.setStatus("current")
_MentisSingleCwdmAddDropUnit_ObjectIdentity = ObjectIdentity
mentisSingleCwdmAddDropUnit = _MentisSingleCwdmAddDropUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 46)
)
if mibBuilder.loadTexts:
    mentisSingleCwdmAddDropUnit.setStatus("current")
_MentisDualCwdmAddDropUnit_ObjectIdentity = ObjectIdentity
mentisDualCwdmAddDropUnit = _MentisDualCwdmAddDropUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 47)
)
if mibBuilder.loadTexts:
    mentisDualCwdmAddDropUnit.setStatus("current")
_Mentis10GLANTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GLANTransponderUnit = _Mentis10GLANTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 48)
)
if mibBuilder.loadTexts:
    mentis10GLANTransponderUnit.setStatus("current")
_Mentis10GRCTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GRCTransponderUnit = _Mentis10GRCTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 49)
)
if mibBuilder.loadTexts:
    mentis10GRCTransponderUnit.setStatus("current")
_MentisEsconMxp8Unit_ObjectIdentity = ObjectIdentity
mentisEsconMxp8Unit = _MentisEsconMxp8Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 50)
)
if mibBuilder.loadTexts:
    mentisEsconMxp8Unit.setStatus("current")
_MentisOpticalAmplifier15dBmUnit_ObjectIdentity = ObjectIdentity
mentisOpticalAmplifier15dBmUnit = _MentisOpticalAmplifier15dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 51)
)
if mibBuilder.loadTexts:
    mentisOpticalAmplifier15dBmUnit.setStatus("current")
_MentisDualOpticalAmplifier15dBmUnit_ObjectIdentity = ObjectIdentity
mentisDualOpticalAmplifier15dBmUnit = _MentisDualOpticalAmplifier15dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 52)
)
if mibBuilder.loadTexts:
    mentisDualOpticalAmplifier15dBmUnit.setStatus("current")
_MentisGxpD2500Unit_ObjectIdentity = ObjectIdentity
mentisGxpD2500Unit = _MentisGxpD2500Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 53)
)
if mibBuilder.loadTexts:
    mentisGxpD2500Unit.setStatus("current")
_MentisGxpC2500Unit_ObjectIdentity = ObjectIdentity
mentisGxpC2500Unit = _MentisGxpC2500Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 54)
)
if mibBuilder.loadTexts:
    mentisGxpC2500Unit.setStatus("current")
_MentisGxpD10GUnit_ObjectIdentity = ObjectIdentity
mentisGxpD10GUnit = _MentisGxpD10GUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 55)
)
if mibBuilder.loadTexts:
    mentisGxpD10GUnit.setStatus("current")
_MentisDualGbEDwdmV2Unit_ObjectIdentity = ObjectIdentity
mentisDualGbEDwdmV2Unit = _MentisDualGbEDwdmV2Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 56)
)
if mibBuilder.loadTexts:
    mentisDualGbEDwdmV2Unit.setStatus("current")
_MentisDualGbECwdmV2Unit_ObjectIdentity = ObjectIdentity
mentisDualGbECwdmV2Unit = _MentisDualGbECwdmV2Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 57)
)
if mibBuilder.loadTexts:
    mentisDualGbECwdmV2Unit.setStatus("current")
_MentisDualFiberChannelDwdmV2Unit_ObjectIdentity = ObjectIdentity
mentisDualFiberChannelDwdmV2Unit = _MentisDualFiberChannelDwdmV2Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 58)
)
if mibBuilder.loadTexts:
    mentisDualFiberChannelDwdmV2Unit.setStatus("current")
_MentisDualFiberChannelCwdmV2Unit_ObjectIdentity = ObjectIdentity
mentisDualFiberChannelCwdmV2Unit = _MentisDualFiberChannelCwdmV2Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 59)
)
if mibBuilder.loadTexts:
    mentisDualFiberChannelCwdmV2Unit.setStatus("current")
_Mentis2xSingleCwdmAddDropUnit_ObjectIdentity = ObjectIdentity
mentis2xSingleCwdmAddDropUnit = _Mentis2xSingleCwdmAddDropUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 60)
)
if mibBuilder.loadTexts:
    mentis2xSingleCwdmAddDropUnit.setStatus("current")
_Mentis2xDualCwdmAddDropUnit_ObjectIdentity = ObjectIdentity
mentis2xDualCwdmAddDropUnit = _Mentis2xDualCwdmAddDropUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 61)
)
if mibBuilder.loadTexts:
    mentis2xDualCwdmAddDropUnit.setStatus("current")
_Mentis8chMuxDemuxTerminal2Unit_ObjectIdentity = ObjectIdentity
mentis8chMuxDemuxTerminal2Unit = _Mentis8chMuxDemuxTerminal2Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 62)
)
if mibBuilder.loadTexts:
    mentis8chMuxDemuxTerminal2Unit.setStatus("current")
_MentisDoubleDualGbETransponderUnit_ObjectIdentity = ObjectIdentity
mentisDoubleDualGbETransponderUnit = _MentisDoubleDualGbETransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 63)
)
if mibBuilder.loadTexts:
    mentisDoubleDualGbETransponderUnit.setStatus("current")
_MentisFpuOas2824Unit_ObjectIdentity = ObjectIdentity
mentisFpuOas2824Unit = _MentisFpuOas2824Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 64)
)
if mibBuilder.loadTexts:
    mentisFpuOas2824Unit.setStatus("current")
_Mentis2Fiber8chCwdmMuxUnit_ObjectIdentity = ObjectIdentity
mentis2Fiber8chCwdmMuxUnit = _Mentis2Fiber8chCwdmMuxUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 65)
)
if mibBuilder.loadTexts:
    mentis2Fiber8chCwdmMuxUnit.setStatus("current")
_Mentis2Fiber8chCwdmDemuxUnit_ObjectIdentity = ObjectIdentity
mentis2Fiber8chCwdmDemuxUnit = _Mentis2Fiber8chCwdmDemuxUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 66)
)
if mibBuilder.loadTexts:
    mentis2Fiber8chCwdmDemuxUnit.setStatus("current")
_MentisDouble10GLiteTransponderUnit_ObjectIdentity = ObjectIdentity
mentisDouble10GLiteTransponderUnit = _MentisDouble10GLiteTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 67)
)
if mibBuilder.loadTexts:
    mentisDouble10GLiteTransponderUnit.setStatus("current")
_Mentis10GBuTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GBuTransponderUnit = _Mentis10GBuTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 68)
)
if mibBuilder.loadTexts:
    mentis10GBuTransponderUnit.setStatus("current")
_Mentis10GLANBuTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GLANBuTransponderUnit = _Mentis10GLANBuTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 69)
)
if mibBuilder.loadTexts:
    mentis10GLANBuTransponderUnit.setStatus("current")
_Mentis10GClBuTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GClBuTransponderUnit = _Mentis10GClBuTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 70)
)
if mibBuilder.loadTexts:
    mentis10GClBuTransponderUnit.setStatus("current")
_Mentis10GLANClBuTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GLANClBuTransponderUnit = _Mentis10GLANClBuTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 71)
)
if mibBuilder.loadTexts:
    mentis10GLANClBuTransponderUnit.setStatus("current")
_Mentis8chMuxDemuxEvenExtensionUnit_ObjectIdentity = ObjectIdentity
mentis8chMuxDemuxEvenExtensionUnit = _Mentis8chMuxDemuxEvenExtensionUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 72)
)
if mibBuilder.loadTexts:
    mentis8chMuxDemuxEvenExtensionUnit.setStatus("current")
_Mentis8chMuxDemuxEvenTerminalUnit_ObjectIdentity = ObjectIdentity
mentis8chMuxDemuxEvenTerminalUnit = _Mentis8chMuxDemuxEvenTerminalUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 73)
)
if mibBuilder.loadTexts:
    mentis8chMuxDemuxEvenTerminalUnit.setStatus("current")
_MentisOpticalPreAmplifier17dBmUnit_ObjectIdentity = ObjectIdentity
mentisOpticalPreAmplifier17dBmUnit = _MentisOpticalPreAmplifier17dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 74)
)
if mibBuilder.loadTexts:
    mentisOpticalPreAmplifier17dBmUnit.setStatus("current")
_MentisDualOpticalAmplifier17dBmUnit_ObjectIdentity = ObjectIdentity
mentisDualOpticalAmplifier17dBmUnit = _MentisDualOpticalAmplifier17dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 75)
)
if mibBuilder.loadTexts:
    mentisDualOpticalAmplifier17dBmUnit.setStatus("current")
_MentisOpticalInterleaverUnit_ObjectIdentity = ObjectIdentity
mentisOpticalInterleaverUnit = _MentisOpticalInterleaverUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 76)
)
if mibBuilder.loadTexts:
    mentisOpticalInterleaverUnit.setStatus("current")
_MentisOpticalPowAmplifier17dBmUnit_ObjectIdentity = ObjectIdentity
mentisOpticalPowAmplifier17dBmUnit = _MentisOpticalPowAmplifier17dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 77)
)
if mibBuilder.loadTexts:
    mentisOpticalPowAmplifier17dBmUnit.setStatus("current")
_MentisSingleOpticalAmplifier17dBmUnit_ObjectIdentity = ObjectIdentity
mentisSingleOpticalAmplifier17dBmUnit = _MentisSingleOpticalAmplifier17dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 78)
)
if mibBuilder.loadTexts:
    mentisSingleOpticalAmplifier17dBmUnit.setStatus("current")
_Mentis9xGbEMuxponderUnit_ObjectIdentity = ObjectIdentity
mentis9xGbEMuxponderUnit = _Mentis9xGbEMuxponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 79)
)
if mibBuilder.loadTexts:
    mentis9xGbEMuxponderUnit.setStatus("current")
_Mentis1chAddDropDwdm2FiberUnit_ObjectIdentity = ObjectIdentity
mentis1chAddDropDwdm2FiberUnit = _Mentis1chAddDropDwdm2FiberUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 80)
)
if mibBuilder.loadTexts:
    mentis1chAddDropDwdm2FiberUnit.setStatus("current")
_Mentis1chAddDropCwdm2FiberUnit_ObjectIdentity = ObjectIdentity
mentis1chAddDropCwdm2FiberUnit = _Mentis1chAddDropCwdm2FiberUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 81)
)
if mibBuilder.loadTexts:
    mentis1chAddDropCwdm2FiberUnit.setStatus("current")
_MentisMdu4chExtendable2FiberUnit_ObjectIdentity = ObjectIdentity
mentisMdu4chExtendable2FiberUnit = _MentisMdu4chExtendable2FiberUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 82)
)
if mibBuilder.loadTexts:
    mentisMdu4chExtendable2FiberUnit.setStatus("current")
_MentisMdu4chTerminal2FiberUnit_ObjectIdentity = ObjectIdentity
mentisMdu4chTerminal2FiberUnit = _MentisMdu4chTerminal2FiberUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 83)
)
if mibBuilder.loadTexts:
    mentisMdu4chTerminal2FiberUnit.setStatus("current")
_Mentis8chVoltageControlledAttenuatorUnit_ObjectIdentity = ObjectIdentity
mentis8chVoltageControlledAttenuatorUnit = _Mentis8chVoltageControlledAttenuatorUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 84)
)
if mibBuilder.loadTexts:
    mentis8chVoltageControlledAttenuatorUnit.setStatus("current")
_MentisSingleOpticalAmplifier20dBmUnit_ObjectIdentity = ObjectIdentity
mentisSingleOpticalAmplifier20dBmUnit = _MentisSingleOpticalAmplifier20dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 85)
)
if mibBuilder.loadTexts:
    mentisSingleOpticalAmplifier20dBmUnit.setStatus("current")
_MentisDualOpticalAmplifier20dBmUnit_ObjectIdentity = ObjectIdentity
mentisDualOpticalAmplifier20dBmUnit = _MentisDualOpticalAmplifier20dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 86)
)
if mibBuilder.loadTexts:
    mentisDualOpticalAmplifier20dBmUnit.setStatus("current")
_MentisFpuYm235Unit_ObjectIdentity = ObjectIdentity
mentisFpuYm235Unit = _MentisFpuYm235Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 87)
)
if mibBuilder.loadTexts:
    mentisFpuYm235Unit.setStatus("current")
_Mentis4chAddDropDwdm2FiberUnit_ObjectIdentity = ObjectIdentity
mentis4chAddDropDwdm2FiberUnit = _Mentis4chAddDropDwdm2FiberUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 88)
)
if mibBuilder.loadTexts:
    mentis4chAddDropDwdm2FiberUnit.setStatus("current")
_MentisQuadMultirateTransponder2Unit_ObjectIdentity = ObjectIdentity
mentisQuadMultirateTransponder2Unit = _MentisQuadMultirateTransponder2Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 89)
)
if mibBuilder.loadTexts:
    mentisQuadMultirateTransponder2Unit.setStatus("current")
_MentisRamanOar450CUnit_ObjectIdentity = ObjectIdentity
mentisRamanOar450CUnit = _MentisRamanOar450CUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 90)
)
if mibBuilder.loadTexts:
    mentisRamanOar450CUnit.setStatus("current")
_MentisControlSfpUnit_ObjectIdentity = ObjectIdentity
mentisControlSfpUnit = _MentisControlSfpUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 91)
)
if mibBuilder.loadTexts:
    mentisControlSfpUnit.setStatus("current")
_MentisMultirate2500TransponderV2Unit_ObjectIdentity = ObjectIdentity
mentisMultirate2500TransponderV2Unit = _MentisMultirate2500TransponderV2Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 92)
)
if mibBuilder.loadTexts:
    mentisMultirate2500TransponderV2Unit.setStatus("current")
_MentisDouble10GbeUnit_ObjectIdentity = ObjectIdentity
mentisDouble10GbeUnit = _MentisDouble10GbeUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 93)
)
if mibBuilder.loadTexts:
    mentisDouble10GbeUnit.setStatus("current")
_Mentis4chMuxDemuxExtensionABUnit_ObjectIdentity = ObjectIdentity
mentis4chMuxDemuxExtensionABUnit = _Mentis4chMuxDemuxExtensionABUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 94)
)
if mibBuilder.loadTexts:
    mentis4chMuxDemuxExtensionABUnit.setStatus("current")
_Mentis4chMuxDemuxExtensionBAUnit_ObjectIdentity = ObjectIdentity
mentis4chMuxDemuxExtensionBAUnit = _Mentis4chMuxDemuxExtensionBAUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 95)
)
if mibBuilder.loadTexts:
    mentis4chMuxDemuxExtensionBAUnit.setStatus("current")
_MentisOpticalInterleaver50100Unit_ObjectIdentity = ObjectIdentity
mentisOpticalInterleaver50100Unit = _MentisOpticalInterleaver50100Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 96)
)
if mibBuilder.loadTexts:
    mentisOpticalInterleaver50100Unit.setStatus("current")
_MentisReconfigurableOpticalAddDropUnit_ObjectIdentity = ObjectIdentity
mentisReconfigurableOpticalAddDropUnit = _MentisReconfigurableOpticalAddDropUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 97)
)
if mibBuilder.loadTexts:
    mentisReconfigurableOpticalAddDropUnit.setStatus("current")
_Mentis6pGbeEthernetDemarcationUnit_ObjectIdentity = ObjectIdentity
mentis6pGbeEthernetDemarcationUnit = _Mentis6pGbeEthernetDemarcationUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 98)
)
if mibBuilder.loadTexts:
    mentis6pGbeEthernetDemarcationUnit.setStatus("current")
_Mentis10GClTcTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GClTcTransponderUnit = _Mentis10GClTcTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 99)
)
if mibBuilder.loadTexts:
    mentis10GClTcTransponderUnit.setStatus("current")
_Mentis4xSTM16MuxponderUnit_ObjectIdentity = ObjectIdentity
mentis4xSTM16MuxponderUnit = _Mentis4xSTM16MuxponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 100)
)
if mibBuilder.loadTexts:
    mentis4xSTM16MuxponderUnit.setStatus("current")
_MentisMroadm1p800Unit_ObjectIdentity = ObjectIdentity
mentisMroadm1p800Unit = _MentisMroadm1p800Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 101)
)
if mibBuilder.loadTexts:
    mentisMroadm1p800Unit.setStatus("current")
_MentisSingleOpticalLowGainAmplifier20dBmUnit_ObjectIdentity = ObjectIdentity
mentisSingleOpticalLowGainAmplifier20dBmUnit = _MentisSingleOpticalLowGainAmplifier20dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 102)
)
if mibBuilder.loadTexts:
    mentisSingleOpticalLowGainAmplifier20dBmUnit.setStatus("current")
_MentisDualOpticalLowGainAmplifier20dBmUnit_ObjectIdentity = ObjectIdentity
mentisDualOpticalLowGainAmplifier20dBmUnit = _MentisDualOpticalLowGainAmplifier20dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 103)
)
if mibBuilder.loadTexts:
    mentisDualOpticalLowGainAmplifier20dBmUnit.setStatus("current")
_MentisSingleOpticalFlatGainAmplifier10dBmUnit_ObjectIdentity = ObjectIdentity
mentisSingleOpticalFlatGainAmplifier10dBmUnit = _MentisSingleOpticalFlatGainAmplifier10dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 104)
)
if mibBuilder.loadTexts:
    mentisSingleOpticalFlatGainAmplifier10dBmUnit.setStatus("current")
_MentisDualOpticalFlatGainAmplifier10dBmUnit_ObjectIdentity = ObjectIdentity
mentisDualOpticalFlatGainAmplifier10dBmUnit = _MentisDualOpticalFlatGainAmplifier10dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 105)
)
if mibBuilder.loadTexts:
    mentisDualOpticalFlatGainAmplifier10dBmUnit.setStatus("current")
_Mentis10GOtnTcTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GOtnTcTransponderUnit = _Mentis10GOtnTcTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 106)
)
if mibBuilder.loadTexts:
    mentis10GOtnTcTransponderUnit.setStatus("current")
_Mentis40channelMuxDemuxEven50GHzDWDMUnit_ObjectIdentity = ObjectIdentity
mentis40channelMuxDemuxEven50GHzDWDMUnit = _Mentis40channelMuxDemuxEven50GHzDWDMUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 107)
)
if mibBuilder.loadTexts:
    mentis40channelMuxDemuxEven50GHzDWDMUnit.setStatus("current")
_Mentis40channelMuxDemuxOdd50GHzDWDMUnit_ObjectIdentity = ObjectIdentity
mentis40channelMuxDemuxOdd50GHzDWDMUnit = _Mentis40channelMuxDemuxOdd50GHzDWDMUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 108)
)
if mibBuilder.loadTexts:
    mentis40channelMuxDemuxOdd50GHzDWDMUnit.setStatus("current")
_Mentis8channelMuxDemuxExtEvenUnit_ObjectIdentity = ObjectIdentity
mentis8channelMuxDemuxExtEvenUnit = _Mentis8channelMuxDemuxExtEvenUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 109)
)
if mibBuilder.loadTexts:
    mentis8channelMuxDemuxExtEvenUnit.setStatus("current")
_Mentis8channelMuxDemuxExtOddUnit_ObjectIdentity = ObjectIdentity
mentis8channelMuxDemuxExtOddUnit = _Mentis8channelMuxDemuxExtOddUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 110)
)
if mibBuilder.loadTexts:
    mentis8channelMuxDemuxExtOddUnit.setStatus("current")
_Mentis2portOpticalChannelMonitor_ObjectIdentity = ObjectIdentity
mentis2portOpticalChannelMonitor = _Mentis2portOpticalChannelMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 111)
)
if mibBuilder.loadTexts:
    mentis2portOpticalChannelMonitor.setStatus("current")
_MentisMultiServiceMuxPonder_ObjectIdentity = ObjectIdentity
mentisMultiServiceMuxPonder = _MentisMultiServiceMuxPonder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 112)
)
if mibBuilder.loadTexts:
    mentisMultiServiceMuxPonder.setStatus("current")
_Mentis8chVariableOpticalAttenuatorII_ObjectIdentity = ObjectIdentity
mentis8chVariableOpticalAttenuatorII = _Mentis8chVariableOpticalAttenuatorII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 113)
)
if mibBuilder.loadTexts:
    mentis8chVariableOpticalAttenuatorII.setStatus("current")
_MentisMultiServiceDoubleQuadGbEMuxPonder_ObjectIdentity = ObjectIdentity
mentisMultiServiceDoubleQuadGbEMuxPonder = _MentisMultiServiceDoubleQuadGbEMuxPonder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 114)
)
if mibBuilder.loadTexts:
    mentisMultiServiceDoubleQuadGbEMuxPonder.setStatus("current")
_Mentis10GTcErTransponderUnit_ObjectIdentity = ObjectIdentity
mentis10GTcErTransponderUnit = _Mentis10GTcErTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 115)
)
if mibBuilder.loadTexts:
    mentis10GTcErTransponderUnit.setStatus("current")
_Mentis10xEthernetMuxPonder_ObjectIdentity = ObjectIdentity
mentis10xEthernetMuxPonder = _Mentis10xEthernetMuxPonder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 116)
)
if mibBuilder.loadTexts:
    mentis10xEthernetMuxPonder.setStatus("current")
_Mentis12pGbeEthernetDemarcationUnit_ObjectIdentity = ObjectIdentity
mentis12pGbeEthernetDemarcationUnit = _Mentis12pGbeEthernetDemarcationUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 117)
)
if mibBuilder.loadTexts:
    mentis12pGbeEthernetDemarcationUnit.setStatus("current")
_MentisGbeMxp10GFecUnit_ObjectIdentity = ObjectIdentity
mentisGbeMxp10GFecUnit = _MentisGbeMxp10GFecUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 118)
)
if mibBuilder.loadTexts:
    mentisGbeMxp10GFecUnit.setStatus("current")
_MentisRoadm1x4G100Unit_ObjectIdentity = ObjectIdentity
mentisRoadm1x4G100Unit = _MentisRoadm1x4G100Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 119)
)
if mibBuilder.loadTexts:
    mentisRoadm1x4G100Unit.setStatus("current")
_MentisQuadMultiServiceTransponder_ObjectIdentity = ObjectIdentity
mentisQuadMultiServiceTransponder = _MentisQuadMultiServiceTransponder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 120)
)
if mibBuilder.loadTexts:
    mentisQuadMultiServiceTransponder.setStatus("current")
_Mentis22xEthernetMuxPonder_ObjectIdentity = ObjectIdentity
mentis22xEthernetMuxPonder = _Mentis22xEthernetMuxPonder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 121)
)
if mibBuilder.loadTexts:
    mentis22xEthernetMuxPonder.setStatus("current")
_MentisPEOa1x26dBmUnit_ObjectIdentity = ObjectIdentity
mentisPEOa1x26dBmUnit = _MentisPEOa1x26dBmUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 122)
)
if mibBuilder.loadTexts:
    mentisPEOa1x26dBmUnit.setStatus("current")
_Mentis2PortProtectionControlUnit_ObjectIdentity = ObjectIdentity
mentis2PortProtectionControlUnit = _Mentis2PortProtectionControlUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 123)
)
if mibBuilder.loadTexts:
    mentis2PortProtectionControlUnit.setStatus("current")
_Mentis2chVariableOpticalAttenuator_ObjectIdentity = ObjectIdentity
mentis2chVariableOpticalAttenuator = _Mentis2chVariableOpticalAttenuator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 124)
)
if mibBuilder.loadTexts:
    mentis2chVariableOpticalAttenuator.setStatus("current")
_MentisMultiServiceMuxPonder10GTCEr_ObjectIdentity = ObjectIdentity
mentisMultiServiceMuxPonder10GTCEr = _MentisMultiServiceMuxPonder10GTCEr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 125)
)
if mibBuilder.loadTexts:
    mentisMultiServiceMuxPonder10GTCEr.setStatus("current")
_MentisMultiServiceMuxPonder10G_ObjectIdentity = ObjectIdentity
mentisMultiServiceMuxPonder10G = _MentisMultiServiceMuxPonder10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 126)
)
if mibBuilder.loadTexts:
    mentisMultiServiceMuxPonder10G.setStatus("current")
_MentisMultiServiceQuad2G5Transponder_ObjectIdentity = ObjectIdentity
mentisMultiServiceQuad2G5Transponder = _MentisMultiServiceQuad2G5Transponder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 127)
)
if mibBuilder.loadTexts:
    mentisMultiServiceQuad2G5Transponder.setStatus("current")
_Mentis4x2G510GOcMuxponder_ObjectIdentity = ObjectIdentity
mentis4x2G510GOcMuxponder = _Mentis4x2G510GOcMuxponder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 128)
)
if mibBuilder.loadTexts:
    mentis4x2G510GOcMuxponder.setStatus("current")
_Mentis22xEthernetMuxPonderII_ObjectIdentity = ObjectIdentity
mentis22xEthernetMuxPonderII = _Mentis22xEthernetMuxPonderII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 129)
)
if mibBuilder.loadTexts:
    mentis22xEthernetMuxPonderII.setStatus("current")
_MentisBandSplitterUnit1x5Even_ObjectIdentity = ObjectIdentity
mentisBandSplitterUnit1x5Even = _MentisBandSplitterUnit1x5Even_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 130)
)
if mibBuilder.loadTexts:
    mentisBandSplitterUnit1x5Even.setStatus("current")
_MentisBandSplitterUnit1x5Odd_ObjectIdentity = ObjectIdentity
mentisBandSplitterUnit1x5Odd = _MentisBandSplitterUnit1x5Odd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 131)
)
if mibBuilder.loadTexts:
    mentisBandSplitterUnit1x5Odd.setStatus("current")
_Mentis10xEthernetMuxPonderII_ObjectIdentity = ObjectIdentity
mentis10xEthernetMuxPonderII = _Mentis10xEthernetMuxPonderII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 132)
)
if mibBuilder.loadTexts:
    mentis10xEthernetMuxPonderII.setStatus("current")
_MentisMSAccessCollector8xE1T1_2xEth_ObjectIdentity = ObjectIdentity
mentisMSAccessCollector8xE1T1_2xEth = _MentisMSAccessCollector8xE1T1_2xEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 133)
)
if mibBuilder.loadTexts:
    mentisMSAccessCollector8xE1T1_2xEth.setStatus("current")
_MentisMSAccessCollector16xE1T1_4xEth_ObjectIdentity = ObjectIdentity
mentisMSAccessCollector16xE1T1_4xEth = _MentisMSAccessCollector16xE1T1_4xEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 134)
)
if mibBuilder.loadTexts:
    mentisMSAccessCollector16xE1T1_4xEth.setStatus("current")
_MentisMSAccessHub4xSTM_1_16xEth_ObjectIdentity = ObjectIdentity
mentisMSAccessHub4xSTM_1_16xEth = _MentisMSAccessHub4xSTM_1_16xEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 135)
)
if mibBuilder.loadTexts:
    mentisMSAccessHub4xSTM_1_16xEth.setStatus("current")
_MentisMSAccessHub4xOC_3_16xEth_ObjectIdentity = ObjectIdentity
mentisMSAccessHub4xOC_3_16xEth = _MentisMSAccessHub4xOC_3_16xEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 136)
)
if mibBuilder.loadTexts:
    mentisMSAccessHub4xOC_3_16xEth.setStatus("current")
_MentisRoadm1x8G50Unit_ObjectIdentity = ObjectIdentity
mentisRoadm1x8G50Unit = _MentisRoadm1x8G50Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 137)
)
if mibBuilder.loadTexts:
    mentisRoadm1x8G50Unit.setStatus("current")
_Mentis4ChAddDropDwdmEven50G_ObjectIdentity = ObjectIdentity
mentis4ChAddDropDwdmEven50G = _Mentis4ChAddDropDwdmEven50G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 138)
)
if mibBuilder.loadTexts:
    mentis4ChAddDropDwdmEven50G.setStatus("current")
_Mentis4ChAddDropDwdmOdd50G_ObjectIdentity = ObjectIdentity
mentis4ChAddDropDwdmOdd50G = _Mentis4ChAddDropDwdmOdd50G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 139)
)
if mibBuilder.loadTexts:
    mentis4ChAddDropDwdmOdd50G.setStatus("current")
_Mentis8x10EthernetMuxPonderII_ObjectIdentity = ObjectIdentity
mentis8x10EthernetMuxPonderII = _Mentis8x10EthernetMuxPonderII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 140)
)
if mibBuilder.loadTexts:
    mentis8x10EthernetMuxPonderII.setStatus("current")
_MentisMxp8iiSdhUnit_ObjectIdentity = ObjectIdentity
mentisMxp8iiSdhUnit = _MentisMxp8iiSdhUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 141)
)
if mibBuilder.loadTexts:
    mentisMxp8iiSdhUnit.setStatus("current")
_MentisMxp8iiSonetUnit_ObjectIdentity = ObjectIdentity
mentisMxp8iiSonetUnit = _MentisMxp8iiSonetUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 142)
)
if mibBuilder.loadTexts:
    mentisMxp8iiSonetUnit.setStatus("current")
_MentisMSAccessCollector16xE1T1_4xEthTempHardend_ObjectIdentity = ObjectIdentity
mentisMSAccessCollector16xE1T1_4xEthTempHardend = _MentisMSAccessCollector16xE1T1_4xEthTempHardend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 143)
)
if mibBuilder.loadTexts:
    mentisMSAccessCollector16xE1T1_4xEthTempHardend.setStatus("current")
_MentisMdu40EvenL_ObjectIdentity = ObjectIdentity
mentisMdu40EvenL = _MentisMdu40EvenL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 144)
)
if mibBuilder.loadTexts:
    mentisMdu40EvenL.setStatus("current")
_MentisMdu40OddL_ObjectIdentity = ObjectIdentity
mentisMdu40OddL = _MentisMdu40OddL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 145)
)
if mibBuilder.loadTexts:
    mentisMdu40OddL.setStatus("current")
_MentisOa1x20dBmVg_ObjectIdentity = ObjectIdentity
mentisOa1x20dBmVg = _MentisOa1x20dBmVg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 146)
)
if mibBuilder.loadTexts:
    mentisOa1x20dBmVg.setStatus("current")
_MentisOa2x20dBmVg_ObjectIdentity = ObjectIdentity
mentisOa2x20dBmVg = _MentisOa2x20dBmVg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 147)
)
if mibBuilder.loadTexts:
    mentisOa2x20dBmVg.setStatus("current")
_MentisRoadm1x2G100_ObjectIdentity = ObjectIdentity
mentisRoadm1x2G100 = _MentisRoadm1x2G100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 148)
)
if mibBuilder.loadTexts:
    mentisRoadm1x2G100.setStatus("current")
_MentisRoadm1x2G50_ObjectIdentity = ObjectIdentity
mentisRoadm1x2G50 = _MentisRoadm1x2G50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 149)
)
if mibBuilder.loadTexts:
    mentisRoadm1x2G50.setStatus("current")
_MentisTpq10GfecUnit_ObjectIdentity = ObjectIdentity
mentisTpq10GfecUnit = _MentisTpq10GfecUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 150)
)
if mibBuilder.loadTexts:
    mentisTpq10GfecUnit.setStatus("current")
_MentisControlSfpiiUnit_ObjectIdentity = ObjectIdentity
mentisControlSfpiiUnit = _MentisControlSfpiiUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 151)
)
if mibBuilder.loadTexts:
    mentisControlSfpiiUnit.setStatus("current")
_MentisCoD40evUnit_ObjectIdentity = ObjectIdentity
mentisCoD40evUnit = _MentisCoD40evUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 152)
)
if mibBuilder.loadTexts:
    mentisCoD40evUnit.setStatus("current")
_MentisCoD40eveUnit_ObjectIdentity = ObjectIdentity
mentisCoD40eveUnit = _MentisCoD40eveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 153)
)
if mibBuilder.loadTexts:
    mentisCoD40eveUnit.setStatus("current")
_MentisCoD40odUnit_ObjectIdentity = ObjectIdentity
mentisCoD40odUnit = _MentisCoD40odUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 154)
)
if mibBuilder.loadTexts:
    mentisCoD40odUnit.setStatus("current")
_MentisCoD40odeUnit_ObjectIdentity = ObjectIdentity
mentisCoD40odeUnit = _MentisCoD40odeUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 155)
)
if mibBuilder.loadTexts:
    mentisCoD40odeUnit.setStatus("current")
_MentisDcDk652km20Unit_ObjectIdentity = ObjectIdentity
mentisDcDk652km20Unit = _MentisDcDk652km20Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 156)
)
if mibBuilder.loadTexts:
    mentisDcDk652km20Unit.setStatus("current")
_MentisDcDk652km40Unit_ObjectIdentity = ObjectIdentity
mentisDcDk652km40Unit = _MentisDcDk652km40Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 157)
)
if mibBuilder.loadTexts:
    mentisDcDk652km40Unit.setStatus("current")
_MentisDcDk652km60Unit_ObjectIdentity = ObjectIdentity
mentisDcDk652km60Unit = _MentisDcDk652km60Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 158)
)
if mibBuilder.loadTexts:
    mentisDcDk652km60Unit.setStatus("current")
_MentisDcDk652km80Unit_ObjectIdentity = ObjectIdentity
mentisDcDk652km80Unit = _MentisDcDk652km80Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 159)
)
if mibBuilder.loadTexts:
    mentisDcDk652km80Unit.setStatus("current")
_MentisDcP652km40Unit_ObjectIdentity = ObjectIdentity
mentisDcP652km40Unit = _MentisDcP652km40Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 160)
)
if mibBuilder.loadTexts:
    mentisDcP652km40Unit.setStatus("current")
_MentisDcP652km60Unit_ObjectIdentity = ObjectIdentity
mentisDcP652km60Unit = _MentisDcP652km60Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 161)
)
if mibBuilder.loadTexts:
    mentisDcP652km60Unit.setStatus("current")
_MentisDcP652km80Unit_ObjectIdentity = ObjectIdentity
mentisDcP652km80Unit = _MentisDcP652km80Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 162)
)
if mibBuilder.loadTexts:
    mentisDcP652km80Unit.setStatus("current")
_MentisDcP652km100Unit_ObjectIdentity = ObjectIdentity
mentisDcP652km100Unit = _MentisDcP652km100Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 163)
)
if mibBuilder.loadTexts:
    mentisDcP652km100Unit.setStatus("current")
_MentisDcP652km120Unit_ObjectIdentity = ObjectIdentity
mentisDcP652km120Unit = _MentisDcP652km120Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 164)
)
if mibBuilder.loadTexts:
    mentisDcP652km120Unit.setStatus("current")
_MentisEmxp40GiiUnit_ObjectIdentity = ObjectIdentity
mentisEmxp40GiiUnit = _MentisEmxp40GiiUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 165)
)
if mibBuilder.loadTexts:
    mentisEmxp40GiiUnit.setStatus("current")
_MentisQuadMultiProtocolTransponderUnit_ObjectIdentity = ObjectIdentity
mentisQuadMultiProtocolTransponderUnit = _MentisQuadMultiProtocolTransponderUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 166)
)
if mibBuilder.loadTexts:
    mentisQuadMultiProtocolTransponderUnit.setStatus("current")
_MentisTpq10GfecRegUnit_ObjectIdentity = ObjectIdentity
mentisTpq10GfecRegUnit = _MentisTpq10GfecRegUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 167)
)
if mibBuilder.loadTexts:
    mentisTpq10GfecRegUnit.setStatus("current")
_MentisColorlessMuxDemuxUnit_ObjectIdentity = ObjectIdentity
mentisColorlessMuxDemuxUnit = _MentisColorlessMuxDemuxUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 168)
)
if mibBuilder.loadTexts:
    mentisColorlessMuxDemuxUnit.setStatus("current")
_Mentis8chSfpBasedVoaUnit_ObjectIdentity = ObjectIdentity
mentis8chSfpBasedVoaUnit = _Mentis8chSfpBasedVoaUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 169)
)
if mibBuilder.loadTexts:
    mentis8chSfpBasedVoaUnit.setStatus("current")
_MentisMsTp40GUnit_ObjectIdentity = ObjectIdentity
mentisMsTp40GUnit = _MentisMsTp40GUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 170)
)
if mibBuilder.loadTexts:
    mentisMsTp40GUnit.setStatus("current")
_MentisMsMxp40GUnit_ObjectIdentity = ObjectIdentity
mentisMsMxp40GUnit = _MentisMsMxp40GUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 171)
)
if mibBuilder.loadTexts:
    mentisMsMxp40GUnit.setStatus("current")
_MentisMXP10GOTN_ObjectIdentity = ObjectIdentity
mentisMXP10GOTN = _MentisMXP10GOTN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 172)
)
if mibBuilder.loadTexts:
    mentisMXP10GOTN.setStatus("current")
_MentisOpticalCouplerUnitDualQuad_ObjectIdentity = ObjectIdentity
mentisOpticalCouplerUnitDualQuad = _MentisOpticalCouplerUnitDualQuad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 173)
)
if mibBuilder.loadTexts:
    mentisOpticalCouplerUnitDualQuad.setStatus("current")
_MentisTm4700Unit_ObjectIdentity = ObjectIdentity
mentisTm4700Unit = _MentisTm4700Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 174)
)
if mibBuilder.loadTexts:
    mentisTm4700Unit.setStatus("current")
_MentisTm4011Unit_ObjectIdentity = ObjectIdentity
mentisTm4011Unit = _MentisTm4011Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 175)
)
if mibBuilder.loadTexts:
    mentisTm4011Unit.setStatus("current")
_MentisTm100MxpUnit_ObjectIdentity = ObjectIdentity
mentisTm100MxpUnit = _MentisTm100MxpUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 176)
)
if mibBuilder.loadTexts:
    mentisTm100MxpUnit.setStatus("current")
_MentisTm100TpUnit_ObjectIdentity = ObjectIdentity
mentisTm100TpUnit = _MentisTm100TpUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 177)
)
if mibBuilder.loadTexts:
    mentisTm100TpUnit.setStatus("current")
_MentisTm100RegUnit_ObjectIdentity = ObjectIdentity
mentisTm100RegUnit = _MentisTm100RegUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 178)
)
if mibBuilder.loadTexts:
    mentisTm100RegUnit.setStatus("current")
_Mentis2PSeedLightCouplerUnit_ObjectIdentity = ObjectIdentity
mentis2PSeedLightCouplerUnit = _Mentis2PSeedLightCouplerUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 179)
)
if mibBuilder.loadTexts:
    mentis2PSeedLightCouplerUnit.setStatus("current")
_MentisDual21dBmSeedLightUnit_ObjectIdentity = ObjectIdentity
mentisDual21dBmSeedLightUnit = _MentisDual21dBmSeedLightUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 180)
)
if mibBuilder.loadTexts:
    mentisDual21dBmSeedLightUnit.setStatus("current")
_MentisEmxp62GiieUnit_ObjectIdentity = ObjectIdentity
mentisEmxp62GiieUnit = _MentisEmxp62GiieUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 181)
)
if mibBuilder.loadTexts:
    mentisEmxp62GiieUnit.setStatus("current")
_MentisEmxp120GiieUnit_ObjectIdentity = ObjectIdentity
mentisEmxp120GiieUnit = _MentisEmxp120GiieUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 182)
)
if mibBuilder.loadTexts:
    mentisEmxp120GiieUnit.setStatus("current")
_MentisOYPatchCordUnit_ObjectIdentity = ObjectIdentity
mentisOYPatchCordUnit = _MentisOYPatchCordUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 183)
)
if mibBuilder.loadTexts:
    mentisOYPatchCordUnit.setStatus("current")
_MentisTpq10gfeciUnit_ObjectIdentity = ObjectIdentity
mentisTpq10gfeciUnit = _MentisTpq10gfeciUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 184)
)
if mibBuilder.loadTexts:
    mentisTpq10gfeciUnit.setStatus("current")
_MentisTpq10gfecregiUnit_ObjectIdentity = ObjectIdentity
mentisTpq10gfecregiUnit = _MentisTpq10gfecregiUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 185)
)
if mibBuilder.loadTexts:
    mentisTpq10gfecregiUnit.setStatus("current")
_MentisTphex10gotn_ObjectIdentity = ObjectIdentity
mentisTphex10gotn = _MentisTphex10gotn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 186)
)
if mibBuilder.loadTexts:
    mentisTphex10gotn.setStatus("current")
_MentisEmxp48GiieUnit_ObjectIdentity = ObjectIdentity
mentisEmxp48GiieUnit = _MentisEmxp48GiieUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 187)
)
if mibBuilder.loadTexts:
    mentisEmxp48GiieUnit.setStatus("current")
_MentisTp100gotn_ObjectIdentity = ObjectIdentity
mentisTp100gotn = _MentisTp100gotn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 188)
)
if mibBuilder.loadTexts:
    mentisTp100gotn.setStatus("current")
_MentisEmxp220GiieUnit_ObjectIdentity = ObjectIdentity
mentisEmxp220GiieUnit = _MentisEmxp220GiieUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 189)
)
if mibBuilder.loadTexts:
    mentisEmxp220GiieUnit.setStatus("current")
_MentisTpmrHL16GUnit_ObjectIdentity = ObjectIdentity
mentisTpmrHL16GUnit = _MentisTpmrHL16GUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 190)
)
if mibBuilder.loadTexts:
    mentisTpmrHL16GUnit.setStatus("current")
_MentisFronthaulMuxPonder10G_ObjectIdentity = ObjectIdentity
mentisFronthaulMuxPonder10G = _MentisFronthaulMuxPonder10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 191)
)
if mibBuilder.loadTexts:
    mentisFronthaulMuxPonder10G.setStatus("current")
_MentisMxp100gotn_ObjectIdentity = ObjectIdentity
mentisMxp100gotn = _MentisMxp100gotn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 192)
)
if mibBuilder.loadTexts:
    mentisMxp100gotn.setStatus("current")
_MentisEmxp240GiieUnit_ObjectIdentity = ObjectIdentity
mentisEmxp240GiieUnit = _MentisEmxp240GiieUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 193)
)
if mibBuilder.loadTexts:
    mentisEmxp240GiieUnit.setStatus("current")
_MentisEmxp3Unit_ObjectIdentity = ObjectIdentity
mentisEmxp3Unit = _MentisEmxp3Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 194)
)
if mibBuilder.loadTexts:
    mentisEmxp3Unit.setStatus("current")
_MentisBoardTypeAUnit_ObjectIdentity = ObjectIdentity
mentisBoardTypeAUnit = _MentisBoardTypeAUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 195)
)
if mibBuilder.loadTexts:
    mentisBoardTypeAUnit.setStatus("current")
_MentisBoardTypeBUnit_ObjectIdentity = ObjectIdentity
mentisBoardTypeBUnit = _MentisBoardTypeBUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 196)
)
if mibBuilder.loadTexts:
    mentisBoardTypeBUnit.setStatus("current")
_MentisFpu1Unit_ObjectIdentity = ObjectIdentity
mentisFpu1Unit = _MentisFpu1Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 197)
)
if mibBuilder.loadTexts:
    mentisFpu1Unit.setStatus("current")
_MentisOaraed21hghybUnit_ObjectIdentity = ObjectIdentity
mentisOaraed21hghybUnit = _MentisOaraed21hghybUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 198)
)
if mibBuilder.loadTexts:
    mentisOaraed21hghybUnit.setStatus("current")
_MentisTpmrHL16GUniUnit_ObjectIdentity = ObjectIdentity
mentisTpmrHL16GUniUnit = _MentisTpmrHL16GUniUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 199)
)
if mibBuilder.loadTexts:
    mentisTpmrHL16GUniUnit.setStatus("current")
_MentisDcDk652km100Unit_ObjectIdentity = ObjectIdentity
mentisDcDk652km100Unit = _MentisDcDk652km100Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 200)
)
if mibBuilder.loadTexts:
    mentisDcDk652km100Unit.setStatus("current")
_MentisDcDk652km120Unit_ObjectIdentity = ObjectIdentity
mentisDcDk652km120Unit = _MentisDcDk652km120Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 201)
)
if mibBuilder.loadTexts:
    mentisDcDk652km120Unit.setStatus("current")
_MentisDcP652km20Unit_ObjectIdentity = ObjectIdentity
mentisDcP652km20Unit = _MentisDcP652km20Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 202)
)
if mibBuilder.loadTexts:
    mentisDcP652km20Unit.setStatus("current")
_MentisFhau1Unit_ObjectIdentity = ObjectIdentity
mentisFhau1Unit = _MentisFhau1Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 203)
)
if mibBuilder.loadTexts:
    mentisFhau1Unit.setStatus("current")
_MentisFha1u1Unit_ObjectIdentity = ObjectIdentity
mentisFha1u1Unit = _MentisFha1u1Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 204)
)
if mibBuilder.loadTexts:
    mentisFha1u1Unit.setStatus("current")
_MentisOa1x20dBmVg2Unit_ObjectIdentity = ObjectIdentity
mentisOa1x20dBmVg2Unit = _MentisOa1x20dBmVg2Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 205)
)
if mibBuilder.loadTexts:
    mentisOa1x20dBmVg2Unit.setStatus("current")
_MentisOa2x20dBmVg2Unit_ObjectIdentity = ObjectIdentity
mentisOa2x20dBmVg2Unit = _MentisOa2x20dBmVg2Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 206)
)
if mibBuilder.loadTexts:
    mentisOa2x20dBmVg2Unit.setStatus("current")
_MentisPtio10GUnit_ObjectIdentity = ObjectIdentity
mentisPtio10GUnit = _MentisPtio10GUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 207)
)
if mibBuilder.loadTexts:
    mentisPtio10GUnit.setStatus("current")
_MentisFxp400gotnUnit_ObjectIdentity = ObjectIdentity
mentisFxp400gotnUnit = _MentisFxp400gotnUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 208)
)
if mibBuilder.loadTexts:
    mentisFxp400gotnUnit.setStatus("current")
_MentisCompo24Unit_ObjectIdentity = ObjectIdentity
mentisCompo24Unit = _MentisCompo24Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 209)
)
if mibBuilder.loadTexts:
    mentisCompo24Unit.setStatus("current")
_MentisTp100gotnii_ObjectIdentity = ObjectIdentity
mentisTp100gotnii = _MentisTp100gotnii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 210)
)
if mibBuilder.loadTexts:
    mentisTp100gotnii.setStatus("current")
_MentisPtio100GUnit_ObjectIdentity = ObjectIdentity
mentisPtio100GUnit = _MentisPtio100GUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 211)
)
if mibBuilder.loadTexts:
    mentisPtio100GUnit.setStatus("current")
_MentisRfu1Unit_ObjectIdentity = ObjectIdentity
mentisRfu1Unit = _MentisRfu1Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 212)
)
if mibBuilder.loadTexts:
    mentisRfu1Unit.setStatus("current")
_MentisCoD919926Unit_ObjectIdentity = ObjectIdentity
mentisCoD919926Unit = _MentisCoD919926Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 213)
)
if mibBuilder.loadTexts:
    mentisCoD919926Unit.setStatus("current")
_MentisCoD927934Unit_ObjectIdentity = ObjectIdentity
mentisCoD927934Unit = _MentisCoD927934Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 214)
)
if mibBuilder.loadTexts:
    mentisCoD927934Unit.setStatus("current")
_MentisCoD935942Unit_ObjectIdentity = ObjectIdentity
mentisCoD935942Unit = _MentisCoD935942Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 215)
)
if mibBuilder.loadTexts:
    mentisCoD935942Unit.setStatus("current")
_MentisCoD943950Unit_ObjectIdentity = ObjectIdentity
mentisCoD943950Unit = _MentisCoD943950Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 216)
)
if mibBuilder.loadTexts:
    mentisCoD943950Unit.setStatus("current")
_MentisCoD951958Unit_ObjectIdentity = ObjectIdentity
mentisCoD951958Unit = _MentisCoD951958Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 217)
)
if mibBuilder.loadTexts:
    mentisCoD951958Unit.setStatus("current")
_MentisCoD919926eUnit_ObjectIdentity = ObjectIdentity
mentisCoD919926eUnit = _MentisCoD919926eUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 218)
)
if mibBuilder.loadTexts:
    mentisCoD919926eUnit.setStatus("current")
_MentisCoD927934eUnit_ObjectIdentity = ObjectIdentity
mentisCoD927934eUnit = _MentisCoD927934eUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 219)
)
if mibBuilder.loadTexts:
    mentisCoD927934eUnit.setStatus("current")
_MentisCoD935942eUnit_ObjectIdentity = ObjectIdentity
mentisCoD935942eUnit = _MentisCoD935942eUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 220)
)
if mibBuilder.loadTexts:
    mentisCoD935942eUnit.setStatus("current")
_MentisCoD943950eUnit_ObjectIdentity = ObjectIdentity
mentisCoD943950eUnit = _MentisCoD943950eUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 221)
)
if mibBuilder.loadTexts:
    mentisCoD943950eUnit.setStatus("current")
_MentisCoD951958eUnit_ObjectIdentity = ObjectIdentity
mentisCoD951958eUnit = _MentisCoD951958eUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 222)
)
if mibBuilder.loadTexts:
    mentisCoD951958eUnit.setStatus("current")
_MentisCo4Unit_ObjectIdentity = ObjectIdentity
mentisCo4Unit = _MentisCo4Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 223)
)
if mibBuilder.loadTexts:
    mentisCo4Unit.setStatus("current")
_MentisCo5Unit_ObjectIdentity = ObjectIdentity
mentisCo5Unit = _MentisCo5Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 224)
)
if mibBuilder.loadTexts:
    mentisCo5Unit.setStatus("current")
_MentisCodsf20evaUnit_ObjectIdentity = ObjectIdentity
mentisCodsf20evaUnit = _MentisCodsf20evaUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 225)
)
if mibBuilder.loadTexts:
    mentisCodsf20evaUnit.setStatus("current")
_MentisCodsf20evbUnit_ObjectIdentity = ObjectIdentity
mentisCodsf20evbUnit = _MentisCodsf20evbUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 226)
)
if mibBuilder.loadTexts:
    mentisCodsf20evbUnit.setStatus("current")
_MentisCodsf4919Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4919Unit = _MentisCodsf4919Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 227)
)
if mibBuilder.loadTexts:
    mentisCodsf4919Unit.setStatus("current")
_MentisCodsf4926Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4926Unit = _MentisCodsf4926Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 228)
)
if mibBuilder.loadTexts:
    mentisCodsf4926Unit.setStatus("current")
_MentisCodsf4927Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4927Unit = _MentisCodsf4927Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 229)
)
if mibBuilder.loadTexts:
    mentisCodsf4927Unit.setStatus("current")
_MentisCodsf4934Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4934Unit = _MentisCodsf4934Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 230)
)
if mibBuilder.loadTexts:
    mentisCodsf4934Unit.setStatus("current")
_MentisCodsf4935Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4935Unit = _MentisCodsf4935Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 231)
)
if mibBuilder.loadTexts:
    mentisCodsf4935Unit.setStatus("current")
_MentisCodsf4942Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4942Unit = _MentisCodsf4942Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 232)
)
if mibBuilder.loadTexts:
    mentisCodsf4942Unit.setStatus("current")
_MentisCodsf4943Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4943Unit = _MentisCodsf4943Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 233)
)
if mibBuilder.loadTexts:
    mentisCodsf4943Unit.setStatus("current")
_MentisCodsf4950Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4950Unit = _MentisCodsf4950Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 234)
)
if mibBuilder.loadTexts:
    mentisCodsf4950Unit.setStatus("current")
_MentisCodsf4951Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4951Unit = _MentisCodsf4951Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 235)
)
if mibBuilder.loadTexts:
    mentisCodsf4951Unit.setStatus("current")
_MentisCodsf4958Unit_ObjectIdentity = ObjectIdentity
mentisCodsf4958Unit = _MentisCodsf4958Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 236)
)
if mibBuilder.loadTexts:
    mentisCodsf4958Unit.setStatus("current")
_MentisCodsf2919Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2919Unit = _MentisCodsf2919Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 237)
)
if mibBuilder.loadTexts:
    mentisCodsf2919Unit.setStatus("current")
_MentisCodsf2922Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2922Unit = _MentisCodsf2922Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 238)
)
if mibBuilder.loadTexts:
    mentisCodsf2922Unit.setStatus("current")
_MentisCodsf2923Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2923Unit = _MentisCodsf2923Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 239)
)
if mibBuilder.loadTexts:
    mentisCodsf2923Unit.setStatus("current")
_MentisCodsf2926Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2926Unit = _MentisCodsf2926Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 240)
)
if mibBuilder.loadTexts:
    mentisCodsf2926Unit.setStatus("current")
_MentisCodsf2927Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2927Unit = _MentisCodsf2927Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 241)
)
if mibBuilder.loadTexts:
    mentisCodsf2927Unit.setStatus("current")
_MentisCodsf2930Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2930Unit = _MentisCodsf2930Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 242)
)
if mibBuilder.loadTexts:
    mentisCodsf2930Unit.setStatus("current")
_MentisCodsf2931Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2931Unit = _MentisCodsf2931Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 243)
)
if mibBuilder.loadTexts:
    mentisCodsf2931Unit.setStatus("current")
_MentisCodsf2934Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2934Unit = _MentisCodsf2934Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 244)
)
if mibBuilder.loadTexts:
    mentisCodsf2934Unit.setStatus("current")
_MentisCodsf2935Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2935Unit = _MentisCodsf2935Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 245)
)
if mibBuilder.loadTexts:
    mentisCodsf2935Unit.setStatus("current")
_MentisCodsf2938Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2938Unit = _MentisCodsf2938Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 246)
)
if mibBuilder.loadTexts:
    mentisCodsf2938Unit.setStatus("current")
_MentisCodsf2939Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2939Unit = _MentisCodsf2939Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 247)
)
if mibBuilder.loadTexts:
    mentisCodsf2939Unit.setStatus("current")
_MentisCodsf2942Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2942Unit = _MentisCodsf2942Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 248)
)
if mibBuilder.loadTexts:
    mentisCodsf2942Unit.setStatus("current")
_MentisCodsf2943Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2943Unit = _MentisCodsf2943Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 249)
)
if mibBuilder.loadTexts:
    mentisCodsf2943Unit.setStatus("current")
_MentisCodsf2946Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2946Unit = _MentisCodsf2946Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 250)
)
if mibBuilder.loadTexts:
    mentisCodsf2946Unit.setStatus("current")
_MentisCodsf2947Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2947Unit = _MentisCodsf2947Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 251)
)
if mibBuilder.loadTexts:
    mentisCodsf2947Unit.setStatus("current")
_MentisCodsf2950Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2950Unit = _MentisCodsf2950Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 252)
)
if mibBuilder.loadTexts:
    mentisCodsf2950Unit.setStatus("current")
_MentisCodsf2951Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2951Unit = _MentisCodsf2951Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 253)
)
if mibBuilder.loadTexts:
    mentisCodsf2951Unit.setStatus("current")
_MentisCodsf2954Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2954Unit = _MentisCodsf2954Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 254)
)
if mibBuilder.loadTexts:
    mentisCodsf2954Unit.setStatus("current")
_MentisCodsf2955Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2955Unit = _MentisCodsf2955Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 255)
)
if mibBuilder.loadTexts:
    mentisCodsf2955Unit.setStatus("current")
_MentisCodsf2958Unit_ObjectIdentity = ObjectIdentity
mentisCodsf2958Unit = _MentisCodsf2958Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 256)
)
if mibBuilder.loadTexts:
    mentisCodsf2958Unit.setStatus("current")
_MentisOadm2chUnit_ObjectIdentity = ObjectIdentity
mentisOadm2chUnit = _MentisOadm2chUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 257)
)
if mibBuilder.loadTexts:
    mentisOadm2chUnit.setStatus("current")
_MentisMxp200gotnUnit_ObjectIdentity = ObjectIdentity
mentisMxp200gotnUnit = _MentisMxp200gotnUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 258)
)
if mibBuilder.loadTexts:
    mentisMxp200gotnUnit.setStatus("current")
_MentisEmxp440Unit_ObjectIdentity = ObjectIdentity
mentisEmxp440Unit = _MentisEmxp440Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 259)
)
if mibBuilder.loadTexts:
    mentisEmxp440Unit.setStatus("current")
_MentisOaraed20lghybUnit_ObjectIdentity = ObjectIdentity
mentisOaraed20lghybUnit = _MentisOaraed20lghybUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 260)
)
if mibBuilder.loadTexts:
    mentisOaraed20lghybUnit.setStatus("current")
_MentisAd1c2fotdrUnit_ObjectIdentity = ObjectIdentity
mentisAd1c2fotdrUnit = _MentisAd1c2fotdrUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 261)
)
if mibBuilder.loadTexts:
    mentisAd1c2fotdrUnit.setStatus("current")
_MentisCodsf243xMPOUnit_ObjectIdentity = ObjectIdentity
mentisCodsf243xMPOUnit = _MentisCodsf243xMPOUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 262)
)
if mibBuilder.loadTexts:
    mentisCodsf243xMPOUnit.setStatus("current")
_MentisOtdr8pUnit_ObjectIdentity = ObjectIdentity
mentisOtdr8pUnit = _MentisOtdr8pUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 263)
)
if mibBuilder.loadTexts:
    mentisOtdr8pUnit.setStatus("current")
_MentisOa1x21dBmVgEC_ObjectIdentity = ObjectIdentity
mentisOa1x21dBmVgEC = _MentisOa1x21dBmVgEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 264)
)
if mibBuilder.loadTexts:
    mentisOa1x21dBmVgEC.setStatus("current")
_MentisOa2x21dBmVgEC_ObjectIdentity = ObjectIdentity
mentisOa2x21dBmVgEC = _MentisOa2x21dBmVgEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 265)
)
if mibBuilder.loadTexts:
    mentisOa2x21dBmVgEC.setStatus("current")
_MentisCo10Unit_ObjectIdentity = ObjectIdentity
mentisCo10Unit = _MentisCo10Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 266)
)
if mibBuilder.loadTexts:
    mentisCo10Unit.setStatus("current")
_MentisCoD48evUnit_ObjectIdentity = ObjectIdentity
mentisCoD48evUnit = _MentisCoD48evUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 267)
)
if mibBuilder.loadTexts:
    mentisCoD48evUnit.setStatus("current")
_EntisCoD48odUnit_ObjectIdentity = ObjectIdentity
entisCoD48odUnit = _EntisCoD48odUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 268)
)
if mibBuilder.loadTexts:
    entisCoD48odUnit.setStatus("current")
_EntisCoOcuD4x4Unit_ObjectIdentity = ObjectIdentity
entisCoOcuD4x4Unit = _EntisCoOcuD4x4Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 269)
)
if mibBuilder.loadTexts:
    entisCoOcuD4x4Unit.setStatus("current")
_EntisCoocuD4x8Unit_ObjectIdentity = ObjectIdentity
entisCoocuD4x8Unit = _EntisCoocuD4x8Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 270)
)
if mibBuilder.loadTexts:
    entisCoocuD4x8Unit.setStatus("current")
_MentisCoOiu50100Unit_ObjectIdentity = ObjectIdentity
mentisCoOiu50100Unit = _MentisCoOiu50100Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 271)
)
if mibBuilder.loadTexts:
    mentisCoOiu50100Unit.setStatus("current")
_MentisCo2xOTDR1611Unit_ObjectIdentity = ObjectIdentity
mentisCo2xOTDR1611Unit = _MentisCo2xOTDR1611Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 272)
)
if mibBuilder.loadTexts:
    mentisCo2xOTDR1611Unit.setStatus("current")
_MentisCoD4919Unit_ObjectIdentity = ObjectIdentity
mentisCoD4919Unit = _MentisCoD4919Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 273)
)
if mibBuilder.loadTexts:
    mentisCoD4919Unit.setStatus("current")
_MentisCoD4923Unit_ObjectIdentity = ObjectIdentity
mentisCoD4923Unit = _MentisCoD4923Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 274)
)
if mibBuilder.loadTexts:
    mentisCoD4923Unit.setStatus("current")
_MentisCoD4927Unit_ObjectIdentity = ObjectIdentity
mentisCoD4927Unit = _MentisCoD4927Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 275)
)
if mibBuilder.loadTexts:
    mentisCoD4927Unit.setStatus("current")
_MentisCoD4931Unit_ObjectIdentity = ObjectIdentity
mentisCoD4931Unit = _MentisCoD4931Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 276)
)
if mibBuilder.loadTexts:
    mentisCoD4931Unit.setStatus("current")
_MentisCoD4935Unit_ObjectIdentity = ObjectIdentity
mentisCoD4935Unit = _MentisCoD4935Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 277)
)
if mibBuilder.loadTexts:
    mentisCoD4935Unit.setStatus("current")
_MentisCoD4939Unit_ObjectIdentity = ObjectIdentity
mentisCoD4939Unit = _MentisCoD4939Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 278)
)
if mibBuilder.loadTexts:
    mentisCoD4939Unit.setStatus("current")
_MentisCoD4943Unit_ObjectIdentity = ObjectIdentity
mentisCoD4943Unit = _MentisCoD4943Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 279)
)
if mibBuilder.loadTexts:
    mentisCoD4943Unit.setStatus("current")
_MentisCoD4947Unit_ObjectIdentity = ObjectIdentity
mentisCoD4947Unit = _MentisCoD4947Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 280)
)
if mibBuilder.loadTexts:
    mentisCoD4947Unit.setStatus("current")
_MentisCoD4951Unit_ObjectIdentity = ObjectIdentity
mentisCoD4951Unit = _MentisCoD4951Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 281)
)
if mibBuilder.loadTexts:
    mentisCoD4951Unit.setStatus("current")
_MentisCoD4955Unit_ObjectIdentity = ObjectIdentity
mentisCoD4955Unit = _MentisCoD4955Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 1, 1, 282)
)
if mibBuilder.loadTexts:
    mentisCoD4955Unit.setStatus("current")
_Mentis300_ObjectIdentity = ObjectIdentity
mentis300 = _Mentis300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 2)
)
if mibBuilder.loadTexts:
    mentis300.setStatus("current")
_Mentis300Backplane_ObjectIdentity = ObjectIdentity
mentis300Backplane = _Mentis300Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mentis300Backplane.setStatus("current")
_Mentis300PowerSlot_ObjectIdentity = ObjectIdentity
mentis300PowerSlot = _Mentis300PowerSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mentis300PowerSlot.setStatus("current")
_Mentis300FanSlot_ObjectIdentity = ObjectIdentity
mentis300FanSlot = _Mentis300FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 2, 3)
)
if mibBuilder.loadTexts:
    mentis300FanSlot.setStatus("current")
_Mentis300PowerSupply_ObjectIdentity = ObjectIdentity
mentis300PowerSupply = _Mentis300PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 2, 4)
)
if mibBuilder.loadTexts:
    mentis300PowerSupply.setStatus("current")
_Mentis300Fan_ObjectIdentity = ObjectIdentity
mentis300Fan = _Mentis300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 2, 5)
)
if mibBuilder.loadTexts:
    mentis300Fan.setStatus("current")
_Mentis3000_ObjectIdentity = ObjectIdentity
mentis3000 = _Mentis3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 3)
)
if mibBuilder.loadTexts:
    mentis3000.setStatus("current")
_Mentis3000Backplane_ObjectIdentity = ObjectIdentity
mentis3000Backplane = _Mentis3000Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mentis3000Backplane.setStatus("current")
_Mentis3000PowerSlot_ObjectIdentity = ObjectIdentity
mentis3000PowerSlot = _Mentis3000PowerSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 3, 2)
)
if mibBuilder.loadTexts:
    mentis3000PowerSlot.setStatus("current")
_Mentis3000FanSlot_ObjectIdentity = ObjectIdentity
mentis3000FanSlot = _Mentis3000FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 3, 3)
)
if mibBuilder.loadTexts:
    mentis3000FanSlot.setStatus("current")
_Mentis3000PowerSupply_ObjectIdentity = ObjectIdentity
mentis3000PowerSupply = _Mentis3000PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 3, 4)
)
if mibBuilder.loadTexts:
    mentis3000PowerSupply.setStatus("current")
_Mentis3000Fan_ObjectIdentity = ObjectIdentity
mentis3000Fan = _Mentis3000Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 3, 5)
)
if mibBuilder.loadTexts:
    mentis3000Fan.setStatus("current")
_Mentis301_ObjectIdentity = ObjectIdentity
mentis301 = _Mentis301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 4)
)
if mibBuilder.loadTexts:
    mentis301.setStatus("current")
_Mentis301Backplane_ObjectIdentity = ObjectIdentity
mentis301Backplane = _Mentis301Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mentis301Backplane.setStatus("current")
_Mentis301PowerSlot_ObjectIdentity = ObjectIdentity
mentis301PowerSlot = _Mentis301PowerSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 4, 2)
)
if mibBuilder.loadTexts:
    mentis301PowerSlot.setStatus("current")
_Mentis301FanSlot_ObjectIdentity = ObjectIdentity
mentis301FanSlot = _Mentis301FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 4, 3)
)
if mibBuilder.loadTexts:
    mentis301FanSlot.setStatus("current")
_Mentis301PowerSupply_ObjectIdentity = ObjectIdentity
mentis301PowerSupply = _Mentis301PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 4, 4)
)
if mibBuilder.loadTexts:
    mentis301PowerSupply.setStatus("current")
_Mentis301Fan_ObjectIdentity = ObjectIdentity
mentis301Fan = _Mentis301Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 4, 5)
)
if mibBuilder.loadTexts:
    mentis301Fan.setStatus("current")
_Mentis101_ObjectIdentity = ObjectIdentity
mentis101 = _Mentis101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 5)
)
if mibBuilder.loadTexts:
    mentis101.setStatus("current")
_Mentis101Backplane_ObjectIdentity = ObjectIdentity
mentis101Backplane = _Mentis101Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mentis101Backplane.setStatus("current")
_Mentis101PowerSlot_ObjectIdentity = ObjectIdentity
mentis101PowerSlot = _Mentis101PowerSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 5, 2)
)
if mibBuilder.loadTexts:
    mentis101PowerSlot.setStatus("current")
_Mentis101FanSlot_ObjectIdentity = ObjectIdentity
mentis101FanSlot = _Mentis101FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 5, 3)
)
if mibBuilder.loadTexts:
    mentis101FanSlot.setStatus("current")
_Mentis101PowerSupply_ObjectIdentity = ObjectIdentity
mentis101PowerSupply = _Mentis101PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 5, 4)
)
if mibBuilder.loadTexts:
    mentis101PowerSupply.setStatus("current")
_Mentis101Fan_ObjectIdentity = ObjectIdentity
mentis101Fan = _Mentis101Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 5, 5)
)
if mibBuilder.loadTexts:
    mentis101Fan.setStatus("current")
_MentisAux_ObjectIdentity = ObjectIdentity
mentisAux = _MentisAux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 6)
)
if mibBuilder.loadTexts:
    mentisAux.setStatus("current")
_MentisAuxBackplane_ObjectIdentity = ObjectIdentity
mentisAuxBackplane = _MentisAuxBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 6, 1)
)
if mibBuilder.loadTexts:
    mentisAuxBackplane.setStatus("current")
_TransmodeNetworkManager_ObjectIdentity = ObjectIdentity
transmodeNetworkManager = _TransmodeNetworkManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 7)
)
if mibBuilder.loadTexts:
    transmodeNetworkManager.setStatus("current")
_Mentis102_ObjectIdentity = ObjectIdentity
mentis102 = _Mentis102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 8)
)
if mibBuilder.loadTexts:
    mentis102.setStatus("current")
_Mentis102Backplane_ObjectIdentity = ObjectIdentity
mentis102Backplane = _Mentis102Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 8, 1)
)
if mibBuilder.loadTexts:
    mentis102Backplane.setStatus("current")
_Mentis102PowerSlot_ObjectIdentity = ObjectIdentity
mentis102PowerSlot = _Mentis102PowerSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 8, 2)
)
if mibBuilder.loadTexts:
    mentis102PowerSlot.setStatus("current")
_Mentis102FanSlot_ObjectIdentity = ObjectIdentity
mentis102FanSlot = _Mentis102FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 8, 3)
)
if mibBuilder.loadTexts:
    mentis102FanSlot.setStatus("current")
_Mentis102PowerSupply_ObjectIdentity = ObjectIdentity
mentis102PowerSupply = _Mentis102PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 8, 4)
)
if mibBuilder.loadTexts:
    mentis102PowerSupply.setStatus("current")
_Mentis102Fan_ObjectIdentity = ObjectIdentity
mentis102Fan = _Mentis102Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 8, 5)
)
if mibBuilder.loadTexts:
    mentis102Fan.setStatus("current")
_MentisMba1_ObjectIdentity = ObjectIdentity
mentisMba1 = _MentisMba1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 9)
)
if mibBuilder.loadTexts:
    mentisMba1.setStatus("current")
_MentisMba2_ObjectIdentity = ObjectIdentity
mentisMba2 = _MentisMba2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 10)
)
if mibBuilder.loadTexts:
    mentisMba2.setStatus("current")
_MentisMba2E_ObjectIdentity = ObjectIdentity
mentisMba2E = _MentisMba2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 11)
)
if mibBuilder.loadTexts:
    mentisMba2E.setStatus("current")
_Mentis102Pas3_ObjectIdentity = ObjectIdentity
mentis102Pas3 = _Mentis102Pas3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 12)
)
if mibBuilder.loadTexts:
    mentis102Pas3.setStatus("current")
_Mentis102Pas3Backplane_ObjectIdentity = ObjectIdentity
mentis102Pas3Backplane = _Mentis102Pas3Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 12, 1)
)
if mibBuilder.loadTexts:
    mentis102Pas3Backplane.setStatus("current")
_Mentis102Pas_ObjectIdentity = ObjectIdentity
mentis102Pas = _Mentis102Pas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 13)
)
if mibBuilder.loadTexts:
    mentis102Pas.setStatus("current")
_Mentis102PasBackplane_ObjectIdentity = ObjectIdentity
mentis102PasBackplane = _Mentis102PasBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 13, 1)
)
if mibBuilder.loadTexts:
    mentis102PasBackplane.setStatus("current")
_Mentis101P_ObjectIdentity = ObjectIdentity
mentis101P = _Mentis101P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 14)
)
if mibBuilder.loadTexts:
    mentis101P.setStatus("current")
_Mentis101PBackplane_ObjectIdentity = ObjectIdentity
mentis101PBackplane = _Mentis101PBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 14, 1)
)
if mibBuilder.loadTexts:
    mentis101PBackplane.setStatus("current")
_Mentis2000_ObjectIdentity = ObjectIdentity
mentis2000 = _Mentis2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 15)
)
if mibBuilder.loadTexts:
    mentis2000.setStatus("current")
_Mentis2000Backplane_ObjectIdentity = ObjectIdentity
mentis2000Backplane = _Mentis2000Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 15, 1)
)
if mibBuilder.loadTexts:
    mentis2000Backplane.setStatus("current")
_Mentis2000PowerSlot_ObjectIdentity = ObjectIdentity
mentis2000PowerSlot = _Mentis2000PowerSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 15, 2)
)
if mibBuilder.loadTexts:
    mentis2000PowerSlot.setStatus("current")
_Mentis2000FanSlot_ObjectIdentity = ObjectIdentity
mentis2000FanSlot = _Mentis2000FanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 15, 3)
)
if mibBuilder.loadTexts:
    mentis2000FanSlot.setStatus("current")
_Mentis2000PowerSupply_ObjectIdentity = ObjectIdentity
mentis2000PowerSupply = _Mentis2000PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 15, 4)
)
if mibBuilder.loadTexts:
    mentis2000PowerSupply.setStatus("current")
_Mentis2000Fan_ObjectIdentity = ObjectIdentity
mentis2000Fan = _Mentis2000Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 15, 5)
)
if mibBuilder.loadTexts:
    mentis2000Fan.setStatus("current")
_MentisFha1u_ObjectIdentity = ObjectIdentity
mentisFha1u = _MentisFha1u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 16)
)
if mibBuilder.loadTexts:
    mentisFha1u.setStatus("current")
_MentisRfuAc1_ObjectIdentity = ObjectIdentity
mentisRfuAc1 = _MentisRfuAc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 3, 17)
)
if mibBuilder.loadTexts:
    mentisRfuAc1.setStatus("current")
_LumCaps_ObjectIdentity = ObjectIdentity
lumCaps = _LumCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 4)
)
if mibBuilder.loadTexts:
    lumCaps.setStatus("current")
_LumReqs_ObjectIdentity = ObjectIdentity
lumReqs = _LumReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 5)
)
if mibBuilder.loadTexts:
    lumReqs.setStatus("current")
_LumExpr_ObjectIdentity = ObjectIdentity
lumExpr = _LumExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 6)
)
if mibBuilder.loadTexts:
    lumExpr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-REG",
    **{"lumentis": lumentis,
       "lumReg": lumReg,
       "lumModules": lumModules,
       "lumRegModule": lumRegModule,
       "lumGeneric": lumGeneric,
       "lumAlarmMIB": lumAlarmMIB,
       "lumSystemMIB": lumSystemMIB,
       "lumInventoryMIB": lumInventoryMIB,
       "lumWdmMIB": lumWdmMIB,
       "lumBackupMIB": lumBackupMIB,
       "lumLambdaMIB": lumLambdaMIB,
       "lumTransponderMIB": lumTransponderMIB,
       "lumTopologyMIB": lumTopologyMIB,
       "lumPowerMIB": lumPowerMIB,
       "lumOxcMIB": lumOxcMIB,
       "lumEquipmentMIB": lumEquipmentMIB,
       "lumMultirateMIB": lumMultirateMIB,
       "lumMuxMIB": lumMuxMIB,
       "lumIpMIB": lumIpMIB,
       "lumPmMIB": lumPmMIB,
       "lumSyncMIB": lumSyncMIB,
       "lumSnmpMIB": lumSnmpMIB,
       "lumEthMIB": lumEthMIB,
       "lumOaMIB": lumOaMIB,
       "lumDcnMIB": lumDcnMIB,
       "lumMemMIB": lumMemMIB,
       "lumFcMIB": lumFcMIB,
       "lumSwuMIB": lumSwuMIB,
       "lumGmplsMIB": lumGmplsMIB,
       "lumGmplsStdMIB": lumGmplsStdMIB,
       "lumConnMIB": lumConnMIB,
       "lumClientMIB": lumClientMIB,
       "lumSoftwareMIB": lumSoftwareMIB,
       "lumAuxMIB": lumAuxMIB,
       "lumCircuitMIB": lumCircuitMIB,
       "lumRoadmMIB": lumRoadmMIB,
       "lumMesMIB": lumMesMIB,
       "lumOcmMIB": lumOcmMIB,
       "lumOtnMIB": lumOtnMIB,
       "lumSdhpdhMIB": lumSdhpdhMIB,
       "lumSatelliteMIB": lumSatelliteMIB,
       "lumMulticastMIB": lumMulticastMIB,
       "lumTrailMIB": lumTrailMIB,
       "lumNcMIB": lumNcMIB,
       "lumMplsMIB": lumMplsMIB,
       "lumPwMIB": lumPwMIB,
       "lumSiteMIB": lumSiteMIB,
       "lumPsrMIB": lumPsrMIB,
       "lumMplsOamMIB": lumMplsOamMIB,
       "lumLinkLossMIB": lumLinkLossMIB,
       "lumIfBasicMIB": lumIfBasicMIB,
       "lumIfPhysicalMIB": lumIfPhysicalMIB,
       "lumIfOpticalMIB": lumIfOpticalMIB,
       "lumPmServerMIB": lumPmServerMIB,
       "lumIfOtnMIB": lumIfOtnMIB,
       "lumIfXcMIB": lumIfXcMIB,
       "lumIfSdhMIB": lumIfSdhMIB,
       "lumIfSonetMIB": lumIfSonetMIB,
       "lumIfEthMIB": lumIfEthMIB,
       "lumIfOtnMonMIB": lumIfOtnMonMIB,
       "lumIfPerfMIB": lumIfPerfMIB,
       "lumPortdeviceMIB": lumPortdeviceMIB,
       "lumPortdeviceIfMIB": lumPortdeviceIfMIB,
       "lumIfFcMIB": lumIfFcMIB,
       "lumSoamPmMIB": lumSoamPmMIB,
       "lumIccpMIB": lumIccpMIB,
       "lumMclagMIB": lumMclagMIB,
       "lumIfIwdmMIB": lumIfIwdmMIB,
       "lumIfMcMIB": lumIfMcMIB,
       "lumIfAmplifierMIB": lumIfAmplifierMIB,
       "lumFpuMIB": lumFpuMIB,
       "lumLldpV2MIB": lumLldpV2MIB,
       "lumIfFhMIB": lumIfFhMIB,
       "lumOpenflowMIB": lumOpenflowMIB,
       "lumIfXcFlexMIB": lumIfXcFlexMIB,
       "lumSysinfoMIB": lumSysinfoMIB,
       "lumIfOtdrMIB": lumIfOtdrMIB,
       "lumCryptoMIB": lumCryptoMIB,
       "lumCommlinkMIB": lumCommlinkMIB,
       "lumAcfMIB": lumAcfMIB,
       "lumProducts": lumProducts,
       "lumProductsGeneric": lumProductsGeneric,
       "mentis": mentis,
       "mentisControlSlot": mentisControlSlot,
       "mentisTrafficSlot": mentisTrafficSlot,
       "mentisControlUnit": mentisControlUnit,
       "mentisMultirate2500TransponderUnit": mentisMultirate2500TransponderUnit,
       "mentisMuxponder028Unit": mentisMuxponder028Unit,
       "mentisOpticalCrossConnect8Unit": mentisOpticalCrossConnect8Unit,
       "mentisOpticalCrossConnect16Unit": mentisOpticalCrossConnect16Unit,
       "mentisSingleAddDropABUnit": mentisSingleAddDropABUnit,
       "mentisSingleAddDropBAUnit": mentisSingleAddDropBAUnit,
       "mentisDualAddDropABUnit": mentisDualAddDropABUnit,
       "mentisDualAddDropBAUnit": mentisDualAddDropBAUnit,
       "mentisDualOpticalCirculationUnit": mentisDualOpticalCirculationUnit,
       "mentis4ChAddDropABUnit": mentis4ChAddDropABUnit,
       "mentis4ChAddDropBAUnit": mentis4ChAddDropBAUnit,
       "mentisDualGbETransponderUnit": mentisDualGbETransponderUnit,
       "mentisOpticalAmplifierUnit": mentisOpticalAmplifierUnit,
       "mentis8chMuxDemuxExtensionUnit": mentis8chMuxDemuxExtensionUnit,
       "mentis8chMuxDemuxTerminalUnit": mentis8chMuxDemuxTerminalUnit,
       "mentisQuadOpticalCouplerUnit": mentisQuadOpticalCouplerUnit,
       "mentisMuxponder004Unit": mentisMuxponder004Unit,
       "mentis2chOpticalAmplifierAddDropABUnit": mentis2chOpticalAmplifierAddDropABUnit,
       "mentis2chOpticalAmplifierAddDropBAUnit": mentis2chOpticalAmplifierAddDropBAUnit,
       "mentisDualOpticalAmplifierUnit": mentisDualOpticalAmplifierUnit,
       "mentisCwdmAddDropUnit": mentisCwdmAddDropUnit,
       "mentisSingleSpurAddDropUnit": mentisSingleSpurAddDropUnit,
       "mentis10GTransponderUnit": mentis10GTransponderUnit,
       "mentisLiteMr2500TransponderUnit": mentisLiteMr2500TransponderUnit,
       "mentisControlOscUnit": mentisControlOscUnit,
       "mentisControlDualOscUnit": mentisControlDualOscUnit,
       "mentisOpticalBandUnit": mentisOpticalBandUnit,
       "mentisSync2MHzUnit": mentisSync2MHzUnit,
       "mentisMxp8Unit": mentisMxp8Unit,
       "mentisMxp16Unit": mentisMxp16Unit,
       "mentisDualGbEDwdmUnit": mentisDualGbEDwdmUnit,
       "mentisDualGbECwdmUnit": mentisDualGbECwdmUnit,
       "mentisDualFiberChannelDwdmUnit": mentisDualFiberChannelDwdmUnit,
       "mentisDualFiberChannelCwdmUnit": mentisDualFiberChannelCwdmUnit,
       "mentisFiberChannelGbEDwdmUnit": mentisFiberChannelGbEDwdmUnit,
       "mentisFiberChannelGbECwdmUnit": mentisFiberChannelGbECwdmUnit,
       "mentisTrippleFiberChannelDwdmUnit": mentisTrippleFiberChannelDwdmUnit,
       "mentisQuadMultirateTransponderUnit": mentisQuadMultirateTransponderUnit,
       "mentis4chMuxDemuxTerminalABUnit": mentis4chMuxDemuxTerminalABUnit,
       "mentis4chMuxDemuxTerminalBAUnit": mentis4chMuxDemuxTerminalBAUnit,
       "mentisSingleCwdmAddDropUnit": mentisSingleCwdmAddDropUnit,
       "mentisDualCwdmAddDropUnit": mentisDualCwdmAddDropUnit,
       "mentis10GLANTransponderUnit": mentis10GLANTransponderUnit,
       "mentis10GRCTransponderUnit": mentis10GRCTransponderUnit,
       "mentisEsconMxp8Unit": mentisEsconMxp8Unit,
       "mentisOpticalAmplifier15dBmUnit": mentisOpticalAmplifier15dBmUnit,
       "mentisDualOpticalAmplifier15dBmUnit": mentisDualOpticalAmplifier15dBmUnit,
       "mentisGxpD2500Unit": mentisGxpD2500Unit,
       "mentisGxpC2500Unit": mentisGxpC2500Unit,
       "mentisGxpD10GUnit": mentisGxpD10GUnit,
       "mentisDualGbEDwdmV2Unit": mentisDualGbEDwdmV2Unit,
       "mentisDualGbECwdmV2Unit": mentisDualGbECwdmV2Unit,
       "mentisDualFiberChannelDwdmV2Unit": mentisDualFiberChannelDwdmV2Unit,
       "mentisDualFiberChannelCwdmV2Unit": mentisDualFiberChannelCwdmV2Unit,
       "mentis2xSingleCwdmAddDropUnit": mentis2xSingleCwdmAddDropUnit,
       "mentis2xDualCwdmAddDropUnit": mentis2xDualCwdmAddDropUnit,
       "mentis8chMuxDemuxTerminal2Unit": mentis8chMuxDemuxTerminal2Unit,
       "mentisDoubleDualGbETransponderUnit": mentisDoubleDualGbETransponderUnit,
       "mentisFpuOas2824Unit": mentisFpuOas2824Unit,
       "mentis2Fiber8chCwdmMuxUnit": mentis2Fiber8chCwdmMuxUnit,
       "mentis2Fiber8chCwdmDemuxUnit": mentis2Fiber8chCwdmDemuxUnit,
       "mentisDouble10GLiteTransponderUnit": mentisDouble10GLiteTransponderUnit,
       "mentis10GBuTransponderUnit": mentis10GBuTransponderUnit,
       "mentis10GLANBuTransponderUnit": mentis10GLANBuTransponderUnit,
       "mentis10GClBuTransponderUnit": mentis10GClBuTransponderUnit,
       "mentis10GLANClBuTransponderUnit": mentis10GLANClBuTransponderUnit,
       "mentis8chMuxDemuxEvenExtensionUnit": mentis8chMuxDemuxEvenExtensionUnit,
       "mentis8chMuxDemuxEvenTerminalUnit": mentis8chMuxDemuxEvenTerminalUnit,
       "mentisOpticalPreAmplifier17dBmUnit": mentisOpticalPreAmplifier17dBmUnit,
       "mentisDualOpticalAmplifier17dBmUnit": mentisDualOpticalAmplifier17dBmUnit,
       "mentisOpticalInterleaverUnit": mentisOpticalInterleaverUnit,
       "mentisOpticalPowAmplifier17dBmUnit": mentisOpticalPowAmplifier17dBmUnit,
       "mentisSingleOpticalAmplifier17dBmUnit": mentisSingleOpticalAmplifier17dBmUnit,
       "mentis9xGbEMuxponderUnit": mentis9xGbEMuxponderUnit,
       "mentis1chAddDropDwdm2FiberUnit": mentis1chAddDropDwdm2FiberUnit,
       "mentis1chAddDropCwdm2FiberUnit": mentis1chAddDropCwdm2FiberUnit,
       "mentisMdu4chExtendable2FiberUnit": mentisMdu4chExtendable2FiberUnit,
       "mentisMdu4chTerminal2FiberUnit": mentisMdu4chTerminal2FiberUnit,
       "mentis8chVoltageControlledAttenuatorUnit": mentis8chVoltageControlledAttenuatorUnit,
       "mentisSingleOpticalAmplifier20dBmUnit": mentisSingleOpticalAmplifier20dBmUnit,
       "mentisDualOpticalAmplifier20dBmUnit": mentisDualOpticalAmplifier20dBmUnit,
       "mentisFpuYm235Unit": mentisFpuYm235Unit,
       "mentis4chAddDropDwdm2FiberUnit": mentis4chAddDropDwdm2FiberUnit,
       "mentisQuadMultirateTransponder2Unit": mentisQuadMultirateTransponder2Unit,
       "mentisRamanOar450CUnit": mentisRamanOar450CUnit,
       "mentisControlSfpUnit": mentisControlSfpUnit,
       "mentisMultirate2500TransponderV2Unit": mentisMultirate2500TransponderV2Unit,
       "mentisDouble10GbeUnit": mentisDouble10GbeUnit,
       "mentis4chMuxDemuxExtensionABUnit": mentis4chMuxDemuxExtensionABUnit,
       "mentis4chMuxDemuxExtensionBAUnit": mentis4chMuxDemuxExtensionBAUnit,
       "mentisOpticalInterleaver50100Unit": mentisOpticalInterleaver50100Unit,
       "mentisReconfigurableOpticalAddDropUnit": mentisReconfigurableOpticalAddDropUnit,
       "mentis6pGbeEthernetDemarcationUnit": mentis6pGbeEthernetDemarcationUnit,
       "mentis10GClTcTransponderUnit": mentis10GClTcTransponderUnit,
       "mentis4xSTM16MuxponderUnit": mentis4xSTM16MuxponderUnit,
       "mentisMroadm1p800Unit": mentisMroadm1p800Unit,
       "mentisSingleOpticalLowGainAmplifier20dBmUnit": mentisSingleOpticalLowGainAmplifier20dBmUnit,
       "mentisDualOpticalLowGainAmplifier20dBmUnit": mentisDualOpticalLowGainAmplifier20dBmUnit,
       "mentisSingleOpticalFlatGainAmplifier10dBmUnit": mentisSingleOpticalFlatGainAmplifier10dBmUnit,
       "mentisDualOpticalFlatGainAmplifier10dBmUnit": mentisDualOpticalFlatGainAmplifier10dBmUnit,
       "mentis10GOtnTcTransponderUnit": mentis10GOtnTcTransponderUnit,
       "mentis40channelMuxDemuxEven50GHzDWDMUnit": mentis40channelMuxDemuxEven50GHzDWDMUnit,
       "mentis40channelMuxDemuxOdd50GHzDWDMUnit": mentis40channelMuxDemuxOdd50GHzDWDMUnit,
       "mentis8channelMuxDemuxExtEvenUnit": mentis8channelMuxDemuxExtEvenUnit,
       "mentis8channelMuxDemuxExtOddUnit": mentis8channelMuxDemuxExtOddUnit,
       "mentis2portOpticalChannelMonitor": mentis2portOpticalChannelMonitor,
       "mentisMultiServiceMuxPonder": mentisMultiServiceMuxPonder,
       "mentis8chVariableOpticalAttenuatorII": mentis8chVariableOpticalAttenuatorII,
       "mentisMultiServiceDoubleQuadGbEMuxPonder": mentisMultiServiceDoubleQuadGbEMuxPonder,
       "mentis10GTcErTransponderUnit": mentis10GTcErTransponderUnit,
       "mentis10xEthernetMuxPonder": mentis10xEthernetMuxPonder,
       "mentis12pGbeEthernetDemarcationUnit": mentis12pGbeEthernetDemarcationUnit,
       "mentisGbeMxp10GFecUnit": mentisGbeMxp10GFecUnit,
       "mentisRoadm1x4G100Unit": mentisRoadm1x4G100Unit,
       "mentisQuadMultiServiceTransponder": mentisQuadMultiServiceTransponder,
       "mentis22xEthernetMuxPonder": mentis22xEthernetMuxPonder,
       "mentisPEOa1x26dBmUnit": mentisPEOa1x26dBmUnit,
       "mentis2PortProtectionControlUnit": mentis2PortProtectionControlUnit,
       "mentis2chVariableOpticalAttenuator": mentis2chVariableOpticalAttenuator,
       "mentisMultiServiceMuxPonder10GTCEr": mentisMultiServiceMuxPonder10GTCEr,
       "mentisMultiServiceMuxPonder10G": mentisMultiServiceMuxPonder10G,
       "mentisMultiServiceQuad2G5Transponder": mentisMultiServiceQuad2G5Transponder,
       "mentis4x2G510GOcMuxponder": mentis4x2G510GOcMuxponder,
       "mentis22xEthernetMuxPonderII": mentis22xEthernetMuxPonderII,
       "mentisBandSplitterUnit1x5Even": mentisBandSplitterUnit1x5Even,
       "mentisBandSplitterUnit1x5Odd": mentisBandSplitterUnit1x5Odd,
       "mentis10xEthernetMuxPonderII": mentis10xEthernetMuxPonderII,
       "mentisMSAccessCollector8xE1T1-2xEth": mentisMSAccessCollector8xE1T1_2xEth,
       "mentisMSAccessCollector16xE1T1-4xEth": mentisMSAccessCollector16xE1T1_4xEth,
       "mentisMSAccessHub4xSTM-1-16xEth": mentisMSAccessHub4xSTM_1_16xEth,
       "mentisMSAccessHub4xOC-3-16xEth": mentisMSAccessHub4xOC_3_16xEth,
       "mentisRoadm1x8G50Unit": mentisRoadm1x8G50Unit,
       "mentis4ChAddDropDwdmEven50G": mentis4ChAddDropDwdmEven50G,
       "mentis4ChAddDropDwdmOdd50G": mentis4ChAddDropDwdmOdd50G,
       "mentis8x10EthernetMuxPonderII": mentis8x10EthernetMuxPonderII,
       "mentisMxp8iiSdhUnit": mentisMxp8iiSdhUnit,
       "mentisMxp8iiSonetUnit": mentisMxp8iiSonetUnit,
       "mentisMSAccessCollector16xE1T1-4xEthTempHardend": mentisMSAccessCollector16xE1T1_4xEthTempHardend,
       "mentisMdu40EvenL": mentisMdu40EvenL,
       "mentisMdu40OddL": mentisMdu40OddL,
       "mentisOa1x20dBmVg": mentisOa1x20dBmVg,
       "mentisOa2x20dBmVg": mentisOa2x20dBmVg,
       "mentisRoadm1x2G100": mentisRoadm1x2G100,
       "mentisRoadm1x2G50": mentisRoadm1x2G50,
       "mentisTpq10GfecUnit": mentisTpq10GfecUnit,
       "mentisControlSfpiiUnit": mentisControlSfpiiUnit,
       "mentisCoD40evUnit": mentisCoD40evUnit,
       "mentisCoD40eveUnit": mentisCoD40eveUnit,
       "mentisCoD40odUnit": mentisCoD40odUnit,
       "mentisCoD40odeUnit": mentisCoD40odeUnit,
       "mentisDcDk652km20Unit": mentisDcDk652km20Unit,
       "mentisDcDk652km40Unit": mentisDcDk652km40Unit,
       "mentisDcDk652km60Unit": mentisDcDk652km60Unit,
       "mentisDcDk652km80Unit": mentisDcDk652km80Unit,
       "mentisDcP652km40Unit": mentisDcP652km40Unit,
       "mentisDcP652km60Unit": mentisDcP652km60Unit,
       "mentisDcP652km80Unit": mentisDcP652km80Unit,
       "mentisDcP652km100Unit": mentisDcP652km100Unit,
       "mentisDcP652km120Unit": mentisDcP652km120Unit,
       "mentisEmxp40GiiUnit": mentisEmxp40GiiUnit,
       "mentisQuadMultiProtocolTransponderUnit": mentisQuadMultiProtocolTransponderUnit,
       "mentisTpq10GfecRegUnit": mentisTpq10GfecRegUnit,
       "mentisColorlessMuxDemuxUnit": mentisColorlessMuxDemuxUnit,
       "mentis8chSfpBasedVoaUnit": mentis8chSfpBasedVoaUnit,
       "mentisMsTp40GUnit": mentisMsTp40GUnit,
       "mentisMsMxp40GUnit": mentisMsMxp40GUnit,
       "mentisMXP10GOTN": mentisMXP10GOTN,
       "mentisOpticalCouplerUnitDualQuad": mentisOpticalCouplerUnitDualQuad,
       "mentisTm4700Unit": mentisTm4700Unit,
       "mentisTm4011Unit": mentisTm4011Unit,
       "mentisTm100MxpUnit": mentisTm100MxpUnit,
       "mentisTm100TpUnit": mentisTm100TpUnit,
       "mentisTm100RegUnit": mentisTm100RegUnit,
       "mentis2PSeedLightCouplerUnit": mentis2PSeedLightCouplerUnit,
       "mentisDual21dBmSeedLightUnit": mentisDual21dBmSeedLightUnit,
       "mentisEmxp62GiieUnit": mentisEmxp62GiieUnit,
       "mentisEmxp120GiieUnit": mentisEmxp120GiieUnit,
       "mentisOYPatchCordUnit": mentisOYPatchCordUnit,
       "mentisTpq10gfeciUnit": mentisTpq10gfeciUnit,
       "mentisTpq10gfecregiUnit": mentisTpq10gfecregiUnit,
       "mentisTphex10gotn": mentisTphex10gotn,
       "mentisEmxp48GiieUnit": mentisEmxp48GiieUnit,
       "mentisTp100gotn": mentisTp100gotn,
       "mentisEmxp220GiieUnit": mentisEmxp220GiieUnit,
       "mentisTpmrHL16GUnit": mentisTpmrHL16GUnit,
       "mentisFronthaulMuxPonder10G": mentisFronthaulMuxPonder10G,
       "mentisMxp100gotn": mentisMxp100gotn,
       "mentisEmxp240GiieUnit": mentisEmxp240GiieUnit,
       "mentisEmxp3Unit": mentisEmxp3Unit,
       "mentisBoardTypeAUnit": mentisBoardTypeAUnit,
       "mentisBoardTypeBUnit": mentisBoardTypeBUnit,
       "mentisFpu1Unit": mentisFpu1Unit,
       "mentisOaraed21hghybUnit": mentisOaraed21hghybUnit,
       "mentisTpmrHL16GUniUnit": mentisTpmrHL16GUniUnit,
       "mentisDcDk652km100Unit": mentisDcDk652km100Unit,
       "mentisDcDk652km120Unit": mentisDcDk652km120Unit,
       "mentisDcP652km20Unit": mentisDcP652km20Unit,
       "mentisFhau1Unit": mentisFhau1Unit,
       "mentisFha1u1Unit": mentisFha1u1Unit,
       "mentisOa1x20dBmVg2Unit": mentisOa1x20dBmVg2Unit,
       "mentisOa2x20dBmVg2Unit": mentisOa2x20dBmVg2Unit,
       "mentisPtio10GUnit": mentisPtio10GUnit,
       "mentisFxp400gotnUnit": mentisFxp400gotnUnit,
       "mentisCompo24Unit": mentisCompo24Unit,
       "mentisTp100gotnii": mentisTp100gotnii,
       "mentisPtio100GUnit": mentisPtio100GUnit,
       "mentisRfu1Unit": mentisRfu1Unit,
       "mentisCoD919926Unit": mentisCoD919926Unit,
       "mentisCoD927934Unit": mentisCoD927934Unit,
       "mentisCoD935942Unit": mentisCoD935942Unit,
       "mentisCoD943950Unit": mentisCoD943950Unit,
       "mentisCoD951958Unit": mentisCoD951958Unit,
       "mentisCoD919926eUnit": mentisCoD919926eUnit,
       "mentisCoD927934eUnit": mentisCoD927934eUnit,
       "mentisCoD935942eUnit": mentisCoD935942eUnit,
       "mentisCoD943950eUnit": mentisCoD943950eUnit,
       "mentisCoD951958eUnit": mentisCoD951958eUnit,
       "mentisCo4Unit": mentisCo4Unit,
       "mentisCo5Unit": mentisCo5Unit,
       "mentisCodsf20evaUnit": mentisCodsf20evaUnit,
       "mentisCodsf20evbUnit": mentisCodsf20evbUnit,
       "mentisCodsf4919Unit": mentisCodsf4919Unit,
       "mentisCodsf4926Unit": mentisCodsf4926Unit,
       "mentisCodsf4927Unit": mentisCodsf4927Unit,
       "mentisCodsf4934Unit": mentisCodsf4934Unit,
       "mentisCodsf4935Unit": mentisCodsf4935Unit,
       "mentisCodsf4942Unit": mentisCodsf4942Unit,
       "mentisCodsf4943Unit": mentisCodsf4943Unit,
       "mentisCodsf4950Unit": mentisCodsf4950Unit,
       "mentisCodsf4951Unit": mentisCodsf4951Unit,
       "mentisCodsf4958Unit": mentisCodsf4958Unit,
       "mentisCodsf2919Unit": mentisCodsf2919Unit,
       "mentisCodsf2922Unit": mentisCodsf2922Unit,
       "mentisCodsf2923Unit": mentisCodsf2923Unit,
       "mentisCodsf2926Unit": mentisCodsf2926Unit,
       "mentisCodsf2927Unit": mentisCodsf2927Unit,
       "mentisCodsf2930Unit": mentisCodsf2930Unit,
       "mentisCodsf2931Unit": mentisCodsf2931Unit,
       "mentisCodsf2934Unit": mentisCodsf2934Unit,
       "mentisCodsf2935Unit": mentisCodsf2935Unit,
       "mentisCodsf2938Unit": mentisCodsf2938Unit,
       "mentisCodsf2939Unit": mentisCodsf2939Unit,
       "mentisCodsf2942Unit": mentisCodsf2942Unit,
       "mentisCodsf2943Unit": mentisCodsf2943Unit,
       "mentisCodsf2946Unit": mentisCodsf2946Unit,
       "mentisCodsf2947Unit": mentisCodsf2947Unit,
       "mentisCodsf2950Unit": mentisCodsf2950Unit,
       "mentisCodsf2951Unit": mentisCodsf2951Unit,
       "mentisCodsf2954Unit": mentisCodsf2954Unit,
       "mentisCodsf2955Unit": mentisCodsf2955Unit,
       "mentisCodsf2958Unit": mentisCodsf2958Unit,
       "mentisOadm2chUnit": mentisOadm2chUnit,
       "mentisMxp200gotnUnit": mentisMxp200gotnUnit,
       "mentisEmxp440Unit": mentisEmxp440Unit,
       "mentisOaraed20lghybUnit": mentisOaraed20lghybUnit,
       "mentisAd1c2fotdrUnit": mentisAd1c2fotdrUnit,
       "mentisCodsf243xMPOUnit": mentisCodsf243xMPOUnit,
       "mentisOtdr8pUnit": mentisOtdr8pUnit,
       "mentisOa1x21dBmVgEC": mentisOa1x21dBmVgEC,
       "mentisOa2x21dBmVgEC": mentisOa2x21dBmVgEC,
       "mentisCo10Unit": mentisCo10Unit,
       "mentisCoD48evUnit": mentisCoD48evUnit,
       "entisCoD48odUnit": entisCoD48odUnit,
       "entisCoOcuD4x4Unit": entisCoOcuD4x4Unit,
       "entisCoocuD4x8Unit": entisCoocuD4x8Unit,
       "mentisCoOiu50100Unit": mentisCoOiu50100Unit,
       "mentisCo2xOTDR1611Unit": mentisCo2xOTDR1611Unit,
       "mentisCoD4919Unit": mentisCoD4919Unit,
       "mentisCoD4923Unit": mentisCoD4923Unit,
       "mentisCoD4927Unit": mentisCoD4927Unit,
       "mentisCoD4931Unit": mentisCoD4931Unit,
       "mentisCoD4935Unit": mentisCoD4935Unit,
       "mentisCoD4939Unit": mentisCoD4939Unit,
       "mentisCoD4943Unit": mentisCoD4943Unit,
       "mentisCoD4947Unit": mentisCoD4947Unit,
       "mentisCoD4951Unit": mentisCoD4951Unit,
       "mentisCoD4955Unit": mentisCoD4955Unit,
       "mentis300": mentis300,
       "mentis300Backplane": mentis300Backplane,
       "mentis300PowerSlot": mentis300PowerSlot,
       "mentis300FanSlot": mentis300FanSlot,
       "mentis300PowerSupply": mentis300PowerSupply,
       "mentis300Fan": mentis300Fan,
       "mentis3000": mentis3000,
       "mentis3000Backplane": mentis3000Backplane,
       "mentis3000PowerSlot": mentis3000PowerSlot,
       "mentis3000FanSlot": mentis3000FanSlot,
       "mentis3000PowerSupply": mentis3000PowerSupply,
       "mentis3000Fan": mentis3000Fan,
       "mentis301": mentis301,
       "mentis301Backplane": mentis301Backplane,
       "mentis301PowerSlot": mentis301PowerSlot,
       "mentis301FanSlot": mentis301FanSlot,
       "mentis301PowerSupply": mentis301PowerSupply,
       "mentis301Fan": mentis301Fan,
       "mentis101": mentis101,
       "mentis101Backplane": mentis101Backplane,
       "mentis101PowerSlot": mentis101PowerSlot,
       "mentis101FanSlot": mentis101FanSlot,
       "mentis101PowerSupply": mentis101PowerSupply,
       "mentis101Fan": mentis101Fan,
       "mentisAux": mentisAux,
       "mentisAuxBackplane": mentisAuxBackplane,
       "transmodeNetworkManager": transmodeNetworkManager,
       "mentis102": mentis102,
       "mentis102Backplane": mentis102Backplane,
       "mentis102PowerSlot": mentis102PowerSlot,
       "mentis102FanSlot": mentis102FanSlot,
       "mentis102PowerSupply": mentis102PowerSupply,
       "mentis102Fan": mentis102Fan,
       "mentisMba1": mentisMba1,
       "mentisMba2": mentisMba2,
       "mentisMba2E": mentisMba2E,
       "mentis102Pas3": mentis102Pas3,
       "mentis102Pas3Backplane": mentis102Pas3Backplane,
       "mentis102Pas": mentis102Pas,
       "mentis102PasBackplane": mentis102PasBackplane,
       "mentis101P": mentis101P,
       "mentis101PBackplane": mentis101PBackplane,
       "mentis2000": mentis2000,
       "mentis2000Backplane": mentis2000Backplane,
       "mentis2000PowerSlot": mentis2000PowerSlot,
       "mentis2000FanSlot": mentis2000FanSlot,
       "mentis2000PowerSupply": mentis2000PowerSupply,
       "mentis2000Fan": mentis2000Fan,
       "mentisFha1u": mentisFha1u,
       "mentisRfuAc1": mentisRfuAc1,
       "lumCaps": lumCaps,
       "lumReqs": lumReqs,
       "lumExpr": lumExpr}
)
