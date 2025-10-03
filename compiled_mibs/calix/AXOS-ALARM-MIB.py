# SNMP MIB module (AXOS-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\AXOS-ALARM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:44 2025
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

(axosModules,) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "axosModules")

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

axosAlarmModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    axosAlarmModule.setRevisions(
        ("2016-04-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxosAlarm_ObjectIdentity = ObjectIdentity
axosAlarm = _AxosAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1)
)
_AxosActiveAlarms_ObjectIdentity = ObjectIdentity
axosActiveAlarms = _AxosActiveAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1)
)
_AxosAlarmTable_Object = MibTable
axosAlarmTable = _AxosAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    axosAlarmTable.setStatus("current")
_AxosAlarmEntry_Object = MibTableRow
axosAlarmEntry = _AxosAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1)
)
axosAlarmEntry.setIndexNames(
    (0, "AXOS-ALARM-MIB", "axosIndex"),
)
if mibBuilder.loadTexts:
    axosAlarmEntry.setStatus("current")


class _AxosAlarmIndex_Type(Integer32):
    """Custom type axosAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AxosAlarmIndex_Type.__name__ = "Integer32"
_AxosAlarmIndex_Object = MibTableColumn
axosAlarmIndex = _AxosAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 1),
    _AxosAlarmIndex_Type()
)
axosAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmIndex.setStatus("current")
_AxosAlarmName_Type = DisplayString
_AxosAlarmName_Object = MibTableColumn
axosAlarmName = _AxosAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 2),
    _AxosAlarmName_Type()
)
axosAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmName.setStatus("current")


class _AxosAlarmType_Type(Integer32):
    """Custom type axosAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("communication", 0),
          ("qos", 1),
          ("processing-error", 2),
          ("equipment", 3),
          ("environmental", 4),
          ("operational-violation", 5),
          ("integrity-violation", 6),
          ("informational", 7))
    )


_AxosAlarmType_Type.__name__ = "Integer32"
_AxosAlarmType_Object = MibTableColumn
axosAlarmType = _AxosAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 3),
    _AxosAlarmType_Type()
)
axosAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmType.setStatus("current")


class _AxosAlarmCategory_Type(Integer32):
    """Custom type axosAlarmCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("general", 0),
          ("security", 1),
          ("dbchange", 2),
          ("qos", 3),
          ("environmental", 4),
          ("tca", 5),
          ("ntp", 6),
          ("oam", 7),
          ("erps", 8),
          ("g8032", 9),
          ("rstp", 10),
          ("port", 11),
          ("lag", 12),
          ("lacp", 13),
          ("arc", 14),
          ("dhcp", 15),
          ("ntwkclk", 16),
          ("pm", 17),
          ("configuration", 18),
          ("isis", 19),
          ("ospf", 20),
          ("bgp", 21),
          ("pon", 22),
          ("bondedgroup", 23),
          ("cardimgmgmt", 24),
          ("ontimgmgmt", 25),
          ("slot", 26),
          ("subscriber", 27),
          ("mpls", 28),
          ("l2vpn", 29),
          ("aeont", 30),
          ("bfd", 31),
          ("vrrp", 32),
          ("pim", 33),
          ("connection", 34),
          ("mfib", 35))
    )


_AxosAlarmCategory_Type.__name__ = "Integer32"
_AxosAlarmCategory_Object = MibTableColumn
axosAlarmCategory = _AxosAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 4),
    _AxosAlarmCategory_Type()
)
axosAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmCategory.setStatus("current")
_AxosAlarmInstanceId_Type = DisplayString
_AxosAlarmInstanceId_Object = MibTableColumn
axosAlarmInstanceId = _AxosAlarmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 5),
    _AxosAlarmInstanceId_Type()
)
axosAlarmInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmInstanceId.setStatus("current")


class _AxosAlarmSeverity_Type(Integer32):
    """Custom type axosAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("warning", 3),
          ("unknown", 4),
          ("info", 5),
          ("clear", 6),
          ("none", 7))
    )


_AxosAlarmSeverity_Type.__name__ = "Integer32"
_AxosAlarmSeverity_Object = MibTableColumn
axosAlarmSeverity = _AxosAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 6),
    _AxosAlarmSeverity_Type()
)
axosAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmSeverity.setStatus("current")


class _AxosAlarmServiceAffecting_Type(Integer32):
    """Custom type axosAlarmServiceAffecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AxosAlarmServiceAffecting_Type.__name__ = "Integer32"
_AxosAlarmServiceAffecting_Object = MibTableColumn
axosAlarmServiceAffecting = _AxosAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 7),
    _AxosAlarmServiceAffecting_Type()
)
axosAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmServiceAffecting.setStatus("current")
_AxosAlarmAddress_Type = DisplayString
_AxosAlarmAddress_Object = MibTableColumn
axosAlarmAddress = _AxosAlarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 8),
    _AxosAlarmAddress_Type()
)
axosAlarmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmAddress.setStatus("current")
_AxosAlarmText_Type = DisplayString
_AxosAlarmText_Object = MibTableColumn
axosAlarmText = _AxosAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 9),
    _AxosAlarmText_Type()
)
axosAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmText.setStatus("current")


class _AxosAlarmTimeStamp_Type(DisplayString):
    """Custom type axosAlarmTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AxosAlarmTimeStamp_Type.__name__ = "DisplayString"
_AxosAlarmTimeStamp_Object = MibTableColumn
axosAlarmTimeStamp = _AxosAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 10),
    _AxosAlarmTimeStamp_Type()
)
axosAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmTimeStamp.setStatus("current")
_AxosAlarmTime_Type = Integer32
_AxosAlarmTime_Object = MibTableColumn
axosAlarmTime = _AxosAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 11),
    _AxosAlarmTime_Type()
)
axosAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmTime.setStatus("current")
_AxosAlarmAdditionalInfo_Type = DisplayString
_AxosAlarmAdditionalInfo_Object = MibTableColumn
axosAlarmAdditionalInfo = _AxosAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 12),
    _AxosAlarmAdditionalInfo_Type()
)
axosAlarmAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmAdditionalInfo.setStatus("current")
_AxosIndex_Type = Integer32
_AxosIndex_Object = MibTableColumn
axosIndex = _AxosIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 1, 1, 13),
    _AxosIndex_Type()
)
axosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosIndex.setStatus("current")
_AxosAlarmCount_ObjectIdentity = ObjectIdentity
axosAlarmCount = _AxosAlarmCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 2)
)
_AxosAlarmCountTotal_Type = Integer32
_AxosAlarmCountTotal_Object = MibScalar
axosAlarmCountTotal = _AxosAlarmCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 2, 1),
    _AxosAlarmCountTotal_Type()
)
axosAlarmCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmCountTotal.setStatus("current")
_AxosAlarmCountCritical_Type = Integer32
_AxosAlarmCountCritical_Object = MibScalar
axosAlarmCountCritical = _AxosAlarmCountCritical_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 2, 2),
    _AxosAlarmCountCritical_Type()
)
axosAlarmCountCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmCountCritical.setStatus("current")
_AxosAlarmCountMajor_Type = Integer32
_AxosAlarmCountMajor_Object = MibScalar
axosAlarmCountMajor = _AxosAlarmCountMajor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 2, 3),
    _AxosAlarmCountMajor_Type()
)
axosAlarmCountMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmCountMajor.setStatus("current")
_AxosAlarmCountMinor_Type = Integer32
_AxosAlarmCountMinor_Object = MibScalar
axosAlarmCountMinor = _AxosAlarmCountMinor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 2, 4),
    _AxosAlarmCountMinor_Type()
)
axosAlarmCountMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmCountMinor.setStatus("current")
_AxosAlarmCountWarning_Type = Integer32
_AxosAlarmCountWarning_Object = MibScalar
axosAlarmCountWarning = _AxosAlarmCountWarning_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 2, 5),
    _AxosAlarmCountWarning_Type()
)
axosAlarmCountWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmCountWarning.setStatus("current")
_AxosAlarmCountInfo_Type = Integer32
_AxosAlarmCountInfo_Object = MibScalar
axosAlarmCountInfo = _AxosAlarmCountInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 1, 2, 6),
    _AxosAlarmCountInfo_Type()
)
axosAlarmCountInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosAlarmCountInfo.setStatus("current")
_AxosEventAttributes_ObjectIdentity = ObjectIdentity
axosEventAttributes = _AxosEventAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 3)
)
_AxosEventAdditionalInfo1_Type = DisplayString
_AxosEventAdditionalInfo1_Object = MibScalar
axosEventAdditionalInfo1 = _AxosEventAdditionalInfo1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 3, 1),
    _AxosEventAdditionalInfo1_Type()
)
axosEventAdditionalInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosEventAdditionalInfo1.setStatus("current")
_AxosEventAdditionalInfo2_Type = DisplayString
_AxosEventAdditionalInfo2_Object = MibScalar
axosEventAdditionalInfo2 = _AxosEventAdditionalInfo2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 3, 2),
    _AxosEventAdditionalInfo2_Type()
)
axosEventAdditionalInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosEventAdditionalInfo2.setStatus("current")
_AxosEventAdditionalInfo3_Type = DisplayString
_AxosEventAdditionalInfo3_Object = MibScalar
axosEventAdditionalInfo3 = _AxosEventAdditionalInfo3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 3, 3),
    _AxosEventAdditionalInfo3_Type()
)
axosEventAdditionalInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosEventAdditionalInfo3.setStatus("current")
_AxosEventAdditionalInfo4_Type = DisplayString
_AxosEventAdditionalInfo4_Object = MibScalar
axosEventAdditionalInfo4 = _AxosEventAdditionalInfo4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 3, 4),
    _AxosEventAdditionalInfo4_Type()
)
axosEventAdditionalInfo4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosEventAdditionalInfo4.setStatus("current")
_AxosEventAdditionalInfo5_Type = DisplayString
_AxosEventAdditionalInfo5_Object = MibScalar
axosEventAdditionalInfo5 = _AxosEventAdditionalInfo5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 3, 5),
    _AxosEventAdditionalInfo5_Type()
)
axosEventAdditionalInfo5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosEventAdditionalInfo5.setStatus("current")
_AxosEventAdditionalInfo6_Type = DisplayString
_AxosEventAdditionalInfo6_Object = MibScalar
axosEventAdditionalInfo6 = _AxosEventAdditionalInfo6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 3, 6),
    _AxosEventAdditionalInfo6_Type()
)
axosEventAdditionalInfo6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosEventAdditionalInfo6.setStatus("current")
_AxosEventAdditionalInfo7_Type = DisplayString
_AxosEventAdditionalInfo7_Object = MibScalar
axosEventAdditionalInfo7 = _AxosEventAdditionalInfo7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 2, 1, 3, 7),
    _AxosEventAdditionalInfo7_Type()
)
axosEventAdditionalInfo7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosEventAdditionalInfo7.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AXOS-ALARM-MIB",
    **{"axosAlarmModule": axosAlarmModule,
       "axosAlarm": axosAlarm,
       "axosActiveAlarms": axosActiveAlarms,
       "axosAlarmTable": axosAlarmTable,
       "axosAlarmEntry": axosAlarmEntry,
       "axosAlarmIndex": axosAlarmIndex,
       "axosAlarmName": axosAlarmName,
       "axosAlarmType": axosAlarmType,
       "axosAlarmCategory": axosAlarmCategory,
       "axosAlarmInstanceId": axosAlarmInstanceId,
       "axosAlarmSeverity": axosAlarmSeverity,
       "axosAlarmServiceAffecting": axosAlarmServiceAffecting,
       "axosAlarmAddress": axosAlarmAddress,
       "axosAlarmText": axosAlarmText,
       "axosAlarmTimeStamp": axosAlarmTimeStamp,
       "axosAlarmTime": axosAlarmTime,
       "axosAlarmAdditionalInfo": axosAlarmAdditionalInfo,
       "axosIndex": axosIndex,
       "axosAlarmCount": axosAlarmCount,
       "axosAlarmCountTotal": axosAlarmCountTotal,
       "axosAlarmCountCritical": axosAlarmCountCritical,
       "axosAlarmCountMajor": axosAlarmCountMajor,
       "axosAlarmCountMinor": axosAlarmCountMinor,
       "axosAlarmCountWarning": axosAlarmCountWarning,
       "axosAlarmCountInfo": axosAlarmCountInfo,
       "axosEventAttributes": axosEventAttributes,
       "axosEventAdditionalInfo1": axosEventAdditionalInfo1,
       "axosEventAdditionalInfo2": axosEventAdditionalInfo2,
       "axosEventAdditionalInfo3": axosEventAdditionalInfo3,
       "axosEventAdditionalInfo4": axosEventAdditionalInfo4,
       "axosEventAdditionalInfo5": axosEventAdditionalInfo5,
       "axosEventAdditionalInfo6": axosEventAdditionalInfo6,
       "axosEventAdditionalInfo7": axosEventAdditionalInfo7}
)
