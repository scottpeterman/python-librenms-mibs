# SNMP MIB module (FORTINET-CORE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-CORE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:44 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

fortinet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356)
)
if mibBuilder.loadTexts:
    fortinet.setRevisions(
        ("2024-02-29 00:00",
         "2023-10-16 00:00",
         "2023-09-21 00:00",
         "2023-08-28 00:00",
         "2021-11-15 00:00",
         "2020-01-30 00:00",
         "2018-12-05 00:00",
         "2018-11-05 00:00",
         "2016-09-30 00:00",
         "2016-05-24 00:00",
         "2015-01-14 00:00",
         "2014-12-10 00:00",
         "2014-04-10 00:00",
         "2014-03-22 00:00",
         "2012-05-09 00:00",
         "2012-04-23 00:00",
         "2011-12-23 00:00",
         "2011-04-25 00:00",
         "2010-05-14 00:00",
         "2009-05-20 00:00",
         "2008-11-19 00:00",
         "2008-10-21 00:00",
         "2008-06-25 00:00",
         "2008-06-16 00:00",
         "2008-04-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FnBoolState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class FnLanguage(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("english", 1),
          ("simplifiedChinese", 2),
          ("japanese", 3),
          ("korean", 4),
          ("spanish", 5),
          ("traditionalChinese", 6),
          ("french", 7),
          ("portuguese", 8),
          ("undefined", 255))
    )



class FnIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class FnSessionProto(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              12,
              17,
              22,
              41,
              46,
              47,
              50,
              51,
              89,
              103,
              108,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ipip", 4),
          ("tcp", 6),
          ("egp", 8),
          ("pup", 12),
          ("udp", 17),
          ("idp", 22),
          ("ipv6", 41),
          ("rsvp", 46),
          ("gre", 47),
          ("esp", 50),
          ("ah", 51),
          ("ospf", 89),
          ("pim", 103),
          ("comp", 108),
          ("raw", 255))
    )



# MIB Managed Objects in the order of their OIDs

_FnCoreMib_ObjectIdentity = ObjectIdentity
fnCoreMib = _FnCoreMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 100)
)
_FnCommon_ObjectIdentity = ObjectIdentity
fnCommon = _FnCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1)
)
_FnSystem_ObjectIdentity = ObjectIdentity
fnSystem = _FnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 1)
)
_FnSysSerial_Type = DisplayString
_FnSysSerial_Object = MibScalar
fnSysSerial = _FnSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 1, 1),
    _FnSysSerial_Type()
)
fnSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSerial.setStatus("current")
_FnMgmt_ObjectIdentity = ObjectIdentity
fnMgmt = _FnMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2)
)
_FnMgmtLanguage_Type = FnLanguage
_FnMgmtLanguage_Object = MibScalar
fnMgmtLanguage = _FnMgmtLanguage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 1),
    _FnMgmtLanguage_Type()
)
fnMgmtLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnMgmtLanguage.setStatus("current")
_FnAdmin_ObjectIdentity = ObjectIdentity
fnAdmin = _FnAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100)
)
_FnAdminNumber_Type = Integer32
_FnAdminNumber_Object = MibScalar
fnAdminNumber = _FnAdminNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 1),
    _FnAdminNumber_Type()
)
fnAdminNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminNumber.setStatus("current")
_FnAdminTable_Object = MibTable
fnAdminTable = _FnAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2)
)
if mibBuilder.loadTexts:
    fnAdminTable.setStatus("current")
_FnAdminEntry_Object = MibTableRow
fnAdminEntry = _FnAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1)
)
fnAdminEntry.setIndexNames(
    (0, "FORTINET-CORE-MIB", "fnAdminIndex"),
)
if mibBuilder.loadTexts:
    fnAdminEntry.setStatus("current")


class _FnAdminIndex_Type(Integer32):
    """Custom type fnAdminIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FnAdminIndex_Type.__name__ = "Integer32"
_FnAdminIndex_Object = MibTableColumn
fnAdminIndex = _FnAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 1),
    _FnAdminIndex_Type()
)
fnAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAdminIndex.setStatus("current")
_FnAdminName_Type = DisplayString
_FnAdminName_Object = MibTableColumn
fnAdminName = _FnAdminName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 2),
    _FnAdminName_Type()
)
fnAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminName.setStatus("current")
_FnAdminAddrType_Type = InetAddressType
_FnAdminAddrType_Object = MibTableColumn
fnAdminAddrType = _FnAdminAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 3),
    _FnAdminAddrType_Type()
)
fnAdminAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminAddrType.setStatus("current")
_FnAdminAddr_Type = InetAddress
_FnAdminAddr_Object = MibTableColumn
fnAdminAddr = _FnAdminAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 4),
    _FnAdminAddr_Type()
)
fnAdminAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminAddr.setStatus("current")
_FnAdminMask_Type = InetAddressPrefixLength
_FnAdminMask_Object = MibTableColumn
fnAdminMask = _FnAdminMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 5),
    _FnAdminMask_Type()
)
fnAdminMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminMask.setStatus("current")
_FnTraps_ObjectIdentity = ObjectIdentity
fnTraps = _FnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3)
)
_FnTrapsPrefix_ObjectIdentity = ObjectIdentity
fnTrapsPrefix = _FnTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0)
)
_FnTrapObjects_ObjectIdentity = ObjectIdentity
fnTrapObjects = _FnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 1)
)
_FnGenTrapMsg_Type = DisplayString
_FnGenTrapMsg_Object = MibScalar
fnGenTrapMsg = _FnGenTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 1, 1),
    _FnGenTrapMsg_Type()
)
fnGenTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnGenTrapMsg.setStatus("current")
_FnMIBConformance_ObjectIdentity = ObjectIdentity
fnMIBConformance = _FnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 100, 10)
)

# Managed Objects groups

fnSystemComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 100, 10, 1)
)
fnSystemComplianceGroup.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnSystemComplianceGroup.setStatus("current")

fnMgmtComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 100, 10, 2)
)
fnMgmtComplianceGroup.setObjects(
    ("FORTINET-CORE-MIB", "fnMgmtLanguage")
)
if mibBuilder.loadTexts:
    fnMgmtComplianceGroup.setStatus("current")

fnAdminComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 100, 10, 3)
)
fnAdminComplianceGroup.setObjects(
      *(("FORTINET-CORE-MIB", "fnAdminNumber"),
        ("FORTINET-CORE-MIB", "fnAdminName"),
        ("FORTINET-CORE-MIB", "fnAdminAddrType"),
        ("FORTINET-CORE-MIB", "fnAdminAddr"),
        ("FORTINET-CORE-MIB", "fnAdminMask"))
)
if mibBuilder.loadTexts:
    fnAdminComplianceGroup.setStatus("current")

fnNotifObjectsComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 100, 10, 5)
)
fnNotifObjectsComplianceGroup.setObjects(
    ("FORTINET-CORE-MIB", "fnGenTrapMsg")
)
if mibBuilder.loadTexts:
    fnNotifObjectsComplianceGroup.setStatus("current")


# Notification objects

fnTrapCpuThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 101)
)
fnTrapCpuThreshold.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapCpuThreshold.setStatus(
        "current"
    )

fnTrapMemThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 102)
)
fnTrapMemThreshold.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    fnTrapMemThreshold.setStatus(
        "current"
    )

fnTrapLogDiskThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 103)
)
fnTrapLogDiskThreshold.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapLogDiskThreshold.setStatus(
        "current"
    )

fnTrapTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 104)
)
fnTrapTempHigh.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapTempHigh.setStatus(
        "current"
    )

fnTrapVoltageOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 105)
)
fnTrapVoltageOutOfRange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapVoltageOutOfRange.setStatus(
        "current"
    )

fnTrapPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 106)
)
fnTrapPowerSupply.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    fnTrapPowerSupply.setStatus(
        "current"
    )

fnTrapAmcIfBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 107)
)
fnTrapAmcIfBypassMode.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapAmcIfBypassMode.setStatus(
        "current"
    )

fnTrapFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 108)
)
fnTrapFanFailure.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapFanFailure.setStatus(
        "current"
    )

fnTrapIfEnterBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 109)
)
fnTrapIfEnterBypassMode.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapIfEnterBypassMode.setStatus(
        "current"
    )

fnTrapIfExitBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 110)
)
fnTrapIfExitBypassMode.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapIfExitBypassMode.setStatus(
        "current"
    )

fnTrapSecurityLevelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 111)
)
fnTrapSecurityLevelChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    fnTrapSecurityLevelChange.setStatus(
        "current"
    )

fnTrapIpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 201)
)
fnTrapIpChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    fnTrapIpChange.setStatus(
        "current"
    )

fnTrapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 999)
)
fnTrapTest.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapTest.setStatus(
        "current"
    )


# Notifications groups

fnTrapsComplianceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 100, 10, 4)
)
fnTrapsComplianceGroup.setObjects(
      *(("FORTINET-CORE-MIB", "fnTrapCpuThreshold"),
        ("FORTINET-CORE-MIB", "fnTrapMemThreshold"),
        ("FORTINET-CORE-MIB", "fnTrapLogDiskThreshold"),
        ("FORTINET-CORE-MIB", "fnTrapTempHigh"),
        ("FORTINET-CORE-MIB", "fnTrapVoltageOutOfRange"),
        ("FORTINET-CORE-MIB", "fnTrapPowerSupply"),
        ("FORTINET-CORE-MIB", "fnTrapAmcIfBypassMode"),
        ("FORTINET-CORE-MIB", "fnTrapIfEnterBypassMode"),
        ("FORTINET-CORE-MIB", "fnTrapIfExitBypassMode"),
        ("FORTINET-CORE-MIB", "fnTrapFanFailure"),
        ("FORTINET-CORE-MIB", "fnTrapSecurityLevelChange"),
        ("FORTINET-CORE-MIB", "fnTrapIpChange"),
        ("FORTINET-CORE-MIB", "fnTrapTest"))
)
if mibBuilder.loadTexts:
    fnTrapsComplianceGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 100, 10, 100)
)
fnMIBCompliance.setObjects(
      *(("FORTINET-CORE-MIB", "fnSystemComplianceGroup"),
        ("FORTINET-CORE-MIB", "fnMgmtComplianceGroup"),
        ("FORTINET-CORE-MIB", "fnAdminComplianceGroup"),
        ("FORTINET-CORE-MIB", "fnTrapsComplianceGroup"),
        ("FORTINET-CORE-MIB", "fnNotifObjectsComplianceGroup"))
)
if mibBuilder.loadTexts:
    fnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-CORE-MIB",
    **{"FnBoolState": FnBoolState,
       "FnLanguage": FnLanguage,
       "FnIndex": FnIndex,
       "FnSessionProto": FnSessionProto,
       "fortinet": fortinet,
       "fnCoreMib": fnCoreMib,
       "fnCommon": fnCommon,
       "fnSystem": fnSystem,
       "fnSysSerial": fnSysSerial,
       "fnMgmt": fnMgmt,
       "fnMgmtLanguage": fnMgmtLanguage,
       "fnAdmin": fnAdmin,
       "fnAdminNumber": fnAdminNumber,
       "fnAdminTable": fnAdminTable,
       "fnAdminEntry": fnAdminEntry,
       "fnAdminIndex": fnAdminIndex,
       "fnAdminName": fnAdminName,
       "fnAdminAddrType": fnAdminAddrType,
       "fnAdminAddr": fnAdminAddr,
       "fnAdminMask": fnAdminMask,
       "fnTraps": fnTraps,
       "fnTrapsPrefix": fnTrapsPrefix,
       "fnTrapCpuThreshold": fnTrapCpuThreshold,
       "fnTrapMemThreshold": fnTrapMemThreshold,
       "fnTrapLogDiskThreshold": fnTrapLogDiskThreshold,
       "fnTrapTempHigh": fnTrapTempHigh,
       "fnTrapVoltageOutOfRange": fnTrapVoltageOutOfRange,
       "fnTrapPowerSupply": fnTrapPowerSupply,
       "fnTrapAmcIfBypassMode": fnTrapAmcIfBypassMode,
       "fnTrapFanFailure": fnTrapFanFailure,
       "fnTrapIfEnterBypassMode": fnTrapIfEnterBypassMode,
       "fnTrapIfExitBypassMode": fnTrapIfExitBypassMode,
       "fnTrapSecurityLevelChange": fnTrapSecurityLevelChange,
       "fnTrapIpChange": fnTrapIpChange,
       "fnTrapTest": fnTrapTest,
       "fnTrapObjects": fnTrapObjects,
       "fnGenTrapMsg": fnGenTrapMsg,
       "fnMIBConformance": fnMIBConformance,
       "fnSystemComplianceGroup": fnSystemComplianceGroup,
       "fnMgmtComplianceGroup": fnMgmtComplianceGroup,
       "fnAdminComplianceGroup": fnAdminComplianceGroup,
       "fnTrapsComplianceGroup": fnTrapsComplianceGroup,
       "fnNotifObjectsComplianceGroup": fnNotifObjectsComplianceGroup,
       "fnMIBCompliance": fnMIBCompliance}
)
