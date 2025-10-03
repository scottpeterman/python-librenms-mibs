# SNMP MIB module (ANUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ixia\ANUE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:09 2025
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

(CounterBasedGauge64,
 ZeroBasedCounter64,
 hcnumTC) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64",
    "ZeroBasedCounter64",
    "hcnumTC")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifEntry,
 ifIndex,
 ifTable) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifEntry",
    "ifIndex",
    "ifTable")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpSecurityModel,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpSecurityModel")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(SnmpUDPAddress,
 snmpUDPDomain) = mibBuilder.importSymbols(
    "SNMPv2-TM",
    "SnmpUDPAddress",
    "snmpUDPDomain")


# MODULE-IDENTITY

anueMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32620)
)
if mibBuilder.loadTexts:
    anueMIB.setRevisions(
        ("2015-06-12 17:00",
         "2015-01-29 17:00",
         "2015-01-27 17:00",
         "2014-12-17 17:00",
         "2014-06-26 17:00",
         "2014-03-13 17:00",
         "2014-03-11 17:00",
         "2014-03-05 17:00",
         "2013-09-05 17:00",
         "2014-03-04 17:00",
         "2012-07-30 17:00",
         "2012-06-13 17:00",
         "2012-03-27 17:00",
         "2012-02-06 17:00",
         "2011-09-20 17:00",
         "2010-10-13 19:08")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AnueStageType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("anueStageTypeNPFilter", 0),
          ("anueStageTypeTPFilter", 1),
          ("anueStageTypeAfmDrop", 2),
          ("anueStageTypeAfmStripGtp", 3),
          ("anueStageTypeAfmStripMpls", 4),
          ("anueStageTypeAfmDedup", 5),
          ("anueStageTypeAfmTrim", 6),
          ("anueStageTypeAfmBurstBuffer", 7),
          ("anueStageTypeNPError", 8),
          ("anueStageTypeStripVlan", 9),
          ("anueStageTypeAfmStripVntag", 10),
          ("anueStageTypeAfmTimestamping", 11),
          ("anueStageTypeAfmStripTrailer", 12),
          ("anueStageTypePortTagging", 13),
          ("anueStageTypeLCInput", 15),
          ("anueStageTypeLCOutput", 16),
          ("anueStageTypeAfmGtpFd", 17),
          ("anueStageTypeAfmStripFabricPath", 18),
          ("anueStageTypeAfmStripVxlan", 19),
          ("anueStageTypeAfmStripL2Gre", 20),
          ("anueStageTypeAfmStripErspan", 21),
          ("anueStageTypeAfmPacketLength", 22),
          ("anueStageTypeAfmDataMasking", 23),
          ("anueStageTypeGscBufOverflow", 32),
          ("anueStageTypeGscNetworkPorts", 33),
          ("anueStageTypeGscSessionToolPorts", 34))
    )


class AnueFilterTypeDT(TextualConvention, Integer32):
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
              100,
              101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("anueFilterTypeNetworkPort", 1),
          ("anueFilterTypeToolPort", 2),
          ("anueFilterTypeDynamic", 3),
          ("anueFilterTypeNetworkPortGroup", 4),
          ("anueFilterTypeToolPortGroup", 5),
          ("anueFilterTypeLineCard", 6),
          ("anueFilterTypeRecAfmResource", 7),
          ("anueFilterTypeGscNetworkPort", 100),
          ("anueFilterTypeGscSessionToolPort", 101),
          ("anueFilterTypeGscNetworkPortGroup", 102),
          ("anueFilterTypeGscSessionToolPortGroup", 103))
    )



class AnueThresholdCrossing(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("thresholdCrossingUpward", 1),
          ("thresholdCrossingDownward", 2))
    )



class AnueNtoUnionMemberActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("memberActionJoinSucceeded", 1),
          ("memberActionJoinFailed", 2),
          ("memberActionLeaveSucceeded", 3),
          ("memberActionLeaveFailed", 4),
          ("memberActionReconnected", 5))
    )



class AnueTimeSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("anueTimeSourceTypeLocal", 1),
          ("anueTimeSourceTypeNTP", 2),
          ("anueTimeSourceTypeGPS", 3),
          ("anueTimeSourceTypeNA", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AnueObjects_ObjectIdentity = ObjectIdentity
anueObjects = _AnueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1)
)
_AnueNtoObjects_ObjectIdentity = ObjectIdentity
anueNtoObjects = _AnueNtoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1)
)
_AnueNtoSystem_ObjectIdentity = ObjectIdentity
anueNtoSystem = _AnueNtoSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1)
)
_AnueNtoLastSnmpAuthnFailure_ObjectIdentity = ObjectIdentity
anueNtoLastSnmpAuthnFailure = _AnueNtoLastSnmpAuthnFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 1)
)
_AnueSnmpAuthnFailureTime_Type = DateAndTime
_AnueSnmpAuthnFailureTime_Object = MibScalar
anueSnmpAuthnFailureTime = _AnueSnmpAuthnFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 1, 1),
    _AnueSnmpAuthnFailureTime_Type()
)
anueSnmpAuthnFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueSnmpAuthnFailureTime.setStatus("current")
_AnueSnmpAuthnFailureUsername_Type = DisplayString
_AnueSnmpAuthnFailureUsername_Object = MibScalar
anueSnmpAuthnFailureUsername = _AnueSnmpAuthnFailureUsername_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 1, 2),
    _AnueSnmpAuthnFailureUsername_Type()
)
anueSnmpAuthnFailureUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueSnmpAuthnFailureUsername.setStatus("current")
_AnueSnmpAuthnFailureSrcIpType_Type = InetAddressType
_AnueSnmpAuthnFailureSrcIpType_Object = MibScalar
anueSnmpAuthnFailureSrcIpType = _AnueSnmpAuthnFailureSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 1, 3),
    _AnueSnmpAuthnFailureSrcIpType_Type()
)
anueSnmpAuthnFailureSrcIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueSnmpAuthnFailureSrcIpType.setStatus("current")
_AnueSnmpAuthnFailureSrcIp_Type = InetAddress
_AnueSnmpAuthnFailureSrcIp_Object = MibScalar
anueSnmpAuthnFailureSrcIp = _AnueSnmpAuthnFailureSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 1, 4),
    _AnueSnmpAuthnFailureSrcIp_Type()
)
anueSnmpAuthnFailureSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueSnmpAuthnFailureSrcIp.setStatus("current")
_AnueSnmpAuthnFailureSecModel_Type = SnmpSecurityModel
_AnueSnmpAuthnFailureSecModel_Object = MibScalar
anueSnmpAuthnFailureSecModel = _AnueSnmpAuthnFailureSecModel_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 1, 5),
    _AnueSnmpAuthnFailureSecModel_Type()
)
anueSnmpAuthnFailureSecModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueSnmpAuthnFailureSecModel.setStatus("current")
_AnueNtoLastClientLoginFailure_ObjectIdentity = ObjectIdentity
anueNtoLastClientLoginFailure = _AnueNtoLastClientLoginFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 2)
)
_AnueClientLoginFailureTime_Type = DateAndTime
_AnueClientLoginFailureTime_Object = MibScalar
anueClientLoginFailureTime = _AnueClientLoginFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 2, 1),
    _AnueClientLoginFailureTime_Type()
)
anueClientLoginFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueClientLoginFailureTime.setStatus("current")
_AnueClientLoginFailureId_Type = DisplayString
_AnueClientLoginFailureId_Object = MibScalar
anueClientLoginFailureId = _AnueClientLoginFailureId_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 2, 2),
    _AnueClientLoginFailureId_Type()
)
anueClientLoginFailureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueClientLoginFailureId.setStatus("current")
_AnueClientLoginFailureSrcIpType_Type = InetAddressType
_AnueClientLoginFailureSrcIpType_Object = MibScalar
anueClientLoginFailureSrcIpType = _AnueClientLoginFailureSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 2, 3),
    _AnueClientLoginFailureSrcIpType_Type()
)
anueClientLoginFailureSrcIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueClientLoginFailureSrcIpType.setStatus("current")
_AnueClientLoginFailureSrcIp_Type = InetAddress
_AnueClientLoginFailureSrcIp_Object = MibScalar
anueClientLoginFailureSrcIp = _AnueClientLoginFailureSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 2, 4),
    _AnueClientLoginFailureSrcIp_Type()
)
anueClientLoginFailureSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueClientLoginFailureSrcIp.setStatus("current")
_AnueClientLoginFailureReason_Type = DisplayString
_AnueClientLoginFailureReason_Object = MibScalar
anueClientLoginFailureReason = _AnueClientLoginFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 2, 5),
    _AnueClientLoginFailureReason_Type()
)
anueClientLoginFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueClientLoginFailureReason.setStatus("current")
_AnueSnmpAuthnFailureTrapEnable_Type = TruthValue
_AnueSnmpAuthnFailureTrapEnable_Object = MibScalar
anueSnmpAuthnFailureTrapEnable = _AnueSnmpAuthnFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 3),
    _AnueSnmpAuthnFailureTrapEnable_Type()
)
anueSnmpAuthnFailureTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueSnmpAuthnFailureTrapEnable.setStatus("current")
_AnueClientLoginFailureTrapEnable_Type = TruthValue
_AnueClientLoginFailureTrapEnable_Object = MibScalar
anueClientLoginFailureTrapEnable = _AnueClientLoginFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 4),
    _AnueClientLoginFailureTrapEnable_Type()
)
anueClientLoginFailureTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueClientLoginFailureTrapEnable.setStatus("current")
_AnueLoginBanner_Type = DisplayString
_AnueLoginBanner_Object = MibScalar
anueLoginBanner = _AnueLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 5),
    _AnueLoginBanner_Type()
)
anueLoginBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueLoginBanner.setStatus("current")
_AnueTimestampingTimeSource_Type = AnueTimeSourceType
_AnueTimestampingTimeSource_Object = MibScalar
anueTimestampingTimeSource = _AnueTimestampingTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 6),
    _AnueTimestampingTimeSource_Type()
)
anueTimestampingTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueTimestampingTimeSource.setStatus("current")
_AnueTimestampingStatus_Type = DisplayString
_AnueTimestampingStatus_Object = MibScalar
anueTimestampingStatus = _AnueTimestampingStatus_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 7),
    _AnueTimestampingStatus_Type()
)
anueTimestampingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueTimestampingStatus.setStatus("current")
_AnueNtoCustomFilterSetConfig_ObjectIdentity = ObjectIdentity
anueNtoCustomFilterSetConfig = _AnueNtoCustomFilterSetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8)
)


class _AnueCustomFieldSetEnableState_Type(Integer32):
    """Custom type anueCustomFieldSetEnableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bothFieldSetsDisabled", 1),
          ("fieldSet1Enabled", 2),
          ("bothFieldSetsEnabledDiffFilters", 3),
          ("bothFieldSetsEnabledSameFilters", 4),
          ("notAvailable", 5))
    )


_AnueCustomFieldSetEnableState_Type.__name__ = "Integer32"
_AnueCustomFieldSetEnableState_Object = MibScalar
anueCustomFieldSetEnableState = _AnueCustomFieldSetEnableState_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 1),
    _AnueCustomFieldSetEnableState_Type()
)
anueCustomFieldSetEnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCustomFieldSetEnableState.setStatus("current")
_AnueCustomFieldSetsTable_Object = MibTable
anueCustomFieldSetsTable = _AnueCustomFieldSetsTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    anueCustomFieldSetsTable.setStatus("current")
_AnueCustomFieldSetsEntry_Object = MibTableRow
anueCustomFieldSetsEntry = _AnueCustomFieldSetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 2, 1)
)
anueCustomFieldSetsEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFieldSetId"),
)
if mibBuilder.loadTexts:
    anueCustomFieldSetsEntry.setStatus("current")


class _AnueFieldSetId_Type(Integer32):
    """Custom type anueFieldSetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueFieldSetId_Type.__name__ = "Integer32"
_AnueFieldSetId_Object = MibTableColumn
anueFieldSetId = _AnueFieldSetId_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 2, 1, 1),
    _AnueFieldSetId_Type()
)
anueFieldSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFieldSetId.setStatus("current")
_AnueFieldSetAvailOuterHdrFlds_Type = DisplayString
_AnueFieldSetAvailOuterHdrFlds_Object = MibTableColumn
anueFieldSetAvailOuterHdrFlds = _AnueFieldSetAvailOuterHdrFlds_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 2, 1, 2),
    _AnueFieldSetAvailOuterHdrFlds_Type()
)
anueFieldSetAvailOuterHdrFlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFieldSetAvailOuterHdrFlds.setStatus("current")
_AnueFieldSetIsAdditOuterHdrs_Type = TruthValue
_AnueFieldSetIsAdditOuterHdrs_Object = MibTableColumn
anueFieldSetIsAdditOuterHdrs = _AnueFieldSetIsAdditOuterHdrs_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 2, 1, 3),
    _AnueFieldSetIsAdditOuterHdrs_Type()
)
anueFieldSetIsAdditOuterHdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFieldSetIsAdditOuterHdrs.setStatus("current")
_AnueCustomFieldsTable_Object = MibTable
anueCustomFieldsTable = _AnueCustomFieldsTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    anueCustomFieldsTable.setStatus("current")
_AnueCustomFieldsEntry_Object = MibTableRow
anueCustomFieldsEntry = _AnueCustomFieldsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 3, 1)
)
anueCustomFieldsEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFieldSetId"),
    (0, "ANUE-MIB", "anueCustomFieldId"),
)
if mibBuilder.loadTexts:
    anueCustomFieldsEntry.setStatus("current")


class _AnueCustomFieldId_Type(Integer32):
    """Custom type anueCustomFieldId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueCustomFieldId_Type.__name__ = "Integer32"
_AnueCustomFieldId_Object = MibTableColumn
anueCustomFieldId = _AnueCustomFieldId_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 3, 1, 1),
    _AnueCustomFieldId_Type()
)
anueCustomFieldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCustomFieldId.setStatus("current")


class _AnueCustomFieldPktType_Type(Integer32):
    """Custom type anueCustomFieldPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("raw", 1),
          ("gtpU", 2),
          ("gtpC", 3),
          ("mpls", 4))
    )


_AnueCustomFieldPktType_Type.__name__ = "Integer32"
_AnueCustomFieldPktType_Object = MibTableColumn
anueCustomFieldPktType = _AnueCustomFieldPktType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 3, 1, 2),
    _AnueCustomFieldPktType_Type()
)
anueCustomFieldPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCustomFieldPktType.setStatus("current")
_AnueCustomFieldSize_Type = Integer32
_AnueCustomFieldSize_Object = MibTableColumn
anueCustomFieldSize = _AnueCustomFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 3, 1, 3),
    _AnueCustomFieldSize_Type()
)
anueCustomFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCustomFieldSize.setStatus("current")
_AnueCustomFieldName_Type = DisplayString
_AnueCustomFieldName_Object = MibTableColumn
anueCustomFieldName = _AnueCustomFieldName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 3, 1, 4),
    _AnueCustomFieldName_Type()
)
anueCustomFieldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCustomFieldName.setStatus("current")
_AnueCustomFieldSpecificAttrList_Type = DisplayString
_AnueCustomFieldSpecificAttrList_Object = MibTableColumn
anueCustomFieldSpecificAttrList = _AnueCustomFieldSpecificAttrList_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 3, 1, 5),
    _AnueCustomFieldSpecificAttrList_Type()
)
anueCustomFieldSpecificAttrList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCustomFieldSpecificAttrList.setStatus("current")
_AnueCustomFieldConfirmFldsList_Type = DisplayString
_AnueCustomFieldConfirmFldsList_Object = MibTableColumn
anueCustomFieldConfirmFldsList = _AnueCustomFieldConfirmFldsList_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 1, 8, 3, 1, 6),
    _AnueCustomFieldConfirmFldsList_Type()
)
anueCustomFieldConfirmFldsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCustomFieldConfirmFldsList.setStatus("current")
_AnueNtoIfExt_ObjectIdentity = ObjectIdentity
anueNtoIfExt = _AnueNtoIfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 2)
)
_AnueNtoIfExtTable_Object = MibTable
anueNtoIfExtTable = _AnueNtoIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    anueNtoIfExtTable.setStatus("current")
_AnueNtoIfExtEntry_Object = MibTableRow
anueNtoIfExtEntry = _AnueNtoIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 2, 1, 1)
)
anueNtoIfExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    anueNtoIfExtEntry.setStatus("current")
_AnueIfIsLicensed_Type = TruthValue
_AnueIfIsLicensed_Object = MibTableColumn
anueIfIsLicensed = _AnueIfIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 2, 1, 1, 2),
    _AnueIfIsLicensed_Type()
)
anueIfIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueIfIsLicensed.setStatus("current")
_AnueIfLicensedMaxSpeed_Type = Gauge32
_AnueIfLicensedMaxSpeed_Object = MibTableColumn
anueIfLicensedMaxSpeed = _AnueIfLicensedMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 2, 1, 1, 3),
    _AnueIfLicensedMaxSpeed_Type()
)
anueIfLicensedMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueIfLicensedMaxSpeed.setStatus("current")


class _AnueIfMode_Type(Integer32):
    """Custom type anueIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("anueIfModeUnknown", 1),
          ("anueIfModeNetwork", 2),
          ("anueIfModeTool", 3),
          ("anueIfModeBidirectional", 4),
          ("anueIfModeSimplex", 5),
          ("anueIfModeLoopback", 6))
    )


_AnueIfMode_Type.__name__ = "Integer32"
_AnueIfMode_Object = MibTableColumn
anueIfMode = _AnueIfMode_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 2, 1, 1, 4),
    _AnueIfMode_Type()
)
anueIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueIfMode.setStatus("current")
_AnueIfDesc_Type = DisplayString
_AnueIfDesc_Object = MibTableColumn
anueIfDesc = _AnueIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 2, 1, 1, 5),
    _AnueIfDesc_Type()
)
anueIfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueIfDesc.setStatus("current")
_AnueIfOnAfm_Type = TruthValue
_AnueIfOnAfm_Object = MibTableColumn
anueIfOnAfm = _AnueIfOnAfm_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 2, 1, 1, 6),
    _AnueIfOnAfm_Type()
)
anueIfOnAfm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueIfOnAfm.setStatus("current")
_AnueIfAdvCapabilities_Type = AnueStageType
_AnueIfAdvCapabilities_Object = MibTableColumn
anueIfAdvCapabilities = _AnueIfAdvCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 2, 1, 1, 7),
    _AnueIfAdvCapabilities_Type()
)
anueIfAdvCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueIfAdvCapabilities.setStatus("current")
_AnueNtoFilter_ObjectIdentity = ObjectIdentity
anueNtoFilter = _AnueNtoFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3)
)
_AnueFilterCollectionPeriod_Type = Gauge32
_AnueFilterCollectionPeriod_Object = MibScalar
anueFilterCollectionPeriod = _AnueFilterCollectionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 1),
    _AnueFilterCollectionPeriod_Type()
)
anueFilterCollectionPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCollectionPeriod.setStatus("current")
_AnueNtoFilterDefTable_Object = MibTable
anueNtoFilterDefTable = _AnueNtoFilterDefTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    anueNtoFilterDefTable.setStatus("current")
_AnueNtoFilterDefEntry_Object = MibTableRow
anueNtoFilterDefEntry = _AnueNtoFilterDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1)
)
anueNtoFilterDefEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterDefEntry.setStatus("current")
_AnueFilterType_Type = AnueFilterTypeDT
_AnueFilterType_Object = MibTableColumn
anueFilterType = _AnueFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 1),
    _AnueFilterType_Type()
)
anueFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterType.setStatus("current")


class _AnueFilterNumber_Type(Integer32):
    """Custom type anueFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueFilterNumber_Type.__name__ = "Integer32"
_AnueFilterNumber_Object = MibTableColumn
anueFilterNumber = _AnueFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 2),
    _AnueFilterNumber_Type()
)
anueFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterNumber.setStatus("current")
_AnueFilterDefaultName_Type = DisplayString
_AnueFilterDefaultName_Object = MibTableColumn
anueFilterDefaultName = _AnueFilterDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 3),
    _AnueFilterDefaultName_Type()
)
anueFilterDefaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterDefaultName.setStatus("current")
_AnueFilterName_Type = DisplayString
_AnueFilterName_Object = MibTableColumn
anueFilterName = _AnueFilterName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 4),
    _AnueFilterName_Type()
)
anueFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterName.setStatus("current")
_AnueFilterDesc_Type = DisplayString
_AnueFilterDesc_Object = MibTableColumn
anueFilterDesc = _AnueFilterDesc_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 5),
    _AnueFilterDesc_Type()
)
anueFilterDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterDesc.setStatus("current")
_AnueFilterIfIndex_Type = Integer32
_AnueFilterIfIndex_Object = MibTableColumn
anueFilterIfIndex = _AnueFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 6),
    _AnueFilterIfIndex_Type()
)
anueFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterIfIndex.setStatus("current")


class _AnueFilterIsTwoStage_Type(Integer32):
    """Custom type anueFilterIsTwoStage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anueFilterIsOneStage", 1),
          ("anueFilterIsTwoStage", 2),
          ("anueFilterNA", 3))
    )


_AnueFilterIsTwoStage_Type.__name__ = "Integer32"
_AnueFilterIsTwoStage_Object = MibTableColumn
anueFilterIsTwoStage = _AnueFilterIsTwoStage_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 7),
    _AnueFilterIsTwoStage_Type()
)
anueFilterIsTwoStage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterIsTwoStage.setStatus("current")


class _AnueFilterMode_Type(Integer32):
    """Custom type anueFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("anueFilterModePassAll", 1),
          ("anueFilterModePassByCriteria", 2),
          ("anueFilterModeDenyAll", 3),
          ("anueFilterModeDenyByCriteria", 4),
          ("anueFilterModePassByCriteriaUnmatched", 5),
          ("anueFilterModeDenyByCriteriaMatched", 6))
    )


_AnueFilterMode_Type.__name__ = "Integer32"
_AnueFilterMode_Object = MibTableColumn
anueFilterMode = _AnueFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 8),
    _AnueFilterMode_Type()
)
anueFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterMode.setStatus("current")
_AnueFilterCriteria_Type = DisplayString
_AnueFilterCriteria_Object = MibTableColumn
anueFilterCriteria = _AnueFilterCriteria_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 9),
    _AnueFilterCriteria_Type()
)
anueFilterCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCriteria.setStatus("current")
_AnueFilterTag_Type = DisplayString
_AnueFilterTag_Object = MibTableColumn
anueFilterTag = _AnueFilterTag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 10),
    _AnueFilterTag_Type()
)
anueFilterTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterTag.setStatus("current")


class _AnueFilterAfmEnabled_Type(TruthValue):
    """Custom type anueFilterAfmEnabled based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AnueFilterAfmEnabled_Type.__name__ = "TruthValue"
_AnueFilterAfmEnabled_Object = MibTableColumn
anueFilterAfmEnabled = _AnueFilterAfmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 11),
    _AnueFilterAfmEnabled_Type()
)
anueFilterAfmEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAfmEnabled.setStatus("current")
_AnueFilterEnabledFeatures_Type = AnueStageType
_AnueFilterEnabledFeatures_Object = MibTableColumn
anueFilterEnabledFeatures = _AnueFilterEnabledFeatures_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 12),
    _AnueFilterEnabledFeatures_Type()
)
anueFilterEnabledFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterEnabledFeatures.setStatus("current")
_AnueFilterCustomFieldSets_Type = DisplayString
_AnueFilterCustomFieldSets_Object = MibTableColumn
anueFilterCustomFieldSets = _AnueFilterCustomFieldSets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 2, 1, 13),
    _AnueFilterCustomFieldSets_Type()
)
anueFilterCustomFieldSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCustomFieldSets.setStatus("current")
_AnueNtoFilterConnTable_Object = MibTable
anueNtoFilterConnTable = _AnueNtoFilterConnTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    anueNtoFilterConnTable.setStatus("current")
_AnueNtoFilterConnEntry_Object = MibTableRow
anueNtoFilterConnEntry = _AnueNtoFilterConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 3, 1)
)
anueNtoFilterConnEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterConnFromOid"),
    (0, "ANUE-MIB", "anueFilterConnToOid"),
)
if mibBuilder.loadTexts:
    anueNtoFilterConnEntry.setStatus("current")
_AnueFilterConnFromOid_Type = ObjectIdentifier
_AnueFilterConnFromOid_Object = MibTableColumn
anueFilterConnFromOid = _AnueFilterConnFromOid_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 3, 1, 1),
    _AnueFilterConnFromOid_Type()
)
anueFilterConnFromOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterConnFromOid.setStatus("current")
_AnueFilterConnToOid_Type = ObjectIdentifier
_AnueFilterConnToOid_Object = MibTableColumn
anueFilterConnToOid = _AnueFilterConnToOid_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 3, 1, 2),
    _AnueFilterConnToOid_Type()
)
anueFilterConnToOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterConnToOid.setStatus("current")
_AnueNtoFilterHistTable_Object = MibTable
anueNtoFilterHistTable = _AnueNtoFilterHistTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    anueNtoFilterHistTable.setStatus("current")
_AnueNtoFilterHistEntry_Object = MibTableRow
anueNtoFilterHistEntry = _AnueNtoFilterHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1)
)
anueNtoFilterHistEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterHistEntry.setStatus("current")
_AnueFilterCreatedTime_Type = DateAndTime
_AnueFilterCreatedTime_Object = MibTableColumn
anueFilterCreatedTime = _AnueFilterCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 3),
    _AnueFilterCreatedTime_Type()
)
anueFilterCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCreatedTime.setStatus("current")
_AnueFilterCreatedBy_Type = DisplayString
_AnueFilterCreatedBy_Object = MibTableColumn
anueFilterCreatedBy = _AnueFilterCreatedBy_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 4),
    _AnueFilterCreatedBy_Type()
)
anueFilterCreatedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCreatedBy.setStatus("current")
_AnueFilterCriteriaModTime_Type = DateAndTime
_AnueFilterCriteriaModTime_Object = MibTableColumn
anueFilterCriteriaModTime = _AnueFilterCriteriaModTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 5),
    _AnueFilterCriteriaModTime_Type()
)
anueFilterCriteriaModTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCriteriaModTime.setStatus("current")
_AnueFilterCriteriaModTimeStamp_Type = TimeStamp
_AnueFilterCriteriaModTimeStamp_Object = MibTableColumn
anueFilterCriteriaModTimeStamp = _AnueFilterCriteriaModTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 6),
    _AnueFilterCriteriaModTimeStamp_Type()
)
anueFilterCriteriaModTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCriteriaModTimeStamp.setStatus("current")
_AnueFilterCriteriaModBy_Type = DisplayString
_AnueFilterCriteriaModBy_Object = MibTableColumn
anueFilterCriteriaModBy = _AnueFilterCriteriaModBy_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 7),
    _AnueFilterCriteriaModBy_Type()
)
anueFilterCriteriaModBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCriteriaModBy.setStatus("current")
_AnueFilterConfigModTime_Type = DateAndTime
_AnueFilterConfigModTime_Object = MibTableColumn
anueFilterConfigModTime = _AnueFilterConfigModTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 8),
    _AnueFilterConfigModTime_Type()
)
anueFilterConfigModTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterConfigModTime.setStatus("current")
_AnueFilterConfigModBy_Type = DisplayString
_AnueFilterConfigModBy_Object = MibTableColumn
anueFilterConfigModBy = _AnueFilterConfigModBy_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 9),
    _AnueFilterConfigModBy_Type()
)
anueFilterConfigModBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterConfigModBy.setStatus("current")
_AnueFilterConfigModFields_Type = DisplayString
_AnueFilterConfigModFields_Object = MibTableColumn
anueFilterConfigModFields = _AnueFilterConfigModFields_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 10),
    _AnueFilterConfigModFields_Type()
)
anueFilterConfigModFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterConfigModFields.setStatus("current")
_AnueFilterStatsResetTime_Type = DateAndTime
_AnueFilterStatsResetTime_Object = MibTableColumn
anueFilterStatsResetTime = _AnueFilterStatsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 11),
    _AnueFilterStatsResetTime_Type()
)
anueFilterStatsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterStatsResetTime.setStatus("current")
_AnueFilterStatsResetBy_Type = DisplayString
_AnueFilterStatsResetBy_Object = MibTableColumn
anueFilterStatsResetBy = _AnueFilterStatsResetBy_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 12),
    _AnueFilterStatsResetBy_Type()
)
anueFilterStatsResetBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterStatsResetBy.setStatus("current")
_AnueFilterDropResetTime_Type = DateAndTime
_AnueFilterDropResetTime_Object = MibTableColumn
anueFilterDropResetTime = _AnueFilterDropResetTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 13),
    _AnueFilterDropResetTime_Type()
)
anueFilterDropResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterDropResetTime.setStatus("current")
_AnueFilterDropResetBy_Type = DisplayString
_AnueFilterDropResetBy_Object = MibTableColumn
anueFilterDropResetBy = _AnueFilterDropResetBy_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 4, 1, 14),
    _AnueFilterDropResetBy_Type()
)
anueFilterDropResetBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterDropResetBy.setStatus("current")
_AnueNtoFilterStatsCntModHCTable_Object = MibTable
anueNtoFilterStatsCntModHCTable = _AnueNtoFilterStatsCntModHCTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCntModHCTable.setStatus("current")
_AnueNtoFilterStatsCntModHCEntry_Object = MibTableRow
anueNtoFilterStatsCntModHCEntry = _AnueNtoFilterStatsCntModHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 5, 1)
)
anueNtoFilterStatsCntModHCEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCntModHCEntry.setStatus("current")
_AnueFilterCntModHCInOctets_Type = Counter64
_AnueFilterCntModHCInOctets_Object = MibTableColumn
anueFilterCntModHCInOctets = _AnueFilterCntModHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 5, 1, 3),
    _AnueFilterCntModHCInOctets_Type()
)
anueFilterCntModHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModHCInOctets.setStatus("current")
_AnueFilterCntModHCOutOctets_Type = Counter64
_AnueFilterCntModHCOutOctets_Object = MibTableColumn
anueFilterCntModHCOutOctets = _AnueFilterCntModHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 5, 1, 4),
    _AnueFilterCntModHCOutOctets_Type()
)
anueFilterCntModHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModHCOutOctets.setStatus("current")
_AnueFilterCntModHCInPkts_Type = Counter64
_AnueFilterCntModHCInPkts_Object = MibTableColumn
anueFilterCntModHCInPkts = _AnueFilterCntModHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 5, 1, 5),
    _AnueFilterCntModHCInPkts_Type()
)
anueFilterCntModHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModHCInPkts.setStatus("current")
_AnueFilterCntModHCOutPkts_Type = Counter64
_AnueFilterCntModHCOutPkts_Object = MibTableColumn
anueFilterCntModHCOutPkts = _AnueFilterCntModHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 5, 1, 6),
    _AnueFilterCntModHCOutPkts_Type()
)
anueFilterCntModHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModHCOutPkts.setStatus("current")
_AnueFilterCntModHCDropPkts_Type = Counter64
_AnueFilterCntModHCDropPkts_Object = MibTableColumn
anueFilterCntModHCDropPkts = _AnueFilterCntModHCDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 5, 1, 7),
    _AnueFilterCntModHCDropPkts_Type()
)
anueFilterCntModHCDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModHCDropPkts.setStatus("current")
_AnueFilterCntModHCDropTime_Type = DateAndTime
_AnueFilterCntModHCDropTime_Object = MibTableColumn
anueFilterCntModHCDropTime = _AnueFilterCntModHCDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 5, 1, 8),
    _AnueFilterCntModHCDropTime_Type()
)
anueFilterCntModHCDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModHCDropTime.setStatus("current")
_AnueNtoFilterStatsCntRstHCTable_Object = MibTable
anueNtoFilterStatsCntRstHCTable = _AnueNtoFilterStatsCntRstHCTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCntRstHCTable.setStatus("current")
_AnueNtoFilterStatsCntRstHCEntry_Object = MibTableRow
anueNtoFilterStatsCntRstHCEntry = _AnueNtoFilterStatsCntRstHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 6, 1)
)
anueNtoFilterStatsCntRstHCEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCntRstHCEntry.setStatus("current")
_AnueFilterCntRstHCInOctets_Type = Counter64
_AnueFilterCntRstHCInOctets_Object = MibTableColumn
anueFilterCntRstHCInOctets = _AnueFilterCntRstHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 6, 1, 3),
    _AnueFilterCntRstHCInOctets_Type()
)
anueFilterCntRstHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstHCInOctets.setStatus("current")
_AnueFilterCntRstHCOutOctets_Type = Counter64
_AnueFilterCntRstHCOutOctets_Object = MibTableColumn
anueFilterCntRstHCOutOctets = _AnueFilterCntRstHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 6, 1, 4),
    _AnueFilterCntRstHCOutOctets_Type()
)
anueFilterCntRstHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstHCOutOctets.setStatus("current")
_AnueFilterCntRstHCInPkts_Type = Counter64
_AnueFilterCntRstHCInPkts_Object = MibTableColumn
anueFilterCntRstHCInPkts = _AnueFilterCntRstHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 6, 1, 5),
    _AnueFilterCntRstHCInPkts_Type()
)
anueFilterCntRstHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstHCInPkts.setStatus("current")
_AnueFilterCntRstHCOutPkts_Type = Counter64
_AnueFilterCntRstHCOutPkts_Object = MibTableColumn
anueFilterCntRstHCOutPkts = _AnueFilterCntRstHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 6, 1, 6),
    _AnueFilterCntRstHCOutPkts_Type()
)
anueFilterCntRstHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstHCOutPkts.setStatus("current")
_AnueFilterCntRstHCDropPkts_Type = Counter64
_AnueFilterCntRstHCDropPkts_Object = MibTableColumn
anueFilterCntRstHCDropPkts = _AnueFilterCntRstHCDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 6, 1, 7),
    _AnueFilterCntRstHCDropPkts_Type()
)
anueFilterCntRstHCDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstHCDropPkts.setStatus("current")
_AnueFilterCntRstHCDropTime_Type = DateAndTime
_AnueFilterCntRstHCDropTime_Object = MibTableColumn
anueFilterCntRstHCDropTime = _AnueFilterCntRstHCDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 6, 1, 8),
    _AnueFilterCntRstHCDropTime_Type()
)
anueFilterCntRstHCDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstHCDropTime.setStatus("current")
_AnueNtoFilterStatsCurHCTable_Object = MibTable
anueNtoFilterStatsCurHCTable = _AnueNtoFilterStatsCurHCTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCurHCTable.setStatus("current")
_AnueNtoFilterStatsCurHCEntry_Object = MibTableRow
anueNtoFilterStatsCurHCEntry = _AnueNtoFilterStatsCurHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7, 1)
)
anueNtoFilterStatsCurHCEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCurHCEntry.setStatus("current")
_AnueFilterCurHCInOctets_Type = CounterBasedGauge64
_AnueFilterCurHCInOctets_Object = MibTableColumn
anueFilterCurHCInOctets = _AnueFilterCurHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7, 1, 3),
    _AnueFilterCurHCInOctets_Type()
)
anueFilterCurHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurHCInOctets.setStatus("current")
_AnueFilterCurHCOutOctets_Type = CounterBasedGauge64
_AnueFilterCurHCOutOctets_Object = MibTableColumn
anueFilterCurHCOutOctets = _AnueFilterCurHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7, 1, 4),
    _AnueFilterCurHCOutOctets_Type()
)
anueFilterCurHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurHCOutOctets.setStatus("current")
_AnueFilterCurHCRateOctets_Type = CounterBasedGauge64
_AnueFilterCurHCRateOctets_Object = MibTableColumn
anueFilterCurHCRateOctets = _AnueFilterCurHCRateOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7, 1, 5),
    _AnueFilterCurHCRateOctets_Type()
)
anueFilterCurHCRateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurHCRateOctets.setStatus("current")
_AnueFilterCurHCInPkts_Type = CounterBasedGauge64
_AnueFilterCurHCInPkts_Object = MibTableColumn
anueFilterCurHCInPkts = _AnueFilterCurHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7, 1, 6),
    _AnueFilterCurHCInPkts_Type()
)
anueFilterCurHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurHCInPkts.setStatus("current")
_AnueFilterCurHCOutPkts_Type = CounterBasedGauge64
_AnueFilterCurHCOutPkts_Object = MibTableColumn
anueFilterCurHCOutPkts = _AnueFilterCurHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7, 1, 7),
    _AnueFilterCurHCOutPkts_Type()
)
anueFilterCurHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurHCOutPkts.setStatus("current")
_AnueFilterCurHCRatePkts_Type = CounterBasedGauge64
_AnueFilterCurHCRatePkts_Object = MibTableColumn
anueFilterCurHCRatePkts = _AnueFilterCurHCRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7, 1, 8),
    _AnueFilterCurHCRatePkts_Type()
)
anueFilterCurHCRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurHCRatePkts.setStatus("current")
_AnueFilterCurHCDropPkts_Type = CounterBasedGauge64
_AnueFilterCurHCDropPkts_Object = MibTableColumn
anueFilterCurHCDropPkts = _AnueFilterCurHCDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7, 1, 9),
    _AnueFilterCurHCDropPkts_Type()
)
anueFilterCurHCDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurHCDropPkts.setStatus("current")
_AnueFilterCurHCUtil_Type = CounterBasedGauge64
_AnueFilterCurHCUtil_Object = MibTableColumn
anueFilterCurHCUtil = _AnueFilterCurHCUtil_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 7, 1, 10),
    _AnueFilterCurHCUtil_Type()
)
anueFilterCurHCUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurHCUtil.setStatus("current")
_AnueNtoFilterStatsAvgHCTable_Object = MibTable
anueNtoFilterStatsAvgHCTable = _AnueNtoFilterStatsAvgHCTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsAvgHCTable.setStatus("current")
_AnueNtoFilterStatsAvgHCEntry_Object = MibTableRow
anueNtoFilterStatsAvgHCEntry = _AnueNtoFilterStatsAvgHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8, 1)
)
anueNtoFilterStatsAvgHCEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsAvgHCEntry.setStatus("current")
_AnueFilterAvgHCInOctets_Type = CounterBasedGauge64
_AnueFilterAvgHCInOctets_Object = MibTableColumn
anueFilterAvgHCInOctets = _AnueFilterAvgHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8, 1, 3),
    _AnueFilterAvgHCInOctets_Type()
)
anueFilterAvgHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgHCInOctets.setStatus("current")
_AnueFilterAvgHCOutOctets_Type = CounterBasedGauge64
_AnueFilterAvgHCOutOctets_Object = MibTableColumn
anueFilterAvgHCOutOctets = _AnueFilterAvgHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8, 1, 4),
    _AnueFilterAvgHCOutOctets_Type()
)
anueFilterAvgHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgHCOutOctets.setStatus("current")
_AnueFilterAvgHCRateOctets_Type = CounterBasedGauge64
_AnueFilterAvgHCRateOctets_Object = MibTableColumn
anueFilterAvgHCRateOctets = _AnueFilterAvgHCRateOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8, 1, 5),
    _AnueFilterAvgHCRateOctets_Type()
)
anueFilterAvgHCRateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgHCRateOctets.setStatus("current")
_AnueFilterAvgHCInPkts_Type = CounterBasedGauge64
_AnueFilterAvgHCInPkts_Object = MibTableColumn
anueFilterAvgHCInPkts = _AnueFilterAvgHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8, 1, 6),
    _AnueFilterAvgHCInPkts_Type()
)
anueFilterAvgHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgHCInPkts.setStatus("current")
_AnueFilterAvgHCOutPkts_Type = CounterBasedGauge64
_AnueFilterAvgHCOutPkts_Object = MibTableColumn
anueFilterAvgHCOutPkts = _AnueFilterAvgHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8, 1, 7),
    _AnueFilterAvgHCOutPkts_Type()
)
anueFilterAvgHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgHCOutPkts.setStatus("current")
_AnueFilterAvgHCRatePkts_Type = CounterBasedGauge64
_AnueFilterAvgHCRatePkts_Object = MibTableColumn
anueFilterAvgHCRatePkts = _AnueFilterAvgHCRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8, 1, 8),
    _AnueFilterAvgHCRatePkts_Type()
)
anueFilterAvgHCRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgHCRatePkts.setStatus("current")
_AnueFilterAvgHCDropPkts_Type = CounterBasedGauge64
_AnueFilterAvgHCDropPkts_Object = MibTableColumn
anueFilterAvgHCDropPkts = _AnueFilterAvgHCDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8, 1, 9),
    _AnueFilterAvgHCDropPkts_Type()
)
anueFilterAvgHCDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgHCDropPkts.setStatus("current")
_AnueFilterAvgHCUtil_Type = CounterBasedGauge64
_AnueFilterAvgHCUtil_Object = MibTableColumn
anueFilterAvgHCUtil = _AnueFilterAvgHCUtil_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 8, 1, 10),
    _AnueFilterAvgHCUtil_Type()
)
anueFilterAvgHCUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgHCUtil.setStatus("current")
_AnueNtoFilterStatsPeakHCTable_Object = MibTable
anueNtoFilterStatsPeakHCTable = _AnueNtoFilterStatsPeakHCTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsPeakHCTable.setStatus("current")
_AnueNtoFilterStatsPeakHCEntry_Object = MibTableRow
anueNtoFilterStatsPeakHCEntry = _AnueNtoFilterStatsPeakHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1)
)
anueNtoFilterStatsPeakHCEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsPeakHCEntry.setStatus("current")
_AnueFilterPeakHCInOctets_Type = CounterBasedGauge64
_AnueFilterPeakHCInOctets_Object = MibTableColumn
anueFilterPeakHCInOctets = _AnueFilterPeakHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 3),
    _AnueFilterPeakHCInOctets_Type()
)
anueFilterPeakHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCInOctets.setStatus("current")
_AnueFilterPeakHCInOctetsTime_Type = DateAndTime
_AnueFilterPeakHCInOctetsTime_Object = MibTableColumn
anueFilterPeakHCInOctetsTime = _AnueFilterPeakHCInOctetsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 4),
    _AnueFilterPeakHCInOctetsTime_Type()
)
anueFilterPeakHCInOctetsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCInOctetsTime.setStatus("current")
_AnueFilterPeakHCOutOctets_Type = CounterBasedGauge64
_AnueFilterPeakHCOutOctets_Object = MibTableColumn
anueFilterPeakHCOutOctets = _AnueFilterPeakHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 5),
    _AnueFilterPeakHCOutOctets_Type()
)
anueFilterPeakHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCOutOctets.setStatus("current")
_AnueFilterPeakHCOutOctetsTime_Type = DateAndTime
_AnueFilterPeakHCOutOctetsTime_Object = MibTableColumn
anueFilterPeakHCOutOctetsTime = _AnueFilterPeakHCOutOctetsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 6),
    _AnueFilterPeakHCOutOctetsTime_Type()
)
anueFilterPeakHCOutOctetsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCOutOctetsTime.setStatus("current")
_AnueFilterPeakHCRateOctets_Type = CounterBasedGauge64
_AnueFilterPeakHCRateOctets_Object = MibTableColumn
anueFilterPeakHCRateOctets = _AnueFilterPeakHCRateOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 7),
    _AnueFilterPeakHCRateOctets_Type()
)
anueFilterPeakHCRateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCRateOctets.setStatus("current")
_AnueFilterPeakHCRateOctetsTime_Type = DateAndTime
_AnueFilterPeakHCRateOctetsTime_Object = MibTableColumn
anueFilterPeakHCRateOctetsTime = _AnueFilterPeakHCRateOctetsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 8),
    _AnueFilterPeakHCRateOctetsTime_Type()
)
anueFilterPeakHCRateOctetsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCRateOctetsTime.setStatus("current")
_AnueFilterPeakHCInPkts_Type = CounterBasedGauge64
_AnueFilterPeakHCInPkts_Object = MibTableColumn
anueFilterPeakHCInPkts = _AnueFilterPeakHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 9),
    _AnueFilterPeakHCInPkts_Type()
)
anueFilterPeakHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCInPkts.setStatus("current")
_AnueFilterPeakHCInPktsTime_Type = DateAndTime
_AnueFilterPeakHCInPktsTime_Object = MibTableColumn
anueFilterPeakHCInPktsTime = _AnueFilterPeakHCInPktsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 10),
    _AnueFilterPeakHCInPktsTime_Type()
)
anueFilterPeakHCInPktsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCInPktsTime.setStatus("current")
_AnueFilterPeakHCOutPkts_Type = CounterBasedGauge64
_AnueFilterPeakHCOutPkts_Object = MibTableColumn
anueFilterPeakHCOutPkts = _AnueFilterPeakHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 11),
    _AnueFilterPeakHCOutPkts_Type()
)
anueFilterPeakHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCOutPkts.setStatus("current")
_AnueFilterPeakHCOutPktsTime_Type = DateAndTime
_AnueFilterPeakHCOutPktsTime_Object = MibTableColumn
anueFilterPeakHCOutPktsTime = _AnueFilterPeakHCOutPktsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 12),
    _AnueFilterPeakHCOutPktsTime_Type()
)
anueFilterPeakHCOutPktsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCOutPktsTime.setStatus("current")
_AnueFilterPeakHCRatePkts_Type = CounterBasedGauge64
_AnueFilterPeakHCRatePkts_Object = MibTableColumn
anueFilterPeakHCRatePkts = _AnueFilterPeakHCRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 13),
    _AnueFilterPeakHCRatePkts_Type()
)
anueFilterPeakHCRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCRatePkts.setStatus("current")
_AnueFilterPeakHCRatePktsTime_Type = DateAndTime
_AnueFilterPeakHCRatePktsTime_Object = MibTableColumn
anueFilterPeakHCRatePktsTime = _AnueFilterPeakHCRatePktsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 14),
    _AnueFilterPeakHCRatePktsTime_Type()
)
anueFilterPeakHCRatePktsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCRatePktsTime.setStatus("current")
_AnueFilterPeakHCDropPkts_Type = CounterBasedGauge64
_AnueFilterPeakHCDropPkts_Object = MibTableColumn
anueFilterPeakHCDropPkts = _AnueFilterPeakHCDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 15),
    _AnueFilterPeakHCDropPkts_Type()
)
anueFilterPeakHCDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCDropPkts.setStatus("current")
_AnueFilterPeakHCDropPktsTime_Type = DateAndTime
_AnueFilterPeakHCDropPktsTime_Object = MibTableColumn
anueFilterPeakHCDropPktsTime = _AnueFilterPeakHCDropPktsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 16),
    _AnueFilterPeakHCDropPktsTime_Type()
)
anueFilterPeakHCDropPktsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCDropPktsTime.setStatus("current")
_AnueFilterPeakHCUtil_Type = CounterBasedGauge64
_AnueFilterPeakHCUtil_Object = MibTableColumn
anueFilterPeakHCUtil = _AnueFilterPeakHCUtil_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 17),
    _AnueFilterPeakHCUtil_Type()
)
anueFilterPeakHCUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCUtil.setStatus("current")
_AnueFilterPeakHCUtilTime_Type = DateAndTime
_AnueFilterPeakHCUtilTime_Object = MibTableColumn
anueFilterPeakHCUtilTime = _AnueFilterPeakHCUtilTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 9, 1, 18),
    _AnueFilterPeakHCUtilTime_Type()
)
anueFilterPeakHCUtilTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakHCUtilTime.setStatus("current")
_AnueNtoFilterStatsCntModTable_Object = MibTable
anueNtoFilterStatsCntModTable = _AnueNtoFilterStatsCntModTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCntModTable.setStatus("current")
_AnueNtoFilterStatsCntModEntry_Object = MibTableRow
anueNtoFilterStatsCntModEntry = _AnueNtoFilterStatsCntModEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 10, 1)
)
anueNtoFilterStatsCntModEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCntModEntry.setStatus("current")
_AnueFilterCntModInOctets_Type = Counter32
_AnueFilterCntModInOctets_Object = MibTableColumn
anueFilterCntModInOctets = _AnueFilterCntModInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 10, 1, 3),
    _AnueFilterCntModInOctets_Type()
)
anueFilterCntModInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModInOctets.setStatus("current")
_AnueFilterCntModOutOctets_Type = Counter32
_AnueFilterCntModOutOctets_Object = MibTableColumn
anueFilterCntModOutOctets = _AnueFilterCntModOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 10, 1, 4),
    _AnueFilterCntModOutOctets_Type()
)
anueFilterCntModOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModOutOctets.setStatus("current")
_AnueFilterCntModInPkts_Type = Counter32
_AnueFilterCntModInPkts_Object = MibTableColumn
anueFilterCntModInPkts = _AnueFilterCntModInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 10, 1, 5),
    _AnueFilterCntModInPkts_Type()
)
anueFilterCntModInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModInPkts.setStatus("current")
_AnueFilterCntModOutPkts_Type = Counter32
_AnueFilterCntModOutPkts_Object = MibTableColumn
anueFilterCntModOutPkts = _AnueFilterCntModOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 10, 1, 6),
    _AnueFilterCntModOutPkts_Type()
)
anueFilterCntModOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModOutPkts.setStatus("current")
_AnueFilterCntModDropPkts_Type = Counter32
_AnueFilterCntModDropPkts_Object = MibTableColumn
anueFilterCntModDropPkts = _AnueFilterCntModDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 10, 1, 7),
    _AnueFilterCntModDropPkts_Type()
)
anueFilterCntModDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModDropPkts.setStatus("current")
_AnueFilterCntModDropTime_Type = DateAndTime
_AnueFilterCntModDropTime_Object = MibTableColumn
anueFilterCntModDropTime = _AnueFilterCntModDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 10, 1, 8),
    _AnueFilterCntModDropTime_Type()
)
anueFilterCntModDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntModDropTime.setStatus("current")
_AnueNtoFilterStatsCntRstTable_Object = MibTable
anueNtoFilterStatsCntRstTable = _AnueNtoFilterStatsCntRstTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCntRstTable.setStatus("current")
_AnueNtoFilterStatsCntRstEntry_Object = MibTableRow
anueNtoFilterStatsCntRstEntry = _AnueNtoFilterStatsCntRstEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 11, 1)
)
anueNtoFilterStatsCntRstEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCntRstEntry.setStatus("current")
_AnueFilterCntRstInOctets_Type = Counter32
_AnueFilterCntRstInOctets_Object = MibTableColumn
anueFilterCntRstInOctets = _AnueFilterCntRstInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 11, 1, 3),
    _AnueFilterCntRstInOctets_Type()
)
anueFilterCntRstInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstInOctets.setStatus("current")
_AnueFilterCntRstOutOctets_Type = Counter32
_AnueFilterCntRstOutOctets_Object = MibTableColumn
anueFilterCntRstOutOctets = _AnueFilterCntRstOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 11, 1, 4),
    _AnueFilterCntRstOutOctets_Type()
)
anueFilterCntRstOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstOutOctets.setStatus("current")
_AnueFilterCntRstInPkts_Type = Counter32
_AnueFilterCntRstInPkts_Object = MibTableColumn
anueFilterCntRstInPkts = _AnueFilterCntRstInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 11, 1, 5),
    _AnueFilterCntRstInPkts_Type()
)
anueFilterCntRstInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstInPkts.setStatus("current")
_AnueFilterCntRstOutPkts_Type = Counter32
_AnueFilterCntRstOutPkts_Object = MibTableColumn
anueFilterCntRstOutPkts = _AnueFilterCntRstOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 11, 1, 6),
    _AnueFilterCntRstOutPkts_Type()
)
anueFilterCntRstOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstOutPkts.setStatus("current")
_AnueFilterCntRstDropPkts_Type = Counter32
_AnueFilterCntRstDropPkts_Object = MibTableColumn
anueFilterCntRstDropPkts = _AnueFilterCntRstDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 11, 1, 7),
    _AnueFilterCntRstDropPkts_Type()
)
anueFilterCntRstDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstDropPkts.setStatus("current")
_AnueFilterCntRstDropTime_Type = DateAndTime
_AnueFilterCntRstDropTime_Object = MibTableColumn
anueFilterCntRstDropTime = _AnueFilterCntRstDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 11, 1, 8),
    _AnueFilterCntRstDropTime_Type()
)
anueFilterCntRstDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCntRstDropTime.setStatus("current")
_AnueNtoFilterStatsCurTable_Object = MibTable
anueNtoFilterStatsCurTable = _AnueNtoFilterStatsCurTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCurTable.setStatus("current")
_AnueNtoFilterStatsCurEntry_Object = MibTableRow
anueNtoFilterStatsCurEntry = _AnueNtoFilterStatsCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12, 1)
)
anueNtoFilterStatsCurEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsCurEntry.setStatus("current")
_AnueFilterCurInOctets_Type = Gauge32
_AnueFilterCurInOctets_Object = MibTableColumn
anueFilterCurInOctets = _AnueFilterCurInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12, 1, 3),
    _AnueFilterCurInOctets_Type()
)
anueFilterCurInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurInOctets.setStatus("current")
_AnueFilterCurOutOctets_Type = Gauge32
_AnueFilterCurOutOctets_Object = MibTableColumn
anueFilterCurOutOctets = _AnueFilterCurOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12, 1, 4),
    _AnueFilterCurOutOctets_Type()
)
anueFilterCurOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurOutOctets.setStatus("current")
_AnueFilterCurRateOctets_Type = Gauge32
_AnueFilterCurRateOctets_Object = MibTableColumn
anueFilterCurRateOctets = _AnueFilterCurRateOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12, 1, 5),
    _AnueFilterCurRateOctets_Type()
)
anueFilterCurRateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurRateOctets.setStatus("current")
_AnueFilterCurInPkts_Type = Gauge32
_AnueFilterCurInPkts_Object = MibTableColumn
anueFilterCurInPkts = _AnueFilterCurInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12, 1, 6),
    _AnueFilterCurInPkts_Type()
)
anueFilterCurInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurInPkts.setStatus("current")
_AnueFilterCurOutPkts_Type = Gauge32
_AnueFilterCurOutPkts_Object = MibTableColumn
anueFilterCurOutPkts = _AnueFilterCurOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12, 1, 7),
    _AnueFilterCurOutPkts_Type()
)
anueFilterCurOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurOutPkts.setStatus("current")
_AnueFilterCurRatePkts_Type = Gauge32
_AnueFilterCurRatePkts_Object = MibTableColumn
anueFilterCurRatePkts = _AnueFilterCurRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12, 1, 8),
    _AnueFilterCurRatePkts_Type()
)
anueFilterCurRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurRatePkts.setStatus("current")
_AnueFilterCurDropPkts_Type = Gauge32
_AnueFilterCurDropPkts_Object = MibTableColumn
anueFilterCurDropPkts = _AnueFilterCurDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12, 1, 9),
    _AnueFilterCurDropPkts_Type()
)
anueFilterCurDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurDropPkts.setStatus("current")
_AnueFilterCurUtil_Type = Gauge32
_AnueFilterCurUtil_Object = MibTableColumn
anueFilterCurUtil = _AnueFilterCurUtil_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 12, 1, 10),
    _AnueFilterCurUtil_Type()
)
anueFilterCurUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurUtil.setStatus("current")
_AnueNtoFilterStatsAvgTable_Object = MibTable
anueNtoFilterStatsAvgTable = _AnueNtoFilterStatsAvgTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsAvgTable.setStatus("current")
_AnueNtoFilterStatsAvgEntry_Object = MibTableRow
anueNtoFilterStatsAvgEntry = _AnueNtoFilterStatsAvgEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13, 1)
)
anueNtoFilterStatsAvgEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsAvgEntry.setStatus("current")
_AnueFilterAvgInOctets_Type = Gauge32
_AnueFilterAvgInOctets_Object = MibTableColumn
anueFilterAvgInOctets = _AnueFilterAvgInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13, 1, 3),
    _AnueFilterAvgInOctets_Type()
)
anueFilterAvgInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgInOctets.setStatus("current")
_AnueFilterAvgOutOctets_Type = Gauge32
_AnueFilterAvgOutOctets_Object = MibTableColumn
anueFilterAvgOutOctets = _AnueFilterAvgOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13, 1, 4),
    _AnueFilterAvgOutOctets_Type()
)
anueFilterAvgOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgOutOctets.setStatus("current")
_AnueFilterAvgRateOctets_Type = Gauge32
_AnueFilterAvgRateOctets_Object = MibTableColumn
anueFilterAvgRateOctets = _AnueFilterAvgRateOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13, 1, 5),
    _AnueFilterAvgRateOctets_Type()
)
anueFilterAvgRateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgRateOctets.setStatus("current")
_AnueFilterAvgInPkts_Type = Gauge32
_AnueFilterAvgInPkts_Object = MibTableColumn
anueFilterAvgInPkts = _AnueFilterAvgInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13, 1, 6),
    _AnueFilterAvgInPkts_Type()
)
anueFilterAvgInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgInPkts.setStatus("current")
_AnueFilterAvgOutPkts_Type = Gauge32
_AnueFilterAvgOutPkts_Object = MibTableColumn
anueFilterAvgOutPkts = _AnueFilterAvgOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13, 1, 7),
    _AnueFilterAvgOutPkts_Type()
)
anueFilterAvgOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgOutPkts.setStatus("current")
_AnueFilterAvgRatePkts_Type = Gauge32
_AnueFilterAvgRatePkts_Object = MibTableColumn
anueFilterAvgRatePkts = _AnueFilterAvgRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13, 1, 8),
    _AnueFilterAvgRatePkts_Type()
)
anueFilterAvgRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgRatePkts.setStatus("current")
_AnueFilterAvgDropPkts_Type = Gauge32
_AnueFilterAvgDropPkts_Object = MibTableColumn
anueFilterAvgDropPkts = _AnueFilterAvgDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13, 1, 9),
    _AnueFilterAvgDropPkts_Type()
)
anueFilterAvgDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgDropPkts.setStatus("current")
_AnueFilterAvgUtil_Type = Gauge32
_AnueFilterAvgUtil_Object = MibTableColumn
anueFilterAvgUtil = _AnueFilterAvgUtil_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 13, 1, 10),
    _AnueFilterAvgUtil_Type()
)
anueFilterAvgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgUtil.setStatus("current")
_AnueNtoFilterStatsPeakTable_Object = MibTable
anueNtoFilterStatsPeakTable = _AnueNtoFilterStatsPeakTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsPeakTable.setStatus("current")
_AnueNtoFilterStatsPeakEntry_Object = MibTableRow
anueNtoFilterStatsPeakEntry = _AnueNtoFilterStatsPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1)
)
anueNtoFilterStatsPeakEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsPeakEntry.setStatus("current")
_AnueFilterPeakInOctets_Type = Gauge32
_AnueFilterPeakInOctets_Object = MibTableColumn
anueFilterPeakInOctets = _AnueFilterPeakInOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 3),
    _AnueFilterPeakInOctets_Type()
)
anueFilterPeakInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakInOctets.setStatus("current")
_AnueFilterPeakInOctetsTime_Type = DateAndTime
_AnueFilterPeakInOctetsTime_Object = MibTableColumn
anueFilterPeakInOctetsTime = _AnueFilterPeakInOctetsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 4),
    _AnueFilterPeakInOctetsTime_Type()
)
anueFilterPeakInOctetsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakInOctetsTime.setStatus("current")
_AnueFilterPeakOutOctets_Type = Gauge32
_AnueFilterPeakOutOctets_Object = MibTableColumn
anueFilterPeakOutOctets = _AnueFilterPeakOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 5),
    _AnueFilterPeakOutOctets_Type()
)
anueFilterPeakOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakOutOctets.setStatus("current")
_AnueFilterPeakOutOctetsTime_Type = DateAndTime
_AnueFilterPeakOutOctetsTime_Object = MibTableColumn
anueFilterPeakOutOctetsTime = _AnueFilterPeakOutOctetsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 6),
    _AnueFilterPeakOutOctetsTime_Type()
)
anueFilterPeakOutOctetsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakOutOctetsTime.setStatus("current")
_AnueFilterPeakRateOctets_Type = Gauge32
_AnueFilterPeakRateOctets_Object = MibTableColumn
anueFilterPeakRateOctets = _AnueFilterPeakRateOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 7),
    _AnueFilterPeakRateOctets_Type()
)
anueFilterPeakRateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakRateOctets.setStatus("current")
_AnueFilterPeakRateOctetsTime_Type = DateAndTime
_AnueFilterPeakRateOctetsTime_Object = MibTableColumn
anueFilterPeakRateOctetsTime = _AnueFilterPeakRateOctetsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 8),
    _AnueFilterPeakRateOctetsTime_Type()
)
anueFilterPeakRateOctetsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakRateOctetsTime.setStatus("current")
_AnueFilterPeakInPkts_Type = Gauge32
_AnueFilterPeakInPkts_Object = MibTableColumn
anueFilterPeakInPkts = _AnueFilterPeakInPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 9),
    _AnueFilterPeakInPkts_Type()
)
anueFilterPeakInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakInPkts.setStatus("current")
_AnueFilterPeakInPktsTime_Type = DateAndTime
_AnueFilterPeakInPktsTime_Object = MibTableColumn
anueFilterPeakInPktsTime = _AnueFilterPeakInPktsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 10),
    _AnueFilterPeakInPktsTime_Type()
)
anueFilterPeakInPktsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakInPktsTime.setStatus("current")
_AnueFilterPeakOutPkts_Type = Gauge32
_AnueFilterPeakOutPkts_Object = MibTableColumn
anueFilterPeakOutPkts = _AnueFilterPeakOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 11),
    _AnueFilterPeakOutPkts_Type()
)
anueFilterPeakOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakOutPkts.setStatus("current")
_AnueFilterPeakOutPktsTime_Type = DateAndTime
_AnueFilterPeakOutPktsTime_Object = MibTableColumn
anueFilterPeakOutPktsTime = _AnueFilterPeakOutPktsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 12),
    _AnueFilterPeakOutPktsTime_Type()
)
anueFilterPeakOutPktsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakOutPktsTime.setStatus("current")
_AnueFilterPeakRatePkts_Type = Gauge32
_AnueFilterPeakRatePkts_Object = MibTableColumn
anueFilterPeakRatePkts = _AnueFilterPeakRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 13),
    _AnueFilterPeakRatePkts_Type()
)
anueFilterPeakRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakRatePkts.setStatus("current")
_AnueFilterPeakRatePktsTime_Type = DateAndTime
_AnueFilterPeakRatePktsTime_Object = MibTableColumn
anueFilterPeakRatePktsTime = _AnueFilterPeakRatePktsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 14),
    _AnueFilterPeakRatePktsTime_Type()
)
anueFilterPeakRatePktsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakRatePktsTime.setStatus("current")
_AnueFilterPeakDropPkts_Type = Gauge32
_AnueFilterPeakDropPkts_Object = MibTableColumn
anueFilterPeakDropPkts = _AnueFilterPeakDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 15),
    _AnueFilterPeakDropPkts_Type()
)
anueFilterPeakDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakDropPkts.setStatus("current")
_AnueFilterPeakDropPktsTime_Type = DateAndTime
_AnueFilterPeakDropPktsTime_Object = MibTableColumn
anueFilterPeakDropPktsTime = _AnueFilterPeakDropPktsTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 16),
    _AnueFilterPeakDropPktsTime_Type()
)
anueFilterPeakDropPktsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakDropPktsTime.setStatus("current")
_AnueFilterPeakUtil_Type = Gauge32
_AnueFilterPeakUtil_Object = MibTableColumn
anueFilterPeakUtil = _AnueFilterPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 17),
    _AnueFilterPeakUtil_Type()
)
anueFilterPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakUtil.setStatus("current")
_AnueFilterPeakUtilTime_Type = DateAndTime
_AnueFilterPeakUtilTime_Object = MibTableColumn
anueFilterPeakUtilTime = _AnueFilterPeakUtilTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 14, 1, 18),
    _AnueFilterPeakUtilTime_Type()
)
anueFilterPeakUtilTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakUtilTime.setStatus("current")
_AnueFilterDefLastChange_Type = TimeTicks
_AnueFilterDefLastChange_Object = MibScalar
anueFilterDefLastChange = _AnueFilterDefLastChange_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 15),
    _AnueFilterDefLastChange_Type()
)
anueFilterDefLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterDefLastChange.setStatus("current")
_AnueFilterConnLastChange_Type = TimeTicks
_AnueFilterConnLastChange_Object = MibScalar
anueFilterConnLastChange = _AnueFilterConnLastChange_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 16),
    _AnueFilterConnLastChange_Type()
)
anueFilterConnLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterConnLastChange.setStatus("current")
_AnueNtoFilterStatsGscSessTable_Object = MibTable
anueNtoFilterStatsGscSessTable = _AnueNtoFilterStatsGscSessTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsGscSessTable.setStatus("current")
_AnueNtoFilterStatsGscSessEntry_Object = MibTableRow
anueNtoFilterStatsGscSessEntry = _AnueNtoFilterStatsGscSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1)
)
anueNtoFilterStatsGscSessEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsGscSessEntry.setStatus("current")
_AnueFilterGscCurDenyGtpV0Sess_Type = Counter64
_AnueFilterGscCurDenyGtpV0Sess_Object = MibTableColumn
anueFilterGscCurDenyGtpV0Sess = _AnueFilterGscCurDenyGtpV0Sess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 3),
    _AnueFilterGscCurDenyGtpV0Sess_Type()
)
anueFilterGscCurDenyGtpV0Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscCurDenyGtpV0Sess.setStatus("current")
_AnueFilterGscCurDenyGtpV1Sess_Type = Counter64
_AnueFilterGscCurDenyGtpV1Sess_Object = MibTableColumn
anueFilterGscCurDenyGtpV1Sess = _AnueFilterGscCurDenyGtpV1Sess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 4),
    _AnueFilterGscCurDenyGtpV1Sess_Type()
)
anueFilterGscCurDenyGtpV1Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscCurDenyGtpV1Sess.setStatus("current")
_AnueFilterGscCurDenyGtpV2Sess_Type = Counter64
_AnueFilterGscCurDenyGtpV2Sess_Object = MibTableColumn
anueFilterGscCurDenyGtpV2Sess = _AnueFilterGscCurDenyGtpV2Sess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 5),
    _AnueFilterGscCurDenyGtpV2Sess_Type()
)
anueFilterGscCurDenyGtpV2Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscCurDenyGtpV2Sess.setStatus("current")
_AnueFilterGscCurDenyGtpTotSess_Type = Counter64
_AnueFilterGscCurDenyGtpTotSess_Object = MibTableColumn
anueFilterGscCurDenyGtpTotSess = _AnueFilterGscCurDenyGtpTotSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 6),
    _AnueFilterGscCurDenyGtpTotSess_Type()
)
anueFilterGscCurDenyGtpTotSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscCurDenyGtpTotSess.setStatus("current")
_AnueFilterGscAvgDenyGtpV0Sess_Type = Counter64
_AnueFilterGscAvgDenyGtpV0Sess_Object = MibTableColumn
anueFilterGscAvgDenyGtpV0Sess = _AnueFilterGscAvgDenyGtpV0Sess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 7),
    _AnueFilterGscAvgDenyGtpV0Sess_Type()
)
anueFilterGscAvgDenyGtpV0Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscAvgDenyGtpV0Sess.setStatus("current")
_AnueFilterGscAvgDenyGtpV1Sess_Type = Counter64
_AnueFilterGscAvgDenyGtpV1Sess_Object = MibTableColumn
anueFilterGscAvgDenyGtpV1Sess = _AnueFilterGscAvgDenyGtpV1Sess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 8),
    _AnueFilterGscAvgDenyGtpV1Sess_Type()
)
anueFilterGscAvgDenyGtpV1Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscAvgDenyGtpV1Sess.setStatus("current")
_AnueFilterGscAvgDenyGtpV2Sess_Type = Counter64
_AnueFilterGscAvgDenyGtpV2Sess_Object = MibTableColumn
anueFilterGscAvgDenyGtpV2Sess = _AnueFilterGscAvgDenyGtpV2Sess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 9),
    _AnueFilterGscAvgDenyGtpV2Sess_Type()
)
anueFilterGscAvgDenyGtpV2Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscAvgDenyGtpV2Sess.setStatus("current")
_AnueFilterGscAvgDenyGtpTotSess_Type = Counter64
_AnueFilterGscAvgDenyGtpTotSess_Object = MibTableColumn
anueFilterGscAvgDenyGtpTotSess = _AnueFilterGscAvgDenyGtpTotSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 10),
    _AnueFilterGscAvgDenyGtpTotSess_Type()
)
anueFilterGscAvgDenyGtpTotSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscAvgDenyGtpTotSess.setStatus("current")
_AnueFilterGscPkDenyGtpV0Sess_Type = Counter64
_AnueFilterGscPkDenyGtpV0Sess_Object = MibTableColumn
anueFilterGscPkDenyGtpV0Sess = _AnueFilterGscPkDenyGtpV0Sess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 11),
    _AnueFilterGscPkDenyGtpV0Sess_Type()
)
anueFilterGscPkDenyGtpV0Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDenyGtpV0Sess.setStatus("current")
_AnueFilterGscPkDenyGtpV1Sess_Type = Counter64
_AnueFilterGscPkDenyGtpV1Sess_Object = MibTableColumn
anueFilterGscPkDenyGtpV1Sess = _AnueFilterGscPkDenyGtpV1Sess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 12),
    _AnueFilterGscPkDenyGtpV1Sess_Type()
)
anueFilterGscPkDenyGtpV1Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDenyGtpV1Sess.setStatus("current")
_AnueFilterGscPkDenyGtpV2Sess_Type = Counter64
_AnueFilterGscPkDenyGtpV2Sess_Object = MibTableColumn
anueFilterGscPkDenyGtpV2Sess = _AnueFilterGscPkDenyGtpV2Sess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 13),
    _AnueFilterGscPkDenyGtpV2Sess_Type()
)
anueFilterGscPkDenyGtpV2Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDenyGtpV2Sess.setStatus("current")
_AnueFilterGscPkDenyGtpTotSess_Type = Counter64
_AnueFilterGscPkDenyGtpTotSess_Object = MibTableColumn
anueFilterGscPkDenyGtpTotSess = _AnueFilterGscPkDenyGtpTotSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 14),
    _AnueFilterGscPkDenyGtpTotSess_Type()
)
anueFilterGscPkDenyGtpTotSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDenyGtpTotSess.setStatus("current")
_AnueFilterGscPkDenyGtpV0SessT_Type = DateAndTime
_AnueFilterGscPkDenyGtpV0SessT_Object = MibTableColumn
anueFilterGscPkDenyGtpV0SessT = _AnueFilterGscPkDenyGtpV0SessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 15),
    _AnueFilterGscPkDenyGtpV0SessT_Type()
)
anueFilterGscPkDenyGtpV0SessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDenyGtpV0SessT.setStatus("current")
_AnueFilterGscPkDenyGtpV1SessT_Type = DateAndTime
_AnueFilterGscPkDenyGtpV1SessT_Object = MibTableColumn
anueFilterGscPkDenyGtpV1SessT = _AnueFilterGscPkDenyGtpV1SessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 16),
    _AnueFilterGscPkDenyGtpV1SessT_Type()
)
anueFilterGscPkDenyGtpV1SessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDenyGtpV1SessT.setStatus("current")
_AnueFilterGscPkDenyGtpV2SessT_Type = DateAndTime
_AnueFilterGscPkDenyGtpV2SessT_Object = MibTableColumn
anueFilterGscPkDenyGtpV2SessT = _AnueFilterGscPkDenyGtpV2SessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 17),
    _AnueFilterGscPkDenyGtpV2SessT_Type()
)
anueFilterGscPkDenyGtpV2SessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDenyGtpV2SessT.setStatus("current")
_AnueFilterGscPkDenyGtpTotSessT_Type = DateAndTime
_AnueFilterGscPkDenyGtpTotSessT_Object = MibTableColumn
anueFilterGscPkDenyGtpTotSessT = _AnueFilterGscPkDenyGtpTotSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 18),
    _AnueFilterGscPkDenyGtpTotSessT_Type()
)
anueFilterGscPkDenyGtpTotSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDenyGtpTotSessT.setStatus("current")
_AnueFilterGscTotOversizePktsTx_Type = Counter64
_AnueFilterGscTotOversizePktsTx_Object = MibTableColumn
anueFilterGscTotOversizePktsTx = _AnueFilterGscTotOversizePktsTx_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 19),
    _AnueFilterGscTotOversizePktsTx_Type()
)
anueFilterGscTotOversizePktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscTotOversizePktsTx.setStatus("current")
_AnueFilterGscCurOversizePktsTx_Type = Counter64
_AnueFilterGscCurOversizePktsTx_Object = MibTableColumn
anueFilterGscCurOversizePktsTx = _AnueFilterGscCurOversizePktsTx_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 20),
    _AnueFilterGscCurOversizePktsTx_Type()
)
anueFilterGscCurOversizePktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscCurOversizePktsTx.setStatus("current")
_AnueFilterGscAvgOversizePktsTx_Type = Counter64
_AnueFilterGscAvgOversizePktsTx_Object = MibTableColumn
anueFilterGscAvgOversizePktsTx = _AnueFilterGscAvgOversizePktsTx_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 21),
    _AnueFilterGscAvgOversizePktsTx_Type()
)
anueFilterGscAvgOversizePktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscAvgOversizePktsTx.setStatus("current")
_AnueFilterGscPkOversizePktsTx_Type = Counter64
_AnueFilterGscPkOversizePktsTx_Object = MibTableColumn
anueFilterGscPkOversizePktsTx = _AnueFilterGscPkOversizePktsTx_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 22),
    _AnueFilterGscPkOversizePktsTx_Type()
)
anueFilterGscPkOversizePktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkOversizePktsTx.setStatus("current")
_AnueFilterGscPkOversizePktsTxT_Type = DateAndTime
_AnueFilterGscPkOversizePktsTxT_Object = MibTableColumn
anueFilterGscPkOversizePktsTxT = _AnueFilterGscPkOversizePktsTxT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 23),
    _AnueFilterGscPkOversizePktsTxT_Type()
)
anueFilterGscPkOversizePktsTxT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkOversizePktsTxT.setStatus("current")
_AnueFilterGscTotDroppedPkts_Type = Counter64
_AnueFilterGscTotDroppedPkts_Object = MibTableColumn
anueFilterGscTotDroppedPkts = _AnueFilterGscTotDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 24),
    _AnueFilterGscTotDroppedPkts_Type()
)
anueFilterGscTotDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscTotDroppedPkts.setStatus("current")
_AnueFilterGscCurDroppedPkts_Type = Counter64
_AnueFilterGscCurDroppedPkts_Object = MibTableColumn
anueFilterGscCurDroppedPkts = _AnueFilterGscCurDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 25),
    _AnueFilterGscCurDroppedPkts_Type()
)
anueFilterGscCurDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscCurDroppedPkts.setStatus("current")
_AnueFilterGscAvgDroppedPkts_Type = Counter64
_AnueFilterGscAvgDroppedPkts_Object = MibTableColumn
anueFilterGscAvgDroppedPkts = _AnueFilterGscAvgDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 26),
    _AnueFilterGscAvgDroppedPkts_Type()
)
anueFilterGscAvgDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscAvgDroppedPkts.setStatus("current")
_AnueFilterGscPkDroppedPkts_Type = Counter64
_AnueFilterGscPkDroppedPkts_Object = MibTableColumn
anueFilterGscPkDroppedPkts = _AnueFilterGscPkDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 27),
    _AnueFilterGscPkDroppedPkts_Type()
)
anueFilterGscPkDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDroppedPkts.setStatus("current")
_AnueFilterGscPkDroppedPktsT_Type = DateAndTime
_AnueFilterGscPkDroppedPktsT_Object = MibTableColumn
anueFilterGscPkDroppedPktsT = _AnueFilterGscPkDroppedPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 28),
    _AnueFilterGscPkDroppedPktsT_Type()
)
anueFilterGscPkDroppedPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDroppedPktsT.setStatus("current")
_AnueFilterGscTotDroppedBytes_Type = Counter64
_AnueFilterGscTotDroppedBytes_Object = MibTableColumn
anueFilterGscTotDroppedBytes = _AnueFilterGscTotDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 29),
    _AnueFilterGscTotDroppedBytes_Type()
)
anueFilterGscTotDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscTotDroppedBytes.setStatus("current")
_AnueFilterGscCurDroppedBytes_Type = Counter64
_AnueFilterGscCurDroppedBytes_Object = MibTableColumn
anueFilterGscCurDroppedBytes = _AnueFilterGscCurDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 30),
    _AnueFilterGscCurDroppedBytes_Type()
)
anueFilterGscCurDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscCurDroppedBytes.setStatus("current")
_AnueFilterGscAvgDroppedBytes_Type = Counter64
_AnueFilterGscAvgDroppedBytes_Object = MibTableColumn
anueFilterGscAvgDroppedBytes = _AnueFilterGscAvgDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 31),
    _AnueFilterGscAvgDroppedBytes_Type()
)
anueFilterGscAvgDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscAvgDroppedBytes.setStatus("current")
_AnueFilterGscPkDroppedBytes_Type = Counter64
_AnueFilterGscPkDroppedBytes_Object = MibTableColumn
anueFilterGscPkDroppedBytes = _AnueFilterGscPkDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 32),
    _AnueFilterGscPkDroppedBytes_Type()
)
anueFilterGscPkDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDroppedBytes.setStatus("current")
_AnueFilterGscPkDroppedBytesT_Type = DateAndTime
_AnueFilterGscPkDroppedBytesT_Object = MibTableColumn
anueFilterGscPkDroppedBytesT = _AnueFilterGscPkDroppedBytesT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 100, 1, 33),
    _AnueFilterGscPkDroppedBytesT_Type()
)
anueFilterGscPkDroppedBytesT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGscPkDroppedBytesT.setStatus("current")
_AnueNtoFilterStatsGscTable_Object = MibTable
anueNtoFilterStatsGscTable = _AnueNtoFilterStatsGscTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 101)
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsGscTable.setStatus("current")
_AnueNtoFilterStatsGscEntry_Object = MibTableRow
anueNtoFilterStatsGscEntry = _AnueNtoFilterStatsGscEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 101, 1)
)
anueNtoFilterStatsGscEntry.setIndexNames(
    (0, "ANUE-MIB", "anueFilterType"),
    (0, "ANUE-MIB", "anueFilterNumber"),
    (0, "ANUE-MIB", "anueFilterGTPPktType"),
)
if mibBuilder.loadTexts:
    anueNtoFilterStatsGscEntry.setStatus("current")
_AnueFilterCurGscPktsRate_Type = CounterBasedGauge64
_AnueFilterCurGscPktsRate_Object = MibTableColumn
anueFilterCurGscPktsRate = _AnueFilterCurGscPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 101, 1, 3),
    _AnueFilterCurGscPktsRate_Type()
)
anueFilterCurGscPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterCurGscPktsRate.setStatus("current")
_AnueFilterAvgGscPktsRate_Type = CounterBasedGauge64
_AnueFilterAvgGscPktsRate_Object = MibTableColumn
anueFilterAvgGscPktsRate = _AnueFilterAvgGscPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 101, 1, 4),
    _AnueFilterAvgGscPktsRate_Type()
)
anueFilterAvgGscPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterAvgGscPktsRate.setStatus("current")
_AnueFilterPeakGscPktsRate_Type = CounterBasedGauge64
_AnueFilterPeakGscPktsRate_Object = MibTableColumn
anueFilterPeakGscPktsRate = _AnueFilterPeakGscPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 101, 1, 5),
    _AnueFilterPeakGscPktsRate_Type()
)
anueFilterPeakGscPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakGscPktsRate.setStatus("current")
_AnueFilterPeakTimeGscPktsRate_Type = DateAndTime
_AnueFilterPeakTimeGscPktsRate_Object = MibTableColumn
anueFilterPeakTimeGscPktsRate = _AnueFilterPeakTimeGscPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 101, 1, 6),
    _AnueFilterPeakTimeGscPktsRate_Type()
)
anueFilterPeakTimeGscPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterPeakTimeGscPktsRate.setStatus("current")
_AnueFilterGTPPktType_Type = DisplayString
_AnueFilterGTPPktType_Object = MibTableColumn
anueFilterGTPPktType = _AnueFilterGTPPktType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 3, 101, 1, 7),
    _AnueFilterGTPPktType_Type()
)
anueFilterGTPPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueFilterGTPPktType.setStatus("current")
_AnueNtoStage_ObjectIdentity = ObjectIdentity
anueNtoStage = _AnueNtoStage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4)
)
_AnueNtoStageStripTable_Object = MibTable
anueNtoStageStripTable = _AnueNtoStageStripTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    anueNtoStageStripTable.setStatus("current")
_AnueNtoStageStripEntry_Object = MibTableRow
anueNtoStageStripEntry = _AnueNtoStageStripEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1)
)
anueNtoStageStripEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageStripFilterType"),
    (0, "ANUE-MIB", "anueStageStripFilterNumber"),
    (0, "ANUE-MIB", "anueStageStripFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageStripEntry.setStatus("current")
_AnueStageStripFilterType_Type = AnueFilterTypeDT
_AnueStageStripFilterType_Object = MibTableColumn
anueStageStripFilterType = _AnueStageStripFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 1),
    _AnueStageStripFilterType_Type()
)
anueStageStripFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripFilterType.setStatus("current")


class _AnueStageStripFilterNumber_Type(Integer32):
    """Custom type anueStageStripFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageStripFilterNumber_Type.__name__ = "Integer32"
_AnueStageStripFilterNumber_Object = MibTableColumn
anueStageStripFilterNumber = _AnueStageStripFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 2),
    _AnueStageStripFilterNumber_Type()
)
anueStageStripFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripFilterNumber.setStatus("current")
_AnueStageStripFeature_Type = AnueStageType
_AnueStageStripFeature_Object = MibTableColumn
anueStageStripFeature = _AnueStageStripFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 3),
    _AnueStageStripFeature_Type()
)
anueStageStripFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripFeature.setStatus("current")


class _AnueStageStripOrder_Type(Integer32):
    """Custom type anueStageStripOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageStripOrder_Type.__name__ = "Integer32"
_AnueStageStripOrder_Object = MibTableColumn
anueStageStripOrder = _AnueStageStripOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 4),
    _AnueStageStripOrder_Type()
)
anueStageStripOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripOrder.setStatus("current")


class _AnueStageStripType_Type(Integer32):
    """Custom type anueStageStripType based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("anueStageStripMplsL3Vpn", 1),
          ("anueStageStripMplsL2VpnPwcwL3Vpn", 2),
          ("anueStageStripMplsL2VpnNoPwcw", 3),
          ("anueStageStripGtp", 4),
          ("anueStageStripVlan", 5),
          ("anueStageStripVntag", 6),
          ("anueStageStripTrailer", 7),
          ("anueStageStripFabricPath", 8),
          ("anueStageStripVxlan", 9),
          ("anueStageStripL2Gre", 10),
          ("anueStageStripErspan", 11))
    )


_AnueStageStripType_Type.__name__ = "Integer32"
_AnueStageStripType_Object = MibTableColumn
anueStageStripType = _AnueStageStripType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 5),
    _AnueStageStripType_Type()
)
anueStageStripType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripType.setStatus("current")
_AnueStageStripModPkts_Type = Counter64
_AnueStageStripModPkts_Object = MibTableColumn
anueStageStripModPkts = _AnueStageStripModPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 6),
    _AnueStageStripModPkts_Type()
)
anueStageStripModPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripModPkts.setStatus("current")
_AnueStageStripModPktPct_Type = Gauge32
_AnueStageStripModPktPct_Object = MibTableColumn
anueStageStripModPktPct = _AnueStageStripModPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 7),
    _AnueStageStripModPktPct_Type()
)
anueStageStripModPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripModPktPct.setStatus("current")
_AnueStageStripErrorPkts_Type = Counter64
_AnueStageStripErrorPkts_Object = MibTableColumn
anueStageStripErrorPkts = _AnueStageStripErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 8),
    _AnueStageStripErrorPkts_Type()
)
anueStageStripErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripErrorPkts.setStatus("current")
_AnueStageStripRstModPkts_Type = Counter64
_AnueStageStripRstModPkts_Object = MibTableColumn
anueStageStripRstModPkts = _AnueStageStripRstModPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 9),
    _AnueStageStripRstModPkts_Type()
)
anueStageStripRstModPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripRstModPkts.setStatus("current")
_AnueStageStripRstModPktPct_Type = Gauge32
_AnueStageStripRstModPktPct_Object = MibTableColumn
anueStageStripRstModPktPct = _AnueStageStripRstModPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 10),
    _AnueStageStripRstModPktPct_Type()
)
anueStageStripRstModPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripRstModPktPct.setStatus("current")
_AnueStageStripRstErrorPkts_Type = Counter64
_AnueStageStripRstErrorPkts_Object = MibTableColumn
anueStageStripRstErrorPkts = _AnueStageStripRstErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 11),
    _AnueStageStripRstErrorPkts_Type()
)
anueStageStripRstErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripRstErrorPkts.setStatus("current")
_AnueStageStripAttributes_Type = DisplayString
_AnueStageStripAttributes_Object = MibTableColumn
anueStageStripAttributes = _AnueStageStripAttributes_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 1, 1, 12),
    _AnueStageStripAttributes_Type()
)
anueStageStripAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageStripAttributes.setStatus("current")
_AnueNtoStageNPErrorTable_Object = MibTable
anueNtoStageNPErrorTable = _AnueNtoStageNPErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    anueNtoStageNPErrorTable.setStatus("current")
_AnueNtoStageNPErrorEntry_Object = MibTableRow
anueNtoStageNPErrorEntry = _AnueNtoStageNPErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 2, 1)
)
anueNtoStageNPErrorEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageNPErrorFilterType"),
    (0, "ANUE-MIB", "anueStageNPErrorFilterNumber"),
    (0, "ANUE-MIB", "anueStageNPErrorFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageNPErrorEntry.setStatus("current")
_AnueStageNPErrorFilterType_Type = AnueFilterTypeDT
_AnueStageNPErrorFilterType_Object = MibTableColumn
anueStageNPErrorFilterType = _AnueStageNPErrorFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 2, 1, 1),
    _AnueStageNPErrorFilterType_Type()
)
anueStageNPErrorFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPErrorFilterType.setStatus("current")


class _AnueStageNPErrorFilterNumber_Type(Integer32):
    """Custom type anueStageNPErrorFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageNPErrorFilterNumber_Type.__name__ = "Integer32"
_AnueStageNPErrorFilterNumber_Object = MibTableColumn
anueStageNPErrorFilterNumber = _AnueStageNPErrorFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 2, 1, 2),
    _AnueStageNPErrorFilterNumber_Type()
)
anueStageNPErrorFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPErrorFilterNumber.setStatus("current")
_AnueStageNPErrorFeature_Type = AnueStageType
_AnueStageNPErrorFeature_Object = MibTableColumn
anueStageNPErrorFeature = _AnueStageNPErrorFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 2, 1, 3),
    _AnueStageNPErrorFeature_Type()
)
anueStageNPErrorFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPErrorFeature.setStatus("current")


class _AnueStageNPErrorOrder_Type(Integer32):
    """Custom type anueStageNPErrorOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageNPErrorOrder_Type.__name__ = "Integer32"
_AnueStageNPErrorOrder_Object = MibTableColumn
anueStageNPErrorOrder = _AnueStageNPErrorOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 2, 1, 4),
    _AnueStageNPErrorOrder_Type()
)
anueStageNPErrorOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPErrorOrder.setStatus("current")
_AnueStageNPErrorPkts_Type = Counter64
_AnueStageNPErrorPkts_Object = MibTableColumn
anueStageNPErrorPkts = _AnueStageNPErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 2, 1, 5),
    _AnueStageNPErrorPkts_Type()
)
anueStageNPErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPErrorPkts.setStatus("current")
_AnueStageNPErrorRstPkts_Type = Counter64
_AnueStageNPErrorRstPkts_Object = MibTableColumn
anueStageNPErrorRstPkts = _AnueStageNPErrorRstPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 2, 1, 6),
    _AnueStageNPErrorRstPkts_Type()
)
anueStageNPErrorRstPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPErrorRstPkts.setStatus("current")
_AnueNtoStageDedupTable_Object = MibTable
anueNtoStageDedupTable = _AnueNtoStageDedupTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    anueNtoStageDedupTable.setStatus("current")
_AnueNtoStageDedupEntry_Object = MibTableRow
anueNtoStageDedupEntry = _AnueNtoStageDedupEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1)
)
anueNtoStageDedupEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageDedupFilterType"),
    (0, "ANUE-MIB", "anueStageDedupFilterNumber"),
    (0, "ANUE-MIB", "anueStageDedupFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageDedupEntry.setStatus("current")
_AnueStageDedupFilterType_Type = AnueFilterTypeDT
_AnueStageDedupFilterType_Object = MibTableColumn
anueStageDedupFilterType = _AnueStageDedupFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 1),
    _AnueStageDedupFilterType_Type()
)
anueStageDedupFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupFilterType.setStatus("current")


class _AnueStageDedupFilterNumber_Type(Integer32):
    """Custom type anueStageDedupFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageDedupFilterNumber_Type.__name__ = "Integer32"
_AnueStageDedupFilterNumber_Object = MibTableColumn
anueStageDedupFilterNumber = _AnueStageDedupFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 2),
    _AnueStageDedupFilterNumber_Type()
)
anueStageDedupFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupFilterNumber.setStatus("current")
_AnueStageDedupFeature_Type = AnueStageType
_AnueStageDedupFeature_Object = MibTableColumn
anueStageDedupFeature = _AnueStageDedupFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 3),
    _AnueStageDedupFeature_Type()
)
anueStageDedupFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupFeature.setStatus("current")


class _AnueStageDedupOrder_Type(Integer32):
    """Custom type anueStageDedupOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageDedupOrder_Type.__name__ = "Integer32"
_AnueStageDedupOrder_Object = MibTableColumn
anueStageDedupOrder = _AnueStageDedupOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 4),
    _AnueStageDedupOrder_Type()
)
anueStageDedupOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupOrder.setStatus("current")


class _AnueStageDedupType_Type(Integer32):
    """Custom type anueStageDedupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("anueStageDedupNone", 1),
          ("anueStageDedupMac", 2),
          ("anueStageDedupMacVlan", 3),
          ("anueStageDedupMacVlanMpls", 4),
          ("anueStageDedupMacVlanMplsL3", 5))
    )


_AnueStageDedupType_Type.__name__ = "Integer32"
_AnueStageDedupType_Object = MibTableColumn
anueStageDedupType = _AnueStageDedupType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 5),
    _AnueStageDedupType_Type()
)
anueStageDedupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupType.setStatus("current")
_AnueStageDedupTimeWindows_Type = Integer32
_AnueStageDedupTimeWindows_Object = MibTableColumn
anueStageDedupTimeWindows = _AnueStageDedupTimeWindows_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 6),
    _AnueStageDedupTimeWindows_Type()
)
anueStageDedupTimeWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupTimeWindows.setStatus("current")
_AnueStageDedupRmvPkts_Type = Counter64
_AnueStageDedupRmvPkts_Object = MibTableColumn
anueStageDedupRmvPkts = _AnueStageDedupRmvPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 7),
    _AnueStageDedupRmvPkts_Type()
)
anueStageDedupRmvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupRmvPkts.setStatus("current")
_AnueStageDedupRmvPktPct_Type = Gauge32
_AnueStageDedupRmvPktPct_Object = MibTableColumn
anueStageDedupRmvPktPct = _AnueStageDedupRmvPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 8),
    _AnueStageDedupRmvPktPct_Type()
)
anueStageDedupRmvPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupRmvPktPct.setStatus("current")
_AnueStageDedupRstRmvPkts_Type = Counter64
_AnueStageDedupRstRmvPkts_Object = MibTableColumn
anueStageDedupRstRmvPkts = _AnueStageDedupRstRmvPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 9),
    _AnueStageDedupRstRmvPkts_Type()
)
anueStageDedupRstRmvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupRstRmvPkts.setStatus("current")
_AnueStageDedupRstRmvPktPct_Type = Gauge32
_AnueStageDedupRstRmvPktPct_Object = MibTableColumn
anueStageDedupRstRmvPktPct = _AnueStageDedupRstRmvPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 3, 1, 10),
    _AnueStageDedupRstRmvPktPct_Type()
)
anueStageDedupRstRmvPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDedupRstRmvPktPct.setStatus("current")
_AnueNtoStageTrimTable_Object = MibTable
anueNtoStageTrimTable = _AnueNtoStageTrimTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    anueNtoStageTrimTable.setStatus("current")
_AnueNtoStageTrimEntry_Object = MibTableRow
anueNtoStageTrimEntry = _AnueNtoStageTrimEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1)
)
anueNtoStageTrimEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageTrimFilterType"),
    (0, "ANUE-MIB", "anueStageTrimFilterNumber"),
    (0, "ANUE-MIB", "anueStageTrimFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageTrimEntry.setStatus("current")
_AnueStageTrimFilterType_Type = AnueFilterTypeDT
_AnueStageTrimFilterType_Object = MibTableColumn
anueStageTrimFilterType = _AnueStageTrimFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 1),
    _AnueStageTrimFilterType_Type()
)
anueStageTrimFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimFilterType.setStatus("current")


class _AnueStageTrimFilterNumber_Type(Integer32):
    """Custom type anueStageTrimFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageTrimFilterNumber_Type.__name__ = "Integer32"
_AnueStageTrimFilterNumber_Object = MibTableColumn
anueStageTrimFilterNumber = _AnueStageTrimFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 2),
    _AnueStageTrimFilterNumber_Type()
)
anueStageTrimFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimFilterNumber.setStatus("current")
_AnueStageTrimFeature_Type = AnueStageType
_AnueStageTrimFeature_Object = MibTableColumn
anueStageTrimFeature = _AnueStageTrimFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 3),
    _AnueStageTrimFeature_Type()
)
anueStageTrimFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimFeature.setStatus("current")


class _AnueStageTrimOrder_Type(Integer32):
    """Custom type anueStageTrimOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageTrimOrder_Type.__name__ = "Integer32"
_AnueStageTrimOrder_Object = MibTableColumn
anueStageTrimOrder = _AnueStageTrimOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 4),
    _AnueStageTrimOrder_Type()
)
anueStageTrimOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimOrder.setStatus("current")


class _AnueStageTrimType_Type(Integer32):
    """Custom type anueStageTrimType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("anueStageTrimRetainedMac", 1),
          ("anueStageTrimRetainedMacVlan", 2),
          ("anueStageTrimRetainedMacVlanMpls", 3),
          ("anueStageTrimRetainedMacMacVlanMplsL3", 4))
    )


_AnueStageTrimType_Type.__name__ = "Integer32"
_AnueStageTrimType_Object = MibTableColumn
anueStageTrimType = _AnueStageTrimType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 5),
    _AnueStageTrimType_Type()
)
anueStageTrimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimType.setStatus("current")
_AnueStageTrimRetainOctets_Type = Integer32
_AnueStageTrimRetainOctets_Object = MibTableColumn
anueStageTrimRetainOctets = _AnueStageTrimRetainOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 6),
    _AnueStageTrimRetainOctets_Type()
)
anueStageTrimRetainOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimRetainOctets.setStatus("current")
_AnueStageTrimModPkts_Type = Counter64
_AnueStageTrimModPkts_Object = MibTableColumn
anueStageTrimModPkts = _AnueStageTrimModPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 7),
    _AnueStageTrimModPkts_Type()
)
anueStageTrimModPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimModPkts.setStatus("current")
_AnueStageTrimModPktPct_Type = Gauge32
_AnueStageTrimModPktPct_Object = MibTableColumn
anueStageTrimModPktPct = _AnueStageTrimModPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 8),
    _AnueStageTrimModPktPct_Type()
)
anueStageTrimModPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimModPktPct.setStatus("current")
_AnueStageTrimRmvOctets_Type = Counter64
_AnueStageTrimRmvOctets_Object = MibTableColumn
anueStageTrimRmvOctets = _AnueStageTrimRmvOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 9),
    _AnueStageTrimRmvOctets_Type()
)
anueStageTrimRmvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimRmvOctets.setStatus("current")
_AnueStageTrimRmvOctetPct_Type = Gauge32
_AnueStageTrimRmvOctetPct_Object = MibTableColumn
anueStageTrimRmvOctetPct = _AnueStageTrimRmvOctetPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 10),
    _AnueStageTrimRmvOctetPct_Type()
)
anueStageTrimRmvOctetPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimRmvOctetPct.setStatus("current")
_AnueStageTrimRstModPkts_Type = Counter64
_AnueStageTrimRstModPkts_Object = MibTableColumn
anueStageTrimRstModPkts = _AnueStageTrimRstModPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 11),
    _AnueStageTrimRstModPkts_Type()
)
anueStageTrimRstModPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimRstModPkts.setStatus("current")
_AnueStageTrimRstModPktPct_Type = Gauge32
_AnueStageTrimRstModPktPct_Object = MibTableColumn
anueStageTrimRstModPktPct = _AnueStageTrimRstModPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 12),
    _AnueStageTrimRstModPktPct_Type()
)
anueStageTrimRstModPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimRstModPktPct.setStatus("current")
_AnueStageTrimRstRmvOctets_Type = Counter64
_AnueStageTrimRstRmvOctets_Object = MibTableColumn
anueStageTrimRstRmvOctets = _AnueStageTrimRstRmvOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 13),
    _AnueStageTrimRstRmvOctets_Type()
)
anueStageTrimRstRmvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimRstRmvOctets.setStatus("current")
_AnueStageTrimRstRmvOctetPct_Type = Gauge32
_AnueStageTrimRstRmvOctetPct_Object = MibTableColumn
anueStageTrimRstRmvOctetPct = _AnueStageTrimRstRmvOctetPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 4, 1, 14),
    _AnueStageTrimRstRmvOctetPct_Type()
)
anueStageTrimRstRmvOctetPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTrimRstRmvOctetPct.setStatus("current")
_AnueNtoStageBurstBufferTable_Object = MibTable
anueNtoStageBurstBufferTable = _AnueNtoStageBurstBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    anueNtoStageBurstBufferTable.setStatus("current")
_AnueNtoStageBurstBufferEntry_Object = MibTableRow
anueNtoStageBurstBufferEntry = _AnueNtoStageBurstBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1)
)
anueNtoStageBurstBufferEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageBufferFilterType"),
    (0, "ANUE-MIB", "anueStageBufferFilterNumber"),
    (0, "ANUE-MIB", "anueStageBufferFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageBurstBufferEntry.setStatus("current")
_AnueStageBufferFilterType_Type = AnueFilterTypeDT
_AnueStageBufferFilterType_Object = MibTableColumn
anueStageBufferFilterType = _AnueStageBufferFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 1),
    _AnueStageBufferFilterType_Type()
)
anueStageBufferFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferFilterType.setStatus("current")


class _AnueStageBufferFilterNumber_Type(Integer32):
    """Custom type anueStageBufferFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageBufferFilterNumber_Type.__name__ = "Integer32"
_AnueStageBufferFilterNumber_Object = MibTableColumn
anueStageBufferFilterNumber = _AnueStageBufferFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 2),
    _AnueStageBufferFilterNumber_Type()
)
anueStageBufferFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferFilterNumber.setStatus("current")
_AnueStageBufferFeature_Type = AnueStageType
_AnueStageBufferFeature_Object = MibTableColumn
anueStageBufferFeature = _AnueStageBufferFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 3),
    _AnueStageBufferFeature_Type()
)
anueStageBufferFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferFeature.setStatus("current")


class _AnueStageBufferOrder_Type(Integer32):
    """Custom type anueStageBufferOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageBufferOrder_Type.__name__ = "Integer32"
_AnueStageBufferOrder_Object = MibTableColumn
anueStageBufferOrder = _AnueStageBufferOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 4),
    _AnueStageBufferOrder_Type()
)
anueStageBufferOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferOrder.setStatus("current")
_AnueStageBufferSize_Type = Integer32
_AnueStageBufferSize_Object = MibTableColumn
anueStageBufferSize = _AnueStageBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 5),
    _AnueStageBufferSize_Type()
)
anueStageBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferSize.setStatus("current")
_AnueStageBufferCurBufferLevel_Type = Gauge32
_AnueStageBufferCurBufferLevel_Object = MibTableColumn
anueStageBufferCurBufferLevel = _AnueStageBufferCurBufferLevel_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 6),
    _AnueStageBufferCurBufferLevel_Type()
)
anueStageBufferCurBufferLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferCurBufferLevel.setStatus("current")
if mibBuilder.loadTexts:
    anueStageBufferCurBufferLevel.setUnits("Megabytes")
_AnueStageBufferPeakBufferLevel_Type = Counter32
_AnueStageBufferPeakBufferLevel_Object = MibTableColumn
anueStageBufferPeakBufferLevel = _AnueStageBufferPeakBufferLevel_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 7),
    _AnueStageBufferPeakBufferLevel_Type()
)
anueStageBufferPeakBufferLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferPeakBufferLevel.setStatus("current")
if mibBuilder.loadTexts:
    anueStageBufferPeakBufferLevel.setUnits("Megabytes")
_AnueStageBufferPeakBufferTime_Type = DateAndTime
_AnueStageBufferPeakBufferTime_Object = MibTableColumn
anueStageBufferPeakBufferTime = _AnueStageBufferPeakBufferTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 8),
    _AnueStageBufferPeakBufferTime_Type()
)
anueStageBufferPeakBufferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferPeakBufferTime.setStatus("current")
_AnueStageBufferDropPkts_Type = Counter64
_AnueStageBufferDropPkts_Object = MibTableColumn
anueStageBufferDropPkts = _AnueStageBufferDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 9),
    _AnueStageBufferDropPkts_Type()
)
anueStageBufferDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferDropPkts.setStatus("current")
_AnueStageBufferDropTime_Type = DateAndTime
_AnueStageBufferDropTime_Object = MibTableColumn
anueStageBufferDropTime = _AnueStageBufferDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 10),
    _AnueStageBufferDropTime_Type()
)
anueStageBufferDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferDropTime.setStatus("current")
_AnueStageBufferRstDropPkts_Type = Counter64
_AnueStageBufferRstDropPkts_Object = MibTableColumn
anueStageBufferRstDropPkts = _AnueStageBufferRstDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 11),
    _AnueStageBufferRstDropPkts_Type()
)
anueStageBufferRstDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferRstDropPkts.setStatus("current")
_AnueStageBufferRstDropTime_Type = DateAndTime
_AnueStageBufferRstDropTime_Object = MibTableColumn
anueStageBufferRstDropTime = _AnueStageBufferRstDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 5, 1, 12),
    _AnueStageBufferRstDropTime_Type()
)
anueStageBufferRstDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageBufferRstDropTime.setStatus("current")
_AnueNtoStageNPFilterTable_Object = MibTable
anueNtoStageNPFilterTable = _AnueNtoStageNPFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    anueNtoStageNPFilterTable.setStatus("current")
_AnueNtoStageNPFilterEntry_Object = MibTableRow
anueNtoStageNPFilterEntry = _AnueNtoStageNPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1)
)
anueNtoStageNPFilterEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageNPFilterFilterType"),
    (0, "ANUE-MIB", "anueStageNPFilterFilterNumber"),
    (0, "ANUE-MIB", "anueStageNPFilterFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageNPFilterEntry.setStatus("current")
_AnueStageNPFilterFilterType_Type = AnueFilterTypeDT
_AnueStageNPFilterFilterType_Object = MibTableColumn
anueStageNPFilterFilterType = _AnueStageNPFilterFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 1),
    _AnueStageNPFilterFilterType_Type()
)
anueStageNPFilterFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterFilterType.setStatus("current")


class _AnueStageNPFilterFilterNumber_Type(Integer32):
    """Custom type anueStageNPFilterFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageNPFilterFilterNumber_Type.__name__ = "Integer32"
_AnueStageNPFilterFilterNumber_Object = MibTableColumn
anueStageNPFilterFilterNumber = _AnueStageNPFilterFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 2),
    _AnueStageNPFilterFilterNumber_Type()
)
anueStageNPFilterFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterFilterNumber.setStatus("current")
_AnueStageNPFilterFeature_Type = AnueStageType
_AnueStageNPFilterFeature_Object = MibTableColumn
anueStageNPFilterFeature = _AnueStageNPFilterFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 3),
    _AnueStageNPFilterFeature_Type()
)
anueStageNPFilterFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterFeature.setStatus("current")


class _AnueStageNPFilterOrder_Type(Integer32):
    """Custom type anueStageNPFilterOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageNPFilterOrder_Type.__name__ = "Integer32"
_AnueStageNPFilterOrder_Object = MibTableColumn
anueStageNPFilterOrder = _AnueStageNPFilterOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 4),
    _AnueStageNPFilterOrder_Type()
)
anueStageNPFilterOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterOrder.setStatus("current")
_AnueStageNPFilterDenyPkts_Type = Counter64
_AnueStageNPFilterDenyPkts_Object = MibTableColumn
anueStageNPFilterDenyPkts = _AnueStageNPFilterDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 5),
    _AnueStageNPFilterDenyPkts_Type()
)
anueStageNPFilterDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterDenyPkts.setStatus("current")
_AnueStageNPFilterDenyPktPct_Type = Gauge32
_AnueStageNPFilterDenyPktPct_Object = MibTableColumn
anueStageNPFilterDenyPktPct = _AnueStageNPFilterDenyPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 6),
    _AnueStageNPFilterDenyPktPct_Type()
)
anueStageNPFilterDenyPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterDenyPktPct.setStatus("current")
_AnueStageNPFilterDenyOctets_Type = Counter64
_AnueStageNPFilterDenyOctets_Object = MibTableColumn
anueStageNPFilterDenyOctets = _AnueStageNPFilterDenyOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 7),
    _AnueStageNPFilterDenyOctets_Type()
)
anueStageNPFilterDenyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterDenyOctets.setStatus("current")
_AnueStageNPFilterDenyOctetPct_Type = Gauge32
_AnueStageNPFilterDenyOctetPct_Object = MibTableColumn
anueStageNPFilterDenyOctetPct = _AnueStageNPFilterDenyOctetPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 8),
    _AnueStageNPFilterDenyOctetPct_Type()
)
anueStageNPFilterDenyOctetPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterDenyOctetPct.setStatus("current")
_AnueStageNPFilterRstDenyPkts_Type = Counter64
_AnueStageNPFilterRstDenyPkts_Object = MibTableColumn
anueStageNPFilterRstDenyPkts = _AnueStageNPFilterRstDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 9),
    _AnueStageNPFilterRstDenyPkts_Type()
)
anueStageNPFilterRstDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterRstDenyPkts.setStatus("current")
_AnueStageNPFilterRstDenyPktPct_Type = Gauge32
_AnueStageNPFilterRstDenyPktPct_Object = MibTableColumn
anueStageNPFilterRstDenyPktPct = _AnueStageNPFilterRstDenyPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 10),
    _AnueStageNPFilterRstDenyPktPct_Type()
)
anueStageNPFilterRstDenyPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterRstDenyPktPct.setStatus("current")
_AnueStageNPFilterRstDenyOctets_Type = Counter64
_AnueStageNPFilterRstDenyOctets_Object = MibTableColumn
anueStageNPFilterRstDenyOctets = _AnueStageNPFilterRstDenyOctets_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 11),
    _AnueStageNPFilterRstDenyOctets_Type()
)
anueStageNPFilterRstDenyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterRstDenyOctets.setStatus("current")
_AnueStageNPFilterRstDenyOctetPct_Type = Gauge32
_AnueStageNPFilterRstDenyOctetPct_Object = MibTableColumn
anueStageNPFilterRstDenyOctetPct = _AnueStageNPFilterRstDenyOctetPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 6, 1, 12),
    _AnueStageNPFilterRstDenyOctetPct_Type()
)
anueStageNPFilterRstDenyOctetPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageNPFilterRstDenyOctetPct.setStatus("current")
_AnueNtoStageTPFilterTable_Object = MibTable
anueNtoStageTPFilterTable = _AnueNtoStageTPFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    anueNtoStageTPFilterTable.setStatus("current")
_AnueNtoStageTPFilterEntry_Object = MibTableRow
anueNtoStageTPFilterEntry = _AnueNtoStageTPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1)
)
anueNtoStageTPFilterEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageTPFilterFilterType"),
    (0, "ANUE-MIB", "anueStageTPFilterFilterNumber"),
    (0, "ANUE-MIB", "anueStageTPFilterFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageTPFilterEntry.setStatus("current")
_AnueStageTPFilterFilterType_Type = AnueFilterTypeDT
_AnueStageTPFilterFilterType_Object = MibTableColumn
anueStageTPFilterFilterType = _AnueStageTPFilterFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 1),
    _AnueStageTPFilterFilterType_Type()
)
anueStageTPFilterFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterFilterType.setStatus("current")


class _AnueStageTPFilterFilterNumber_Type(Integer32):
    """Custom type anueStageTPFilterFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageTPFilterFilterNumber_Type.__name__ = "Integer32"
_AnueStageTPFilterFilterNumber_Object = MibTableColumn
anueStageTPFilterFilterNumber = _AnueStageTPFilterFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 2),
    _AnueStageTPFilterFilterNumber_Type()
)
anueStageTPFilterFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterFilterNumber.setStatus("current")
_AnueStageTPFilterFeature_Type = AnueStageType
_AnueStageTPFilterFeature_Object = MibTableColumn
anueStageTPFilterFeature = _AnueStageTPFilterFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 3),
    _AnueStageTPFilterFeature_Type()
)
anueStageTPFilterFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterFeature.setStatus("current")


class _AnueStageTPFilterOrder_Type(Integer32):
    """Custom type anueStageTPFilterOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageTPFilterOrder_Type.__name__ = "Integer32"
_AnueStageTPFilterOrder_Object = MibTableColumn
anueStageTPFilterOrder = _AnueStageTPFilterOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 4),
    _AnueStageTPFilterOrder_Type()
)
anueStageTPFilterOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterOrder.setStatus("current")
_AnueStageTPFilterDenyPkts_Type = Counter64
_AnueStageTPFilterDenyPkts_Object = MibTableColumn
anueStageTPFilterDenyPkts = _AnueStageTPFilterDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 5),
    _AnueStageTPFilterDenyPkts_Type()
)
anueStageTPFilterDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterDenyPkts.setStatus("current")
_AnueStageTPFilterDenyPktPct_Type = Gauge32
_AnueStageTPFilterDenyPktPct_Object = MibTableColumn
anueStageTPFilterDenyPktPct = _AnueStageTPFilterDenyPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 6),
    _AnueStageTPFilterDenyPktPct_Type()
)
anueStageTPFilterDenyPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterDenyPktPct.setStatus("current")
_AnueStageTPFilterDropPkts_Type = Counter64
_AnueStageTPFilterDropPkts_Object = MibTableColumn
anueStageTPFilterDropPkts = _AnueStageTPFilterDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 7),
    _AnueStageTPFilterDropPkts_Type()
)
anueStageTPFilterDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterDropPkts.setStatus("current")
_AnueStageTPFilterDropTime_Type = DateAndTime
_AnueStageTPFilterDropTime_Object = MibTableColumn
anueStageTPFilterDropTime = _AnueStageTPFilterDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 8),
    _AnueStageTPFilterDropTime_Type()
)
anueStageTPFilterDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterDropTime.setStatus("current")
_AnueStageTPFilterRstDenyPkts_Type = Counter64
_AnueStageTPFilterRstDenyPkts_Object = MibTableColumn
anueStageTPFilterRstDenyPkts = _AnueStageTPFilterRstDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 9),
    _AnueStageTPFilterRstDenyPkts_Type()
)
anueStageTPFilterRstDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterRstDenyPkts.setStatus("current")
_AnueStageTPFilterRstDenyPktPct_Type = Gauge32
_AnueStageTPFilterRstDenyPktPct_Object = MibTableColumn
anueStageTPFilterRstDenyPktPct = _AnueStageTPFilterRstDenyPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 10),
    _AnueStageTPFilterRstDenyPktPct_Type()
)
anueStageTPFilterRstDenyPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterRstDenyPktPct.setStatus("current")
_AnueStageTPFilterRstDropPkts_Type = Counter64
_AnueStageTPFilterRstDropPkts_Object = MibTableColumn
anueStageTPFilterRstDropPkts = _AnueStageTPFilterRstDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 11),
    _AnueStageTPFilterRstDropPkts_Type()
)
anueStageTPFilterRstDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterRstDropPkts.setStatus("current")
_AnueStageTPFilterRstDropTime_Type = DateAndTime
_AnueStageTPFilterRstDropTime_Object = MibTableColumn
anueStageTPFilterRstDropTime = _AnueStageTPFilterRstDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 7, 1, 12),
    _AnueStageTPFilterRstDropTime_Type()
)
anueStageTPFilterRstDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTPFilterRstDropTime.setStatus("current")
_AnueNtoStageAfmDropTable_Object = MibTable
anueNtoStageAfmDropTable = _AnueNtoStageAfmDropTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    anueNtoStageAfmDropTable.setStatus("current")
_AnueNtoStageAfmDropEntry_Object = MibTableRow
anueNtoStageAfmDropEntry = _AnueNtoStageAfmDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8, 1)
)
anueNtoStageAfmDropEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageAfmDropFilterType"),
    (0, "ANUE-MIB", "anueStageAfmDropFilterNumber"),
    (0, "ANUE-MIB", "anueStageAfmDropFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageAfmDropEntry.setStatus("current")
_AnueStageAfmDropFilterType_Type = AnueFilterTypeDT
_AnueStageAfmDropFilterType_Object = MibTableColumn
anueStageAfmDropFilterType = _AnueStageAfmDropFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8, 1, 1),
    _AnueStageAfmDropFilterType_Type()
)
anueStageAfmDropFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageAfmDropFilterType.setStatus("current")


class _AnueStageAfmDropFilterNumber_Type(Integer32):
    """Custom type anueStageAfmDropFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageAfmDropFilterNumber_Type.__name__ = "Integer32"
_AnueStageAfmDropFilterNumber_Object = MibTableColumn
anueStageAfmDropFilterNumber = _AnueStageAfmDropFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8, 1, 2),
    _AnueStageAfmDropFilterNumber_Type()
)
anueStageAfmDropFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageAfmDropFilterNumber.setStatus("current")
_AnueStageAfmDropFeature_Type = AnueStageType
_AnueStageAfmDropFeature_Object = MibTableColumn
anueStageAfmDropFeature = _AnueStageAfmDropFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8, 1, 3),
    _AnueStageAfmDropFeature_Type()
)
anueStageAfmDropFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageAfmDropFeature.setStatus("current")


class _AnueStageAfmDropOrder_Type(Integer32):
    """Custom type anueStageAfmDropOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageAfmDropOrder_Type.__name__ = "Integer32"
_AnueStageAfmDropOrder_Object = MibTableColumn
anueStageAfmDropOrder = _AnueStageAfmDropOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8, 1, 4),
    _AnueStageAfmDropOrder_Type()
)
anueStageAfmDropOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageAfmDropOrder.setStatus("current")
_AnueStageAfmDropDropPkts_Type = Counter64
_AnueStageAfmDropDropPkts_Object = MibTableColumn
anueStageAfmDropDropPkts = _AnueStageAfmDropDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8, 1, 5),
    _AnueStageAfmDropDropPkts_Type()
)
anueStageAfmDropDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageAfmDropDropPkts.setStatus("current")
_AnueStageAfmDropDropTime_Type = DateAndTime
_AnueStageAfmDropDropTime_Object = MibTableColumn
anueStageAfmDropDropTime = _AnueStageAfmDropDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8, 1, 6),
    _AnueStageAfmDropDropTime_Type()
)
anueStageAfmDropDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageAfmDropDropTime.setStatus("current")
_AnueStageAfmDropRstDropPkts_Type = Counter64
_AnueStageAfmDropRstDropPkts_Object = MibTableColumn
anueStageAfmDropRstDropPkts = _AnueStageAfmDropRstDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8, 1, 7),
    _AnueStageAfmDropRstDropPkts_Type()
)
anueStageAfmDropRstDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageAfmDropRstDropPkts.setStatus("current")
_AnueStageAfmDropRstDropTime_Type = DateAndTime
_AnueStageAfmDropRstDropTime_Object = MibTableColumn
anueStageAfmDropRstDropTime = _AnueStageAfmDropRstDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 8, 1, 8),
    _AnueStageAfmDropRstDropTime_Type()
)
anueStageAfmDropRstDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageAfmDropRstDropTime.setStatus("current")
_AnueNtoStageTagTable_Object = MibTable
anueNtoStageTagTable = _AnueNtoStageTagTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9)
)
if mibBuilder.loadTexts:
    anueNtoStageTagTable.setStatus("current")
_AnueNtoStageTagEntry_Object = MibTableRow
anueNtoStageTagEntry = _AnueNtoStageTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1)
)
anueNtoStageTagEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageTagFilterType"),
    (0, "ANUE-MIB", "anueStageTagFilterNumber"),
    (0, "ANUE-MIB", "anueStageTagFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageTagEntry.setStatus("current")
_AnueStageTagFilterType_Type = AnueFilterTypeDT
_AnueStageTagFilterType_Object = MibTableColumn
anueStageTagFilterType = _AnueStageTagFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1, 1),
    _AnueStageTagFilterType_Type()
)
anueStageTagFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTagFilterType.setStatus("current")


class _AnueStageTagFilterNumber_Type(Integer32):
    """Custom type anueStageTagFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageTagFilterNumber_Type.__name__ = "Integer32"
_AnueStageTagFilterNumber_Object = MibTableColumn
anueStageTagFilterNumber = _AnueStageTagFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1, 2),
    _AnueStageTagFilterNumber_Type()
)
anueStageTagFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTagFilterNumber.setStatus("current")
_AnueStageTagFeature_Type = AnueStageType
_AnueStageTagFeature_Object = MibTableColumn
anueStageTagFeature = _AnueStageTagFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1, 3),
    _AnueStageTagFeature_Type()
)
anueStageTagFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTagFeature.setStatus("current")


class _AnueStageTagOrder_Type(Integer32):
    """Custom type anueStageTagOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageTagOrder_Type.__name__ = "Integer32"
_AnueStageTagOrder_Object = MibTableColumn
anueStageTagOrder = _AnueStageTagOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1, 4),
    _AnueStageTagOrder_Type()
)
anueStageTagOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTagOrder.setStatus("current")
_AnueStageTagAttributes_Type = DisplayString
_AnueStageTagAttributes_Object = MibTableColumn
anueStageTagAttributes = _AnueStageTagAttributes_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1, 5),
    _AnueStageTagAttributes_Type()
)
anueStageTagAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTagAttributes.setStatus("current")
_AnueStageTagModPkts_Type = Counter64
_AnueStageTagModPkts_Object = MibTableColumn
anueStageTagModPkts = _AnueStageTagModPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1, 6),
    _AnueStageTagModPkts_Type()
)
anueStageTagModPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTagModPkts.setStatus("current")
_AnueStageTagModPktPct_Type = Gauge32
_AnueStageTagModPktPct_Object = MibTableColumn
anueStageTagModPktPct = _AnueStageTagModPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1, 7),
    _AnueStageTagModPktPct_Type()
)
anueStageTagModPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTagModPktPct.setStatus("current")
_AnueStageTagRstModPkts_Type = Counter64
_AnueStageTagRstModPkts_Object = MibTableColumn
anueStageTagRstModPkts = _AnueStageTagRstModPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1, 8),
    _AnueStageTagRstModPkts_Type()
)
anueStageTagRstModPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTagRstModPkts.setStatus("current")
_AnueStageTagRstModPktPct_Type = Gauge32
_AnueStageTagRstModPktPct_Object = MibTableColumn
anueStageTagRstModPktPct = _AnueStageTagRstModPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 9, 1, 9),
    _AnueStageTagRstModPktPct_Type()
)
anueStageTagRstModPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageTagRstModPktPct.setStatus("current")
_AnueNtoStageDropTable_Object = MibTable
anueNtoStageDropTable = _AnueNtoStageDropTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10)
)
if mibBuilder.loadTexts:
    anueNtoStageDropTable.setStatus("current")
_AnueNtoStageDropEntry_Object = MibTableRow
anueNtoStageDropEntry = _AnueNtoStageDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1)
)
anueNtoStageDropEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageDropFilterType"),
    (0, "ANUE-MIB", "anueStageDropFilterNumber"),
    (0, "ANUE-MIB", "anueStageDropFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageDropEntry.setStatus("current")
_AnueStageDropFilterType_Type = AnueFilterTypeDT
_AnueStageDropFilterType_Object = MibTableColumn
anueStageDropFilterType = _AnueStageDropFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1, 1),
    _AnueStageDropFilterType_Type()
)
anueStageDropFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDropFilterType.setStatus("current")


class _AnueStageDropFilterNumber_Type(Integer32):
    """Custom type anueStageDropFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageDropFilterNumber_Type.__name__ = "Integer32"
_AnueStageDropFilterNumber_Object = MibTableColumn
anueStageDropFilterNumber = _AnueStageDropFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1, 2),
    _AnueStageDropFilterNumber_Type()
)
anueStageDropFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDropFilterNumber.setStatus("current")
_AnueStageDropFeature_Type = AnueStageType
_AnueStageDropFeature_Object = MibTableColumn
anueStageDropFeature = _AnueStageDropFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1, 3),
    _AnueStageDropFeature_Type()
)
anueStageDropFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDropFeature.setStatus("current")
_AnueStageCntDropPkts_Type = Counter64
_AnueStageCntDropPkts_Object = MibTableColumn
anueStageCntDropPkts = _AnueStageCntDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1, 4),
    _AnueStageCntDropPkts_Type()
)
anueStageCntDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageCntDropPkts.setStatus("current")
_AnueStageCntDropTime_Type = DateAndTime
_AnueStageCntDropTime_Object = MibTableColumn
anueStageCntDropTime = _AnueStageCntDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1, 5),
    _AnueStageCntDropTime_Type()
)
anueStageCntDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageCntDropTime.setStatus("current")
_AnueStageCurDropPkts_Type = Counter64
_AnueStageCurDropPkts_Object = MibTableColumn
anueStageCurDropPkts = _AnueStageCurDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1, 6),
    _AnueStageCurDropPkts_Type()
)
anueStageCurDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageCurDropPkts.setStatus("current")
_AnueStageAvgDropPkts_Type = Counter64
_AnueStageAvgDropPkts_Object = MibTableColumn
anueStageAvgDropPkts = _AnueStageAvgDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1, 7),
    _AnueStageAvgDropPkts_Type()
)
anueStageAvgDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageAvgDropPkts.setStatus("current")
_AnueStagePeakDropPkts_Type = Counter64
_AnueStagePeakDropPkts_Object = MibTableColumn
anueStagePeakDropPkts = _AnueStagePeakDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1, 8),
    _AnueStagePeakDropPkts_Type()
)
anueStagePeakDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStagePeakDropPkts.setStatus("current")
_AnueStagePeakDropTime_Type = DateAndTime
_AnueStagePeakDropTime_Object = MibTableColumn
anueStagePeakDropTime = _AnueStagePeakDropTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 10, 1, 9),
    _AnueStagePeakDropTime_Type()
)
anueStagePeakDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStagePeakDropTime.setStatus("current")
_AnueNtoStageGtpFdTable_Object = MibTable
anueNtoStageGtpFdTable = _AnueNtoStageGtpFdTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 11)
)
if mibBuilder.loadTexts:
    anueNtoStageGtpFdTable.setStatus("current")
_AnueNtoStageGtpFdEntry_Object = MibTableRow
anueNtoStageGtpFdEntry = _AnueNtoStageGtpFdEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 11, 1)
)
anueNtoStageGtpFdEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageGtpFdFilterType"),
    (0, "ANUE-MIB", "anueStageGtpFdFilterNumber"),
    (0, "ANUE-MIB", "anueStageGtpFdFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageGtpFdEntry.setStatus("current")
_AnueStageGtpFdFilterType_Type = AnueFilterTypeDT
_AnueStageGtpFdFilterType_Object = MibTableColumn
anueStageGtpFdFilterType = _AnueStageGtpFdFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 11, 1, 1),
    _AnueStageGtpFdFilterType_Type()
)
anueStageGtpFdFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageGtpFdFilterType.setStatus("current")


class _AnueStageGtpFdFilterNumber_Type(Integer32):
    """Custom type anueStageGtpFdFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageGtpFdFilterNumber_Type.__name__ = "Integer32"
_AnueStageGtpFdFilterNumber_Object = MibTableColumn
anueStageGtpFdFilterNumber = _AnueStageGtpFdFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 11, 1, 2),
    _AnueStageGtpFdFilterNumber_Type()
)
anueStageGtpFdFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageGtpFdFilterNumber.setStatus("current")
_AnueStageGtpFdFeature_Type = AnueStageType
_AnueStageGtpFdFeature_Object = MibTableColumn
anueStageGtpFdFeature = _AnueStageGtpFdFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 11, 1, 3),
    _AnueStageGtpFdFeature_Type()
)
anueStageGtpFdFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageGtpFdFeature.setStatus("current")
_AnueStageRateGtpCPps_Type = Counter64
_AnueStageRateGtpCPps_Object = MibTableColumn
anueStageRateGtpCPps = _AnueStageRateGtpCPps_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 11, 1, 4),
    _AnueStageRateGtpCPps_Type()
)
anueStageRateGtpCPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageRateGtpCPps.setStatus("current")
_AnueStageRateGtpUPps_Type = Counter64
_AnueStageRateGtpUPps_Object = MibTableColumn
anueStageRateGtpUPps = _AnueStageRateGtpUPps_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 11, 1, 5),
    _AnueStageRateGtpUPps_Type()
)
anueStageRateGtpUPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageRateGtpUPps.setStatus("current")
_AnueStageRateGtpCBps_Type = Counter64
_AnueStageRateGtpCBps_Object = MibTableColumn
anueStageRateGtpCBps = _AnueStageRateGtpCBps_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 11, 1, 6),
    _AnueStageRateGtpCBps_Type()
)
anueStageRateGtpCBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageRateGtpCBps.setStatus("current")
_AnueStageRateGtpUBps_Type = Counter64
_AnueStageRateGtpUBps_Object = MibTableColumn
anueStageRateGtpUBps = _AnueStageRateGtpUBps_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 11, 1, 7),
    _AnueStageRateGtpUBps_Type()
)
anueStageRateGtpUBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageRateGtpUBps.setStatus("current")
_AnueNtoStageDataMaskingTable_Object = MibTable
anueNtoStageDataMaskingTable = _AnueNtoStageDataMaskingTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12)
)
if mibBuilder.loadTexts:
    anueNtoStageDataMaskingTable.setStatus("current")
_AnueNtoStageDataMaskingEntry_Object = MibTableRow
anueNtoStageDataMaskingEntry = _AnueNtoStageDataMaskingEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1)
)
anueNtoStageDataMaskingEntry.setIndexNames(
    (0, "ANUE-MIB", "anueStageDataMaskingFilterType"),
    (0, "ANUE-MIB", "anueStageDataMaskingFilterNumber"),
    (0, "ANUE-MIB", "anueStageDataMaskingFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageDataMaskingEntry.setStatus("current")
_AnueStageDataMaskingFilterType_Type = AnueFilterTypeDT
_AnueStageDataMaskingFilterType_Object = MibTableColumn
anueStageDataMaskingFilterType = _AnueStageDataMaskingFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 1),
    _AnueStageDataMaskingFilterType_Type()
)
anueStageDataMaskingFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingFilterType.setStatus("current")


class _AnueStageDataMaskingFilterNumber_Type(Integer32):
    """Custom type anueStageDataMaskingFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageDataMaskingFilterNumber_Type.__name__ = "Integer32"
_AnueStageDataMaskingFilterNumber_Object = MibTableColumn
anueStageDataMaskingFilterNumber = _AnueStageDataMaskingFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 2),
    _AnueStageDataMaskingFilterNumber_Type()
)
anueStageDataMaskingFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingFilterNumber.setStatus("current")
_AnueStageDataMaskingFeature_Type = AnueStageType
_AnueStageDataMaskingFeature_Object = MibTableColumn
anueStageDataMaskingFeature = _AnueStageDataMaskingFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 3),
    _AnueStageDataMaskingFeature_Type()
)
anueStageDataMaskingFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingFeature.setStatus("current")


class _AnueStageDataMaskingOrder_Type(Integer32):
    """Custom type anueStageDataMaskingOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueStageDataMaskingOrder_Type.__name__ = "Integer32"
_AnueStageDataMaskingOrder_Object = MibTableColumn
anueStageDataMaskingOrder = _AnueStageDataMaskingOrder_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 4),
    _AnueStageDataMaskingOrder_Type()
)
anueStageDataMaskingOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingOrder.setStatus("current")


class _AnueStageDataMaskingOffsetLayer_Type(Integer32):
    """Custom type anueStageDataMaskingOffsetLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anueStageDataMaskingL2Start", 1),
          ("anueStageDataMaskingL2End", 2),
          ("anueStageDataMaskingL3End", 3))
    )


_AnueStageDataMaskingOffsetLayer_Type.__name__ = "Integer32"
_AnueStageDataMaskingOffsetLayer_Object = MibTableColumn
anueStageDataMaskingOffsetLayer = _AnueStageDataMaskingOffsetLayer_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 5),
    _AnueStageDataMaskingOffsetLayer_Type()
)
anueStageDataMaskingOffsetLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingOffsetLayer.setStatus("current")
_AnueStageDataMaskingOffset_Type = Counter64
_AnueStageDataMaskingOffset_Object = MibTableColumn
anueStageDataMaskingOffset = _AnueStageDataMaskingOffset_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 6),
    _AnueStageDataMaskingOffset_Type()
)
anueStageDataMaskingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingOffset.setStatus("current")
_AnueStageDataMaskingLength_Type = Counter64
_AnueStageDataMaskingLength_Object = MibTableColumn
anueStageDataMaskingLength = _AnueStageDataMaskingLength_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 7),
    _AnueStageDataMaskingLength_Type()
)
anueStageDataMaskingLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingLength.setStatus("current")
_AnueStageDataMaskingFillValue_Type = OctetString
_AnueStageDataMaskingFillValue_Object = MibTableColumn
anueStageDataMaskingFillValue = _AnueStageDataMaskingFillValue_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 8),
    _AnueStageDataMaskingFillValue_Type()
)
anueStageDataMaskingFillValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingFillValue.setStatus("current")
_AnueStageDataMaskingModPkts_Type = Counter64
_AnueStageDataMaskingModPkts_Object = MibTableColumn
anueStageDataMaskingModPkts = _AnueStageDataMaskingModPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 9),
    _AnueStageDataMaskingModPkts_Type()
)
anueStageDataMaskingModPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingModPkts.setStatus("current")
_AnueStageDataMaskingModPktPct_Type = Gauge32
_AnueStageDataMaskingModPktPct_Object = MibTableColumn
anueStageDataMaskingModPktPct = _AnueStageDataMaskingModPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 10),
    _AnueStageDataMaskingModPktPct_Type()
)
anueStageDataMaskingModPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingModPktPct.setStatus("current")
_AnueStageDataMaskingRstModPkts_Type = Counter64
_AnueStageDataMaskingRstModPkts_Object = MibTableColumn
anueStageDataMaskingRstModPkts = _AnueStageDataMaskingRstModPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 11),
    _AnueStageDataMaskingRstModPkts_Type()
)
anueStageDataMaskingRstModPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingRstModPkts.setStatus("current")
_AnueStageDataMaskingRstModPktPct_Type = Gauge32
_AnueStageDataMaskingRstModPktPct_Object = MibTableColumn
anueStageDataMaskingRstModPktPct = _AnueStageDataMaskingRstModPktPct_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 12, 1, 12),
    _AnueStageDataMaskingRstModPktPct_Type()
)
anueStageDataMaskingRstModPktPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueStageDataMaskingRstModPktPct.setStatus("current")
_AnueNtoStageGscNetworkFilterTable_Object = MibTable
anueNtoStageGscNetworkFilterTable = _AnueNtoStageGscNetworkFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100)
)
if mibBuilder.loadTexts:
    anueNtoStageGscNetworkFilterTable.setStatus("current")
_AnueNtoStageGscNetworkFilterEntry_Object = MibTableRow
anueNtoStageGscNetworkFilterEntry = _AnueNtoStageGscNetworkFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1)
)
anueNtoStageGscNetworkFilterEntry.setIndexNames(
    (0, "ANUE-MIB", "anueNtoStageGscNetworkFilterType"),
    (0, "ANUE-MIB", "anueNtoStageGscNetworkFilterNumber"),
    (0, "ANUE-MIB", "anueNtoStageGscNetworkFilterFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageGscNetworkFilterEntry.setStatus("current")
_AnueNtoStageGscNetworkFilterType_Type = AnueFilterTypeDT
_AnueNtoStageGscNetworkFilterType_Object = MibTableColumn
anueNtoStageGscNetworkFilterType = _AnueNtoStageGscNetworkFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 1),
    _AnueNtoStageGscNetworkFilterType_Type()
)
anueNtoStageGscNetworkFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueNtoStageGscNetworkFilterType.setStatus("current")


class _AnueNtoStageGscNetworkFilterNumber_Type(Integer32):
    """Custom type anueNtoStageGscNetworkFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueNtoStageGscNetworkFilterNumber_Type.__name__ = "Integer32"
_AnueNtoStageGscNetworkFilterNumber_Object = MibTableColumn
anueNtoStageGscNetworkFilterNumber = _AnueNtoStageGscNetworkFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 2),
    _AnueNtoStageGscNetworkFilterNumber_Type()
)
anueNtoStageGscNetworkFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueNtoStageGscNetworkFilterNumber.setStatus("current")
_AnueGscNWFltrExcSess_Type = Counter64
_AnueGscNWFltrExcSess_Object = MibTableColumn
anueGscNWFltrExcSess = _AnueGscNWFltrExcSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 3),
    _AnueGscNWFltrExcSess_Type()
)
anueGscNWFltrExcSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrExcSess.setStatus("current")
_AnueNtoStageGscNetworkFilterFeature_Type = AnueStageType
_AnueNtoStageGscNetworkFilterFeature_Object = MibTableColumn
anueNtoStageGscNetworkFilterFeature = _AnueNtoStageGscNetworkFilterFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 4),
    _AnueNtoStageGscNetworkFilterFeature_Type()
)
anueNtoStageGscNetworkFilterFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueNtoStageGscNetworkFilterFeature.setStatus("current")
_AnueGscNWFltrAvgGscPktFrag_Type = Counter64
_AnueGscNWFltrAvgGscPktFrag_Object = MibTableColumn
anueGscNWFltrAvgGscPktFrag = _AnueGscNWFltrAvgGscPktFrag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 5),
    _AnueGscNWFltrAvgGscPktFrag_Type()
)
anueGscNWFltrAvgGscPktFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGscPktFrag.setStatus("current")
_AnueGscNWFltrAvgTdoutFrag_Type = Counter64
_AnueGscNWFltrAvgTdoutFrag_Object = MibTableColumn
anueGscNWFltrAvgTdoutFrag = _AnueGscNWFltrAvgTdoutFrag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 6),
    _AnueGscNWFltrAvgTdoutFrag_Type()
)
anueGscNWFltrAvgTdoutFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgTdoutFrag.setStatus("current")
_AnueGscNWFltrCurPacketFrag_Type = Counter64
_AnueGscNWFltrCurPacketFrag_Object = MibTableColumn
anueGscNWFltrCurPacketFrag = _AnueGscNWFltrCurPacketFrag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 7),
    _AnueGscNWFltrCurPacketFrag_Type()
)
anueGscNWFltrCurPacketFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurPacketFrag.setStatus("current")
_AnueGscNWFltrCurTdoutFrag_Type = Counter64
_AnueGscNWFltrCurTdoutFrag_Object = MibTableColumn
anueGscNWFltrCurTdoutFrag = _AnueGscNWFltrCurTdoutFrag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 8),
    _AnueGscNWFltrCurTdoutFrag_Type()
)
anueGscNWFltrCurTdoutFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurTdoutFrag.setStatus("current")
_AnueGscNWFltrPkPacketFrag_Type = Counter64
_AnueGscNWFltrPkPacketFrag_Object = MibTableColumn
anueGscNWFltrPkPacketFrag = _AnueGscNWFltrPkPacketFrag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 9),
    _AnueGscNWFltrPkPacketFrag_Type()
)
anueGscNWFltrPkPacketFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkPacketFrag.setStatus("current")
_AnueGscNWFltrPkPacketFragT_Type = DateAndTime
_AnueGscNWFltrPkPacketFragT_Object = MibTableColumn
anueGscNWFltrPkPacketFragT = _AnueGscNWFltrPkPacketFragT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 10),
    _AnueGscNWFltrPkPacketFragT_Type()
)
anueGscNWFltrPkPacketFragT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkPacketFragT.setStatus("current")
_AnueGscNWFltrPkTdOutFrag_Type = Counter64
_AnueGscNWFltrPkTdOutFrag_Object = MibTableColumn
anueGscNWFltrPkTdOutFrag = _AnueGscNWFltrPkTdOutFrag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 11),
    _AnueGscNWFltrPkTdOutFrag_Type()
)
anueGscNWFltrPkTdOutFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkTdOutFrag.setStatus("current")
_AnueGscNWFltrPkTdOutFragT_Type = DateAndTime
_AnueGscNWFltrPkTdOutFragT_Object = MibTableColumn
anueGscNWFltrPkTdOutFragT = _AnueGscNWFltrPkTdOutFragT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 12),
    _AnueGscNWFltrPkTdOutFragT_Type()
)
anueGscNWFltrPkTdOutFragT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkTdOutFragT.setStatus("current")
_AnueGscNWFltrTotFrag_Type = Counter64
_AnueGscNWFltrTotFrag_Object = MibTableColumn
anueGscNWFltrTotFrag = _AnueGscNWFltrTotFrag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 13),
    _AnueGscNWFltrTotFrag_Type()
)
anueGscNWFltrTotFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotFrag.setStatus("current")
_AnueGscNWFltrTotRxCountFrag_Type = Counter64
_AnueGscNWFltrTotRxCountFrag_Object = MibTableColumn
anueGscNWFltrTotRxCountFrag = _AnueGscNWFltrTotRxCountFrag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 14),
    _AnueGscNWFltrTotRxCountFrag_Type()
)
anueGscNWFltrTotRxCountFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotRxCountFrag.setStatus("current")
_AnueGscNWFltrTotTdOutFrag_Type = Counter64
_AnueGscNWFltrTotTdOutFrag_Object = MibTableColumn
anueGscNWFltrTotTdOutFrag = _AnueGscNWFltrTotTdOutFrag_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 15),
    _AnueGscNWFltrTotTdOutFrag_Type()
)
anueGscNWFltrTotTdOutFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotTdOutFrag.setStatus("current")
_AnueGscNWFltrAvgCompFragPkts_Type = Counter64
_AnueGscNWFltrAvgCompFragPkts_Object = MibTableColumn
anueGscNWFltrAvgCompFragPkts = _AnueGscNWFltrAvgCompFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 16),
    _AnueGscNWFltrAvgCompFragPkts_Type()
)
anueGscNWFltrAvgCompFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgCompFragPkts.setStatus("current")
_AnueGscNWFltrAvgCompFragPktsPerc_Type = Counter64
_AnueGscNWFltrAvgCompFragPktsPerc_Object = MibTableColumn
anueGscNWFltrAvgCompFragPktsPerc = _AnueGscNWFltrAvgCompFragPktsPerc_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 17),
    _AnueGscNWFltrAvgCompFragPktsPerc_Type()
)
anueGscNWFltrAvgCompFragPktsPerc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgCompFragPktsPerc.setStatus("current")
_AnueGscNWFltrAvgIncomFragPkts_Type = Counter64
_AnueGscNWFltrAvgIncomFragPkts_Object = MibTableColumn
anueGscNWFltrAvgIncomFragPkts = _AnueGscNWFltrAvgIncomFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 18),
    _AnueGscNWFltrAvgIncomFragPkts_Type()
)
anueGscNWFltrAvgIncomFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgIncomFragPkts.setStatus("current")
_AnueGscNWFltrCurCompFragPkts_Type = Counter64
_AnueGscNWFltrCurCompFragPkts_Object = MibTableColumn
anueGscNWFltrCurCompFragPkts = _AnueGscNWFltrCurCompFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 19),
    _AnueGscNWFltrCurCompFragPkts_Type()
)
anueGscNWFltrCurCompFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurCompFragPkts.setStatus("current")
_AnueGscNWFltrCurCompFragPktsPerc_Type = Counter64
_AnueGscNWFltrCurCompFragPktsPerc_Object = MibTableColumn
anueGscNWFltrCurCompFragPktsPerc = _AnueGscNWFltrCurCompFragPktsPerc_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 20),
    _AnueGscNWFltrCurCompFragPktsPerc_Type()
)
anueGscNWFltrCurCompFragPktsPerc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurCompFragPktsPerc.setStatus("current")
_AnueGscNWFltrCurIncomFragPkts_Type = Counter64
_AnueGscNWFltrCurIncomFragPkts_Object = MibTableColumn
anueGscNWFltrCurIncomFragPkts = _AnueGscNWFltrCurIncomFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 21),
    _AnueGscNWFltrCurIncomFragPkts_Type()
)
anueGscNWFltrCurIncomFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurIncomFragPkts.setStatus("current")
_AnueGscNWFltrPkCompFragPkts_Type = Counter64
_AnueGscNWFltrPkCompFragPkts_Object = MibTableColumn
anueGscNWFltrPkCompFragPkts = _AnueGscNWFltrPkCompFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 22),
    _AnueGscNWFltrPkCompFragPkts_Type()
)
anueGscNWFltrPkCompFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkCompFragPkts.setStatus("current")
_AnueGscNWFltrPkCompFragPktsT_Type = DateAndTime
_AnueGscNWFltrPkCompFragPktsT_Object = MibTableColumn
anueGscNWFltrPkCompFragPktsT = _AnueGscNWFltrPkCompFragPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 23),
    _AnueGscNWFltrPkCompFragPktsT_Type()
)
anueGscNWFltrPkCompFragPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkCompFragPktsT.setStatus("current")
_AnueGscNWFltrPkCompFragPktsPerc_Type = Counter64
_AnueGscNWFltrPkCompFragPktsPerc_Object = MibTableColumn
anueGscNWFltrPkCompFragPktsPerc = _AnueGscNWFltrPkCompFragPktsPerc_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 24),
    _AnueGscNWFltrPkCompFragPktsPerc_Type()
)
anueGscNWFltrPkCompFragPktsPerc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkCompFragPktsPerc.setStatus("current")
_AnueGscNWFltrPkCompFragPktsPercT_Type = DateAndTime
_AnueGscNWFltrPkCompFragPktsPercT_Object = MibTableColumn
anueGscNWFltrPkCompFragPktsPercT = _AnueGscNWFltrPkCompFragPktsPercT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 25),
    _AnueGscNWFltrPkCompFragPktsPercT_Type()
)
anueGscNWFltrPkCompFragPktsPercT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkCompFragPktsPercT.setStatus("current")
_AnueGscNWFltrPkIncomFragPkts_Type = Counter64
_AnueGscNWFltrPkIncomFragPkts_Object = MibTableColumn
anueGscNWFltrPkIncomFragPkts = _AnueGscNWFltrPkIncomFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 26),
    _AnueGscNWFltrPkIncomFragPkts_Type()
)
anueGscNWFltrPkIncomFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkIncomFragPkts.setStatus("current")
_AnueGscNWFltrPkIncomFragPktsT_Type = DateAndTime
_AnueGscNWFltrPkIncomFragPktsT_Object = MibTableColumn
anueGscNWFltrPkIncomFragPktsT = _AnueGscNWFltrPkIncomFragPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 27),
    _AnueGscNWFltrPkIncomFragPktsT_Type()
)
anueGscNWFltrPkIncomFragPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkIncomFragPktsT.setStatus("current")
_AnueGscNWFltrPkTotCompFragPkts_Type = Counter64
_AnueGscNWFltrPkTotCompFragPkts_Object = MibTableColumn
anueGscNWFltrPkTotCompFragPkts = _AnueGscNWFltrPkTotCompFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 28),
    _AnueGscNWFltrPkTotCompFragPkts_Type()
)
anueGscNWFltrPkTotCompFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkTotCompFragPkts.setStatus("current")
_AnueGscNWFltrAvgActiveUsers_Type = Counter64
_AnueGscNWFltrAvgActiveUsers_Object = MibTableColumn
anueGscNWFltrAvgActiveUsers = _AnueGscNWFltrAvgActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 29),
    _AnueGscNWFltrAvgActiveUsers_Type()
)
anueGscNWFltrAvgActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgActiveUsers.setStatus("current")
_AnueGscNWFltrCurActiveUsers_Type = Counter64
_AnueGscNWFltrCurActiveUsers_Object = MibTableColumn
anueGscNWFltrCurActiveUsers = _AnueGscNWFltrCurActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 30),
    _AnueGscNWFltrCurActiveUsers_Type()
)
anueGscNWFltrCurActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurActiveUsers.setStatus("current")
_AnueGscNWFltrPkActiveUsers_Type = Counter64
_AnueGscNWFltrPkActiveUsers_Object = MibTableColumn
anueGscNWFltrPkActiveUsers = _AnueGscNWFltrPkActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 31),
    _AnueGscNWFltrPkActiveUsers_Type()
)
anueGscNWFltrPkActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkActiveUsers.setStatus("current")
_AnueGscNWFltrPkActiveUsersT_Type = DateAndTime
_AnueGscNWFltrPkActiveUsersT_Object = MibTableColumn
anueGscNWFltrPkActiveUsersT = _AnueGscNWFltrPkActiveUsersT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 32),
    _AnueGscNWFltrPkActiveUsersT_Type()
)
anueGscNWFltrPkActiveUsersT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkActiveUsersT.setStatus("current")
_AnueGscNWFltrAvgExcSess_Type = Counter64
_AnueGscNWFltrAvgExcSess_Object = MibTableColumn
anueGscNWFltrAvgExcSess = _AnueGscNWFltrAvgExcSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 33),
    _AnueGscNWFltrAvgExcSess_Type()
)
anueGscNWFltrAvgExcSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgExcSess.setStatus("current")
_AnueGscNWFltrCurExcSess_Type = Counter64
_AnueGscNWFltrCurExcSess_Object = MibTableColumn
anueGscNWFltrCurExcSess = _AnueGscNWFltrCurExcSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 34),
    _AnueGscNWFltrCurExcSess_Type()
)
anueGscNWFltrCurExcSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurExcSess.setStatus("current")
_AnueGscNWFltrPkExcSess_Type = Counter64
_AnueGscNWFltrPkExcSess_Object = MibTableColumn
anueGscNWFltrPkExcSess = _AnueGscNWFltrPkExcSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 35),
    _AnueGscNWFltrPkExcSess_Type()
)
anueGscNWFltrPkExcSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkExcSess.setStatus("current")
_AnueGscNWFltrPkExcSessT_Type = DateAndTime
_AnueGscNWFltrPkExcSessT_Object = MibTableColumn
anueGscNWFltrPkExcSessT = _AnueGscNWFltrPkExcSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 36),
    _AnueGscNWFltrPkExcSessT_Type()
)
anueGscNWFltrPkExcSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkExcSessT.setStatus("current")
_AnueGscNWFltrTotExcSess_Type = Counter64
_AnueGscNWFltrTotExcSess_Object = MibTableColumn
anueGscNWFltrTotExcSess = _AnueGscNWFltrTotExcSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 37),
    _AnueGscNWFltrTotExcSess_Type()
)
anueGscNWFltrTotExcSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotExcSess.setStatus("current")
_AnueGscNWFltrTotGtpV0CrSess_Type = Counter64
_AnueGscNWFltrTotGtpV0CrSess_Object = MibTableColumn
anueGscNWFltrTotGtpV0CrSess = _AnueGscNWFltrTotGtpV0CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 38),
    _AnueGscNWFltrTotGtpV0CrSess_Type()
)
anueGscNWFltrTotGtpV0CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV0CrSess.setStatus("current")
_AnueGscNWFltrTotGtpV1CrSess_Type = Counter64
_AnueGscNWFltrTotGtpV1CrSess_Object = MibTableColumn
anueGscNWFltrTotGtpV1CrSess = _AnueGscNWFltrTotGtpV1CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 39),
    _AnueGscNWFltrTotGtpV1CrSess_Type()
)
anueGscNWFltrTotGtpV1CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV1CrSess.setStatus("current")
_AnueGscNWFltrTotGtpV2CrSess_Type = Counter64
_AnueGscNWFltrTotGtpV2CrSess_Object = MibTableColumn
anueGscNWFltrTotGtpV2CrSess = _AnueGscNWFltrTotGtpV2CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 40),
    _AnueGscNWFltrTotGtpV2CrSess_Type()
)
anueGscNWFltrTotGtpV2CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV2CrSess.setStatus("current")
_AnueGscNWFltrTotGtpTotCrSess_Type = Counter64
_AnueGscNWFltrTotGtpTotCrSess_Object = MibTableColumn
anueGscNWFltrTotGtpTotCrSess = _AnueGscNWFltrTotGtpTotCrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 41),
    _AnueGscNWFltrTotGtpTotCrSess_Type()
)
anueGscNWFltrTotGtpTotCrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpTotCrSess.setStatus("current")
_AnueGscNWFltrAvgGtpV0CrSess_Type = Counter64
_AnueGscNWFltrAvgGtpV0CrSess_Object = MibTableColumn
anueGscNWFltrAvgGtpV0CrSess = _AnueGscNWFltrAvgGtpV0CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 42),
    _AnueGscNWFltrAvgGtpV0CrSess_Type()
)
anueGscNWFltrAvgGtpV0CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV0CrSess.setStatus("current")
_AnueGscNWFltrAvgGtpV1CrSess_Type = Counter64
_AnueGscNWFltrAvgGtpV1CrSess_Object = MibTableColumn
anueGscNWFltrAvgGtpV1CrSess = _AnueGscNWFltrAvgGtpV1CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 43),
    _AnueGscNWFltrAvgGtpV1CrSess_Type()
)
anueGscNWFltrAvgGtpV1CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV1CrSess.setStatus("current")
_AnueGscNWFltrAvgGtpV2CrSess_Type = Counter64
_AnueGscNWFltrAvgGtpV2CrSess_Object = MibTableColumn
anueGscNWFltrAvgGtpV2CrSess = _AnueGscNWFltrAvgGtpV2CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 44),
    _AnueGscNWFltrAvgGtpV2CrSess_Type()
)
anueGscNWFltrAvgGtpV2CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV2CrSess.setStatus("current")
_AnueGscNWFltrAvgGtpTotCrSess_Type = Counter64
_AnueGscNWFltrAvgGtpTotCrSess_Object = MibTableColumn
anueGscNWFltrAvgGtpTotCrSess = _AnueGscNWFltrAvgGtpTotCrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 45),
    _AnueGscNWFltrAvgGtpTotCrSess_Type()
)
anueGscNWFltrAvgGtpTotCrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpTotCrSess.setStatus("current")
_AnueGscNWFltrCurGtpV0CrSess_Type = Counter64
_AnueGscNWFltrCurGtpV0CrSess_Object = MibTableColumn
anueGscNWFltrCurGtpV0CrSess = _AnueGscNWFltrCurGtpV0CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 46),
    _AnueGscNWFltrCurGtpV0CrSess_Type()
)
anueGscNWFltrCurGtpV0CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV0CrSess.setStatus("current")
_AnueGscNWFltrCurGtpV1CrSess_Type = Counter64
_AnueGscNWFltrCurGtpV1CrSess_Object = MibTableColumn
anueGscNWFltrCurGtpV1CrSess = _AnueGscNWFltrCurGtpV1CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 47),
    _AnueGscNWFltrCurGtpV1CrSess_Type()
)
anueGscNWFltrCurGtpV1CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV1CrSess.setStatus("current")
_AnueGscNWFltrCurGtpV2CrSess_Type = Counter64
_AnueGscNWFltrCurGtpV2CrSess_Object = MibTableColumn
anueGscNWFltrCurGtpV2CrSess = _AnueGscNWFltrCurGtpV2CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 48),
    _AnueGscNWFltrCurGtpV2CrSess_Type()
)
anueGscNWFltrCurGtpV2CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV2CrSess.setStatus("current")
_AnueGscNWFltrCurGtpTotCrSess_Type = Counter64
_AnueGscNWFltrCurGtpTotCrSess_Object = MibTableColumn
anueGscNWFltrCurGtpTotCrSess = _AnueGscNWFltrCurGtpTotCrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 49),
    _AnueGscNWFltrCurGtpTotCrSess_Type()
)
anueGscNWFltrCurGtpTotCrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpTotCrSess.setStatus("current")
_AnueGscNWFltrPkGtpV0CrSess_Type = Counter64
_AnueGscNWFltrPkGtpV0CrSess_Object = MibTableColumn
anueGscNWFltrPkGtpV0CrSess = _AnueGscNWFltrPkGtpV0CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 50),
    _AnueGscNWFltrPkGtpV0CrSess_Type()
)
anueGscNWFltrPkGtpV0CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0CrSess.setStatus("current")
_AnueGscNWFltrPkGtpV1CrSess_Type = Counter64
_AnueGscNWFltrPkGtpV1CrSess_Object = MibTableColumn
anueGscNWFltrPkGtpV1CrSess = _AnueGscNWFltrPkGtpV1CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 51),
    _AnueGscNWFltrPkGtpV1CrSess_Type()
)
anueGscNWFltrPkGtpV1CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1CrSess.setStatus("current")
_AnueGscNWFltrPkGtpV2CrSess_Type = Counter64
_AnueGscNWFltrPkGtpV2CrSess_Object = MibTableColumn
anueGscNWFltrPkGtpV2CrSess = _AnueGscNWFltrPkGtpV2CrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 52),
    _AnueGscNWFltrPkGtpV2CrSess_Type()
)
anueGscNWFltrPkGtpV2CrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2CrSess.setStatus("current")
_AnueGscNWFltrPkGtpTotCrSess_Type = Counter64
_AnueGscNWFltrPkGtpTotCrSess_Object = MibTableColumn
anueGscNWFltrPkGtpTotCrSess = _AnueGscNWFltrPkGtpTotCrSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 53),
    _AnueGscNWFltrPkGtpTotCrSess_Type()
)
anueGscNWFltrPkGtpTotCrSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotCrSess.setStatus("current")
_AnueGscNWFltrPkGtpV0CrSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpV0CrSessT_Object = MibTableColumn
anueGscNWFltrPkGtpV0CrSessT = _AnueGscNWFltrPkGtpV0CrSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 54),
    _AnueGscNWFltrPkGtpV0CrSessT_Type()
)
anueGscNWFltrPkGtpV0CrSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0CrSessT.setStatus("current")
_AnueGscNWFltrPkGtpV1CrSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpV1CrSessT_Object = MibTableColumn
anueGscNWFltrPkGtpV1CrSessT = _AnueGscNWFltrPkGtpV1CrSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 55),
    _AnueGscNWFltrPkGtpV1CrSessT_Type()
)
anueGscNWFltrPkGtpV1CrSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1CrSessT.setStatus("current")
_AnueGscNWFltrPkGtpV2CrSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpV2CrSessT_Object = MibTableColumn
anueGscNWFltrPkGtpV2CrSessT = _AnueGscNWFltrPkGtpV2CrSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 56),
    _AnueGscNWFltrPkGtpV2CrSessT_Type()
)
anueGscNWFltrPkGtpV2CrSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2CrSessT.setStatus("current")
_AnueGscNWFltrPkGtpTotCrSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpTotCrSessT_Object = MibTableColumn
anueGscNWFltrPkGtpTotCrSessT = _AnueGscNWFltrPkGtpTotCrSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 57),
    _AnueGscNWFltrPkGtpTotCrSessT_Type()
)
anueGscNWFltrPkGtpTotCrSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotCrSessT.setStatus("current")
_AnueGscNWFltrTotGtpV0DelSess_Type = Counter64
_AnueGscNWFltrTotGtpV0DelSess_Object = MibTableColumn
anueGscNWFltrTotGtpV0DelSess = _AnueGscNWFltrTotGtpV0DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 58),
    _AnueGscNWFltrTotGtpV0DelSess_Type()
)
anueGscNWFltrTotGtpV0DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV0DelSess.setStatus("current")
_AnueGscNWFltrTotGtpV1DelSess_Type = Counter64
_AnueGscNWFltrTotGtpV1DelSess_Object = MibTableColumn
anueGscNWFltrTotGtpV1DelSess = _AnueGscNWFltrTotGtpV1DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 59),
    _AnueGscNWFltrTotGtpV1DelSess_Type()
)
anueGscNWFltrTotGtpV1DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV1DelSess.setStatus("current")
_AnueGscNWFltrTotGtpV2DelSess_Type = Counter64
_AnueGscNWFltrTotGtpV2DelSess_Object = MibTableColumn
anueGscNWFltrTotGtpV2DelSess = _AnueGscNWFltrTotGtpV2DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 60),
    _AnueGscNWFltrTotGtpV2DelSess_Type()
)
anueGscNWFltrTotGtpV2DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV2DelSess.setStatus("current")
_AnueGscNWFltrTotGtpTotDelSess_Type = Counter64
_AnueGscNWFltrTotGtpTotDelSess_Object = MibTableColumn
anueGscNWFltrTotGtpTotDelSess = _AnueGscNWFltrTotGtpTotDelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 61),
    _AnueGscNWFltrTotGtpTotDelSess_Type()
)
anueGscNWFltrTotGtpTotDelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpTotDelSess.setStatus("current")
_AnueGscNWFltrAvgGtpV0DelSess_Type = Counter64
_AnueGscNWFltrAvgGtpV0DelSess_Object = MibTableColumn
anueGscNWFltrAvgGtpV0DelSess = _AnueGscNWFltrAvgGtpV0DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 62),
    _AnueGscNWFltrAvgGtpV0DelSess_Type()
)
anueGscNWFltrAvgGtpV0DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV0DelSess.setStatus("current")
_AnueGscNWFltrAvgGtpV1DelSess_Type = Counter64
_AnueGscNWFltrAvgGtpV1DelSess_Object = MibTableColumn
anueGscNWFltrAvgGtpV1DelSess = _AnueGscNWFltrAvgGtpV1DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 63),
    _AnueGscNWFltrAvgGtpV1DelSess_Type()
)
anueGscNWFltrAvgGtpV1DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV1DelSess.setStatus("current")
_AnueGscNWFltrAvgGtpV2DelSess_Type = Counter64
_AnueGscNWFltrAvgGtpV2DelSess_Object = MibTableColumn
anueGscNWFltrAvgGtpV2DelSess = _AnueGscNWFltrAvgGtpV2DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 64),
    _AnueGscNWFltrAvgGtpV2DelSess_Type()
)
anueGscNWFltrAvgGtpV2DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV2DelSess.setStatus("current")
_AnueGscNWFltrAvgGtpTotDelSess_Type = Counter64
_AnueGscNWFltrAvgGtpTotDelSess_Object = MibTableColumn
anueGscNWFltrAvgGtpTotDelSess = _AnueGscNWFltrAvgGtpTotDelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 65),
    _AnueGscNWFltrAvgGtpTotDelSess_Type()
)
anueGscNWFltrAvgGtpTotDelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpTotDelSess.setStatus("current")
_AnueGscNWFltrCurGtpV0DelSess_Type = Counter64
_AnueGscNWFltrCurGtpV0DelSess_Object = MibTableColumn
anueGscNWFltrCurGtpV0DelSess = _AnueGscNWFltrCurGtpV0DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 66),
    _AnueGscNWFltrCurGtpV0DelSess_Type()
)
anueGscNWFltrCurGtpV0DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV0DelSess.setStatus("current")
_AnueGscNWFltrCurGtpV1DelSess_Type = Counter64
_AnueGscNWFltrCurGtpV1DelSess_Object = MibTableColumn
anueGscNWFltrCurGtpV1DelSess = _AnueGscNWFltrCurGtpV1DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 67),
    _AnueGscNWFltrCurGtpV1DelSess_Type()
)
anueGscNWFltrCurGtpV1DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV1DelSess.setStatus("current")
_AnueGscNWFltrCurGtpV2DelSess_Type = Counter64
_AnueGscNWFltrCurGtpV2DelSess_Object = MibTableColumn
anueGscNWFltrCurGtpV2DelSess = _AnueGscNWFltrCurGtpV2DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 68),
    _AnueGscNWFltrCurGtpV2DelSess_Type()
)
anueGscNWFltrCurGtpV2DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV2DelSess.setStatus("current")
_AnueGscNWFltrCurGtpTotDelSess_Type = Counter64
_AnueGscNWFltrCurGtpTotDelSess_Object = MibTableColumn
anueGscNWFltrCurGtpTotDelSess = _AnueGscNWFltrCurGtpTotDelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 69),
    _AnueGscNWFltrCurGtpTotDelSess_Type()
)
anueGscNWFltrCurGtpTotDelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpTotDelSess.setStatus("current")
_AnueGscNWFltrPkGtpV0DelSess_Type = Counter64
_AnueGscNWFltrPkGtpV0DelSess_Object = MibTableColumn
anueGscNWFltrPkGtpV0DelSess = _AnueGscNWFltrPkGtpV0DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 70),
    _AnueGscNWFltrPkGtpV0DelSess_Type()
)
anueGscNWFltrPkGtpV0DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0DelSess.setStatus("current")
_AnueGscNWFltrPkGtpV1DelSess_Type = Counter64
_AnueGscNWFltrPkGtpV1DelSess_Object = MibTableColumn
anueGscNWFltrPkGtpV1DelSess = _AnueGscNWFltrPkGtpV1DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 71),
    _AnueGscNWFltrPkGtpV1DelSess_Type()
)
anueGscNWFltrPkGtpV1DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1DelSess.setStatus("current")
_AnueGscNWFltrPkGtpV2DelSess_Type = Counter64
_AnueGscNWFltrPkGtpV2DelSess_Object = MibTableColumn
anueGscNWFltrPkGtpV2DelSess = _AnueGscNWFltrPkGtpV2DelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 72),
    _AnueGscNWFltrPkGtpV2DelSess_Type()
)
anueGscNWFltrPkGtpV2DelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2DelSess.setStatus("current")
_AnueGscNWFltrPkGtpTotDelSess_Type = Counter64
_AnueGscNWFltrPkGtpTotDelSess_Object = MibTableColumn
anueGscNWFltrPkGtpTotDelSess = _AnueGscNWFltrPkGtpTotDelSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 73),
    _AnueGscNWFltrPkGtpTotDelSess_Type()
)
anueGscNWFltrPkGtpTotDelSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotDelSess.setStatus("current")
_AnueGscNWFltrPkGtpV0DelSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpV0DelSessT_Object = MibTableColumn
anueGscNWFltrPkGtpV0DelSessT = _AnueGscNWFltrPkGtpV0DelSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 74),
    _AnueGscNWFltrPkGtpV0DelSessT_Type()
)
anueGscNWFltrPkGtpV0DelSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0DelSessT.setStatus("current")
_AnueGscNWFltrPkGtpV1DelSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpV1DelSessT_Object = MibTableColumn
anueGscNWFltrPkGtpV1DelSessT = _AnueGscNWFltrPkGtpV1DelSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 75),
    _AnueGscNWFltrPkGtpV1DelSessT_Type()
)
anueGscNWFltrPkGtpV1DelSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1DelSessT.setStatus("current")
_AnueGscNWFltrPkGtpV2DelSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpV2DelSessT_Object = MibTableColumn
anueGscNWFltrPkGtpV2DelSessT = _AnueGscNWFltrPkGtpV2DelSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 76),
    _AnueGscNWFltrPkGtpV2DelSessT_Type()
)
anueGscNWFltrPkGtpV2DelSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2DelSessT.setStatus("current")
_AnueGscNWFltrPkGtpTotDelSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpTotDelSessT_Object = MibTableColumn
anueGscNWFltrPkGtpTotDelSessT = _AnueGscNWFltrPkGtpTotDelSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 77),
    _AnueGscNWFltrPkGtpTotDelSessT_Type()
)
anueGscNWFltrPkGtpTotDelSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotDelSessT.setStatus("current")
_AnueGscNWFltrAvgGtpV0Bearers_Type = Counter64
_AnueGscNWFltrAvgGtpV0Bearers_Object = MibTableColumn
anueGscNWFltrAvgGtpV0Bearers = _AnueGscNWFltrAvgGtpV0Bearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 78),
    _AnueGscNWFltrAvgGtpV0Bearers_Type()
)
anueGscNWFltrAvgGtpV0Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV0Bearers.setStatus("current")
_AnueGscNWFltrAvgGtpV1Bearers_Type = Counter64
_AnueGscNWFltrAvgGtpV1Bearers_Object = MibTableColumn
anueGscNWFltrAvgGtpV1Bearers = _AnueGscNWFltrAvgGtpV1Bearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 79),
    _AnueGscNWFltrAvgGtpV1Bearers_Type()
)
anueGscNWFltrAvgGtpV1Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV1Bearers.setStatus("current")
_AnueGscNWFltrAvgGtpV2Bearers_Type = Counter64
_AnueGscNWFltrAvgGtpV2Bearers_Object = MibTableColumn
anueGscNWFltrAvgGtpV2Bearers = _AnueGscNWFltrAvgGtpV2Bearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 80),
    _AnueGscNWFltrAvgGtpV2Bearers_Type()
)
anueGscNWFltrAvgGtpV2Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV2Bearers.setStatus("current")
_AnueGscNWFltrAvgGtpTotBearers_Type = Counter64
_AnueGscNWFltrAvgGtpTotBearers_Object = MibTableColumn
anueGscNWFltrAvgGtpTotBearers = _AnueGscNWFltrAvgGtpTotBearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 81),
    _AnueGscNWFltrAvgGtpTotBearers_Type()
)
anueGscNWFltrAvgGtpTotBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpTotBearers.setStatus("current")
_AnueGscNWFltrCurGtpV0Bearers_Type = Counter64
_AnueGscNWFltrCurGtpV0Bearers_Object = MibTableColumn
anueGscNWFltrCurGtpV0Bearers = _AnueGscNWFltrCurGtpV0Bearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 82),
    _AnueGscNWFltrCurGtpV0Bearers_Type()
)
anueGscNWFltrCurGtpV0Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV0Bearers.setStatus("current")
_AnueGscNWFltrCurGtpV1Bearers_Type = Counter64
_AnueGscNWFltrCurGtpV1Bearers_Object = MibTableColumn
anueGscNWFltrCurGtpV1Bearers = _AnueGscNWFltrCurGtpV1Bearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 83),
    _AnueGscNWFltrCurGtpV1Bearers_Type()
)
anueGscNWFltrCurGtpV1Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV1Bearers.setStatus("current")
_AnueGscNWFltrCurGtpV2Bearers_Type = Counter64
_AnueGscNWFltrCurGtpV2Bearers_Object = MibTableColumn
anueGscNWFltrCurGtpV2Bearers = _AnueGscNWFltrCurGtpV2Bearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 84),
    _AnueGscNWFltrCurGtpV2Bearers_Type()
)
anueGscNWFltrCurGtpV2Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV2Bearers.setStatus("current")
_AnueGscNWFltrCurGtpTotBearers_Type = Counter64
_AnueGscNWFltrCurGtpTotBearers_Object = MibTableColumn
anueGscNWFltrCurGtpTotBearers = _AnueGscNWFltrCurGtpTotBearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 85),
    _AnueGscNWFltrCurGtpTotBearers_Type()
)
anueGscNWFltrCurGtpTotBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpTotBearers.setStatus("current")
_AnueGscNWFltrPkGtpV0Bearers_Type = Counter64
_AnueGscNWFltrPkGtpV0Bearers_Object = MibTableColumn
anueGscNWFltrPkGtpV0Bearers = _AnueGscNWFltrPkGtpV0Bearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 86),
    _AnueGscNWFltrPkGtpV0Bearers_Type()
)
anueGscNWFltrPkGtpV0Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0Bearers.setStatus("current")
_AnueGscNWFltrPkGtpV1Bearers_Type = Counter64
_AnueGscNWFltrPkGtpV1Bearers_Object = MibTableColumn
anueGscNWFltrPkGtpV1Bearers = _AnueGscNWFltrPkGtpV1Bearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 87),
    _AnueGscNWFltrPkGtpV1Bearers_Type()
)
anueGscNWFltrPkGtpV1Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1Bearers.setStatus("current")
_AnueGscNWFltrPkGtpV2Bearers_Type = Counter64
_AnueGscNWFltrPkGtpV2Bearers_Object = MibTableColumn
anueGscNWFltrPkGtpV2Bearers = _AnueGscNWFltrPkGtpV2Bearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 88),
    _AnueGscNWFltrPkGtpV2Bearers_Type()
)
anueGscNWFltrPkGtpV2Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2Bearers.setStatus("current")
_AnueGscNWFltrPkGtpTotBearers_Type = Counter64
_AnueGscNWFltrPkGtpTotBearers_Object = MibTableColumn
anueGscNWFltrPkGtpTotBearers = _AnueGscNWFltrPkGtpTotBearers_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 89),
    _AnueGscNWFltrPkGtpTotBearers_Type()
)
anueGscNWFltrPkGtpTotBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotBearers.setStatus("current")
_AnueGscNWFltrPkGtpV0BearersT_Type = DateAndTime
_AnueGscNWFltrPkGtpV0BearersT_Object = MibTableColumn
anueGscNWFltrPkGtpV0BearersT = _AnueGscNWFltrPkGtpV0BearersT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 90),
    _AnueGscNWFltrPkGtpV0BearersT_Type()
)
anueGscNWFltrPkGtpV0BearersT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0BearersT.setStatus("current")
_AnueGscNWFltrPkGtpV1BearersT_Type = DateAndTime
_AnueGscNWFltrPkGtpV1BearersT_Object = MibTableColumn
anueGscNWFltrPkGtpV1BearersT = _AnueGscNWFltrPkGtpV1BearersT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 91),
    _AnueGscNWFltrPkGtpV1BearersT_Type()
)
anueGscNWFltrPkGtpV1BearersT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1BearersT.setStatus("current")
_AnueGscNWFltrPkGtpV2BearersT_Type = DateAndTime
_AnueGscNWFltrPkGtpV2BearersT_Object = MibTableColumn
anueGscNWFltrPkGtpV2BearersT = _AnueGscNWFltrPkGtpV2BearersT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 92),
    _AnueGscNWFltrPkGtpV2BearersT_Type()
)
anueGscNWFltrPkGtpV2BearersT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2BearersT.setStatus("current")
_AnueGscNWFltrPkGtpTotBearersT_Type = DateAndTime
_AnueGscNWFltrPkGtpTotBearersT_Object = MibTableColumn
anueGscNWFltrPkGtpTotBearersT = _AnueGscNWFltrPkGtpTotBearersT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 93),
    _AnueGscNWFltrPkGtpTotBearersT_Type()
)
anueGscNWFltrPkGtpTotBearersT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotBearersT.setStatus("current")
_AnueGscNWFltrAvgGtpV0Pkts_Type = Counter64
_AnueGscNWFltrAvgGtpV0Pkts_Object = MibTableColumn
anueGscNWFltrAvgGtpV0Pkts = _AnueGscNWFltrAvgGtpV0Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 94),
    _AnueGscNWFltrAvgGtpV0Pkts_Type()
)
anueGscNWFltrAvgGtpV0Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV0Pkts.setStatus("current")
_AnueGscNWFltrAvgGtpV1Pkts_Type = Counter64
_AnueGscNWFltrAvgGtpV1Pkts_Object = MibTableColumn
anueGscNWFltrAvgGtpV1Pkts = _AnueGscNWFltrAvgGtpV1Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 95),
    _AnueGscNWFltrAvgGtpV1Pkts_Type()
)
anueGscNWFltrAvgGtpV1Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV1Pkts.setStatus("current")
_AnueGscNWFltrAvgGtpV2Pkts_Type = Counter64
_AnueGscNWFltrAvgGtpV2Pkts_Object = MibTableColumn
anueGscNWFltrAvgGtpV2Pkts = _AnueGscNWFltrAvgGtpV2Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 96),
    _AnueGscNWFltrAvgGtpV2Pkts_Type()
)
anueGscNWFltrAvgGtpV2Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV2Pkts.setStatus("current")
_AnueGscNWFltrAvgGtpTotPkts_Type = Counter64
_AnueGscNWFltrAvgGtpTotPkts_Object = MibTableColumn
anueGscNWFltrAvgGtpTotPkts = _AnueGscNWFltrAvgGtpTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 97),
    _AnueGscNWFltrAvgGtpTotPkts_Type()
)
anueGscNWFltrAvgGtpTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpTotPkts.setStatus("current")
_AnueGscNWFltrCurGtpV0Pkts_Type = Counter64
_AnueGscNWFltrCurGtpV0Pkts_Object = MibTableColumn
anueGscNWFltrCurGtpV0Pkts = _AnueGscNWFltrCurGtpV0Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 98),
    _AnueGscNWFltrCurGtpV0Pkts_Type()
)
anueGscNWFltrCurGtpV0Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV0Pkts.setStatus("current")
_AnueGscNWFltrCurGtpV1Pkts_Type = Counter64
_AnueGscNWFltrCurGtpV1Pkts_Object = MibTableColumn
anueGscNWFltrCurGtpV1Pkts = _AnueGscNWFltrCurGtpV1Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 99),
    _AnueGscNWFltrCurGtpV1Pkts_Type()
)
anueGscNWFltrCurGtpV1Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV1Pkts.setStatus("current")
_AnueGscNWFltrCurGtpV2Pkts_Type = Counter64
_AnueGscNWFltrCurGtpV2Pkts_Object = MibTableColumn
anueGscNWFltrCurGtpV2Pkts = _AnueGscNWFltrCurGtpV2Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 100),
    _AnueGscNWFltrCurGtpV2Pkts_Type()
)
anueGscNWFltrCurGtpV2Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV2Pkts.setStatus("current")
_AnueGscNWFltrCurGtpTotPkts_Type = Counter64
_AnueGscNWFltrCurGtpTotPkts_Object = MibTableColumn
anueGscNWFltrCurGtpTotPkts = _AnueGscNWFltrCurGtpTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 101),
    _AnueGscNWFltrCurGtpTotPkts_Type()
)
anueGscNWFltrCurGtpTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpTotPkts.setStatus("current")
_AnueGscNWFltrTotGtpV1Pkts_Type = Counter64
_AnueGscNWFltrTotGtpV1Pkts_Object = MibTableColumn
anueGscNWFltrTotGtpV1Pkts = _AnueGscNWFltrTotGtpV1Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 102),
    _AnueGscNWFltrTotGtpV1Pkts_Type()
)
anueGscNWFltrTotGtpV1Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV1Pkts.setStatus("current")
_AnueGscNWFltrTotGtpV0Pkts_Type = Counter64
_AnueGscNWFltrTotGtpV0Pkts_Object = MibTableColumn
anueGscNWFltrTotGtpV0Pkts = _AnueGscNWFltrTotGtpV0Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 103),
    _AnueGscNWFltrTotGtpV0Pkts_Type()
)
anueGscNWFltrTotGtpV0Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV0Pkts.setStatus("current")
_AnueGscNWFltrTotGtpV2Pkts_Type = Counter64
_AnueGscNWFltrTotGtpV2Pkts_Object = MibTableColumn
anueGscNWFltrTotGtpV2Pkts = _AnueGscNWFltrTotGtpV2Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 104),
    _AnueGscNWFltrTotGtpV2Pkts_Type()
)
anueGscNWFltrTotGtpV2Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV2Pkts.setStatus("current")
_AnueGscNWFltrTotGtpTotPkts_Type = Counter64
_AnueGscNWFltrTotGtpTotPkts_Object = MibTableColumn
anueGscNWFltrTotGtpTotPkts = _AnueGscNWFltrTotGtpTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 105),
    _AnueGscNWFltrTotGtpTotPkts_Type()
)
anueGscNWFltrTotGtpTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpTotPkts.setStatus("current")
_AnueGscNWFltrPkGtpV0Pkts_Type = Counter64
_AnueGscNWFltrPkGtpV0Pkts_Object = MibTableColumn
anueGscNWFltrPkGtpV0Pkts = _AnueGscNWFltrPkGtpV0Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 106),
    _AnueGscNWFltrPkGtpV0Pkts_Type()
)
anueGscNWFltrPkGtpV0Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0Pkts.setStatus("current")
_AnueGscNWFltrPkGtpV1Pkts_Type = Counter64
_AnueGscNWFltrPkGtpV1Pkts_Object = MibTableColumn
anueGscNWFltrPkGtpV1Pkts = _AnueGscNWFltrPkGtpV1Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 107),
    _AnueGscNWFltrPkGtpV1Pkts_Type()
)
anueGscNWFltrPkGtpV1Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1Pkts.setStatus("current")
_AnueGscNWFltrPkGtpV2Pkts_Type = Counter64
_AnueGscNWFltrPkGtpV2Pkts_Object = MibTableColumn
anueGscNWFltrPkGtpV2Pkts = _AnueGscNWFltrPkGtpV2Pkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 108),
    _AnueGscNWFltrPkGtpV2Pkts_Type()
)
anueGscNWFltrPkGtpV2Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2Pkts.setStatus("current")
_AnueGscNWFltrPkGtpTotPkts_Type = Counter64
_AnueGscNWFltrPkGtpTotPkts_Object = MibTableColumn
anueGscNWFltrPkGtpTotPkts = _AnueGscNWFltrPkGtpTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 109),
    _AnueGscNWFltrPkGtpTotPkts_Type()
)
anueGscNWFltrPkGtpTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotPkts.setStatus("current")
_AnueGscNWFltrPkGtpV0PktsT_Type = DateAndTime
_AnueGscNWFltrPkGtpV0PktsT_Object = MibTableColumn
anueGscNWFltrPkGtpV0PktsT = _AnueGscNWFltrPkGtpV0PktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 110),
    _AnueGscNWFltrPkGtpV0PktsT_Type()
)
anueGscNWFltrPkGtpV0PktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0PktsT.setStatus("current")
_AnueGscNWFltrPkGtpV1PktsT_Type = DateAndTime
_AnueGscNWFltrPkGtpV1PktsT_Object = MibTableColumn
anueGscNWFltrPkGtpV1PktsT = _AnueGscNWFltrPkGtpV1PktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 111),
    _AnueGscNWFltrPkGtpV1PktsT_Type()
)
anueGscNWFltrPkGtpV1PktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1PktsT.setStatus("current")
_AnueGscNWFltrPkGtpV2PktsT_Type = DateAndTime
_AnueGscNWFltrPkGtpV2PktsT_Object = MibTableColumn
anueGscNWFltrPkGtpV2PktsT = _AnueGscNWFltrPkGtpV2PktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 112),
    _AnueGscNWFltrPkGtpV2PktsT_Type()
)
anueGscNWFltrPkGtpV2PktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2PktsT.setStatus("current")
_AnueGscNWFltrPkGtpTotPktsT_Type = DateAndTime
_AnueGscNWFltrPkGtpTotPktsT_Object = MibTableColumn
anueGscNWFltrPkGtpTotPktsT = _AnueGscNWFltrPkGtpTotPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 113),
    _AnueGscNWFltrPkGtpTotPktsT_Type()
)
anueGscNWFltrPkGtpTotPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotPktsT.setStatus("current")
_AnueGscNWFltrTotGtpV0ToutSess_Type = Counter64
_AnueGscNWFltrTotGtpV0ToutSess_Object = MibTableColumn
anueGscNWFltrTotGtpV0ToutSess = _AnueGscNWFltrTotGtpV0ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 114),
    _AnueGscNWFltrTotGtpV0ToutSess_Type()
)
anueGscNWFltrTotGtpV0ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV0ToutSess.setStatus("current")
_AnueGscNWFltrTotGtpV1ToutSess_Type = Counter64
_AnueGscNWFltrTotGtpV1ToutSess_Object = MibTableColumn
anueGscNWFltrTotGtpV1ToutSess = _AnueGscNWFltrTotGtpV1ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 115),
    _AnueGscNWFltrTotGtpV1ToutSess_Type()
)
anueGscNWFltrTotGtpV1ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV1ToutSess.setStatus("current")
_AnueGscNWFltrTotGtpV2ToutSess_Type = Counter64
_AnueGscNWFltrTotGtpV2ToutSess_Object = MibTableColumn
anueGscNWFltrTotGtpV2ToutSess = _AnueGscNWFltrTotGtpV2ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 116),
    _AnueGscNWFltrTotGtpV2ToutSess_Type()
)
anueGscNWFltrTotGtpV2ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpV2ToutSess.setStatus("current")
_AnueGscNWFltrTotGtpTotToutSess_Type = Counter64
_AnueGscNWFltrTotGtpTotToutSess_Object = MibTableColumn
anueGscNWFltrTotGtpTotToutSess = _AnueGscNWFltrTotGtpTotToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 117),
    _AnueGscNWFltrTotGtpTotToutSess_Type()
)
anueGscNWFltrTotGtpTotToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpTotToutSess.setStatus("current")
_AnueGscNWFltrAvgGtpV0ToutSess_Type = Counter64
_AnueGscNWFltrAvgGtpV0ToutSess_Object = MibTableColumn
anueGscNWFltrAvgGtpV0ToutSess = _AnueGscNWFltrAvgGtpV0ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 118),
    _AnueGscNWFltrAvgGtpV0ToutSess_Type()
)
anueGscNWFltrAvgGtpV0ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV0ToutSess.setStatus("current")
_AnueGscNWFltrAvgGtpV1ToutSess_Type = Counter64
_AnueGscNWFltrAvgGtpV1ToutSess_Object = MibTableColumn
anueGscNWFltrAvgGtpV1ToutSess = _AnueGscNWFltrAvgGtpV1ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 119),
    _AnueGscNWFltrAvgGtpV1ToutSess_Type()
)
anueGscNWFltrAvgGtpV1ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV1ToutSess.setStatus("current")
_AnueGscNWFltrAvgGtpV2ToutSess_Type = Counter64
_AnueGscNWFltrAvgGtpV2ToutSess_Object = MibTableColumn
anueGscNWFltrAvgGtpV2ToutSess = _AnueGscNWFltrAvgGtpV2ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 120),
    _AnueGscNWFltrAvgGtpV2ToutSess_Type()
)
anueGscNWFltrAvgGtpV2ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpV2ToutSess.setStatus("current")
_AnueGscNWFltrAvgGtpTotToutSess_Type = Counter64
_AnueGscNWFltrAvgGtpTotToutSess_Object = MibTableColumn
anueGscNWFltrAvgGtpTotToutSess = _AnueGscNWFltrAvgGtpTotToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 121),
    _AnueGscNWFltrAvgGtpTotToutSess_Type()
)
anueGscNWFltrAvgGtpTotToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpTotToutSess.setStatus("current")
_AnueGscNWFltrCurGtpV0ToutSess_Type = Counter64
_AnueGscNWFltrCurGtpV0ToutSess_Object = MibTableColumn
anueGscNWFltrCurGtpV0ToutSess = _AnueGscNWFltrCurGtpV0ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 122),
    _AnueGscNWFltrCurGtpV0ToutSess_Type()
)
anueGscNWFltrCurGtpV0ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV0ToutSess.setStatus("current")
_AnueGscNWFltrCurGtpV1ToutSess_Type = Counter64
_AnueGscNWFltrCurGtpV1ToutSess_Object = MibTableColumn
anueGscNWFltrCurGtpV1ToutSess = _AnueGscNWFltrCurGtpV1ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 123),
    _AnueGscNWFltrCurGtpV1ToutSess_Type()
)
anueGscNWFltrCurGtpV1ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV1ToutSess.setStatus("current")
_AnueGscNWFltrCurGtpV2ToutSess_Type = Counter64
_AnueGscNWFltrCurGtpV2ToutSess_Object = MibTableColumn
anueGscNWFltrCurGtpV2ToutSess = _AnueGscNWFltrCurGtpV2ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 124),
    _AnueGscNWFltrCurGtpV2ToutSess_Type()
)
anueGscNWFltrCurGtpV2ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpV2ToutSess.setStatus("current")
_AnueGscNWFltrCurGtpTotToutSess_Type = Counter64
_AnueGscNWFltrCurGtpTotToutSess_Object = MibTableColumn
anueGscNWFltrCurGtpTotToutSess = _AnueGscNWFltrCurGtpTotToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 125),
    _AnueGscNWFltrCurGtpTotToutSess_Type()
)
anueGscNWFltrCurGtpTotToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpTotToutSess.setStatus("current")
_AnueGscNWFltrPkGtpV0ToutSess_Type = Counter64
_AnueGscNWFltrPkGtpV0ToutSess_Object = MibTableColumn
anueGscNWFltrPkGtpV0ToutSess = _AnueGscNWFltrPkGtpV0ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 126),
    _AnueGscNWFltrPkGtpV0ToutSess_Type()
)
anueGscNWFltrPkGtpV0ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0ToutSess.setStatus("current")
_AnueGscNWFltrPkGtpV1ToutSess_Type = Counter64
_AnueGscNWFltrPkGtpV1ToutSess_Object = MibTableColumn
anueGscNWFltrPkGtpV1ToutSess = _AnueGscNWFltrPkGtpV1ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 127),
    _AnueGscNWFltrPkGtpV1ToutSess_Type()
)
anueGscNWFltrPkGtpV1ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1ToutSess.setStatus("current")
_AnueGscNWFltrPkGtpV2ToutSess_Type = Counter64
_AnueGscNWFltrPkGtpV2ToutSess_Object = MibTableColumn
anueGscNWFltrPkGtpV2ToutSess = _AnueGscNWFltrPkGtpV2ToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 128),
    _AnueGscNWFltrPkGtpV2ToutSess_Type()
)
anueGscNWFltrPkGtpV2ToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2ToutSess.setStatus("current")
_AnueGscNWFltrPkGtpTotToutSess_Type = Counter64
_AnueGscNWFltrPkGtpTotToutSess_Object = MibTableColumn
anueGscNWFltrPkGtpTotToutSess = _AnueGscNWFltrPkGtpTotToutSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 129),
    _AnueGscNWFltrPkGtpTotToutSess_Type()
)
anueGscNWFltrPkGtpTotToutSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotToutSess.setStatus("current")
_AnueGscNWFltrPkGtpV0ToutSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpV0ToutSessT_Object = MibTableColumn
anueGscNWFltrPkGtpV0ToutSessT = _AnueGscNWFltrPkGtpV0ToutSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 130),
    _AnueGscNWFltrPkGtpV0ToutSessT_Type()
)
anueGscNWFltrPkGtpV0ToutSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV0ToutSessT.setStatus("current")
_AnueGscNWFltrPkGtpV1ToutSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpV1ToutSessT_Object = MibTableColumn
anueGscNWFltrPkGtpV1ToutSessT = _AnueGscNWFltrPkGtpV1ToutSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 131),
    _AnueGscNWFltrPkGtpV1ToutSessT_Type()
)
anueGscNWFltrPkGtpV1ToutSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV1ToutSessT.setStatus("current")
_AnueGscNWFltrPkGtpV2ToutSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpV2ToutSessT_Object = MibTableColumn
anueGscNWFltrPkGtpV2ToutSessT = _AnueGscNWFltrPkGtpV2ToutSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 132),
    _AnueGscNWFltrPkGtpV2ToutSessT_Type()
)
anueGscNWFltrPkGtpV2ToutSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpV2ToutSessT.setStatus("current")
_AnueGscNWFltrPkGtpTotToutSessT_Type = DateAndTime
_AnueGscNWFltrPkGtpTotToutSessT_Object = MibTableColumn
anueGscNWFltrPkGtpTotToutSessT = _AnueGscNWFltrPkGtpTotToutSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 133),
    _AnueGscNWFltrPkGtpTotToutSessT_Type()
)
anueGscNWFltrPkGtpTotToutSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpTotToutSessT.setStatus("current")
_AnueGscNWFltrAvgGtpCPkts_Type = Counter64
_AnueGscNWFltrAvgGtpCPkts_Object = MibTableColumn
anueGscNWFltrAvgGtpCPkts = _AnueGscNWFltrAvgGtpCPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 134),
    _AnueGscNWFltrAvgGtpCPkts_Type()
)
anueGscNWFltrAvgGtpCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpCPkts.setStatus("current")
_AnueGscNWFltrAvgGtpUPkts_Type = Counter64
_AnueGscNWFltrAvgGtpUPkts_Object = MibTableColumn
anueGscNWFltrAvgGtpUPkts = _AnueGscNWFltrAvgGtpUPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 135),
    _AnueGscNWFltrAvgGtpUPkts_Type()
)
anueGscNWFltrAvgGtpUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGtpUPkts.setStatus("current")
_AnueGscNWFltrAvgDiameterPkts_Type = Counter64
_AnueGscNWFltrAvgDiameterPkts_Object = MibTableColumn
anueGscNWFltrAvgDiameterPkts = _AnueGscNWFltrAvgDiameterPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 136),
    _AnueGscNWFltrAvgDiameterPkts_Type()
)
anueGscNWFltrAvgDiameterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgDiameterPkts.setStatus("current")
_AnueGscNWFltrAvgDnsPkts_Type = Counter64
_AnueGscNWFltrAvgDnsPkts_Object = MibTableColumn
anueGscNWFltrAvgDnsPkts = _AnueGscNWFltrAvgDnsPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 137),
    _AnueGscNWFltrAvgDnsPkts_Type()
)
anueGscNWFltrAvgDnsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgDnsPkts.setStatus("current")
_AnueGscNWFltrAvgRadiusPkts_Type = Counter64
_AnueGscNWFltrAvgRadiusPkts_Object = MibTableColumn
anueGscNWFltrAvgRadiusPkts = _AnueGscNWFltrAvgRadiusPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 138),
    _AnueGscNWFltrAvgRadiusPkts_Type()
)
anueGscNWFltrAvgRadiusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgRadiusPkts.setStatus("current")
_AnueGscNWFltrAvgNonGtpPkts_Type = Counter64
_AnueGscNWFltrAvgNonGtpPkts_Object = MibTableColumn
anueGscNWFltrAvgNonGtpPkts = _AnueGscNWFltrAvgNonGtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 139),
    _AnueGscNWFltrAvgNonGtpPkts_Type()
)
anueGscNWFltrAvgNonGtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgNonGtpPkts.setStatus("current")
_AnueGscNWFltrCurGtpCPkts_Type = Counter64
_AnueGscNWFltrCurGtpCPkts_Object = MibTableColumn
anueGscNWFltrCurGtpCPkts = _AnueGscNWFltrCurGtpCPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 140),
    _AnueGscNWFltrCurGtpCPkts_Type()
)
anueGscNWFltrCurGtpCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpCPkts.setStatus("current")
_AnueGscNWFltrCurGtpUPkts_Type = Counter64
_AnueGscNWFltrCurGtpUPkts_Object = MibTableColumn
anueGscNWFltrCurGtpUPkts = _AnueGscNWFltrCurGtpUPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 141),
    _AnueGscNWFltrCurGtpUPkts_Type()
)
anueGscNWFltrCurGtpUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGtpUPkts.setStatus("current")
_AnueGscNWFltrCurDiameterPkts_Type = Counter64
_AnueGscNWFltrCurDiameterPkts_Object = MibTableColumn
anueGscNWFltrCurDiameterPkts = _AnueGscNWFltrCurDiameterPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 142),
    _AnueGscNWFltrCurDiameterPkts_Type()
)
anueGscNWFltrCurDiameterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurDiameterPkts.setStatus("current")
_AnueGscNWFltrCurDnsPkts_Type = Counter64
_AnueGscNWFltrCurDnsPkts_Object = MibTableColumn
anueGscNWFltrCurDnsPkts = _AnueGscNWFltrCurDnsPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 143),
    _AnueGscNWFltrCurDnsPkts_Type()
)
anueGscNWFltrCurDnsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurDnsPkts.setStatus("current")
_AnueGscNWFltrCurRadiusPkts_Type = Counter64
_AnueGscNWFltrCurRadiusPkts_Object = MibTableColumn
anueGscNWFltrCurRadiusPkts = _AnueGscNWFltrCurRadiusPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 144),
    _AnueGscNWFltrCurRadiusPkts_Type()
)
anueGscNWFltrCurRadiusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurRadiusPkts.setStatus("current")
_AnueGscNWFltrCurNonGtpPkts_Type = Counter64
_AnueGscNWFltrCurNonGtpPkts_Object = MibTableColumn
anueGscNWFltrCurNonGtpPkts = _AnueGscNWFltrCurNonGtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 145),
    _AnueGscNWFltrCurNonGtpPkts_Type()
)
anueGscNWFltrCurNonGtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurNonGtpPkts.setStatus("current")
_AnueGscNWFltrPkGtpCPkts_Type = Counter64
_AnueGscNWFltrPkGtpCPkts_Object = MibTableColumn
anueGscNWFltrPkGtpCPkts = _AnueGscNWFltrPkGtpCPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 146),
    _AnueGscNWFltrPkGtpCPkts_Type()
)
anueGscNWFltrPkGtpCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpCPkts.setStatus("current")
_AnueGscNWFltrPkGtpUPkts_Type = Counter64
_AnueGscNWFltrPkGtpUPkts_Object = MibTableColumn
anueGscNWFltrPkGtpUPkts = _AnueGscNWFltrPkGtpUPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 147),
    _AnueGscNWFltrPkGtpUPkts_Type()
)
anueGscNWFltrPkGtpUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpUPkts.setStatus("current")
_AnueGscNWFltrPkDiameterPkts_Type = Counter64
_AnueGscNWFltrPkDiameterPkts_Object = MibTableColumn
anueGscNWFltrPkDiameterPkts = _AnueGscNWFltrPkDiameterPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 148),
    _AnueGscNWFltrPkDiameterPkts_Type()
)
anueGscNWFltrPkDiameterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkDiameterPkts.setStatus("current")
_AnueGscNWFltrPkDnsPkts_Type = Counter64
_AnueGscNWFltrPkDnsPkts_Object = MibTableColumn
anueGscNWFltrPkDnsPkts = _AnueGscNWFltrPkDnsPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 149),
    _AnueGscNWFltrPkDnsPkts_Type()
)
anueGscNWFltrPkDnsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkDnsPkts.setStatus("current")
_AnueGscNWFltrPkRadiusPkts_Type = Counter64
_AnueGscNWFltrPkRadiusPkts_Object = MibTableColumn
anueGscNWFltrPkRadiusPkts = _AnueGscNWFltrPkRadiusPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 150),
    _AnueGscNWFltrPkRadiusPkts_Type()
)
anueGscNWFltrPkRadiusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkRadiusPkts.setStatus("current")
_AnueGscNWFltrPkNonGtpPkts_Type = Counter64
_AnueGscNWFltrPkNonGtpPkts_Object = MibTableColumn
anueGscNWFltrPkNonGtpPkts = _AnueGscNWFltrPkNonGtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 151),
    _AnueGscNWFltrPkNonGtpPkts_Type()
)
anueGscNWFltrPkNonGtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkNonGtpPkts.setStatus("current")
_AnueGscNWFltrPkGtpCPktsT_Type = DateAndTime
_AnueGscNWFltrPkGtpCPktsT_Object = MibTableColumn
anueGscNWFltrPkGtpCPktsT = _AnueGscNWFltrPkGtpCPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 152),
    _AnueGscNWFltrPkGtpCPktsT_Type()
)
anueGscNWFltrPkGtpCPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpCPktsT.setStatus("current")
_AnueGscNWFltrPkGtpUPktsT_Type = DateAndTime
_AnueGscNWFltrPkGtpUPktsT_Object = MibTableColumn
anueGscNWFltrPkGtpUPktsT = _AnueGscNWFltrPkGtpUPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 153),
    _AnueGscNWFltrPkGtpUPktsT_Type()
)
anueGscNWFltrPkGtpUPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGtpUPktsT.setStatus("current")
_AnueGscNWFltrPkDiameterPktsT_Type = DateAndTime
_AnueGscNWFltrPkDiameterPktsT_Object = MibTableColumn
anueGscNWFltrPkDiameterPktsT = _AnueGscNWFltrPkDiameterPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 154),
    _AnueGscNWFltrPkDiameterPktsT_Type()
)
anueGscNWFltrPkDiameterPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkDiameterPktsT.setStatus("current")
_AnueGscNWFltrPkDnsPktsT_Type = DateAndTime
_AnueGscNWFltrPkDnsPktsT_Object = MibTableColumn
anueGscNWFltrPkDnsPktsT = _AnueGscNWFltrPkDnsPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 155),
    _AnueGscNWFltrPkDnsPktsT_Type()
)
anueGscNWFltrPkDnsPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkDnsPktsT.setStatus("current")
_AnueGscNWFltrPkRadiusPktsT_Type = DateAndTime
_AnueGscNWFltrPkRadiusPktsT_Object = MibTableColumn
anueGscNWFltrPkRadiusPktsT = _AnueGscNWFltrPkRadiusPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 156),
    _AnueGscNWFltrPkRadiusPktsT_Type()
)
anueGscNWFltrPkRadiusPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkRadiusPktsT.setStatus("current")
_AnueGscNWFltrPkNonGtpPktsT_Type = DateAndTime
_AnueGscNWFltrPkNonGtpPktsT_Object = MibTableColumn
anueGscNWFltrPkNonGtpPktsT = _AnueGscNWFltrPkNonGtpPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 157),
    _AnueGscNWFltrPkNonGtpPktsT_Type()
)
anueGscNWFltrPkNonGtpPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkNonGtpPktsT.setStatus("current")
_AnueGscNWFltrTotGtpCPkts_Type = Counter64
_AnueGscNWFltrTotGtpCPkts_Object = MibTableColumn
anueGscNWFltrTotGtpCPkts = _AnueGscNWFltrTotGtpCPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 158),
    _AnueGscNWFltrTotGtpCPkts_Type()
)
anueGscNWFltrTotGtpCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpCPkts.setStatus("current")
_AnueGscNWFltrTotGtpUPkts_Type = Counter64
_AnueGscNWFltrTotGtpUPkts_Object = MibTableColumn
anueGscNWFltrTotGtpUPkts = _AnueGscNWFltrTotGtpUPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 159),
    _AnueGscNWFltrTotGtpUPkts_Type()
)
anueGscNWFltrTotGtpUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGtpUPkts.setStatus("current")
_AnueGscNWFltrTotDiameterPkts_Type = Counter64
_AnueGscNWFltrTotDiameterPkts_Object = MibTableColumn
anueGscNWFltrTotDiameterPkts = _AnueGscNWFltrTotDiameterPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 160),
    _AnueGscNWFltrTotDiameterPkts_Type()
)
anueGscNWFltrTotDiameterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotDiameterPkts.setStatus("current")
_AnueGscNWFltrTotDnsPkts_Type = Counter64
_AnueGscNWFltrTotDnsPkts_Object = MibTableColumn
anueGscNWFltrTotDnsPkts = _AnueGscNWFltrTotDnsPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 161),
    _AnueGscNWFltrTotDnsPkts_Type()
)
anueGscNWFltrTotDnsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotDnsPkts.setStatus("current")
_AnueGscNWFltrTotRadiusPkts_Type = Counter64
_AnueGscNWFltrTotRadiusPkts_Object = MibTableColumn
anueGscNWFltrTotRadiusPkts = _AnueGscNWFltrTotRadiusPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 162),
    _AnueGscNWFltrTotRadiusPkts_Type()
)
anueGscNWFltrTotRadiusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotRadiusPkts.setStatus("current")
_AnueGscNWFltrTotNonGtpPkts_Type = Counter64
_AnueGscNWFltrTotNonGtpPkts_Object = MibTableColumn
anueGscNWFltrTotNonGtpPkts = _AnueGscNWFltrTotNonGtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 163),
    _AnueGscNWFltrTotNonGtpPkts_Type()
)
anueGscNWFltrTotNonGtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotNonGtpPkts.setStatus("current")
_AnueGscNWFltrTotGscDropPkts_Type = Counter64
_AnueGscNWFltrTotGscDropPkts_Object = MibTableColumn
anueGscNWFltrTotGscDropPkts = _AnueGscNWFltrTotGscDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 164),
    _AnueGscNWFltrTotGscDropPkts_Type()
)
anueGscNWFltrTotGscDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGscDropPkts.setStatus("current")
_AnueGscNWFltrCurGscSessLoad_Type = CounterBasedGauge64
_AnueGscNWFltrCurGscSessLoad_Object = MibTableColumn
anueGscNWFltrCurGscSessLoad = _AnueGscNWFltrCurGscSessLoad_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 165),
    _AnueGscNWFltrCurGscSessLoad_Type()
)
anueGscNWFltrCurGscSessLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGscSessLoad.setStatus("current")
_AnueGscNWFltrAvgGscSessLoad_Type = CounterBasedGauge64
_AnueGscNWFltrAvgGscSessLoad_Object = MibTableColumn
anueGscNWFltrAvgGscSessLoad = _AnueGscNWFltrAvgGscSessLoad_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 166),
    _AnueGscNWFltrAvgGscSessLoad_Type()
)
anueGscNWFltrAvgGscSessLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGscSessLoad.setStatus("current")
_AnueGscNWFltrPeakGscSessLoad_Type = CounterBasedGauge64
_AnueGscNWFltrPeakGscSessLoad_Object = MibTableColumn
anueGscNWFltrPeakGscSessLoad = _AnueGscNWFltrPeakGscSessLoad_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 167),
    _AnueGscNWFltrPeakGscSessLoad_Type()
)
anueGscNWFltrPeakGscSessLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPeakGscSessLoad.setStatus("current")
_AnueGscNWFltrPeakGscSessLoadT_Type = DateAndTime
_AnueGscNWFltrPeakGscSessLoadT_Object = MibTableColumn
anueGscNWFltrPeakGscSessLoadT = _AnueGscNWFltrPeakGscSessLoadT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 168),
    _AnueGscNWFltrPeakGscSessLoadT_Type()
)
anueGscNWFltrPeakGscSessLoadT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPeakGscSessLoadT.setStatus("current")
_AnueGscNWFltrCurNetwElemLoad_Type = CounterBasedGauge64
_AnueGscNWFltrCurNetwElemLoad_Object = MibTableColumn
anueGscNWFltrCurNetwElemLoad = _AnueGscNWFltrCurNetwElemLoad_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 169),
    _AnueGscNWFltrCurNetwElemLoad_Type()
)
anueGscNWFltrCurNetwElemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurNetwElemLoad.setStatus("current")
_AnueGscNWFltrPeakNetwElemLoad_Type = CounterBasedGauge64
_AnueGscNWFltrPeakNetwElemLoad_Object = MibTableColumn
anueGscNWFltrPeakNetwElemLoad = _AnueGscNWFltrPeakNetwElemLoad_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 170),
    _AnueGscNWFltrPeakNetwElemLoad_Type()
)
anueGscNWFltrPeakNetwElemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPeakNetwElemLoad.setStatus("current")
_AnueGscNWFltrPeakNetwElemLoadT_Type = DateAndTime
_AnueGscNWFltrPeakNetwElemLoadT_Object = MibTableColumn
anueGscNWFltrPeakNetwElemLoadT = _AnueGscNWFltrPeakNetwElemLoadT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 171),
    _AnueGscNWFltrPeakNetwElemLoadT_Type()
)
anueGscNWFltrPeakNetwElemLoadT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPeakNetwElemLoadT.setStatus("current")
_AnueGscNWFltrCurReqRespLoad_Type = CounterBasedGauge64
_AnueGscNWFltrCurReqRespLoad_Object = MibTableColumn
anueGscNWFltrCurReqRespLoad = _AnueGscNWFltrCurReqRespLoad_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 172),
    _AnueGscNWFltrCurReqRespLoad_Type()
)
anueGscNWFltrCurReqRespLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurReqRespLoad.setStatus("current")
_AnueGscNWFltrPeakReqRespLoad_Type = CounterBasedGauge64
_AnueGscNWFltrPeakReqRespLoad_Object = MibTableColumn
anueGscNWFltrPeakReqRespLoad = _AnueGscNWFltrPeakReqRespLoad_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 173),
    _AnueGscNWFltrPeakReqRespLoad_Type()
)
anueGscNWFltrPeakReqRespLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPeakReqRespLoad.setStatus("current")
_AnueGscNWFltrPeakReqRespLoadT_Type = DateAndTime
_AnueGscNWFltrPeakReqRespLoadT_Object = MibTableColumn
anueGscNWFltrPeakReqRespLoadT = _AnueGscNWFltrPeakReqRespLoadT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 174),
    _AnueGscNWFltrPeakReqRespLoadT_Type()
)
anueGscNWFltrPeakReqRespLoadT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPeakReqRespLoadT.setStatus("current")
_AnueGscNWFltrCurFragLoad_Type = CounterBasedGauge64
_AnueGscNWFltrCurFragLoad_Object = MibTableColumn
anueGscNWFltrCurFragLoad = _AnueGscNWFltrCurFragLoad_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 175),
    _AnueGscNWFltrCurFragLoad_Type()
)
anueGscNWFltrCurFragLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurFragLoad.setStatus("current")
_AnueGscNWFltrPeakFragLoad_Type = CounterBasedGauge64
_AnueGscNWFltrPeakFragLoad_Object = MibTableColumn
anueGscNWFltrPeakFragLoad = _AnueGscNWFltrPeakFragLoad_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 176),
    _AnueGscNWFltrPeakFragLoad_Type()
)
anueGscNWFltrPeakFragLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPeakFragLoad.setStatus("current")
_AnueGscNWFltrPeakFragLoadT_Type = DateAndTime
_AnueGscNWFltrPeakFragLoadT_Object = MibTableColumn
anueGscNWFltrPeakFragLoadT = _AnueGscNWFltrPeakFragLoadT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 177),
    _AnueGscNWFltrPeakFragLoadT_Type()
)
anueGscNWFltrPeakFragLoadT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPeakFragLoadT.setStatus("current")
_AnueGscNWFltrAvgGscUnassignedSess_Type = Counter64
_AnueGscNWFltrAvgGscUnassignedSess_Object = MibTableColumn
anueGscNWFltrAvgGscUnassignedSess = _AnueGscNWFltrAvgGscUnassignedSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 178),
    _AnueGscNWFltrAvgGscUnassignedSess_Type()
)
anueGscNWFltrAvgGscUnassignedSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgGscUnassignedSess.setStatus("current")
_AnueGscNWFltrCurGscUnassignedSess_Type = Counter64
_AnueGscNWFltrCurGscUnassignedSess_Object = MibTableColumn
anueGscNWFltrCurGscUnassignedSess = _AnueGscNWFltrCurGscUnassignedSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 179),
    _AnueGscNWFltrCurGscUnassignedSess_Type()
)
anueGscNWFltrCurGscUnassignedSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurGscUnassignedSess.setStatus("current")
_AnueGscNWFltrPkGscUnassignedSess_Type = Counter64
_AnueGscNWFltrPkGscUnassignedSess_Object = MibTableColumn
anueGscNWFltrPkGscUnassignedSess = _AnueGscNWFltrPkGscUnassignedSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 180),
    _AnueGscNWFltrPkGscUnassignedSess_Type()
)
anueGscNWFltrPkGscUnassignedSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGscUnassignedSess.setStatus("current")
_AnueGscNWFltrPkGscUnassignedSessT_Type = DateAndTime
_AnueGscNWFltrPkGscUnassignedSessT_Object = MibTableColumn
anueGscNWFltrPkGscUnassignedSessT = _AnueGscNWFltrPkGscUnassignedSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 181),
    _AnueGscNWFltrPkGscUnassignedSessT_Type()
)
anueGscNWFltrPkGscUnassignedSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkGscUnassignedSessT.setStatus("current")
_AnueGscNWFltrTotGscUnassignedSess_Type = Counter64
_AnueGscNWFltrTotGscUnassignedSess_Object = MibTableColumn
anueGscNWFltrTotGscUnassignedSess = _AnueGscNWFltrTotGscUnassignedSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 182),
    _AnueGscNWFltrTotGscUnassignedSess_Type()
)
anueGscNWFltrTotGscUnassignedSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotGscUnassignedSess.setStatus("current")
_AnueGscNWFltrAvgUnprocReq_Type = Counter64
_AnueGscNWFltrAvgUnprocReq_Object = MibTableColumn
anueGscNWFltrAvgUnprocReq = _AnueGscNWFltrAvgUnprocReq_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 183),
    _AnueGscNWFltrAvgUnprocReq_Type()
)
anueGscNWFltrAvgUnprocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgUnprocReq.setStatus("current")
_AnueGscNWFltrCurUnprocReq_Type = Counter64
_AnueGscNWFltrCurUnprocReq_Object = MibTableColumn
anueGscNWFltrCurUnprocReq = _AnueGscNWFltrCurUnprocReq_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 184),
    _AnueGscNWFltrCurUnprocReq_Type()
)
anueGscNWFltrCurUnprocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurUnprocReq.setStatus("current")
_AnueGscNWFltrPkUnprocReq_Type = Counter64
_AnueGscNWFltrPkUnprocReq_Object = MibTableColumn
anueGscNWFltrPkUnprocReq = _AnueGscNWFltrPkUnprocReq_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 185),
    _AnueGscNWFltrPkUnprocReq_Type()
)
anueGscNWFltrPkUnprocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkUnprocReq.setStatus("current")
_AnueGscNWFltrPkUnprocReqT_Type = DateAndTime
_AnueGscNWFltrPkUnprocReqT_Object = MibTableColumn
anueGscNWFltrPkUnprocReqT = _AnueGscNWFltrPkUnprocReqT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 186),
    _AnueGscNWFltrPkUnprocReqT_Type()
)
anueGscNWFltrPkUnprocReqT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkUnprocReqT.setStatus("current")
_AnueGscNWFltrTotUnprocReq_Type = Counter64
_AnueGscNWFltrTotUnprocReq_Object = MibTableColumn
anueGscNWFltrTotUnprocReq = _AnueGscNWFltrTotUnprocReq_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 187),
    _AnueGscNWFltrTotUnprocReq_Type()
)
anueGscNWFltrTotUnprocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotUnprocReq.setStatus("current")
_AnueGscNWFltrAvgTdOutReq_Type = Counter64
_AnueGscNWFltrAvgTdOutReq_Object = MibTableColumn
anueGscNWFltrAvgTdOutReq = _AnueGscNWFltrAvgTdOutReq_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 188),
    _AnueGscNWFltrAvgTdOutReq_Type()
)
anueGscNWFltrAvgTdOutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgTdOutReq.setStatus("current")
_AnueGscNWFltrCurTdOutReq_Type = Counter64
_AnueGscNWFltrCurTdOutReq_Object = MibTableColumn
anueGscNWFltrCurTdOutReq = _AnueGscNWFltrCurTdOutReq_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 189),
    _AnueGscNWFltrCurTdOutReq_Type()
)
anueGscNWFltrCurTdOutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurTdOutReq.setStatus("current")
_AnueGscNWFltrPkTdOutReq_Type = Counter64
_AnueGscNWFltrPkTdOutReq_Object = MibTableColumn
anueGscNWFltrPkTdOutReq = _AnueGscNWFltrPkTdOutReq_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 190),
    _AnueGscNWFltrPkTdOutReq_Type()
)
anueGscNWFltrPkTdOutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkTdOutReq.setStatus("current")
_AnueGscNWFltrPkTdOutReqT_Type = DateAndTime
_AnueGscNWFltrPkTdOutReqT_Object = MibTableColumn
anueGscNWFltrPkTdOutReqT = _AnueGscNWFltrPkTdOutReqT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 191),
    _AnueGscNWFltrPkTdOutReqT_Type()
)
anueGscNWFltrPkTdOutReqT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkTdOutReqT.setStatus("current")
_AnueGscNWFltrTotTdOutReq_Type = Counter64
_AnueGscNWFltrTotTdOutReq_Object = MibTableColumn
anueGscNWFltrTotTdOutReq = _AnueGscNWFltrTotTdOutReq_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 192),
    _AnueGscNWFltrTotTdOutReq_Type()
)
anueGscNWFltrTotTdOutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotTdOutReq.setStatus("current")
_AnueGscNWFltrAvgUnmatchedResp_Type = Counter64
_AnueGscNWFltrAvgUnmatchedResp_Object = MibTableColumn
anueGscNWFltrAvgUnmatchedResp = _AnueGscNWFltrAvgUnmatchedResp_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 193),
    _AnueGscNWFltrAvgUnmatchedResp_Type()
)
anueGscNWFltrAvgUnmatchedResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrAvgUnmatchedResp.setStatus("current")
_AnueGscNWFltrCurUnmatchedResp_Type = Counter64
_AnueGscNWFltrCurUnmatchedResp_Object = MibTableColumn
anueGscNWFltrCurUnmatchedResp = _AnueGscNWFltrCurUnmatchedResp_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 194),
    _AnueGscNWFltrCurUnmatchedResp_Type()
)
anueGscNWFltrCurUnmatchedResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrCurUnmatchedResp.setStatus("current")
_AnueGscNWFltrPkUnmatchedResp_Type = Counter64
_AnueGscNWFltrPkUnmatchedResp_Object = MibTableColumn
anueGscNWFltrPkUnmatchedResp = _AnueGscNWFltrPkUnmatchedResp_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 195),
    _AnueGscNWFltrPkUnmatchedResp_Type()
)
anueGscNWFltrPkUnmatchedResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkUnmatchedResp.setStatus("current")
_AnueGscNWFltrPkUnmatchedRespT_Type = DateAndTime
_AnueGscNWFltrPkUnmatchedRespT_Object = MibTableColumn
anueGscNWFltrPkUnmatchedRespT = _AnueGscNWFltrPkUnmatchedRespT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 196),
    _AnueGscNWFltrPkUnmatchedRespT_Type()
)
anueGscNWFltrPkUnmatchedRespT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrPkUnmatchedRespT.setStatus("current")
_AnueGscNWFltrTotUnmatchedResp_Type = Counter64
_AnueGscNWFltrTotUnmatchedResp_Object = MibTableColumn
anueGscNWFltrTotUnmatchedResp = _AnueGscNWFltrTotUnmatchedResp_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 197),
    _AnueGscNWFltrTotUnmatchedResp_Type()
)
anueGscNWFltrTotUnmatchedResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrTotUnmatchedResp.setStatus("current")
_AnueGscNWFltrOverloadErrCode_Type = Counter64
_AnueGscNWFltrOverloadErrCode_Object = MibTableColumn
anueGscNWFltrOverloadErrCode = _AnueGscNWFltrOverloadErrCode_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 198),
    _AnueGscNWFltrOverloadErrCode_Type()
)
anueGscNWFltrOverloadErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrOverloadErrCode.setStatus("current")
_AnueGscNWFltrOverloadT_Type = DateAndTime
_AnueGscNWFltrOverloadT_Object = MibTableColumn
anueGscNWFltrOverloadT = _AnueGscNWFltrOverloadT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 100, 1, 199),
    _AnueGscNWFltrOverloadT_Type()
)
anueGscNWFltrOverloadT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscNWFltrOverloadT.setStatus("current")
_AnueNtoStageGscToolFilterTable_Object = MibTable
anueNtoStageGscToolFilterTable = _AnueNtoStageGscToolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101)
)
if mibBuilder.loadTexts:
    anueNtoStageGscToolFilterTable.setStatus("current")
_AnueNtoStageGscToolFilterEntry_Object = MibTableRow
anueNtoStageGscToolFilterEntry = _AnueNtoStageGscToolFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1)
)
anueNtoStageGscToolFilterEntry.setIndexNames(
    (0, "ANUE-MIB", "anueNtoStageGscToolFilterType"),
    (0, "ANUE-MIB", "anueNtoStageGscToolFilterNumber"),
    (0, "ANUE-MIB", "anueNtoStageGscToolFilterFeature"),
)
if mibBuilder.loadTexts:
    anueNtoStageGscToolFilterEntry.setStatus("current")
_AnueNtoStageGscToolFilterType_Type = AnueFilterTypeDT
_AnueNtoStageGscToolFilterType_Object = MibTableColumn
anueNtoStageGscToolFilterType = _AnueNtoStageGscToolFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 1),
    _AnueNtoStageGscToolFilterType_Type()
)
anueNtoStageGscToolFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueNtoStageGscToolFilterType.setStatus("current")


class _AnueNtoStageGscToolFilterNumber_Type(Integer32):
    """Custom type anueNtoStageGscToolFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueNtoStageGscToolFilterNumber_Type.__name__ = "Integer32"
_AnueNtoStageGscToolFilterNumber_Object = MibTableColumn
anueNtoStageGscToolFilterNumber = _AnueNtoStageGscToolFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 2),
    _AnueNtoStageGscToolFilterNumber_Type()
)
anueNtoStageGscToolFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueNtoStageGscToolFilterNumber.setStatus("current")
_AnueNtoStageGscToolFilterFeature_Type = AnueStageType
_AnueNtoStageGscToolFilterFeature_Object = MibTableColumn
anueNtoStageGscToolFilterFeature = _AnueNtoStageGscToolFilterFeature_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 3),
    _AnueNtoStageGscToolFilterFeature_Type()
)
anueNtoStageGscToolFilterFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueNtoStageGscToolFilterFeature.setStatus("current")
_AnueGscTFltrCurGtpV0ActSess_Type = Counter64
_AnueGscTFltrCurGtpV0ActSess_Object = MibTableColumn
anueGscTFltrCurGtpV0ActSess = _AnueGscTFltrCurGtpV0ActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 4),
    _AnueGscTFltrCurGtpV0ActSess_Type()
)
anueGscTFltrCurGtpV0ActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrCurGtpV0ActSess.setStatus("current")
_AnueGscTFltrCurGtpV1ActSess_Type = Counter64
_AnueGscTFltrCurGtpV1ActSess_Object = MibTableColumn
anueGscTFltrCurGtpV1ActSess = _AnueGscTFltrCurGtpV1ActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 5),
    _AnueGscTFltrCurGtpV1ActSess_Type()
)
anueGscTFltrCurGtpV1ActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrCurGtpV1ActSess.setStatus("current")
_AnueGscTFltrCurGtpV2ActSess_Type = Counter64
_AnueGscTFltrCurGtpV2ActSess_Object = MibTableColumn
anueGscTFltrCurGtpV2ActSess = _AnueGscTFltrCurGtpV2ActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 6),
    _AnueGscTFltrCurGtpV2ActSess_Type()
)
anueGscTFltrCurGtpV2ActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrCurGtpV2ActSess.setStatus("current")
_AnueGscTFltrCurGtpTotActSess_Type = Counter64
_AnueGscTFltrCurGtpTotActSess_Object = MibTableColumn
anueGscTFltrCurGtpTotActSess = _AnueGscTFltrCurGtpTotActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 7),
    _AnueGscTFltrCurGtpTotActSess_Type()
)
anueGscTFltrCurGtpTotActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrCurGtpTotActSess.setStatus("current")
_AnueGscTFltrAvgGtpV0ActSess_Type = Counter64
_AnueGscTFltrAvgGtpV0ActSess_Object = MibTableColumn
anueGscTFltrAvgGtpV0ActSess = _AnueGscTFltrAvgGtpV0ActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 8),
    _AnueGscTFltrAvgGtpV0ActSess_Type()
)
anueGscTFltrAvgGtpV0ActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrAvgGtpV0ActSess.setStatus("current")
_AnueGscTFltrAvgGtpV1ActSess_Type = Counter64
_AnueGscTFltrAvgGtpV1ActSess_Object = MibTableColumn
anueGscTFltrAvgGtpV1ActSess = _AnueGscTFltrAvgGtpV1ActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 9),
    _AnueGscTFltrAvgGtpV1ActSess_Type()
)
anueGscTFltrAvgGtpV1ActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrAvgGtpV1ActSess.setStatus("current")
_AnueGscTFltrAvgGtpV2ActSess_Type = Counter64
_AnueGscTFltrAvgGtpV2ActSess_Object = MibTableColumn
anueGscTFltrAvgGtpV2ActSess = _AnueGscTFltrAvgGtpV2ActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 10),
    _AnueGscTFltrAvgGtpV2ActSess_Type()
)
anueGscTFltrAvgGtpV2ActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrAvgGtpV2ActSess.setStatus("current")
_AnueGscTFltrAvgGtpTotActSess_Type = Counter64
_AnueGscTFltrAvgGtpTotActSess_Object = MibTableColumn
anueGscTFltrAvgGtpTotActSess = _AnueGscTFltrAvgGtpTotActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 11),
    _AnueGscTFltrAvgGtpTotActSess_Type()
)
anueGscTFltrAvgGtpTotActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrAvgGtpTotActSess.setStatus("current")
_AnueGscTFltrPeakGtpV0ActSess_Type = Counter64
_AnueGscTFltrPeakGtpV0ActSess_Object = MibTableColumn
anueGscTFltrPeakGtpV0ActSess = _AnueGscTFltrPeakGtpV0ActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 12),
    _AnueGscTFltrPeakGtpV0ActSess_Type()
)
anueGscTFltrPeakGtpV0ActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpV0ActSess.setStatus("current")
_AnueGscTFltrPeakGtpV1ActSess_Type = Counter64
_AnueGscTFltrPeakGtpV1ActSess_Object = MibTableColumn
anueGscTFltrPeakGtpV1ActSess = _AnueGscTFltrPeakGtpV1ActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 13),
    _AnueGscTFltrPeakGtpV1ActSess_Type()
)
anueGscTFltrPeakGtpV1ActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpV1ActSess.setStatus("current")
_AnueGscTFltrPeakGtpV2ActSess_Type = Counter64
_AnueGscTFltrPeakGtpV2ActSess_Object = MibTableColumn
anueGscTFltrPeakGtpV2ActSess = _AnueGscTFltrPeakGtpV2ActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 14),
    _AnueGscTFltrPeakGtpV2ActSess_Type()
)
anueGscTFltrPeakGtpV2ActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpV2ActSess.setStatus("current")
_AnueGscTFltrPeakGtpTotActSess_Type = Counter64
_AnueGscTFltrPeakGtpTotActSess_Object = MibTableColumn
anueGscTFltrPeakGtpTotActSess = _AnueGscTFltrPeakGtpTotActSess_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 15),
    _AnueGscTFltrPeakGtpTotActSess_Type()
)
anueGscTFltrPeakGtpTotActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpTotActSess.setStatus("current")
_AnueGscTFltrPeakGtpV0ActSessT_Type = DateAndTime
_AnueGscTFltrPeakGtpV0ActSessT_Object = MibTableColumn
anueGscTFltrPeakGtpV0ActSessT = _AnueGscTFltrPeakGtpV0ActSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 16),
    _AnueGscTFltrPeakGtpV0ActSessT_Type()
)
anueGscTFltrPeakGtpV0ActSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpV0ActSessT.setStatus("current")
_AnueGscTFltrPeakGtpV1ActSessT_Type = DateAndTime
_AnueGscTFltrPeakGtpV1ActSessT_Object = MibTableColumn
anueGscTFltrPeakGtpV1ActSessT = _AnueGscTFltrPeakGtpV1ActSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 17),
    _AnueGscTFltrPeakGtpV1ActSessT_Type()
)
anueGscTFltrPeakGtpV1ActSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpV1ActSessT.setStatus("current")
_AnueGscTFltrPeakGtpV2ActSessT_Type = DateAndTime
_AnueGscTFltrPeakGtpV2ActSessT_Object = MibTableColumn
anueGscTFltrPeakGtpV2ActSessT = _AnueGscTFltrPeakGtpV2ActSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 18),
    _AnueGscTFltrPeakGtpV2ActSessT_Type()
)
anueGscTFltrPeakGtpV2ActSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpV2ActSessT.setStatus("current")
_AnueGscTFltrPeakGtpTotActSessT_Type = DateAndTime
_AnueGscTFltrPeakGtpTotActSessT_Object = MibTableColumn
anueGscTFltrPeakGtpTotActSessT = _AnueGscTFltrPeakGtpTotActSessT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 19),
    _AnueGscTFltrPeakGtpTotActSessT_Type()
)
anueGscTFltrPeakGtpTotActSessT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpTotActSessT.setStatus("current")
_AnueGscTFltrAvgGtpCPkts_Type = Counter64
_AnueGscTFltrAvgGtpCPkts_Object = MibTableColumn
anueGscTFltrAvgGtpCPkts = _AnueGscTFltrAvgGtpCPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 20),
    _AnueGscTFltrAvgGtpCPkts_Type()
)
anueGscTFltrAvgGtpCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrAvgGtpCPkts.setStatus("current")
_AnueGscTFltrAvgGtpUPkts_Type = Counter64
_AnueGscTFltrAvgGtpUPkts_Object = MibTableColumn
anueGscTFltrAvgGtpUPkts = _AnueGscTFltrAvgGtpUPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 21),
    _AnueGscTFltrAvgGtpUPkts_Type()
)
anueGscTFltrAvgGtpUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrAvgGtpUPkts.setStatus("current")
_AnueGscTFltrAvgDiameterPkts_Type = Counter64
_AnueGscTFltrAvgDiameterPkts_Object = MibTableColumn
anueGscTFltrAvgDiameterPkts = _AnueGscTFltrAvgDiameterPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 22),
    _AnueGscTFltrAvgDiameterPkts_Type()
)
anueGscTFltrAvgDiameterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrAvgDiameterPkts.setStatus("current")
_AnueGscTFltrAvgDnsPkts_Type = Counter64
_AnueGscTFltrAvgDnsPkts_Object = MibTableColumn
anueGscTFltrAvgDnsPkts = _AnueGscTFltrAvgDnsPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 23),
    _AnueGscTFltrAvgDnsPkts_Type()
)
anueGscTFltrAvgDnsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrAvgDnsPkts.setStatus("current")
_AnueGscTFltrAvgRadiusPkts_Type = Counter64
_AnueGscTFltrAvgRadiusPkts_Object = MibTableColumn
anueGscTFltrAvgRadiusPkts = _AnueGscTFltrAvgRadiusPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 24),
    _AnueGscTFltrAvgRadiusPkts_Type()
)
anueGscTFltrAvgRadiusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrAvgRadiusPkts.setStatus("current")
_AnueGscTFltrPeakGtpCPkts_Type = Counter64
_AnueGscTFltrPeakGtpCPkts_Object = MibTableColumn
anueGscTFltrPeakGtpCPkts = _AnueGscTFltrPeakGtpCPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 25),
    _AnueGscTFltrPeakGtpCPkts_Type()
)
anueGscTFltrPeakGtpCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpCPkts.setStatus("current")
_AnueGscTFltrPeakGtpUPkts_Type = Counter64
_AnueGscTFltrPeakGtpUPkts_Object = MibTableColumn
anueGscTFltrPeakGtpUPkts = _AnueGscTFltrPeakGtpUPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 26),
    _AnueGscTFltrPeakGtpUPkts_Type()
)
anueGscTFltrPeakGtpUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpUPkts.setStatus("current")
_AnueGscTFltrPeakDiameterPkts_Type = Counter64
_AnueGscTFltrPeakDiameterPkts_Object = MibTableColumn
anueGscTFltrPeakDiameterPkts = _AnueGscTFltrPeakDiameterPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 27),
    _AnueGscTFltrPeakDiameterPkts_Type()
)
anueGscTFltrPeakDiameterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakDiameterPkts.setStatus("current")
_AnueGscTFltrPeakDnsPkts_Type = Counter64
_AnueGscTFltrPeakDnsPkts_Object = MibTableColumn
anueGscTFltrPeakDnsPkts = _AnueGscTFltrPeakDnsPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 28),
    _AnueGscTFltrPeakDnsPkts_Type()
)
anueGscTFltrPeakDnsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakDnsPkts.setStatus("current")
_AnueGscTFltrPeakRadiusPkts_Type = Counter64
_AnueGscTFltrPeakRadiusPkts_Object = MibTableColumn
anueGscTFltrPeakRadiusPkts = _AnueGscTFltrPeakRadiusPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 29),
    _AnueGscTFltrPeakRadiusPkts_Type()
)
anueGscTFltrPeakRadiusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakRadiusPkts.setStatus("current")
_AnueGscTFltrPeakGtpCPktsT_Type = DateAndTime
_AnueGscTFltrPeakGtpCPktsT_Object = MibTableColumn
anueGscTFltrPeakGtpCPktsT = _AnueGscTFltrPeakGtpCPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 30),
    _AnueGscTFltrPeakGtpCPktsT_Type()
)
anueGscTFltrPeakGtpCPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpCPktsT.setStatus("current")
_AnueGscTFltrPeakGtpUPktsT_Type = DateAndTime
_AnueGscTFltrPeakGtpUPktsT_Object = MibTableColumn
anueGscTFltrPeakGtpUPktsT = _AnueGscTFltrPeakGtpUPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 31),
    _AnueGscTFltrPeakGtpUPktsT_Type()
)
anueGscTFltrPeakGtpUPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakGtpUPktsT.setStatus("current")
_AnueGscTFltrPeakDiameterPktsT_Type = DateAndTime
_AnueGscTFltrPeakDiameterPktsT_Object = MibTableColumn
anueGscTFltrPeakDiameterPktsT = _AnueGscTFltrPeakDiameterPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 32),
    _AnueGscTFltrPeakDiameterPktsT_Type()
)
anueGscTFltrPeakDiameterPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakDiameterPktsT.setStatus("current")
_AnueGscTFltrPeakDnsPktsT_Type = DateAndTime
_AnueGscTFltrPeakDnsPktsT_Object = MibTableColumn
anueGscTFltrPeakDnsPktsT = _AnueGscTFltrPeakDnsPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 33),
    _AnueGscTFltrPeakDnsPktsT_Type()
)
anueGscTFltrPeakDnsPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakDnsPktsT.setStatus("current")
_AnueGscTFltrPeakRadiusPktsT_Type = DateAndTime
_AnueGscTFltrPeakRadiusPktsT_Object = MibTableColumn
anueGscTFltrPeakRadiusPktsT = _AnueGscTFltrPeakRadiusPktsT_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 34),
    _AnueGscTFltrPeakRadiusPktsT_Type()
)
anueGscTFltrPeakRadiusPktsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrPeakRadiusPktsT.setStatus("current")
_AnueGscTFltrTotGtpCPkts_Type = Counter64
_AnueGscTFltrTotGtpCPkts_Object = MibTableColumn
anueGscTFltrTotGtpCPkts = _AnueGscTFltrTotGtpCPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 35),
    _AnueGscTFltrTotGtpCPkts_Type()
)
anueGscTFltrTotGtpCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrTotGtpCPkts.setStatus("current")
_AnueGscTFltrTotGtpUPkts_Type = Counter64
_AnueGscTFltrTotGtpUPkts_Object = MibTableColumn
anueGscTFltrTotGtpUPkts = _AnueGscTFltrTotGtpUPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 36),
    _AnueGscTFltrTotGtpUPkts_Type()
)
anueGscTFltrTotGtpUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrTotGtpUPkts.setStatus("current")
_AnueGscTFltrTotDiameterPkts_Type = Counter64
_AnueGscTFltrTotDiameterPkts_Object = MibTableColumn
anueGscTFltrTotDiameterPkts = _AnueGscTFltrTotDiameterPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 37),
    _AnueGscTFltrTotDiameterPkts_Type()
)
anueGscTFltrTotDiameterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrTotDiameterPkts.setStatus("current")
_AnueGscTFltrTotDnsPkts_Type = Counter64
_AnueGscTFltrTotDnsPkts_Object = MibTableColumn
anueGscTFltrTotDnsPkts = _AnueGscTFltrTotDnsPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 38),
    _AnueGscTFltrTotDnsPkts_Type()
)
anueGscTFltrTotDnsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrTotDnsPkts.setStatus("current")
_AnueGscTFltrTotRadiusPkts_Type = Counter64
_AnueGscTFltrTotRadiusPkts_Object = MibTableColumn
anueGscTFltrTotRadiusPkts = _AnueGscTFltrTotRadiusPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 39),
    _AnueGscTFltrTotRadiusPkts_Type()
)
anueGscTFltrTotRadiusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrTotRadiusPkts.setStatus("current")
_AnueGscTFltrCurGtpCPkts_Type = Counter64
_AnueGscTFltrCurGtpCPkts_Object = MibTableColumn
anueGscTFltrCurGtpCPkts = _AnueGscTFltrCurGtpCPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 40),
    _AnueGscTFltrCurGtpCPkts_Type()
)
anueGscTFltrCurGtpCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrCurGtpCPkts.setStatus("current")
_AnueGscTFltrCurGtpUPkts_Type = Counter64
_AnueGscTFltrCurGtpUPkts_Object = MibTableColumn
anueGscTFltrCurGtpUPkts = _AnueGscTFltrCurGtpUPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 41),
    _AnueGscTFltrCurGtpUPkts_Type()
)
anueGscTFltrCurGtpUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrCurGtpUPkts.setStatus("current")
_AnueGscTFltrCurDiameterPkts_Type = Counter64
_AnueGscTFltrCurDiameterPkts_Object = MibTableColumn
anueGscTFltrCurDiameterPkts = _AnueGscTFltrCurDiameterPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 42),
    _AnueGscTFltrCurDiameterPkts_Type()
)
anueGscTFltrCurDiameterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrCurDiameterPkts.setStatus("current")
_AnueGscTFltrCurDnsPkts_Type = Counter64
_AnueGscTFltrCurDnsPkts_Object = MibTableColumn
anueGscTFltrCurDnsPkts = _AnueGscTFltrCurDnsPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 43),
    _AnueGscTFltrCurDnsPkts_Type()
)
anueGscTFltrCurDnsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrCurDnsPkts.setStatus("current")
_AnueGscTFltrCurRadiusPkts_Type = Counter64
_AnueGscTFltrCurRadiusPkts_Object = MibTableColumn
anueGscTFltrCurRadiusPkts = _AnueGscTFltrCurRadiusPkts_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 4, 101, 1, 44),
    _AnueGscTFltrCurRadiusPkts_Type()
)
anueGscTFltrCurRadiusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscTFltrCurRadiusPkts.setStatus("current")
_AnueNtoPayload_ObjectIdentity = ObjectIdentity
anueNtoPayload = _AnueNtoPayload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5)
)
_AnueNtoEventMonData_ObjectIdentity = ObjectIdentity
anueNtoEventMonData = _AnueNtoEventMonData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1)
)
_AnueNtoEventMonDataDateAndTime_Type = DateAndTime
_AnueNtoEventMonDataDateAndTime_Object = MibScalar
anueNtoEventMonDataDateAndTime = _AnueNtoEventMonDataDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 1),
    _AnueNtoEventMonDataDateAndTime_Type()
)
anueNtoEventMonDataDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataDateAndTime.setStatus("current")
_AnueNtoEventMonDataTriggerCause_Type = ObjectIdentifier
_AnueNtoEventMonDataTriggerCause_Object = MibScalar
anueNtoEventMonDataTriggerCause = _AnueNtoEventMonDataTriggerCause_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 2),
    _AnueNtoEventMonDataTriggerCause_Type()
)
anueNtoEventMonDataTriggerCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataTriggerCause.setStatus("current")
_AnueNtoEventMonDataTriggerValue_Type = DisplayString
_AnueNtoEventMonDataTriggerValue_Object = MibScalar
anueNtoEventMonDataTriggerValue = _AnueNtoEventMonDataTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 3),
    _AnueNtoEventMonDataTriggerValue_Type()
)
anueNtoEventMonDataTriggerValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataTriggerValue.setStatus("current")
_AnueNtoEventMonDataDirection_Type = AnueThresholdCrossing
_AnueNtoEventMonDataDirection_Object = MibScalar
anueNtoEventMonDataDirection = _AnueNtoEventMonDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 4),
    _AnueNtoEventMonDataDirection_Type()
)
anueNtoEventMonDataDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataDirection.setStatus("current")
_AnueNtoEventMonDataStatName_Type = DisplayString
_AnueNtoEventMonDataStatName_Object = MibScalar
anueNtoEventMonDataStatName = _AnueNtoEventMonDataStatName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 5),
    _AnueNtoEventMonDataStatName_Type()
)
anueNtoEventMonDataStatName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataStatName.setStatus("current")
_AnueNtoEventMonDataEntityName_Type = DisplayString
_AnueNtoEventMonDataEntityName_Object = MibScalar
anueNtoEventMonDataEntityName = _AnueNtoEventMonDataEntityName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 6),
    _AnueNtoEventMonDataEntityName_Type()
)
anueNtoEventMonDataEntityName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataEntityName.setStatus("current")
_AnueNtoEventMonDataNotSent_Type = Counter32
_AnueNtoEventMonDataNotSent_Object = MibScalar
anueNtoEventMonDataNotSent = _AnueNtoEventMonDataNotSent_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 7),
    _AnueNtoEventMonDataNotSent_Type()
)
anueNtoEventMonDataNotSent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataNotSent.setStatus("current")
_AnueNtoEventMonDataTriggerDescr_Type = DisplayString
_AnueNtoEventMonDataTriggerDescr_Object = MibScalar
anueNtoEventMonDataTriggerDescr = _AnueNtoEventMonDataTriggerDescr_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 8),
    _AnueNtoEventMonDataTriggerDescr_Type()
)
anueNtoEventMonDataTriggerDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataTriggerDescr.setStatus("current")
_AnueNtoEventMonDataThreshold_Type = CounterBasedGauge64
_AnueNtoEventMonDataThreshold_Object = MibScalar
anueNtoEventMonDataThreshold = _AnueNtoEventMonDataThreshold_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 11),
    _AnueNtoEventMonDataThreshold_Type()
)
anueNtoEventMonDataThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataThreshold.setStatus("current")
_AnueNtoEventMonDataInterval_Type = Integer32
_AnueNtoEventMonDataInterval_Object = MibScalar
anueNtoEventMonDataInterval = _AnueNtoEventMonDataInterval_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 12),
    _AnueNtoEventMonDataInterval_Type()
)
anueNtoEventMonDataInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataInterval.setStatus("current")
_AnueNtoEventMonDataWindowSize_Type = Integer32
_AnueNtoEventMonDataWindowSize_Object = MibScalar
anueNtoEventMonDataWindowSize = _AnueNtoEventMonDataWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 13),
    _AnueNtoEventMonDataWindowSize_Type()
)
anueNtoEventMonDataWindowSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataWindowSize.setStatus("current")
_AnueNtoEventMonDataWindowCount_Type = Integer32
_AnueNtoEventMonDataWindowCount_Object = MibScalar
anueNtoEventMonDataWindowCount = _AnueNtoEventMonDataWindowCount_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 1, 14),
    _AnueNtoEventMonDataWindowCount_Type()
)
anueNtoEventMonDataWindowCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueNtoEventMonDataWindowCount.setStatus("current")
_AnueNtoEventTestData_ObjectIdentity = ObjectIdentity
anueNtoEventTestData = _AnueNtoEventTestData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 2)
)
_AnueNtoEventTestTime_Type = DateAndTime
_AnueNtoEventTestTime_Object = MibScalar
anueNtoEventTestTime = _AnueNtoEventTestTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 2, 1),
    _AnueNtoEventTestTime_Type()
)
anueNtoEventTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueNtoEventTestTime.setStatus("current")
_AnueNtoEventTestMessage_Type = DisplayString
_AnueNtoEventTestMessage_Object = MibScalar
anueNtoEventTestMessage = _AnueNtoEventTestMessage_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 2, 2),
    _AnueNtoEventTestMessage_Type()
)
anueNtoEventTestMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueNtoEventTestMessage.setStatus("current")
_AnueMemberActionData_ObjectIdentity = ObjectIdentity
anueMemberActionData = _AnueMemberActionData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 3)
)
_AnueMemberActionDataMemberName_Type = DisplayString
_AnueMemberActionDataMemberName_Object = MibScalar
anueMemberActionDataMemberName = _AnueMemberActionDataMemberName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 3, 1),
    _AnueMemberActionDataMemberName_Type()
)
anueMemberActionDataMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueMemberActionDataMemberName.setStatus("current")
_AnueMemberActionDataType_Type = AnueNtoUnionMemberActionType
_AnueMemberActionDataType_Object = MibScalar
anueMemberActionDataType = _AnueMemberActionDataType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 5, 3, 2),
    _AnueMemberActionDataType_Type()
)
anueMemberActionDataType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    anueMemberActionDataType.setStatus("current")
_AnueNtoCapture_ObjectIdentity = ObjectIdentity
anueNtoCapture = _AnueNtoCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6)
)
_AnueNtoCaptureTable_Object = MibTable
anueNtoCaptureTable = _AnueNtoCaptureTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    anueNtoCaptureTable.setStatus("current")
_AnueNtoCaptureEntry_Object = MibTableRow
anueNtoCaptureEntry = _AnueNtoCaptureEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1)
)
anueNtoCaptureEntry.setIndexNames(
    (0, "ANUE-MIB", "anueCaptureNumber"),
)
if mibBuilder.loadTexts:
    anueNtoCaptureEntry.setStatus("current")


class _AnueCaptureNumber_Type(Integer32):
    """Custom type anueCaptureNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueCaptureNumber_Type.__name__ = "Integer32"
_AnueCaptureNumber_Object = MibTableColumn
anueCaptureNumber = _AnueCaptureNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 1),
    _AnueCaptureNumber_Type()
)
anueCaptureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureNumber.setStatus("current")
_AnueCaptureDefaultName_Type = DisplayString
_AnueCaptureDefaultName_Object = MibTableColumn
anueCaptureDefaultName = _AnueCaptureDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 2),
    _AnueCaptureDefaultName_Type()
)
anueCaptureDefaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureDefaultName.setStatus("current")
_AnueCaptureName_Type = DisplayString
_AnueCaptureName_Object = MibTableColumn
anueCaptureName = _AnueCaptureName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 3),
    _AnueCaptureName_Type()
)
anueCaptureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureName.setStatus("current")
_AnueCaptureDesc_Type = DisplayString
_AnueCaptureDesc_Object = MibTableColumn
anueCaptureDesc = _AnueCaptureDesc_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 4),
    _AnueCaptureDesc_Type()
)
anueCaptureDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureDesc.setStatus("current")


class _AnueCaptureStatus_Type(Integer32):
    """Custom type anueCaptureStatus based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("anueCaptureStatusIdleEmpty", 1),
          ("anueCaptureStatusStartedEmpty", 2),
          ("anueCaptureStatusStartedWithData", 3),
          ("anueCaptureStatusStartedTriggered", 4),
          ("anueCaptureStatusIdleWithData", 5),
          ("anueCaptureStatusUnassigned", 6),
          ("anueCaptureStatusPlaybackStopped", 7),
          ("anueCaptureStatusPlaybackStarted", 8),
          ("anueCaptureStatusOffline", 9),
          ("anueCaptureStatusError", 10))
    )


_AnueCaptureStatus_Type.__name__ = "Integer32"
_AnueCaptureStatus_Object = MibTableColumn
anueCaptureStatus = _AnueCaptureStatus_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 5),
    _AnueCaptureStatus_Type()
)
anueCaptureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureStatus.setStatus("current")
_AnueCaptureBufferSize_Type = Integer32
_AnueCaptureBufferSize_Object = MibTableColumn
anueCaptureBufferSize = _AnueCaptureBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 6),
    _AnueCaptureBufferSize_Type()
)
anueCaptureBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureBufferSize.setStatus("current")


class _AnueCaptureBufferType_Type(Integer32):
    """Custom type anueCaptureBufferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anueCaptureBufferTypeStopOnBufferFull", 1),
          ("anueCaptureBufferTypeCircular", 2))
    )


_AnueCaptureBufferType_Type.__name__ = "Integer32"
_AnueCaptureBufferType_Object = MibTableColumn
anueCaptureBufferType = _AnueCaptureBufferType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 7),
    _AnueCaptureBufferType_Type()
)
anueCaptureBufferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureBufferType.setStatus("current")


class _AnueCaptureTriggerMode_Type(Integer32):
    """Custom type anueCaptureTriggerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anueCaptureTriggerModeManual", 1),
          ("anueCaptureTrigerModeTriggered", 2))
    )


_AnueCaptureTriggerMode_Type.__name__ = "Integer32"
_AnueCaptureTriggerMode_Object = MibTableColumn
anueCaptureTriggerMode = _AnueCaptureTriggerMode_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 8),
    _AnueCaptureTriggerMode_Type()
)
anueCaptureTriggerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTriggerMode.setStatus("current")
_AnueCaptureTriggerPosition_Type = Integer32
_AnueCaptureTriggerPosition_Object = MibTableColumn
anueCaptureTriggerPosition = _AnueCaptureTriggerPosition_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 9),
    _AnueCaptureTriggerPosition_Type()
)
anueCaptureTriggerPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTriggerPosition.setStatus("current")
_AnueCaptureFillBufferToTrigger_Type = TruthValue
_AnueCaptureFillBufferToTrigger_Object = MibTableColumn
anueCaptureFillBufferToTrigger = _AnueCaptureFillBufferToTrigger_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 10),
    _AnueCaptureFillBufferToTrigger_Type()
)
anueCaptureFillBufferToTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureFillBufferToTrigger.setStatus("current")


class _AnueCaptureEnableTrailerStripping_Type(Integer32):
    """Custom type anueCaptureEnableTrailerStripping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anueCaptureEnableTrailerStrippingDisabled", 1),
          ("anueCaptureEnableTrailerStrippingPreserveAndTimeStamp", 2),
          ("anueCaptureEnableTrailerStrippingLocalTime", 3))
    )


_AnueCaptureEnableTrailerStripping_Type.__name__ = "Integer32"
_AnueCaptureEnableTrailerStripping_Object = MibTableColumn
anueCaptureEnableTrailerStripping = _AnueCaptureEnableTrailerStripping_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 11),
    _AnueCaptureEnableTrailerStripping_Type()
)
anueCaptureEnableTrailerStripping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureEnableTrailerStripping.setStatus("current")
_AnueCaptureTriggerCriteria_Type = DisplayString
_AnueCaptureTriggerCriteria_Object = MibTableColumn
anueCaptureTriggerCriteria = _AnueCaptureTriggerCriteria_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 12),
    _AnueCaptureTriggerCriteria_Type()
)
anueCaptureTriggerCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTriggerCriteria.setStatus("current")
_AnueCaptureConnection_Type = ObjectIdentifier
_AnueCaptureConnection_Object = MibTableColumn
anueCaptureConnection = _AnueCaptureConnection_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 1, 1, 13),
    _AnueCaptureConnection_Type()
)
anueCaptureConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureConnection.setStatus("current")
_AnueNtoCaptureStatsTable_Object = MibTable
anueNtoCaptureStatsTable = _AnueNtoCaptureStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    anueNtoCaptureStatsTable.setStatus("current")
_AnueNtoCaptureStatsEntry_Object = MibTableRow
anueNtoCaptureStatsEntry = _AnueNtoCaptureStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1)
)
anueNtoCaptureStatsEntry.setIndexNames(
    (0, "ANUE-MIB", "anueCaptureNumber"),
)
if mibBuilder.loadTexts:
    anueNtoCaptureStatsEntry.setStatus("current")
_AnueCaptureTransBytesTotal_Type = Counter64
_AnueCaptureTransBytesTotal_Object = MibTableColumn
anueCaptureTransBytesTotal = _AnueCaptureTransBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 1),
    _AnueCaptureTransBytesTotal_Type()
)
anueCaptureTransBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransBytesTotal.setStatus("current")
_AnueCaptureTransBytesCur_Type = Counter64
_AnueCaptureTransBytesCur_Object = MibTableColumn
anueCaptureTransBytesCur = _AnueCaptureTransBytesCur_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 2),
    _AnueCaptureTransBytesCur_Type()
)
anueCaptureTransBytesCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransBytesCur.setStatus("current")
_AnueCaptureTransBytesAvg_Type = Counter64
_AnueCaptureTransBytesAvg_Object = MibTableColumn
anueCaptureTransBytesAvg = _AnueCaptureTransBytesAvg_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 3),
    _AnueCaptureTransBytesAvg_Type()
)
anueCaptureTransBytesAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransBytesAvg.setStatus("current")
_AnueCaptureTransBytesPeak_Type = Counter64
_AnueCaptureTransBytesPeak_Object = MibTableColumn
anueCaptureTransBytesPeak = _AnueCaptureTransBytesPeak_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 4),
    _AnueCaptureTransBytesPeak_Type()
)
anueCaptureTransBytesPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransBytesPeak.setStatus("current")
_AnueCaptureTransBytesPeakTime_Type = DateAndTime
_AnueCaptureTransBytesPeakTime_Object = MibTableColumn
anueCaptureTransBytesPeakTime = _AnueCaptureTransBytesPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 5),
    _AnueCaptureTransBytesPeakTime_Type()
)
anueCaptureTransBytesPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransBytesPeakTime.setStatus("current")
_AnueCaptureTransBytesTimeSincePeak_Type = Counter64
_AnueCaptureTransBytesTimeSincePeak_Object = MibTableColumn
anueCaptureTransBytesTimeSincePeak = _AnueCaptureTransBytesTimeSincePeak_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 6),
    _AnueCaptureTransBytesTimeSincePeak_Type()
)
anueCaptureTransBytesTimeSincePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransBytesTimeSincePeak.setStatus("current")
_AnueCaptureTransPktsTotal_Type = Counter64
_AnueCaptureTransPktsTotal_Object = MibTableColumn
anueCaptureTransPktsTotal = _AnueCaptureTransPktsTotal_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 7),
    _AnueCaptureTransPktsTotal_Type()
)
anueCaptureTransPktsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransPktsTotal.setStatus("current")
_AnueCaptureTransPktsCur_Type = Counter64
_AnueCaptureTransPktsCur_Object = MibTableColumn
anueCaptureTransPktsCur = _AnueCaptureTransPktsCur_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 8),
    _AnueCaptureTransPktsCur_Type()
)
anueCaptureTransPktsCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransPktsCur.setStatus("current")
_AnueCaptureTransPktsAvg_Type = Counter64
_AnueCaptureTransPktsAvg_Object = MibTableColumn
anueCaptureTransPktsAvg = _AnueCaptureTransPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 9),
    _AnueCaptureTransPktsAvg_Type()
)
anueCaptureTransPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransPktsAvg.setStatus("current")
_AnueCaptureTransPktsPeak_Type = Counter64
_AnueCaptureTransPktsPeak_Object = MibTableColumn
anueCaptureTransPktsPeak = _AnueCaptureTransPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 10),
    _AnueCaptureTransPktsPeak_Type()
)
anueCaptureTransPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransPktsPeak.setStatus("current")
_AnueCaptureTransPktsPeakTime_Type = DateAndTime
_AnueCaptureTransPktsPeakTime_Object = MibTableColumn
anueCaptureTransPktsPeakTime = _AnueCaptureTransPktsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 11),
    _AnueCaptureTransPktsPeakTime_Type()
)
anueCaptureTransPktsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransPktsPeakTime.setStatus("current")
_AnueCaptureTransPktsTimeSincePeak_Type = Counter64
_AnueCaptureTransPktsTimeSincePeak_Object = MibTableColumn
anueCaptureTransPktsTimeSincePeak = _AnueCaptureTransPktsTimeSincePeak_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 12),
    _AnueCaptureTransPktsTimeSincePeak_Type()
)
anueCaptureTransPktsTimeSincePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTransPktsTimeSincePeak.setStatus("current")
_AnueCaptureDropPktsTotal_Type = Counter64
_AnueCaptureDropPktsTotal_Object = MibTableColumn
anueCaptureDropPktsTotal = _AnueCaptureDropPktsTotal_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 13),
    _AnueCaptureDropPktsTotal_Type()
)
anueCaptureDropPktsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureDropPktsTotal.setStatus("current")
_AnueCaptureDropPktsCur_Type = Counter64
_AnueCaptureDropPktsCur_Object = MibTableColumn
anueCaptureDropPktsCur = _AnueCaptureDropPktsCur_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 14),
    _AnueCaptureDropPktsCur_Type()
)
anueCaptureDropPktsCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureDropPktsCur.setStatus("current")
_AnueCaptureDropPktsAvg_Type = Counter64
_AnueCaptureDropPktsAvg_Object = MibTableColumn
anueCaptureDropPktsAvg = _AnueCaptureDropPktsAvg_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 15),
    _AnueCaptureDropPktsAvg_Type()
)
anueCaptureDropPktsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureDropPktsAvg.setStatus("current")
_AnueCaptureDropPktsPeak_Type = Counter64
_AnueCaptureDropPktsPeak_Object = MibTableColumn
anueCaptureDropPktsPeak = _AnueCaptureDropPktsPeak_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 16),
    _AnueCaptureDropPktsPeak_Type()
)
anueCaptureDropPktsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureDropPktsPeak.setStatus("current")
_AnueCaptureDropPktsPeakTime_Type = DateAndTime
_AnueCaptureDropPktsPeakTime_Object = MibTableColumn
anueCaptureDropPktsPeakTime = _AnueCaptureDropPktsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 17),
    _AnueCaptureDropPktsPeakTime_Type()
)
anueCaptureDropPktsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureDropPktsPeakTime.setStatus("current")
_AnueCaptureDropPktsTimeSincePeak_Type = Counter64
_AnueCaptureDropPktsTimeSincePeak_Object = MibTableColumn
anueCaptureDropPktsTimeSincePeak = _AnueCaptureDropPktsTimeSincePeak_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 18),
    _AnueCaptureDropPktsTimeSincePeak_Type()
)
anueCaptureDropPktsTimeSincePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureDropPktsTimeSincePeak.setStatus("current")
_AnueCaptureBufferUtilizationPerc_Type = Counter64
_AnueCaptureBufferUtilizationPerc_Object = MibTableColumn
anueCaptureBufferUtilizationPerc = _AnueCaptureBufferUtilizationPerc_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 19),
    _AnueCaptureBufferUtilizationPerc_Type()
)
anueCaptureBufferUtilizationPerc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureBufferUtilizationPerc.setStatus("current")
_AnueCaptureTimeSinceReset_Type = Counter64
_AnueCaptureTimeSinceReset_Object = MibTableColumn
anueCaptureTimeSinceReset = _AnueCaptureTimeSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 20),
    _AnueCaptureTimeSinceReset_Type()
)
anueCaptureTimeSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureTimeSinceReset.setStatus("current")
_AnueCaptureResetById_Type = DisplayString
_AnueCaptureResetById_Object = MibTableColumn
anueCaptureResetById = _AnueCaptureResetById_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 6, 2, 1, 21),
    _AnueCaptureResetById_Type()
)
anueCaptureResetById.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCaptureResetById.setStatus("current")
_AnueNtoResource_ObjectIdentity = ObjectIdentity
anueNtoResource = _AnueNtoResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 7)
)
_AnueNtoResourceTable_Object = MibTable
anueNtoResourceTable = _AnueNtoResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    anueNtoResourceTable.setStatus("current")
_AnueNtoResourceEntry_Object = MibTableRow
anueNtoResourceEntry = _AnueNtoResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 7, 1, 1)
)
anueNtoResourceEntry.setIndexNames(
    (0, "ANUE-MIB", "anueResourceFilterType"),
    (0, "ANUE-MIB", "anueResourceNumber"),
)
if mibBuilder.loadTexts:
    anueNtoResourceEntry.setStatus("current")
_AnueResourceFilterType_Type = AnueFilterTypeDT
_AnueResourceFilterType_Object = MibTableColumn
anueResourceFilterType = _AnueResourceFilterType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 7, 1, 1, 1),
    _AnueResourceFilterType_Type()
)
anueResourceFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueResourceFilterType.setStatus("current")


class _AnueResourceNumber_Type(Integer32):
    """Custom type anueResourceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueResourceNumber_Type.__name__ = "Integer32"
_AnueResourceNumber_Object = MibTableColumn
anueResourceNumber = _AnueResourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 7, 1, 1, 2),
    _AnueResourceNumber_Type()
)
anueResourceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueResourceNumber.setStatus("current")
_AnueResourceDefaultName_Type = DisplayString
_AnueResourceDefaultName_Object = MibTableColumn
anueResourceDefaultName = _AnueResourceDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 7, 1, 1, 3),
    _AnueResourceDefaultName_Type()
)
anueResourceDefaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueResourceDefaultName.setStatus("current")
_AnueResourceName_Type = DisplayString
_AnueResourceName_Object = MibTableColumn
anueResourceName = _AnueResourceName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 7, 1, 1, 4),
    _AnueResourceName_Type()
)
anueResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueResourceName.setStatus("current")
_AnueResourceDesc_Type = DisplayString
_AnueResourceDesc_Object = MibTableColumn
anueResourceDesc = _AnueResourceDesc_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 7, 1, 1, 5),
    _AnueResourceDesc_Type()
)
anueResourceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueResourceDesc.setStatus("current")


class _AnueResourceStatus_Type(Integer32):
    """Custom type anueResourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("anueResourceStatusInitializing", 1),
          ("anueResourceStatusUpgrading", 2),
          ("anueResourceStatusInitializationFailed", 3),
          ("anueResourceStatusNotPresent", 4),
          ("anueResourceStatusReady", 5),
          ("anueResourceStatusNotLicensed", 6))
    )


_AnueResourceStatus_Type.__name__ = "Integer32"
_AnueResourceStatus_Object = MibTableColumn
anueResourceStatus = _AnueResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 1, 7, 1, 1, 6),
    _AnueResourceStatus_Type()
)
anueResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueResourceStatus.setStatus("current")
_AnueGscObjects_ObjectIdentity = ObjectIdentity
anueGscObjects = _AnueGscObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2)
)
_AnueGscSystem_ObjectIdentity = ObjectIdentity
anueGscSystem = _AnueGscSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 1)
)
_AnueGscLastCriticalFailure_ObjectIdentity = ObjectIdentity
anueGscLastCriticalFailure = _AnueGscLastCriticalFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 1, 9)
)
_AnueCriticalFailureDateAndTime_Type = DateAndTime
_AnueCriticalFailureDateAndTime_Object = MibScalar
anueCriticalFailureDateAndTime = _AnueCriticalFailureDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 1, 9, 1),
    _AnueCriticalFailureDateAndTime_Type()
)
anueCriticalFailureDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCriticalFailureDateAndTime.setStatus("current")
_AnueCriticalFailureType_Type = DisplayString
_AnueCriticalFailureType_Object = MibScalar
anueCriticalFailureType = _AnueCriticalFailureType_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 1, 9, 2),
    _AnueCriticalFailureType_Type()
)
anueCriticalFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueCriticalFailureType.setStatus("current")
_AnueGscData_ObjectIdentity = ObjectIdentity
anueGscData = _AnueGscData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6)
)
_AnueGscPortProbeTable_Object = MibTable
anueGscPortProbeTable = _AnueGscPortProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    anueGscPortProbeTable.setStatus("current")
_AnueGscPortProbeEntry_Object = MibTableRow
anueGscPortProbeEntry = _AnueGscPortProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 1, 1)
)
anueGscPortProbeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    anueGscPortProbeEntry.setStatus("current")
_AnueGscPortIfIndex_Type = InterfaceIndex
_AnueGscPortIfIndex_Object = MibTableColumn
anueGscPortIfIndex = _AnueGscPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 1, 1, 2),
    _AnueGscPortIfIndex_Type()
)
anueGscPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscPortIfIndex.setStatus("current")


class _AnueGscPortProbeId_Type(Integer32):
    """Custom type anueGscPortProbeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueGscPortProbeId_Type.__name__ = "Integer32"
_AnueGscPortProbeId_Object = MibTableColumn
anueGscPortProbeId = _AnueGscPortProbeId_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 1, 1, 3),
    _AnueGscPortProbeId_Type()
)
anueGscPortProbeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscPortProbeId.setStatus("current")
_AnueGscProbeTable_Object = MibTable
anueGscProbeTable = _AnueGscProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    anueGscProbeTable.setStatus("current")
_AnueGscProbeEntry_Object = MibTableRow
anueGscProbeEntry = _AnueGscProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1)
)
anueGscProbeEntry.setIndexNames(
    (0, "ANUE-MIB", "anueGscProbeId"),
)
if mibBuilder.loadTexts:
    anueGscProbeEntry.setStatus("current")


class _AnueGscProbeId_Type(Integer32):
    """Custom type anueGscProbeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueGscProbeId_Type.__name__ = "Integer32"
_AnueGscProbeId_Object = MibTableColumn
anueGscProbeId = _AnueGscProbeId_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1, 1),
    _AnueGscProbeId_Type()
)
anueGscProbeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscProbeId.setStatus("current")
_AnueGscProbePgIfIndex_Type = InterfaceIndex
_AnueGscProbePgIfIndex_Object = MibTableColumn
anueGscProbePgIfIndex = _AnueGscProbePgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1, 2),
    _AnueGscProbePgIfIndex_Type()
)
anueGscProbePgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscProbePgIfIndex.setStatus("current")
_AnueGscProbeName_Type = DisplayString
_AnueGscProbeName_Object = MibTableColumn
anueGscProbeName = _AnueGscProbeName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1, 3),
    _AnueGscProbeName_Type()
)
anueGscProbeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscProbeName.setStatus("current")
_AnueGscProbeIp_Type = InetAddress
_AnueGscProbeIp_Object = MibTableColumn
anueGscProbeIp = _AnueGscProbeIp_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1, 4),
    _AnueGscProbeIp_Type()
)
anueGscProbeIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscProbeIp.setStatus("current")
_AnueGscProbeIsActive_Type = TruthValue
_AnueGscProbeIsActive_Object = MibTableColumn
anueGscProbeIsActive = _AnueGscProbeIsActive_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1, 5),
    _AnueGscProbeIsActive_Type()
)
anueGscProbeIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscProbeIsActive.setStatus("current")
_AnueGscProbeIsRedundant_Type = TruthValue
_AnueGscProbeIsRedundant_Object = MibTableColumn
anueGscProbeIsRedundant = _AnueGscProbeIsRedundant_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1, 6),
    _AnueGscProbeIsRedundant_Type()
)
anueGscProbeIsRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscProbeIsRedundant.setStatus("current")
_AnueGscProbeLastRxHeartbeatTime_Type = DateAndTime
_AnueGscProbeLastRxHeartbeatTime_Object = MibTableColumn
anueGscProbeLastRxHeartbeatTime = _AnueGscProbeLastRxHeartbeatTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1, 7),
    _AnueGscProbeLastRxHeartbeatTime_Type()
)
anueGscProbeLastRxHeartbeatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscProbeLastRxHeartbeatTime.setStatus("current")
_AnueGscProbeLastRxFailMsgTime_Type = DateAndTime
_AnueGscProbeLastRxFailMsgTime_Object = MibTableColumn
anueGscProbeLastRxFailMsgTime = _AnueGscProbeLastRxFailMsgTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1, 8),
    _AnueGscProbeLastRxFailMsgTime_Type()
)
anueGscProbeLastRxFailMsgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscProbeLastRxFailMsgTime.setStatus("current")


class _AnueGscProbeFailoverId_Type(Integer32):
    """Custom type anueGscProbeFailoverId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueGscProbeFailoverId_Type.__name__ = "Integer32"
_AnueGscProbeFailoverId_Object = MibTableColumn
anueGscProbeFailoverId = _AnueGscProbeFailoverId_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 6, 2, 1, 9),
    _AnueGscProbeFailoverId_Type()
)
anueGscProbeFailoverId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscProbeFailoverId.setStatus("current")
_AnueGscPayload_ObjectIdentity = ObjectIdentity
anueGscPayload = _AnueGscPayload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7)
)
_AnueGscEventFailedProbeData_ObjectIdentity = ObjectIdentity
anueGscEventFailedProbeData = _AnueGscEventFailedProbeData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1)
)
_AnueGscEvFailedPbDateAndTime_Type = DateAndTime
_AnueGscEvFailedPbDateAndTime_Object = MibScalar
anueGscEvFailedPbDateAndTime = _AnueGscEvFailedPbDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 1),
    _AnueGscEvFailedPbDateAndTime_Type()
)
anueGscEvFailedPbDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailedPbDateAndTime.setStatus("current")


class _AnueGscEvFailedPbId_Type(Integer32):
    """Custom type anueGscEvFailedPbId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueGscEvFailedPbId_Type.__name__ = "Integer32"
_AnueGscEvFailedPbId_Object = MibScalar
anueGscEvFailedPbId = _AnueGscEvFailedPbId_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 2),
    _AnueGscEvFailedPbId_Type()
)
anueGscEvFailedPbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailedPbId.setStatus("current")
_AnueGscEvFailedPbName_Type = DisplayString
_AnueGscEvFailedPbName_Object = MibScalar
anueGscEvFailedPbName = _AnueGscEvFailedPbName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 3),
    _AnueGscEvFailedPbName_Type()
)
anueGscEvFailedPbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailedPbName.setStatus("current")
_AnueGscEvFailedPbIP_Type = InetAddress
_AnueGscEvFailedPbIP_Object = MibScalar
anueGscEvFailedPbIP = _AnueGscEvFailedPbIP_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 4),
    _AnueGscEvFailedPbIP_Type()
)
anueGscEvFailedPbIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailedPbIP.setStatus("current")
_AnueGscEvFailedPbPortList_Type = DisplayString
_AnueGscEvFailedPbPortList_Object = MibScalar
anueGscEvFailedPbPortList = _AnueGscEvFailedPbPortList_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 5),
    _AnueGscEvFailedPbPortList_Type()
)
anueGscEvFailedPbPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailedPbPortList.setStatus("current")
_AnueGscEvFailedPbLastRxHeartbeat_Type = DateAndTime
_AnueGscEvFailedPbLastRxHeartbeat_Object = MibScalar
anueGscEvFailedPbLastRxHeartbeat = _AnueGscEvFailedPbLastRxHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 6),
    _AnueGscEvFailedPbLastRxHeartbeat_Type()
)
anueGscEvFailedPbLastRxHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailedPbLastRxHeartbeat.setStatus("current")
_AnueGscEvFailedPbLastRxFailMsg_Type = DateAndTime
_AnueGscEvFailedPbLastRxFailMsg_Object = MibScalar
anueGscEvFailedPbLastRxFailMsg = _AnueGscEvFailedPbLastRxFailMsg_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 7),
    _AnueGscEvFailedPbLastRxFailMsg_Type()
)
anueGscEvFailedPbLastRxFailMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailedPbLastRxFailMsg.setStatus("current")


class _AnueGscEvFailoverPbId_Type(Integer32):
    """Custom type anueGscEvFailoverPbId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AnueGscEvFailoverPbId_Type.__name__ = "Integer32"
_AnueGscEvFailoverPbId_Object = MibScalar
anueGscEvFailoverPbId = _AnueGscEvFailoverPbId_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 8),
    _AnueGscEvFailoverPbId_Type()
)
anueGscEvFailoverPbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailoverPbId.setStatus("current")
_AnueGscEvFailoverPbName_Type = DisplayString
_AnueGscEvFailoverPbName_Object = MibScalar
anueGscEvFailoverPbName = _AnueGscEvFailoverPbName_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 9),
    _AnueGscEvFailoverPbName_Type()
)
anueGscEvFailoverPbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailoverPbName.setStatus("current")
_AnueGscEvFailoverPbIP_Type = InetAddress
_AnueGscEvFailoverPbIP_Object = MibScalar
anueGscEvFailoverPbIP = _AnueGscEvFailoverPbIP_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 10),
    _AnueGscEvFailoverPbIP_Type()
)
anueGscEvFailoverPbIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailoverPbIP.setStatus("current")
_AnueGscEvFailoverPbPortList_Type = DisplayString
_AnueGscEvFailoverPbPortList_Object = MibScalar
anueGscEvFailoverPbPortList = _AnueGscEvFailoverPbPortList_Object(
    (1, 3, 6, 1, 4, 1, 32620, 1, 2, 7, 1, 11),
    _AnueGscEvFailoverPbPortList_Type()
)
anueGscEvFailoverPbPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anueGscEvFailoverPbPortList.setStatus("current")
_AnueEvents_ObjectIdentity = ObjectIdentity
anueEvents = _AnueEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 2)
)
_AnueNtoEvents_ObjectIdentity = ObjectIdentity
anueNtoEvents = _AnueNtoEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1)
)
_AnueGscEvents_ObjectIdentity = ObjectIdentity
anueGscEvents = _AnueGscEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2)
)
_AnueConformance_ObjectIdentity = ObjectIdentity
anueConformance = _AnueConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 3)
)
_AnueNtoConformance_ObjectIdentity = ObjectIdentity
anueNtoConformance = _AnueNtoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1)
)
_AnueGroups_ObjectIdentity = ObjectIdentity
anueGroups = _AnueGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1)
)
_AnueNtoGroups_ObjectIdentity = ObjectIdentity
anueNtoGroups = _AnueNtoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1)
)
_AnueGscGroups_ObjectIdentity = ObjectIdentity
anueGscGroups = _AnueGscGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 2)
)
_AnueCompliances_ObjectIdentity = ObjectIdentity
anueCompliances = _AnueCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 2)
)

# Managed Objects groups

anueNtoSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1, 1)
)
anueNtoSystemGroup.setObjects(
      *(("ANUE-MIB", "anueSnmpAuthnFailureTime"),
        ("ANUE-MIB", "anueSnmpAuthnFailureUsername"),
        ("ANUE-MIB", "anueSnmpAuthnFailureSrcIpType"),
        ("ANUE-MIB", "anueSnmpAuthnFailureSrcIp"),
        ("ANUE-MIB", "anueSnmpAuthnFailureSecModel"),
        ("ANUE-MIB", "anueClientLoginFailureId"),
        ("ANUE-MIB", "anueClientLoginFailureSrcIpType"),
        ("ANUE-MIB", "anueClientLoginFailureSrcIp"),
        ("ANUE-MIB", "anueClientLoginFailureReason"),
        ("ANUE-MIB", "anueClientLoginFailureTime"),
        ("ANUE-MIB", "anueSnmpAuthnFailureTrapEnable"),
        ("ANUE-MIB", "anueClientLoginFailureTrapEnable"),
        ("ANUE-MIB", "anueLoginBanner"),
        ("ANUE-MIB", "anueTimestampingTimeSource"),
        ("ANUE-MIB", "anueTimestampingStatus"),
        ("ANUE-MIB", "anueCustomFieldSetEnableState"),
        ("ANUE-MIB", "anueFieldSetId"),
        ("ANUE-MIB", "anueFieldSetAvailOuterHdrFlds"),
        ("ANUE-MIB", "anueFieldSetIsAdditOuterHdrs"),
        ("ANUE-MIB", "anueCustomFieldId"),
        ("ANUE-MIB", "anueCustomFieldName"),
        ("ANUE-MIB", "anueCustomFieldPktType"),
        ("ANUE-MIB", "anueCustomFieldSize"),
        ("ANUE-MIB", "anueCustomFieldSpecificAttrList"),
        ("ANUE-MIB", "anueCustomFieldConfirmFldsList"),
        ("ANUE-MIB", "anueCriticalFailureDateAndTime"),
        ("ANUE-MIB", "anueCriticalFailureType"))
)
if mibBuilder.loadTexts:
    anueNtoSystemGroup.setStatus("current")

anueNtoIfExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1, 2)
)
anueNtoIfExtGroup.setObjects(
      *(("ANUE-MIB", "anueIfIsLicensed"),
        ("ANUE-MIB", "anueIfLicensedMaxSpeed"),
        ("ANUE-MIB", "anueIfMode"),
        ("ANUE-MIB", "anueIfDesc"),
        ("ANUE-MIB", "anueIfOnAfm"),
        ("ANUE-MIB", "anueIfAdvCapabilities"))
)
if mibBuilder.loadTexts:
    anueNtoIfExtGroup.setStatus("current")

anueNtoFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1, 3)
)
anueNtoFilterGroup.setObjects(
      *(("ANUE-MIB", "anueFilterCollectionPeriod"),
        ("ANUE-MIB", "anueFilterType"),
        ("ANUE-MIB", "anueFilterNumber"),
        ("ANUE-MIB", "anueFilterDefaultName"),
        ("ANUE-MIB", "anueFilterName"),
        ("ANUE-MIB", "anueFilterDesc"),
        ("ANUE-MIB", "anueFilterIfIndex"),
        ("ANUE-MIB", "anueFilterIsTwoStage"),
        ("ANUE-MIB", "anueFilterMode"),
        ("ANUE-MIB", "anueFilterCriteria"),
        ("ANUE-MIB", "anueFilterTag"),
        ("ANUE-MIB", "anueFilterAfmEnabled"),
        ("ANUE-MIB", "anueFilterEnabledFeatures"),
        ("ANUE-MIB", "anueFilterCustomFieldSets"),
        ("ANUE-MIB", "anueFilterConnFromOid"),
        ("ANUE-MIB", "anueFilterConnToOid"),
        ("ANUE-MIB", "anueFilterCntModHCInOctets"),
        ("ANUE-MIB", "anueFilterCntModHCOutOctets"),
        ("ANUE-MIB", "anueFilterCntModHCInPkts"),
        ("ANUE-MIB", "anueFilterCntModHCOutPkts"),
        ("ANUE-MIB", "anueFilterCntModHCDropPkts"),
        ("ANUE-MIB", "anueFilterCntModHCDropTime"),
        ("ANUE-MIB", "anueFilterCntModInOctets"),
        ("ANUE-MIB", "anueFilterCntModOutOctets"),
        ("ANUE-MIB", "anueFilterCntModInPkts"),
        ("ANUE-MIB", "anueFilterCntModOutPkts"),
        ("ANUE-MIB", "anueFilterCntModDropPkts"),
        ("ANUE-MIB", "anueFilterCntModDropTime"),
        ("ANUE-MIB", "anueFilterCntRstHCInOctets"),
        ("ANUE-MIB", "anueFilterCntRstHCOutOctets"),
        ("ANUE-MIB", "anueFilterCntRstHCInPkts"),
        ("ANUE-MIB", "anueFilterCntRstHCOutPkts"),
        ("ANUE-MIB", "anueFilterCntRstHCDropPkts"),
        ("ANUE-MIB", "anueFilterCntRstHCDropTime"),
        ("ANUE-MIB", "anueFilterCntRstInOctets"),
        ("ANUE-MIB", "anueFilterCntRstOutOctets"),
        ("ANUE-MIB", "anueFilterCntRstInPkts"),
        ("ANUE-MIB", "anueFilterCntRstOutPkts"),
        ("ANUE-MIB", "anueFilterCntRstDropPkts"),
        ("ANUE-MIB", "anueFilterCntRstDropTime"),
        ("ANUE-MIB", "anueFilterCurHCInOctets"),
        ("ANUE-MIB", "anueFilterCurHCOutOctets"),
        ("ANUE-MIB", "anueFilterCurHCRateOctets"),
        ("ANUE-MIB", "anueFilterCurHCInPkts"),
        ("ANUE-MIB", "anueFilterCurHCOutPkts"),
        ("ANUE-MIB", "anueFilterCurHCRatePkts"),
        ("ANUE-MIB", "anueFilterCurHCDropPkts"),
        ("ANUE-MIB", "anueFilterCurHCUtil"),
        ("ANUE-MIB", "anueFilterAvgHCInOctets"),
        ("ANUE-MIB", "anueFilterAvgHCOutOctets"),
        ("ANUE-MIB", "anueFilterAvgHCRateOctets"),
        ("ANUE-MIB", "anueFilterAvgHCInPkts"),
        ("ANUE-MIB", "anueFilterAvgHCOutPkts"),
        ("ANUE-MIB", "anueFilterAvgHCRatePkts"),
        ("ANUE-MIB", "anueFilterAvgHCDropPkts"),
        ("ANUE-MIB", "anueFilterAvgHCUtil"),
        ("ANUE-MIB", "anueFilterPeakHCInOctets"),
        ("ANUE-MIB", "anueFilterPeakHCInOctetsTime"),
        ("ANUE-MIB", "anueFilterPeakHCOutOctets"),
        ("ANUE-MIB", "anueFilterPeakHCOutOctetsTime"),
        ("ANUE-MIB", "anueFilterPeakHCRateOctets"),
        ("ANUE-MIB", "anueFilterPeakHCRateOctetsTime"),
        ("ANUE-MIB", "anueFilterPeakHCInPkts"),
        ("ANUE-MIB", "anueFilterPeakHCInPktsTime"),
        ("ANUE-MIB", "anueFilterPeakHCOutPkts"),
        ("ANUE-MIB", "anueFilterPeakHCOutPktsTime"),
        ("ANUE-MIB", "anueFilterPeakHCRatePkts"),
        ("ANUE-MIB", "anueFilterPeakHCRatePktsTime"),
        ("ANUE-MIB", "anueFilterPeakHCDropPkts"),
        ("ANUE-MIB", "anueFilterPeakHCDropPktsTime"),
        ("ANUE-MIB", "anueFilterPeakHCUtil"),
        ("ANUE-MIB", "anueFilterPeakHCUtilTime"),
        ("ANUE-MIB", "anueFilterCurInOctets"),
        ("ANUE-MIB", "anueFilterCurOutOctets"),
        ("ANUE-MIB", "anueFilterCurRateOctets"),
        ("ANUE-MIB", "anueFilterCurInPkts"),
        ("ANUE-MIB", "anueFilterCurOutPkts"),
        ("ANUE-MIB", "anueFilterCurRatePkts"),
        ("ANUE-MIB", "anueFilterCurDropPkts"),
        ("ANUE-MIB", "anueFilterCurUtil"),
        ("ANUE-MIB", "anueFilterAvgInOctets"),
        ("ANUE-MIB", "anueFilterAvgOutOctets"),
        ("ANUE-MIB", "anueFilterAvgRateOctets"),
        ("ANUE-MIB", "anueFilterAvgInPkts"),
        ("ANUE-MIB", "anueFilterAvgOutPkts"),
        ("ANUE-MIB", "anueFilterAvgRatePkts"),
        ("ANUE-MIB", "anueFilterAvgDropPkts"),
        ("ANUE-MIB", "anueFilterAvgUtil"),
        ("ANUE-MIB", "anueFilterPeakInOctets"),
        ("ANUE-MIB", "anueFilterPeakInOctetsTime"),
        ("ANUE-MIB", "anueFilterPeakOutOctets"),
        ("ANUE-MIB", "anueFilterPeakOutOctetsTime"),
        ("ANUE-MIB", "anueFilterPeakRateOctets"),
        ("ANUE-MIB", "anueFilterPeakRateOctetsTime"),
        ("ANUE-MIB", "anueFilterPeakInPkts"),
        ("ANUE-MIB", "anueFilterPeakInPktsTime"),
        ("ANUE-MIB", "anueFilterPeakOutPkts"),
        ("ANUE-MIB", "anueFilterPeakOutPktsTime"),
        ("ANUE-MIB", "anueFilterPeakRatePkts"),
        ("ANUE-MIB", "anueFilterPeakRatePktsTime"),
        ("ANUE-MIB", "anueFilterPeakDropPkts"),
        ("ANUE-MIB", "anueFilterPeakDropPktsTime"),
        ("ANUE-MIB", "anueFilterPeakUtil"),
        ("ANUE-MIB", "anueFilterPeakUtilTime"),
        ("ANUE-MIB", "anueFilterCreatedTime"),
        ("ANUE-MIB", "anueFilterCreatedBy"),
        ("ANUE-MIB", "anueFilterCriteriaModTime"),
        ("ANUE-MIB", "anueFilterCriteriaModTimeStamp"),
        ("ANUE-MIB", "anueFilterCriteriaModBy"),
        ("ANUE-MIB", "anueFilterConfigModTime"),
        ("ANUE-MIB", "anueFilterConfigModBy"),
        ("ANUE-MIB", "anueFilterConfigModFields"),
        ("ANUE-MIB", "anueFilterStatsResetTime"),
        ("ANUE-MIB", "anueFilterStatsResetBy"),
        ("ANUE-MIB", "anueFilterDropResetTime"),
        ("ANUE-MIB", "anueFilterDropResetBy"),
        ("ANUE-MIB", "anueFilterDefLastChange"),
        ("ANUE-MIB", "anueFilterConnLastChange"),
        ("ANUE-MIB", "anueFilterCurGscPktsRate"),
        ("ANUE-MIB", "anueFilterAvgGscPktsRate"),
        ("ANUE-MIB", "anueFilterPeakGscPktsRate"),
        ("ANUE-MIB", "anueFilterPeakTimeGscPktsRate"),
        ("ANUE-MIB", "anueFilterGTPPktType"),
        ("ANUE-MIB", "anueFilterGscCurDenyGtpV0Sess"),
        ("ANUE-MIB", "anueFilterGscCurDenyGtpV1Sess"),
        ("ANUE-MIB", "anueFilterGscCurDenyGtpV2Sess"),
        ("ANUE-MIB", "anueFilterGscCurDenyGtpTotSess"),
        ("ANUE-MIB", "anueFilterGscAvgDenyGtpV0Sess"),
        ("ANUE-MIB", "anueFilterGscAvgDenyGtpV1Sess"),
        ("ANUE-MIB", "anueFilterGscAvgDenyGtpV2Sess"),
        ("ANUE-MIB", "anueFilterGscAvgDenyGtpTotSess"),
        ("ANUE-MIB", "anueFilterGscPkDenyGtpV0Sess"),
        ("ANUE-MIB", "anueFilterGscPkDenyGtpV1Sess"),
        ("ANUE-MIB", "anueFilterGscPkDenyGtpV2Sess"),
        ("ANUE-MIB", "anueFilterGscPkDenyGtpTotSess"),
        ("ANUE-MIB", "anueFilterGscPkDenyGtpV0SessT"),
        ("ANUE-MIB", "anueFilterGscPkDenyGtpV1SessT"),
        ("ANUE-MIB", "anueFilterGscPkDenyGtpV2SessT"),
        ("ANUE-MIB", "anueFilterGscPkDenyGtpTotSessT"),
        ("ANUE-MIB", "anueFilterGscTotOversizePktsTx"),
        ("ANUE-MIB", "anueFilterGscCurOversizePktsTx"),
        ("ANUE-MIB", "anueFilterGscAvgOversizePktsTx"),
        ("ANUE-MIB", "anueFilterGscPkOversizePktsTx"),
        ("ANUE-MIB", "anueFilterGscPkOversizePktsTxT"),
        ("ANUE-MIB", "anueFilterGscTotDroppedPkts"),
        ("ANUE-MIB", "anueFilterGscCurDroppedPkts"),
        ("ANUE-MIB", "anueFilterGscAvgDroppedPkts"),
        ("ANUE-MIB", "anueFilterGscPkDroppedPkts"),
        ("ANUE-MIB", "anueFilterGscPkDroppedPktsT"),
        ("ANUE-MIB", "anueFilterGscTotDroppedBytes"),
        ("ANUE-MIB", "anueFilterGscCurDroppedBytes"),
        ("ANUE-MIB", "anueFilterGscAvgDroppedBytes"),
        ("ANUE-MIB", "anueFilterGscPkDroppedBytes"),
        ("ANUE-MIB", "anueFilterGscPkDroppedBytesT"))
)
if mibBuilder.loadTexts:
    anueNtoFilterGroup.setStatus("current")

anueNtoPayloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1, 4)
)
anueNtoPayloadGroup.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerDescr"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"),
        ("ANUE-MIB", "anueNtoEventTestTime"),
        ("ANUE-MIB", "anueNtoEventTestMessage"),
        ("ANUE-MIB", "anueMemberActionDataMemberName"),
        ("ANUE-MIB", "anueMemberActionDataType"))
)
if mibBuilder.loadTexts:
    anueNtoPayloadGroup.setStatus("current")

anueNtoCaptureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1, 5)
)
anueNtoCaptureGroup.setObjects(
      *(("ANUE-MIB", "anueCaptureNumber"),
        ("ANUE-MIB", "anueCaptureDefaultName"),
        ("ANUE-MIB", "anueCaptureName"),
        ("ANUE-MIB", "anueCaptureDesc"),
        ("ANUE-MIB", "anueCaptureStatus"),
        ("ANUE-MIB", "anueCaptureBufferSize"),
        ("ANUE-MIB", "anueCaptureBufferType"),
        ("ANUE-MIB", "anueCaptureTriggerMode"),
        ("ANUE-MIB", "anueCaptureTriggerPosition"),
        ("ANUE-MIB", "anueCaptureFillBufferToTrigger"),
        ("ANUE-MIB", "anueCaptureEnableTrailerStripping"),
        ("ANUE-MIB", "anueCaptureTriggerCriteria"),
        ("ANUE-MIB", "anueCaptureConnection"))
)
if mibBuilder.loadTexts:
    anueNtoCaptureGroup.setStatus("current")

anueNtoCaptureStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1, 6)
)
anueNtoCaptureStatsGroup.setObjects(
      *(("ANUE-MIB", "anueCaptureTransBytesTotal"),
        ("ANUE-MIB", "anueCaptureTransBytesCur"),
        ("ANUE-MIB", "anueCaptureTransBytesAvg"),
        ("ANUE-MIB", "anueCaptureTransBytesPeak"),
        ("ANUE-MIB", "anueCaptureTransBytesPeakTime"),
        ("ANUE-MIB", "anueCaptureTransBytesTimeSincePeak"),
        ("ANUE-MIB", "anueCaptureTransPktsTotal"),
        ("ANUE-MIB", "anueCaptureTransPktsCur"),
        ("ANUE-MIB", "anueCaptureTransPktsAvg"),
        ("ANUE-MIB", "anueCaptureTransPktsPeak"),
        ("ANUE-MIB", "anueCaptureTransPktsPeakTime"),
        ("ANUE-MIB", "anueCaptureTransPktsTimeSincePeak"),
        ("ANUE-MIB", "anueCaptureDropPktsTotal"),
        ("ANUE-MIB", "anueCaptureDropPktsCur"),
        ("ANUE-MIB", "anueCaptureDropPktsAvg"),
        ("ANUE-MIB", "anueCaptureDropPktsPeak"),
        ("ANUE-MIB", "anueCaptureDropPktsPeakTime"),
        ("ANUE-MIB", "anueCaptureDropPktsTimeSincePeak"),
        ("ANUE-MIB", "anueCaptureBufferUtilizationPerc"),
        ("ANUE-MIB", "anueCaptureTimeSinceReset"),
        ("ANUE-MIB", "anueCaptureResetById"))
)
if mibBuilder.loadTexts:
    anueNtoCaptureStatsGroup.setStatus("current")

anueNtoStageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1, 8)
)
anueNtoStageGroup.setObjects(
      *(("ANUE-MIB", "anueStageStripFilterType"),
        ("ANUE-MIB", "anueStageStripFilterNumber"),
        ("ANUE-MIB", "anueStageStripFeature"),
        ("ANUE-MIB", "anueStageStripOrder"),
        ("ANUE-MIB", "anueStageStripType"),
        ("ANUE-MIB", "anueStageStripModPkts"),
        ("ANUE-MIB", "anueStageStripModPktPct"),
        ("ANUE-MIB", "anueStageStripErrorPkts"),
        ("ANUE-MIB", "anueStageStripRstModPkts"),
        ("ANUE-MIB", "anueStageStripRstModPktPct"),
        ("ANUE-MIB", "anueStageStripRstErrorPkts"),
        ("ANUE-MIB", "anueStageStripAttributes"),
        ("ANUE-MIB", "anueStageDedupFilterType"),
        ("ANUE-MIB", "anueStageDedupFilterNumber"),
        ("ANUE-MIB", "anueStageDedupFeature"),
        ("ANUE-MIB", "anueStageDedupOrder"),
        ("ANUE-MIB", "anueStageDedupType"),
        ("ANUE-MIB", "anueStageDedupTimeWindows"),
        ("ANUE-MIB", "anueStageDedupRmvPkts"),
        ("ANUE-MIB", "anueStageDedupRmvPktPct"),
        ("ANUE-MIB", "anueStageDedupRstRmvPkts"),
        ("ANUE-MIB", "anueStageDedupRstRmvPktPct"),
        ("ANUE-MIB", "anueStageTrimFilterType"),
        ("ANUE-MIB", "anueStageTrimFilterNumber"),
        ("ANUE-MIB", "anueStageTrimFeature"),
        ("ANUE-MIB", "anueStageTrimOrder"),
        ("ANUE-MIB", "anueStageTrimType"),
        ("ANUE-MIB", "anueStageTrimRetainOctets"),
        ("ANUE-MIB", "anueStageTrimModPkts"),
        ("ANUE-MIB", "anueStageTrimModPktPct"),
        ("ANUE-MIB", "anueStageTrimRmvOctets"),
        ("ANUE-MIB", "anueStageTrimRmvOctetPct"),
        ("ANUE-MIB", "anueStageTrimRstModPkts"),
        ("ANUE-MIB", "anueStageTrimRstModPktPct"),
        ("ANUE-MIB", "anueStageTrimRstRmvOctets"),
        ("ANUE-MIB", "anueStageTrimRstRmvOctetPct"),
        ("ANUE-MIB", "anueStageBufferFilterType"),
        ("ANUE-MIB", "anueStageBufferFilterNumber"),
        ("ANUE-MIB", "anueStageBufferFeature"),
        ("ANUE-MIB", "anueStageBufferOrder"),
        ("ANUE-MIB", "anueStageBufferSize"),
        ("ANUE-MIB", "anueStageBufferCurBufferLevel"),
        ("ANUE-MIB", "anueStageBufferPeakBufferLevel"),
        ("ANUE-MIB", "anueStageBufferPeakBufferTime"),
        ("ANUE-MIB", "anueStageBufferDropPkts"),
        ("ANUE-MIB", "anueStageBufferDropTime"),
        ("ANUE-MIB", "anueStageBufferRstDropPkts"),
        ("ANUE-MIB", "anueStageBufferRstDropTime"),
        ("ANUE-MIB", "anueStageNPFilterFilterType"),
        ("ANUE-MIB", "anueStageNPFilterFilterNumber"),
        ("ANUE-MIB", "anueStageNPFilterFeature"),
        ("ANUE-MIB", "anueStageNPFilterOrder"),
        ("ANUE-MIB", "anueStageNPFilterDenyPkts"),
        ("ANUE-MIB", "anueStageNPFilterDenyPktPct"),
        ("ANUE-MIB", "anueStageNPFilterDenyOctets"),
        ("ANUE-MIB", "anueStageNPFilterDenyOctetPct"),
        ("ANUE-MIB", "anueStageNPFilterRstDenyPkts"),
        ("ANUE-MIB", "anueStageNPFilterRstDenyPktPct"),
        ("ANUE-MIB", "anueStageNPFilterRstDenyOctets"),
        ("ANUE-MIB", "anueStageNPFilterRstDenyOctetPct"),
        ("ANUE-MIB", "anueStageTPFilterFilterType"),
        ("ANUE-MIB", "anueStageTPFilterFilterNumber"),
        ("ANUE-MIB", "anueStageTPFilterFeature"),
        ("ANUE-MIB", "anueStageTPFilterOrder"),
        ("ANUE-MIB", "anueStageTPFilterDenyPkts"),
        ("ANUE-MIB", "anueStageTPFilterDenyPktPct"),
        ("ANUE-MIB", "anueStageTPFilterDropPkts"),
        ("ANUE-MIB", "anueStageTPFilterDropTime"),
        ("ANUE-MIB", "anueStageTPFilterRstDenyPkts"),
        ("ANUE-MIB", "anueStageTPFilterRstDenyPktPct"),
        ("ANUE-MIB", "anueStageTPFilterRstDropPkts"),
        ("ANUE-MIB", "anueStageTPFilterRstDropTime"),
        ("ANUE-MIB", "anueStageAfmDropFilterType"),
        ("ANUE-MIB", "anueStageAfmDropFilterNumber"),
        ("ANUE-MIB", "anueStageAfmDropFeature"),
        ("ANUE-MIB", "anueStageAfmDropOrder"),
        ("ANUE-MIB", "anueStageAfmDropDropPkts"),
        ("ANUE-MIB", "anueStageAfmDropDropTime"),
        ("ANUE-MIB", "anueStageAfmDropRstDropPkts"),
        ("ANUE-MIB", "anueStageAfmDropRstDropTime"),
        ("ANUE-MIB", "anueStageTagFilterType"),
        ("ANUE-MIB", "anueStageTagFilterNumber"),
        ("ANUE-MIB", "anueStageTagFeature"),
        ("ANUE-MIB", "anueStageTagOrder"),
        ("ANUE-MIB", "anueStageTagModPkts"),
        ("ANUE-MIB", "anueStageTagModPktPct"),
        ("ANUE-MIB", "anueStageTagRstModPkts"),
        ("ANUE-MIB", "anueStageTagRstModPktPct"),
        ("ANUE-MIB", "anueStageTagAttributes"),
        ("ANUE-MIB", "anueStageNPErrorFilterType"),
        ("ANUE-MIB", "anueStageNPErrorFilterNumber"),
        ("ANUE-MIB", "anueStageNPErrorFeature"),
        ("ANUE-MIB", "anueStageNPErrorOrder"),
        ("ANUE-MIB", "anueStageNPErrorPkts"),
        ("ANUE-MIB", "anueStageNPErrorRstPkts"),
        ("ANUE-MIB", "anueStageDropFilterType"),
        ("ANUE-MIB", "anueStageDropFilterNumber"),
        ("ANUE-MIB", "anueStageDropFeature"),
        ("ANUE-MIB", "anueStageCntDropPkts"),
        ("ANUE-MIB", "anueStageCntDropTime"),
        ("ANUE-MIB", "anueStageCurDropPkts"),
        ("ANUE-MIB", "anueStageAvgDropPkts"),
        ("ANUE-MIB", "anueStagePeakDropPkts"),
        ("ANUE-MIB", "anueStagePeakDropTime"),
        ("ANUE-MIB", "anueNtoStageGscNetworkFilterType"),
        ("ANUE-MIB", "anueNtoStageGscNetworkFilterNumber"),
        ("ANUE-MIB", "anueGscNWFltrExcSess"),
        ("ANUE-MIB", "anueNtoStageGscNetworkFilterFeature"),
        ("ANUE-MIB", "anueGscNWFltrAvgGscPktFrag"),
        ("ANUE-MIB", "anueGscNWFltrAvgTdoutFrag"),
        ("ANUE-MIB", "anueGscNWFltrCurPacketFrag"),
        ("ANUE-MIB", "anueGscNWFltrCurTdoutFrag"),
        ("ANUE-MIB", "anueGscNWFltrPkPacketFrag"),
        ("ANUE-MIB", "anueGscNWFltrPkPacketFragT"),
        ("ANUE-MIB", "anueGscNWFltrPkTdOutFrag"),
        ("ANUE-MIB", "anueGscNWFltrPkTdOutFragT"),
        ("ANUE-MIB", "anueGscNWFltrTotFrag"),
        ("ANUE-MIB", "anueGscNWFltrTotRxCountFrag"),
        ("ANUE-MIB", "anueGscNWFltrTotTdOutFrag"),
        ("ANUE-MIB", "anueGscNWFltrAvgCompFragPkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgCompFragPktsPerc"),
        ("ANUE-MIB", "anueGscNWFltrAvgIncomFragPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurCompFragPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurCompFragPktsPerc"),
        ("ANUE-MIB", "anueGscNWFltrCurIncomFragPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkCompFragPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkCompFragPktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkCompFragPktsPerc"),
        ("ANUE-MIB", "anueGscNWFltrPkCompFragPktsPercT"),
        ("ANUE-MIB", "anueGscNWFltrPkIncomFragPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkIncomFragPktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkTotCompFragPkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgActiveUsers"),
        ("ANUE-MIB", "anueGscNWFltrCurActiveUsers"),
        ("ANUE-MIB", "anueGscNWFltrPkActiveUsers"),
        ("ANUE-MIB", "anueGscNWFltrPkActiveUsersT"),
        ("ANUE-MIB", "anueGscNWFltrAvgExcSess"),
        ("ANUE-MIB", "anueGscNWFltrCurExcSess"),
        ("ANUE-MIB", "anueGscNWFltrPkExcSess"),
        ("ANUE-MIB", "anueGscNWFltrPkExcSessT"),
        ("ANUE-MIB", "anueGscNWFltrTotExcSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV0CrSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV1CrSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV2CrSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpTotCrSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV0CrSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV1CrSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV2CrSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpTotCrSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV0CrSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV1CrSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV2CrSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpTotCrSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0CrSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1CrSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2CrSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotCrSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0CrSessT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1CrSessT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2CrSessT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotCrSessT"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV0DelSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV1DelSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV2DelSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpTotDelSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV0DelSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV1DelSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV2DelSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpTotDelSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV0DelSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV1DelSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV2DelSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpTotDelSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0DelSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1DelSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2DelSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotDelSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0DelSessT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1DelSessT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2DelSessT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotDelSessT"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV0Bearers"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV1Bearers"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV2Bearers"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpTotBearers"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV0Bearers"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV1Bearers"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV2Bearers"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpTotBearers"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0Bearers"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1Bearers"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2Bearers"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotBearers"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0BearersT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1BearersT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2BearersT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotBearersT"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV0Pkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV1Pkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV2Pkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpTotPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV0Pkts"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV1Pkts"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV2Pkts"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpTotPkts"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV1Pkts"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV0Pkts"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV2Pkts"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpTotPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0Pkts"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1Pkts"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2Pkts"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0PktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1PktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2PktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotPktsT"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV0ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV1ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpV2ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpTotToutSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV0ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV1ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpV2ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpTotToutSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV0ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV1ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpV2ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpTotToutSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2ToutSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotToutSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV0ToutSessT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV1ToutSessT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpV2ToutSessT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpTotToutSessT"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpCPkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgGtpUPkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgDiameterPkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgDnsPkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgRadiusPkts"),
        ("ANUE-MIB", "anueGscNWFltrAvgNonGtpPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpCPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurGtpUPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurDiameterPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurDnsPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurRadiusPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurNonGtpPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpCPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpUPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkDiameterPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkDnsPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkRadiusPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkNonGtpPkts"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpCPktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkGtpUPktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkDiameterPktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkDnsPktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkRadiusPktsT"),
        ("ANUE-MIB", "anueGscNWFltrPkNonGtpPktsT"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpCPkts"),
        ("ANUE-MIB", "anueGscNWFltrTotGtpUPkts"),
        ("ANUE-MIB", "anueGscNWFltrTotDiameterPkts"),
        ("ANUE-MIB", "anueGscNWFltrTotDnsPkts"),
        ("ANUE-MIB", "anueGscNWFltrTotRadiusPkts"),
        ("ANUE-MIB", "anueGscNWFltrTotNonGtpPkts"),
        ("ANUE-MIB", "anueGscNWFltrTotGscDropPkts"),
        ("ANUE-MIB", "anueGscNWFltrCurGscSessLoad"),
        ("ANUE-MIB", "anueGscNWFltrAvgGscSessLoad"),
        ("ANUE-MIB", "anueGscNWFltrPeakGscSessLoad"),
        ("ANUE-MIB", "anueGscNWFltrPeakGscSessLoadT"),
        ("ANUE-MIB", "anueGscNWFltrCurNetwElemLoad"),
        ("ANUE-MIB", "anueGscNWFltrPeakNetwElemLoad"),
        ("ANUE-MIB", "anueGscNWFltrPeakNetwElemLoadT"),
        ("ANUE-MIB", "anueGscNWFltrCurReqRespLoad"),
        ("ANUE-MIB", "anueGscNWFltrPeakReqRespLoad"),
        ("ANUE-MIB", "anueGscNWFltrPeakReqRespLoadT"),
        ("ANUE-MIB", "anueGscNWFltrCurFragLoad"),
        ("ANUE-MIB", "anueGscNWFltrPeakFragLoad"),
        ("ANUE-MIB", "anueGscNWFltrPeakFragLoadT"),
        ("ANUE-MIB", "anueGscNWFltrAvgGscUnassignedSess"),
        ("ANUE-MIB", "anueGscNWFltrCurGscUnassignedSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGscUnassignedSess"),
        ("ANUE-MIB", "anueGscNWFltrPkGscUnassignedSessT"),
        ("ANUE-MIB", "anueGscNWFltrTotGscUnassignedSess"),
        ("ANUE-MIB", "anueGscNWFltrAvgUnprocReq"),
        ("ANUE-MIB", "anueGscNWFltrCurUnprocReq"),
        ("ANUE-MIB", "anueGscNWFltrPkUnprocReq"),
        ("ANUE-MIB", "anueGscNWFltrPkUnprocReqT"),
        ("ANUE-MIB", "anueGscNWFltrTotUnprocReq"),
        ("ANUE-MIB", "anueGscNWFltrAvgTdOutReq"),
        ("ANUE-MIB", "anueGscNWFltrCurTdOutReq"),
        ("ANUE-MIB", "anueGscNWFltrPkTdOutReq"),
        ("ANUE-MIB", "anueGscNWFltrPkTdOutReqT"),
        ("ANUE-MIB", "anueGscNWFltrTotTdOutReq"),
        ("ANUE-MIB", "anueGscNWFltrAvgUnmatchedResp"),
        ("ANUE-MIB", "anueGscNWFltrCurUnmatchedResp"),
        ("ANUE-MIB", "anueGscNWFltrPkUnmatchedResp"),
        ("ANUE-MIB", "anueGscNWFltrPkUnmatchedRespT"),
        ("ANUE-MIB", "anueGscNWFltrTotUnmatchedResp"),
        ("ANUE-MIB", "anueGscNWFltrOverloadErrCode"),
        ("ANUE-MIB", "anueGscNWFltrOverloadT"),
        ("ANUE-MIB", "anueNtoStageGscToolFilterType"),
        ("ANUE-MIB", "anueNtoStageGscToolFilterNumber"),
        ("ANUE-MIB", "anueNtoStageGscToolFilterFeature"),
        ("ANUE-MIB", "anueGscTFltrCurGtpV0ActSess"),
        ("ANUE-MIB", "anueGscTFltrCurGtpV1ActSess"),
        ("ANUE-MIB", "anueGscTFltrCurGtpV2ActSess"),
        ("ANUE-MIB", "anueGscTFltrCurGtpTotActSess"),
        ("ANUE-MIB", "anueGscTFltrAvgGtpV0ActSess"),
        ("ANUE-MIB", "anueGscTFltrAvgGtpV1ActSess"),
        ("ANUE-MIB", "anueGscTFltrAvgGtpV2ActSess"),
        ("ANUE-MIB", "anueGscTFltrAvgGtpTotActSess"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpV0ActSess"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpV1ActSess"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpV2ActSess"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpTotActSess"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpV0ActSessT"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpV1ActSessT"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpV2ActSessT"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpTotActSessT"),
        ("ANUE-MIB", "anueGscTFltrAvgGtpCPkts"),
        ("ANUE-MIB", "anueGscTFltrAvgGtpUPkts"),
        ("ANUE-MIB", "anueGscTFltrAvgDiameterPkts"),
        ("ANUE-MIB", "anueGscTFltrAvgDnsPkts"),
        ("ANUE-MIB", "anueGscTFltrAvgRadiusPkts"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpCPkts"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpUPkts"),
        ("ANUE-MIB", "anueGscTFltrPeakDiameterPkts"),
        ("ANUE-MIB", "anueGscTFltrPeakDnsPkts"),
        ("ANUE-MIB", "anueGscTFltrPeakRadiusPkts"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpCPktsT"),
        ("ANUE-MIB", "anueGscTFltrPeakGtpUPktsT"),
        ("ANUE-MIB", "anueGscTFltrPeakDiameterPktsT"),
        ("ANUE-MIB", "anueGscTFltrPeakDnsPktsT"),
        ("ANUE-MIB", "anueGscTFltrPeakRadiusPktsT"),
        ("ANUE-MIB", "anueGscTFltrTotGtpCPkts"),
        ("ANUE-MIB", "anueGscTFltrTotGtpUPkts"),
        ("ANUE-MIB", "anueGscTFltrTotDiameterPkts"),
        ("ANUE-MIB", "anueGscTFltrTotDnsPkts"),
        ("ANUE-MIB", "anueGscTFltrTotRadiusPkts"),
        ("ANUE-MIB", "anueGscTFltrCurGtpCPkts"),
        ("ANUE-MIB", "anueGscTFltrCurGtpUPkts"),
        ("ANUE-MIB", "anueGscTFltrCurDiameterPkts"),
        ("ANUE-MIB", "anueGscTFltrCurDnsPkts"),
        ("ANUE-MIB", "anueGscTFltrCurRadiusPkts"),
        ("ANUE-MIB", "anueStageGtpFdFilterType"),
        ("ANUE-MIB", "anueStageGtpFdFilterNumber"),
        ("ANUE-MIB", "anueStageGtpFdFeature"),
        ("ANUE-MIB", "anueStageRateGtpCPps"),
        ("ANUE-MIB", "anueStageRateGtpUPps"),
        ("ANUE-MIB", "anueStageRateGtpCBps"),
        ("ANUE-MIB", "anueStageRateGtpUBps"),
        ("ANUE-MIB", "anueStageDataMaskingFilterType"),
        ("ANUE-MIB", "anueStageDataMaskingFilterNumber"),
        ("ANUE-MIB", "anueStageDataMaskingFeature"),
        ("ANUE-MIB", "anueStageDataMaskingOrder"),
        ("ANUE-MIB", "anueStageDataMaskingOffsetLayer"),
        ("ANUE-MIB", "anueStageDataMaskingOffset"),
        ("ANUE-MIB", "anueStageDataMaskingLength"),
        ("ANUE-MIB", "anueStageDataMaskingFillValue"),
        ("ANUE-MIB", "anueStageDataMaskingModPkts"),
        ("ANUE-MIB", "anueStageDataMaskingModPktPct"),
        ("ANUE-MIB", "anueStageDataMaskingRstModPkts"),
        ("ANUE-MIB", "anueStageDataMaskingRstModPktPct"))
)
if mibBuilder.loadTexts:
    anueNtoStageGroup.setStatus("current")

anueNtoResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1, 9)
)
anueNtoResourceGroup.setObjects(
      *(("ANUE-MIB", "anueResourceFilterType"),
        ("ANUE-MIB", "anueResourceNumber"),
        ("ANUE-MIB", "anueResourceDefaultName"),
        ("ANUE-MIB", "anueResourceName"),
        ("ANUE-MIB", "anueResourceDesc"),
        ("ANUE-MIB", "anueResourceStatus"))
)
if mibBuilder.loadTexts:
    anueNtoResourceGroup.setStatus("current")

anueGscDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 2, 2)
)
anueGscDataGroup.setObjects(
      *(("ANUE-MIB", "anueGscProbeId"),
        ("ANUE-MIB", "anueGscProbePgIfIndex"),
        ("ANUE-MIB", "anueGscProbeName"),
        ("ANUE-MIB", "anueGscProbeIp"),
        ("ANUE-MIB", "anueGscProbeIsActive"),
        ("ANUE-MIB", "anueGscProbeIsRedundant"),
        ("ANUE-MIB", "anueGscProbeLastRxHeartbeatTime"),
        ("ANUE-MIB", "anueGscProbeLastRxFailMsgTime"),
        ("ANUE-MIB", "anueGscProbeFailoverId"),
        ("ANUE-MIB", "anueGscPortIfIndex"),
        ("ANUE-MIB", "anueGscPortProbeId"))
)
if mibBuilder.loadTexts:
    anueGscDataGroup.setStatus("current")

anueGscPayloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 2, 3)
)
anueGscPayloadGroup.setObjects(
      *(("ANUE-MIB", "anueGscEvFailedPbDateAndTime"),
        ("ANUE-MIB", "anueGscEvFailedPbId"),
        ("ANUE-MIB", "anueGscEvFailedPbName"),
        ("ANUE-MIB", "anueGscEvFailedPbIP"),
        ("ANUE-MIB", "anueGscEvFailedPbPortList"),
        ("ANUE-MIB", "anueGscEvFailedPbLastRxHeartbeat"),
        ("ANUE-MIB", "anueGscEvFailedPbLastRxFailMsg"),
        ("ANUE-MIB", "anueGscEvFailoverPbId"),
        ("ANUE-MIB", "anueGscEvFailoverPbName"),
        ("ANUE-MIB", "anueGscEvFailoverPbIP"),
        ("ANUE-MIB", "anueGscEvFailoverPbPortList"))
)
if mibBuilder.loadTexts:
    anueGscPayloadGroup.setStatus("current")


# Notification objects

anueSnmpAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1, 1)
)
anueSnmpAuthenticationFailure.setObjects(
      *(("ANUE-MIB", "anueSnmpAuthnFailureTime"),
        ("ANUE-MIB", "anueSnmpAuthnFailureUsername"),
        ("ANUE-MIB", "anueSnmpAuthnFailureSrcIp"),
        ("ANUE-MIB", "anueSnmpAuthnFailureSrcIpType"),
        ("ANUE-MIB", "anueSnmpAuthnFailureSecModel"))
)
if mibBuilder.loadTexts:
    anueSnmpAuthenticationFailure.setStatus(
        "current"
    )

anueClientLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1, 2)
)
anueClientLoginFailure.setObjects(
      *(("ANUE-MIB", "anueClientLoginFailureTime"),
        ("ANUE-MIB", "anueClientLoginFailureId"),
        ("ANUE-MIB", "anueClientLoginFailureSrcIpType"),
        ("ANUE-MIB", "anueClientLoginFailureSrcIp"),
        ("ANUE-MIB", "anueClientLoginFailureReason"))
)
if mibBuilder.loadTexts:
    anueClientLoginFailure.setStatus(
        "current"
    )

anueNtoEventMonStatInvalidCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1, 3)
)
anueNtoEventMonStatInvalidCount.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueNtoEventMonStatInvalidCount.setStatus(
        "current"
    )

anueNtoEventMonStatDropCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1, 4)
)
anueNtoEventMonStatDropCount.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueNtoEventMonStatDropCount.setStatus(
        "current"
    )

anueNtoEventMonStatRxUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1, 5)
)
anueNtoEventMonStatRxUtilization.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueNtoEventMonStatRxUtilization.setStatus(
        "current"
    )

anueNtoEventMonStatTxUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1, 6)
)
anueNtoEventMonStatTxUtilization.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueNtoEventMonStatTxUtilization.setStatus(
        "current"
    )

anueNtoEventTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1, 7)
)
anueNtoEventTest.setObjects(
      *(("ANUE-MIB", "anueNtoEventTestTime"),
        ("ANUE-MIB", "anueNtoEventTestMessage"))
)
if mibBuilder.loadTexts:
    anueNtoEventTest.setStatus(
        "current"
    )

anueNtoEventUnionMemberAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1, 8)
)
anueNtoEventUnionMemberAction.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueMemberActionDataType"),
        ("ANUE-MIB", "anueMemberActionDataMemberName"))
)
if mibBuilder.loadTexts:
    anueNtoEventUnionMemberAction.setStatus(
        "current"
    )

anueNtoEventMonStatLoadDistribution = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 1, 9)
)
anueNtoEventMonStatLoadDistribution.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueNtoEventMonStatLoadDistribution.setStatus(
        "current"
    )

anueGscEventMonStatOverflowPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 1)
)
anueGscEventMonStatOverflowPkts.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueGscEventMonStatOverflowPkts.setStatus(
        "current"
    )

anueGscEventMonStatControlPlanePktRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 2)
)
anueGscEventMonStatControlPlanePktRate.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueGscEventMonStatControlPlanePktRate.setStatus(
        "current"
    )

anueGscEventMonStatExcessSessions = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 3)
)
anueGscEventMonStatExcessSessions.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueGscEventMonStatExcessSessions.setStatus(
        "current"
    )

anueGscEventMonStatIngressPktDrops = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 4)
)
anueGscEventMonStatIngressPktDrops.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueGscEventMonStatIngressPktDrops.setStatus(
        "current"
    )

anueGscEventMonStatSessionsTableLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 5)
)
anueGscEventMonStatSessionsTableLoad.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueGscEventMonStatSessionsTableLoad.setStatus(
        "current"
    )

anueGscEventMonStatNetworkElemLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 6)
)
anueGscEventMonStatNetworkElemLoad.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueGscEventMonStatNetworkElemLoad.setStatus(
        "current"
    )

anueGscEventMonStatReqRespLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 7)
)
anueGscEventMonStatReqRespLoad.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueGscEventMonStatReqRespLoad.setStatus(
        "current"
    )

anueGscEventMonStatFragmentationLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 8)
)
anueGscEventMonStatFragmentationLoad.setObjects(
      *(("ANUE-MIB", "anueNtoEventMonDataDateAndTime"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerCause"),
        ("ANUE-MIB", "anueNtoEventMonDataTriggerValue"),
        ("ANUE-MIB", "anueNtoEventMonDataDirection"),
        ("ANUE-MIB", "anueNtoEventMonDataStatName"),
        ("ANUE-MIB", "anueNtoEventMonDataEntityName"),
        ("ANUE-MIB", "anueNtoEventMonDataNotSent"),
        ("ANUE-MIB", "anueNtoEventMonDataThreshold"),
        ("ANUE-MIB", "anueNtoEventMonDataInterval"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowSize"),
        ("ANUE-MIB", "anueNtoEventMonDataWindowCount"))
)
if mibBuilder.loadTexts:
    anueGscEventMonStatFragmentationLoad.setStatus(
        "current"
    )

anueGscCriticalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 9)
)
anueGscCriticalFailure.setObjects(
      *(("ANUE-MIB", "anueCriticalFailureDateAndTime"),
        ("ANUE-MIB", "anueCriticalFailureType"))
)
if mibBuilder.loadTexts:
    anueGscCriticalFailure.setStatus(
        "current"
    )

anueGscProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 32620, 2, 2, 10)
)
anueGscProbeFailure.setObjects(
      *(("ANUE-MIB", "anueGscEvFailedPbDateAndTime"),
        ("ANUE-MIB", "anueGscEvFailedPbId"),
        ("ANUE-MIB", "anueGscEvFailedPbName"),
        ("ANUE-MIB", "anueGscEvFailedPbIP"),
        ("ANUE-MIB", "anueGscEvFailedPbPortList"),
        ("ANUE-MIB", "anueGscEvFailedPbLastRxHeartbeat"),
        ("ANUE-MIB", "anueGscEvFailedPbLastRxFailMsg"),
        ("ANUE-MIB", "anueGscEvFailoverPbId"),
        ("ANUE-MIB", "anueGscEvFailoverPbName"),
        ("ANUE-MIB", "anueGscEvFailoverPbIP"),
        ("ANUE-MIB", "anueGscEvFailoverPbPortList"))
)
if mibBuilder.loadTexts:
    anueGscProbeFailure.setStatus(
        "current"
    )


# Notifications groups

anueNtoEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 1, 7)
)
anueNtoEventGroup.setObjects(
      *(("ANUE-MIB", "anueSnmpAuthenticationFailure"),
        ("ANUE-MIB", "anueClientLoginFailure"),
        ("ANUE-MIB", "anueNtoEventMonStatInvalidCount"),
        ("ANUE-MIB", "anueNtoEventMonStatDropCount"),
        ("ANUE-MIB", "anueNtoEventMonStatRxUtilization"),
        ("ANUE-MIB", "anueNtoEventMonStatTxUtilization"),
        ("ANUE-MIB", "anueNtoEventTest"),
        ("ANUE-MIB", "anueNtoEventMonStatLoadDistribution"),
        ("ANUE-MIB", "anueNtoEventUnionMemberAction"))
)
if mibBuilder.loadTexts:
    anueNtoEventGroup.setStatus(
        "current"
    )

anueGscEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 1, 2, 1)
)
anueGscEventGroup.setObjects(
      *(("ANUE-MIB", "anueGscEventMonStatOverflowPkts"),
        ("ANUE-MIB", "anueGscEventMonStatControlPlanePktRate"),
        ("ANUE-MIB", "anueGscEventMonStatExcessSessions"),
        ("ANUE-MIB", "anueGscEventMonStatIngressPktDrops"),
        ("ANUE-MIB", "anueGscEventMonStatSessionsTableLoad"),
        ("ANUE-MIB", "anueGscEventMonStatNetworkElemLoad"),
        ("ANUE-MIB", "anueGscEventMonStatReqRespLoad"),
        ("ANUE-MIB", "anueGscEventMonStatFragmentationLoad"),
        ("ANUE-MIB", "anueGscCriticalFailure"),
        ("ANUE-MIB", "anueGscProbeFailure"))
)
if mibBuilder.loadTexts:
    anueGscEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

anueMIBCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 32620, 3, 1, 2, 2)
)
anueMIBCompliances.setObjects(
      *(("ANUE-MIB", "anueNtoSystemGroup"),
        ("ANUE-MIB", "anueNtoEventGroup"),
        ("ANUE-MIB", "anueNtoFilterGroup"),
        ("ANUE-MIB", "anueNtoIfExtGroup"),
        ("ANUE-MIB", "anueNtoStageGroup"),
        ("ANUE-MIB", "anueNtoCaptureGroup"),
        ("ANUE-MIB", "anueNtoCaptureStatsGroup"),
        ("ANUE-MIB", "anueNtoResourceGroup"),
        ("ANUE-MIB", "anueGscEventGroup"))
)
if mibBuilder.loadTexts:
    anueMIBCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANUE-MIB",
    **{"AnueStageType": AnueStageType,
       "AnueFilterTypeDT": AnueFilterTypeDT,
       "AnueThresholdCrossing": AnueThresholdCrossing,
       "AnueNtoUnionMemberActionType": AnueNtoUnionMemberActionType,
       "AnueTimeSourceType": AnueTimeSourceType,
       "anueMIB": anueMIB,
       "anueObjects": anueObjects,
       "anueNtoObjects": anueNtoObjects,
       "anueNtoSystem": anueNtoSystem,
       "anueNtoLastSnmpAuthnFailure": anueNtoLastSnmpAuthnFailure,
       "anueSnmpAuthnFailureTime": anueSnmpAuthnFailureTime,
       "anueSnmpAuthnFailureUsername": anueSnmpAuthnFailureUsername,
       "anueSnmpAuthnFailureSrcIpType": anueSnmpAuthnFailureSrcIpType,
       "anueSnmpAuthnFailureSrcIp": anueSnmpAuthnFailureSrcIp,
       "anueSnmpAuthnFailureSecModel": anueSnmpAuthnFailureSecModel,
       "anueNtoLastClientLoginFailure": anueNtoLastClientLoginFailure,
       "anueClientLoginFailureTime": anueClientLoginFailureTime,
       "anueClientLoginFailureId": anueClientLoginFailureId,
       "anueClientLoginFailureSrcIpType": anueClientLoginFailureSrcIpType,
       "anueClientLoginFailureSrcIp": anueClientLoginFailureSrcIp,
       "anueClientLoginFailureReason": anueClientLoginFailureReason,
       "anueSnmpAuthnFailureTrapEnable": anueSnmpAuthnFailureTrapEnable,
       "anueClientLoginFailureTrapEnable": anueClientLoginFailureTrapEnable,
       "anueLoginBanner": anueLoginBanner,
       "anueTimestampingTimeSource": anueTimestampingTimeSource,
       "anueTimestampingStatus": anueTimestampingStatus,
       "anueNtoCustomFilterSetConfig": anueNtoCustomFilterSetConfig,
       "anueCustomFieldSetEnableState": anueCustomFieldSetEnableState,
       "anueCustomFieldSetsTable": anueCustomFieldSetsTable,
       "anueCustomFieldSetsEntry": anueCustomFieldSetsEntry,
       "anueFieldSetId": anueFieldSetId,
       "anueFieldSetAvailOuterHdrFlds": anueFieldSetAvailOuterHdrFlds,
       "anueFieldSetIsAdditOuterHdrs": anueFieldSetIsAdditOuterHdrs,
       "anueCustomFieldsTable": anueCustomFieldsTable,
       "anueCustomFieldsEntry": anueCustomFieldsEntry,
       "anueCustomFieldId": anueCustomFieldId,
       "anueCustomFieldPktType": anueCustomFieldPktType,
       "anueCustomFieldSize": anueCustomFieldSize,
       "anueCustomFieldName": anueCustomFieldName,
       "anueCustomFieldSpecificAttrList": anueCustomFieldSpecificAttrList,
       "anueCustomFieldConfirmFldsList": anueCustomFieldConfirmFldsList,
       "anueNtoIfExt": anueNtoIfExt,
       "anueNtoIfExtTable": anueNtoIfExtTable,
       "anueNtoIfExtEntry": anueNtoIfExtEntry,
       "anueIfIsLicensed": anueIfIsLicensed,
       "anueIfLicensedMaxSpeed": anueIfLicensedMaxSpeed,
       "anueIfMode": anueIfMode,
       "anueIfDesc": anueIfDesc,
       "anueIfOnAfm": anueIfOnAfm,
       "anueIfAdvCapabilities": anueIfAdvCapabilities,
       "anueNtoFilter": anueNtoFilter,
       "anueFilterCollectionPeriod": anueFilterCollectionPeriod,
       "anueNtoFilterDefTable": anueNtoFilterDefTable,
       "anueNtoFilterDefEntry": anueNtoFilterDefEntry,
       "anueFilterType": anueFilterType,
       "anueFilterNumber": anueFilterNumber,
       "anueFilterDefaultName": anueFilterDefaultName,
       "anueFilterName": anueFilterName,
       "anueFilterDesc": anueFilterDesc,
       "anueFilterIfIndex": anueFilterIfIndex,
       "anueFilterIsTwoStage": anueFilterIsTwoStage,
       "anueFilterMode": anueFilterMode,
       "anueFilterCriteria": anueFilterCriteria,
       "anueFilterTag": anueFilterTag,
       "anueFilterAfmEnabled": anueFilterAfmEnabled,
       "anueFilterEnabledFeatures": anueFilterEnabledFeatures,
       "anueFilterCustomFieldSets": anueFilterCustomFieldSets,
       "anueNtoFilterConnTable": anueNtoFilterConnTable,
       "anueNtoFilterConnEntry": anueNtoFilterConnEntry,
       "anueFilterConnFromOid": anueFilterConnFromOid,
       "anueFilterConnToOid": anueFilterConnToOid,
       "anueNtoFilterHistTable": anueNtoFilterHistTable,
       "anueNtoFilterHistEntry": anueNtoFilterHistEntry,
       "anueFilterCreatedTime": anueFilterCreatedTime,
       "anueFilterCreatedBy": anueFilterCreatedBy,
       "anueFilterCriteriaModTime": anueFilterCriteriaModTime,
       "anueFilterCriteriaModTimeStamp": anueFilterCriteriaModTimeStamp,
       "anueFilterCriteriaModBy": anueFilterCriteriaModBy,
       "anueFilterConfigModTime": anueFilterConfigModTime,
       "anueFilterConfigModBy": anueFilterConfigModBy,
       "anueFilterConfigModFields": anueFilterConfigModFields,
       "anueFilterStatsResetTime": anueFilterStatsResetTime,
       "anueFilterStatsResetBy": anueFilterStatsResetBy,
       "anueFilterDropResetTime": anueFilterDropResetTime,
       "anueFilterDropResetBy": anueFilterDropResetBy,
       "anueNtoFilterStatsCntModHCTable": anueNtoFilterStatsCntModHCTable,
       "anueNtoFilterStatsCntModHCEntry": anueNtoFilterStatsCntModHCEntry,
       "anueFilterCntModHCInOctets": anueFilterCntModHCInOctets,
       "anueFilterCntModHCOutOctets": anueFilterCntModHCOutOctets,
       "anueFilterCntModHCInPkts": anueFilterCntModHCInPkts,
       "anueFilterCntModHCOutPkts": anueFilterCntModHCOutPkts,
       "anueFilterCntModHCDropPkts": anueFilterCntModHCDropPkts,
       "anueFilterCntModHCDropTime": anueFilterCntModHCDropTime,
       "anueNtoFilterStatsCntRstHCTable": anueNtoFilterStatsCntRstHCTable,
       "anueNtoFilterStatsCntRstHCEntry": anueNtoFilterStatsCntRstHCEntry,
       "anueFilterCntRstHCInOctets": anueFilterCntRstHCInOctets,
       "anueFilterCntRstHCOutOctets": anueFilterCntRstHCOutOctets,
       "anueFilterCntRstHCInPkts": anueFilterCntRstHCInPkts,
       "anueFilterCntRstHCOutPkts": anueFilterCntRstHCOutPkts,
       "anueFilterCntRstHCDropPkts": anueFilterCntRstHCDropPkts,
       "anueFilterCntRstHCDropTime": anueFilterCntRstHCDropTime,
       "anueNtoFilterStatsCurHCTable": anueNtoFilterStatsCurHCTable,
       "anueNtoFilterStatsCurHCEntry": anueNtoFilterStatsCurHCEntry,
       "anueFilterCurHCInOctets": anueFilterCurHCInOctets,
       "anueFilterCurHCOutOctets": anueFilterCurHCOutOctets,
       "anueFilterCurHCRateOctets": anueFilterCurHCRateOctets,
       "anueFilterCurHCInPkts": anueFilterCurHCInPkts,
       "anueFilterCurHCOutPkts": anueFilterCurHCOutPkts,
       "anueFilterCurHCRatePkts": anueFilterCurHCRatePkts,
       "anueFilterCurHCDropPkts": anueFilterCurHCDropPkts,
       "anueFilterCurHCUtil": anueFilterCurHCUtil,
       "anueNtoFilterStatsAvgHCTable": anueNtoFilterStatsAvgHCTable,
       "anueNtoFilterStatsAvgHCEntry": anueNtoFilterStatsAvgHCEntry,
       "anueFilterAvgHCInOctets": anueFilterAvgHCInOctets,
       "anueFilterAvgHCOutOctets": anueFilterAvgHCOutOctets,
       "anueFilterAvgHCRateOctets": anueFilterAvgHCRateOctets,
       "anueFilterAvgHCInPkts": anueFilterAvgHCInPkts,
       "anueFilterAvgHCOutPkts": anueFilterAvgHCOutPkts,
       "anueFilterAvgHCRatePkts": anueFilterAvgHCRatePkts,
       "anueFilterAvgHCDropPkts": anueFilterAvgHCDropPkts,
       "anueFilterAvgHCUtil": anueFilterAvgHCUtil,
       "anueNtoFilterStatsPeakHCTable": anueNtoFilterStatsPeakHCTable,
       "anueNtoFilterStatsPeakHCEntry": anueNtoFilterStatsPeakHCEntry,
       "anueFilterPeakHCInOctets": anueFilterPeakHCInOctets,
       "anueFilterPeakHCInOctetsTime": anueFilterPeakHCInOctetsTime,
       "anueFilterPeakHCOutOctets": anueFilterPeakHCOutOctets,
       "anueFilterPeakHCOutOctetsTime": anueFilterPeakHCOutOctetsTime,
       "anueFilterPeakHCRateOctets": anueFilterPeakHCRateOctets,
       "anueFilterPeakHCRateOctetsTime": anueFilterPeakHCRateOctetsTime,
       "anueFilterPeakHCInPkts": anueFilterPeakHCInPkts,
       "anueFilterPeakHCInPktsTime": anueFilterPeakHCInPktsTime,
       "anueFilterPeakHCOutPkts": anueFilterPeakHCOutPkts,
       "anueFilterPeakHCOutPktsTime": anueFilterPeakHCOutPktsTime,
       "anueFilterPeakHCRatePkts": anueFilterPeakHCRatePkts,
       "anueFilterPeakHCRatePktsTime": anueFilterPeakHCRatePktsTime,
       "anueFilterPeakHCDropPkts": anueFilterPeakHCDropPkts,
       "anueFilterPeakHCDropPktsTime": anueFilterPeakHCDropPktsTime,
       "anueFilterPeakHCUtil": anueFilterPeakHCUtil,
       "anueFilterPeakHCUtilTime": anueFilterPeakHCUtilTime,
       "anueNtoFilterStatsCntModTable": anueNtoFilterStatsCntModTable,
       "anueNtoFilterStatsCntModEntry": anueNtoFilterStatsCntModEntry,
       "anueFilterCntModInOctets": anueFilterCntModInOctets,
       "anueFilterCntModOutOctets": anueFilterCntModOutOctets,
       "anueFilterCntModInPkts": anueFilterCntModInPkts,
       "anueFilterCntModOutPkts": anueFilterCntModOutPkts,
       "anueFilterCntModDropPkts": anueFilterCntModDropPkts,
       "anueFilterCntModDropTime": anueFilterCntModDropTime,
       "anueNtoFilterStatsCntRstTable": anueNtoFilterStatsCntRstTable,
       "anueNtoFilterStatsCntRstEntry": anueNtoFilterStatsCntRstEntry,
       "anueFilterCntRstInOctets": anueFilterCntRstInOctets,
       "anueFilterCntRstOutOctets": anueFilterCntRstOutOctets,
       "anueFilterCntRstInPkts": anueFilterCntRstInPkts,
       "anueFilterCntRstOutPkts": anueFilterCntRstOutPkts,
       "anueFilterCntRstDropPkts": anueFilterCntRstDropPkts,
       "anueFilterCntRstDropTime": anueFilterCntRstDropTime,
       "anueNtoFilterStatsCurTable": anueNtoFilterStatsCurTable,
       "anueNtoFilterStatsCurEntry": anueNtoFilterStatsCurEntry,
       "anueFilterCurInOctets": anueFilterCurInOctets,
       "anueFilterCurOutOctets": anueFilterCurOutOctets,
       "anueFilterCurRateOctets": anueFilterCurRateOctets,
       "anueFilterCurInPkts": anueFilterCurInPkts,
       "anueFilterCurOutPkts": anueFilterCurOutPkts,
       "anueFilterCurRatePkts": anueFilterCurRatePkts,
       "anueFilterCurDropPkts": anueFilterCurDropPkts,
       "anueFilterCurUtil": anueFilterCurUtil,
       "anueNtoFilterStatsAvgTable": anueNtoFilterStatsAvgTable,
       "anueNtoFilterStatsAvgEntry": anueNtoFilterStatsAvgEntry,
       "anueFilterAvgInOctets": anueFilterAvgInOctets,
       "anueFilterAvgOutOctets": anueFilterAvgOutOctets,
       "anueFilterAvgRateOctets": anueFilterAvgRateOctets,
       "anueFilterAvgInPkts": anueFilterAvgInPkts,
       "anueFilterAvgOutPkts": anueFilterAvgOutPkts,
       "anueFilterAvgRatePkts": anueFilterAvgRatePkts,
       "anueFilterAvgDropPkts": anueFilterAvgDropPkts,
       "anueFilterAvgUtil": anueFilterAvgUtil,
       "anueNtoFilterStatsPeakTable": anueNtoFilterStatsPeakTable,
       "anueNtoFilterStatsPeakEntry": anueNtoFilterStatsPeakEntry,
       "anueFilterPeakInOctets": anueFilterPeakInOctets,
       "anueFilterPeakInOctetsTime": anueFilterPeakInOctetsTime,
       "anueFilterPeakOutOctets": anueFilterPeakOutOctets,
       "anueFilterPeakOutOctetsTime": anueFilterPeakOutOctetsTime,
       "anueFilterPeakRateOctets": anueFilterPeakRateOctets,
       "anueFilterPeakRateOctetsTime": anueFilterPeakRateOctetsTime,
       "anueFilterPeakInPkts": anueFilterPeakInPkts,
       "anueFilterPeakInPktsTime": anueFilterPeakInPktsTime,
       "anueFilterPeakOutPkts": anueFilterPeakOutPkts,
       "anueFilterPeakOutPktsTime": anueFilterPeakOutPktsTime,
       "anueFilterPeakRatePkts": anueFilterPeakRatePkts,
       "anueFilterPeakRatePktsTime": anueFilterPeakRatePktsTime,
       "anueFilterPeakDropPkts": anueFilterPeakDropPkts,
       "anueFilterPeakDropPktsTime": anueFilterPeakDropPktsTime,
       "anueFilterPeakUtil": anueFilterPeakUtil,
       "anueFilterPeakUtilTime": anueFilterPeakUtilTime,
       "anueFilterDefLastChange": anueFilterDefLastChange,
       "anueFilterConnLastChange": anueFilterConnLastChange,
       "anueNtoFilterStatsGscSessTable": anueNtoFilterStatsGscSessTable,
       "anueNtoFilterStatsGscSessEntry": anueNtoFilterStatsGscSessEntry,
       "anueFilterGscCurDenyGtpV0Sess": anueFilterGscCurDenyGtpV0Sess,
       "anueFilterGscCurDenyGtpV1Sess": anueFilterGscCurDenyGtpV1Sess,
       "anueFilterGscCurDenyGtpV2Sess": anueFilterGscCurDenyGtpV2Sess,
       "anueFilterGscCurDenyGtpTotSess": anueFilterGscCurDenyGtpTotSess,
       "anueFilterGscAvgDenyGtpV0Sess": anueFilterGscAvgDenyGtpV0Sess,
       "anueFilterGscAvgDenyGtpV1Sess": anueFilterGscAvgDenyGtpV1Sess,
       "anueFilterGscAvgDenyGtpV2Sess": anueFilterGscAvgDenyGtpV2Sess,
       "anueFilterGscAvgDenyGtpTotSess": anueFilterGscAvgDenyGtpTotSess,
       "anueFilterGscPkDenyGtpV0Sess": anueFilterGscPkDenyGtpV0Sess,
       "anueFilterGscPkDenyGtpV1Sess": anueFilterGscPkDenyGtpV1Sess,
       "anueFilterGscPkDenyGtpV2Sess": anueFilterGscPkDenyGtpV2Sess,
       "anueFilterGscPkDenyGtpTotSess": anueFilterGscPkDenyGtpTotSess,
       "anueFilterGscPkDenyGtpV0SessT": anueFilterGscPkDenyGtpV0SessT,
       "anueFilterGscPkDenyGtpV1SessT": anueFilterGscPkDenyGtpV1SessT,
       "anueFilterGscPkDenyGtpV2SessT": anueFilterGscPkDenyGtpV2SessT,
       "anueFilterGscPkDenyGtpTotSessT": anueFilterGscPkDenyGtpTotSessT,
       "anueFilterGscTotOversizePktsTx": anueFilterGscTotOversizePktsTx,
       "anueFilterGscCurOversizePktsTx": anueFilterGscCurOversizePktsTx,
       "anueFilterGscAvgOversizePktsTx": anueFilterGscAvgOversizePktsTx,
       "anueFilterGscPkOversizePktsTx": anueFilterGscPkOversizePktsTx,
       "anueFilterGscPkOversizePktsTxT": anueFilterGscPkOversizePktsTxT,
       "anueFilterGscTotDroppedPkts": anueFilterGscTotDroppedPkts,
       "anueFilterGscCurDroppedPkts": anueFilterGscCurDroppedPkts,
       "anueFilterGscAvgDroppedPkts": anueFilterGscAvgDroppedPkts,
       "anueFilterGscPkDroppedPkts": anueFilterGscPkDroppedPkts,
       "anueFilterGscPkDroppedPktsT": anueFilterGscPkDroppedPktsT,
       "anueFilterGscTotDroppedBytes": anueFilterGscTotDroppedBytes,
       "anueFilterGscCurDroppedBytes": anueFilterGscCurDroppedBytes,
       "anueFilterGscAvgDroppedBytes": anueFilterGscAvgDroppedBytes,
       "anueFilterGscPkDroppedBytes": anueFilterGscPkDroppedBytes,
       "anueFilterGscPkDroppedBytesT": anueFilterGscPkDroppedBytesT,
       "anueNtoFilterStatsGscTable": anueNtoFilterStatsGscTable,
       "anueNtoFilterStatsGscEntry": anueNtoFilterStatsGscEntry,
       "anueFilterCurGscPktsRate": anueFilterCurGscPktsRate,
       "anueFilterAvgGscPktsRate": anueFilterAvgGscPktsRate,
       "anueFilterPeakGscPktsRate": anueFilterPeakGscPktsRate,
       "anueFilterPeakTimeGscPktsRate": anueFilterPeakTimeGscPktsRate,
       "anueFilterGTPPktType": anueFilterGTPPktType,
       "anueNtoStage": anueNtoStage,
       "anueNtoStageStripTable": anueNtoStageStripTable,
       "anueNtoStageStripEntry": anueNtoStageStripEntry,
       "anueStageStripFilterType": anueStageStripFilterType,
       "anueStageStripFilterNumber": anueStageStripFilterNumber,
       "anueStageStripFeature": anueStageStripFeature,
       "anueStageStripOrder": anueStageStripOrder,
       "anueStageStripType": anueStageStripType,
       "anueStageStripModPkts": anueStageStripModPkts,
       "anueStageStripModPktPct": anueStageStripModPktPct,
       "anueStageStripErrorPkts": anueStageStripErrorPkts,
       "anueStageStripRstModPkts": anueStageStripRstModPkts,
       "anueStageStripRstModPktPct": anueStageStripRstModPktPct,
       "anueStageStripRstErrorPkts": anueStageStripRstErrorPkts,
       "anueStageStripAttributes": anueStageStripAttributes,
       "anueNtoStageNPErrorTable": anueNtoStageNPErrorTable,
       "anueNtoStageNPErrorEntry": anueNtoStageNPErrorEntry,
       "anueStageNPErrorFilterType": anueStageNPErrorFilterType,
       "anueStageNPErrorFilterNumber": anueStageNPErrorFilterNumber,
       "anueStageNPErrorFeature": anueStageNPErrorFeature,
       "anueStageNPErrorOrder": anueStageNPErrorOrder,
       "anueStageNPErrorPkts": anueStageNPErrorPkts,
       "anueStageNPErrorRstPkts": anueStageNPErrorRstPkts,
       "anueNtoStageDedupTable": anueNtoStageDedupTable,
       "anueNtoStageDedupEntry": anueNtoStageDedupEntry,
       "anueStageDedupFilterType": anueStageDedupFilterType,
       "anueStageDedupFilterNumber": anueStageDedupFilterNumber,
       "anueStageDedupFeature": anueStageDedupFeature,
       "anueStageDedupOrder": anueStageDedupOrder,
       "anueStageDedupType": anueStageDedupType,
       "anueStageDedupTimeWindows": anueStageDedupTimeWindows,
       "anueStageDedupRmvPkts": anueStageDedupRmvPkts,
       "anueStageDedupRmvPktPct": anueStageDedupRmvPktPct,
       "anueStageDedupRstRmvPkts": anueStageDedupRstRmvPkts,
       "anueStageDedupRstRmvPktPct": anueStageDedupRstRmvPktPct,
       "anueNtoStageTrimTable": anueNtoStageTrimTable,
       "anueNtoStageTrimEntry": anueNtoStageTrimEntry,
       "anueStageTrimFilterType": anueStageTrimFilterType,
       "anueStageTrimFilterNumber": anueStageTrimFilterNumber,
       "anueStageTrimFeature": anueStageTrimFeature,
       "anueStageTrimOrder": anueStageTrimOrder,
       "anueStageTrimType": anueStageTrimType,
       "anueStageTrimRetainOctets": anueStageTrimRetainOctets,
       "anueStageTrimModPkts": anueStageTrimModPkts,
       "anueStageTrimModPktPct": anueStageTrimModPktPct,
       "anueStageTrimRmvOctets": anueStageTrimRmvOctets,
       "anueStageTrimRmvOctetPct": anueStageTrimRmvOctetPct,
       "anueStageTrimRstModPkts": anueStageTrimRstModPkts,
       "anueStageTrimRstModPktPct": anueStageTrimRstModPktPct,
       "anueStageTrimRstRmvOctets": anueStageTrimRstRmvOctets,
       "anueStageTrimRstRmvOctetPct": anueStageTrimRstRmvOctetPct,
       "anueNtoStageBurstBufferTable": anueNtoStageBurstBufferTable,
       "anueNtoStageBurstBufferEntry": anueNtoStageBurstBufferEntry,
       "anueStageBufferFilterType": anueStageBufferFilterType,
       "anueStageBufferFilterNumber": anueStageBufferFilterNumber,
       "anueStageBufferFeature": anueStageBufferFeature,
       "anueStageBufferOrder": anueStageBufferOrder,
       "anueStageBufferSize": anueStageBufferSize,
       "anueStageBufferCurBufferLevel": anueStageBufferCurBufferLevel,
       "anueStageBufferPeakBufferLevel": anueStageBufferPeakBufferLevel,
       "anueStageBufferPeakBufferTime": anueStageBufferPeakBufferTime,
       "anueStageBufferDropPkts": anueStageBufferDropPkts,
       "anueStageBufferDropTime": anueStageBufferDropTime,
       "anueStageBufferRstDropPkts": anueStageBufferRstDropPkts,
       "anueStageBufferRstDropTime": anueStageBufferRstDropTime,
       "anueNtoStageNPFilterTable": anueNtoStageNPFilterTable,
       "anueNtoStageNPFilterEntry": anueNtoStageNPFilterEntry,
       "anueStageNPFilterFilterType": anueStageNPFilterFilterType,
       "anueStageNPFilterFilterNumber": anueStageNPFilterFilterNumber,
       "anueStageNPFilterFeature": anueStageNPFilterFeature,
       "anueStageNPFilterOrder": anueStageNPFilterOrder,
       "anueStageNPFilterDenyPkts": anueStageNPFilterDenyPkts,
       "anueStageNPFilterDenyPktPct": anueStageNPFilterDenyPktPct,
       "anueStageNPFilterDenyOctets": anueStageNPFilterDenyOctets,
       "anueStageNPFilterDenyOctetPct": anueStageNPFilterDenyOctetPct,
       "anueStageNPFilterRstDenyPkts": anueStageNPFilterRstDenyPkts,
       "anueStageNPFilterRstDenyPktPct": anueStageNPFilterRstDenyPktPct,
       "anueStageNPFilterRstDenyOctets": anueStageNPFilterRstDenyOctets,
       "anueStageNPFilterRstDenyOctetPct": anueStageNPFilterRstDenyOctetPct,
       "anueNtoStageTPFilterTable": anueNtoStageTPFilterTable,
       "anueNtoStageTPFilterEntry": anueNtoStageTPFilterEntry,
       "anueStageTPFilterFilterType": anueStageTPFilterFilterType,
       "anueStageTPFilterFilterNumber": anueStageTPFilterFilterNumber,
       "anueStageTPFilterFeature": anueStageTPFilterFeature,
       "anueStageTPFilterOrder": anueStageTPFilterOrder,
       "anueStageTPFilterDenyPkts": anueStageTPFilterDenyPkts,
       "anueStageTPFilterDenyPktPct": anueStageTPFilterDenyPktPct,
       "anueStageTPFilterDropPkts": anueStageTPFilterDropPkts,
       "anueStageTPFilterDropTime": anueStageTPFilterDropTime,
       "anueStageTPFilterRstDenyPkts": anueStageTPFilterRstDenyPkts,
       "anueStageTPFilterRstDenyPktPct": anueStageTPFilterRstDenyPktPct,
       "anueStageTPFilterRstDropPkts": anueStageTPFilterRstDropPkts,
       "anueStageTPFilterRstDropTime": anueStageTPFilterRstDropTime,
       "anueNtoStageAfmDropTable": anueNtoStageAfmDropTable,
       "anueNtoStageAfmDropEntry": anueNtoStageAfmDropEntry,
       "anueStageAfmDropFilterType": anueStageAfmDropFilterType,
       "anueStageAfmDropFilterNumber": anueStageAfmDropFilterNumber,
       "anueStageAfmDropFeature": anueStageAfmDropFeature,
       "anueStageAfmDropOrder": anueStageAfmDropOrder,
       "anueStageAfmDropDropPkts": anueStageAfmDropDropPkts,
       "anueStageAfmDropDropTime": anueStageAfmDropDropTime,
       "anueStageAfmDropRstDropPkts": anueStageAfmDropRstDropPkts,
       "anueStageAfmDropRstDropTime": anueStageAfmDropRstDropTime,
       "anueNtoStageTagTable": anueNtoStageTagTable,
       "anueNtoStageTagEntry": anueNtoStageTagEntry,
       "anueStageTagFilterType": anueStageTagFilterType,
       "anueStageTagFilterNumber": anueStageTagFilterNumber,
       "anueStageTagFeature": anueStageTagFeature,
       "anueStageTagOrder": anueStageTagOrder,
       "anueStageTagAttributes": anueStageTagAttributes,
       "anueStageTagModPkts": anueStageTagModPkts,
       "anueStageTagModPktPct": anueStageTagModPktPct,
       "anueStageTagRstModPkts": anueStageTagRstModPkts,
       "anueStageTagRstModPktPct": anueStageTagRstModPktPct,
       "anueNtoStageDropTable": anueNtoStageDropTable,
       "anueNtoStageDropEntry": anueNtoStageDropEntry,
       "anueStageDropFilterType": anueStageDropFilterType,
       "anueStageDropFilterNumber": anueStageDropFilterNumber,
       "anueStageDropFeature": anueStageDropFeature,
       "anueStageCntDropPkts": anueStageCntDropPkts,
       "anueStageCntDropTime": anueStageCntDropTime,
       "anueStageCurDropPkts": anueStageCurDropPkts,
       "anueStageAvgDropPkts": anueStageAvgDropPkts,
       "anueStagePeakDropPkts": anueStagePeakDropPkts,
       "anueStagePeakDropTime": anueStagePeakDropTime,
       "anueNtoStageGtpFdTable": anueNtoStageGtpFdTable,
       "anueNtoStageGtpFdEntry": anueNtoStageGtpFdEntry,
       "anueStageGtpFdFilterType": anueStageGtpFdFilterType,
       "anueStageGtpFdFilterNumber": anueStageGtpFdFilterNumber,
       "anueStageGtpFdFeature": anueStageGtpFdFeature,
       "anueStageRateGtpCPps": anueStageRateGtpCPps,
       "anueStageRateGtpUPps": anueStageRateGtpUPps,
       "anueStageRateGtpCBps": anueStageRateGtpCBps,
       "anueStageRateGtpUBps": anueStageRateGtpUBps,
       "anueNtoStageDataMaskingTable": anueNtoStageDataMaskingTable,
       "anueNtoStageDataMaskingEntry": anueNtoStageDataMaskingEntry,
       "anueStageDataMaskingFilterType": anueStageDataMaskingFilterType,
       "anueStageDataMaskingFilterNumber": anueStageDataMaskingFilterNumber,
       "anueStageDataMaskingFeature": anueStageDataMaskingFeature,
       "anueStageDataMaskingOrder": anueStageDataMaskingOrder,
       "anueStageDataMaskingOffsetLayer": anueStageDataMaskingOffsetLayer,
       "anueStageDataMaskingOffset": anueStageDataMaskingOffset,
       "anueStageDataMaskingLength": anueStageDataMaskingLength,
       "anueStageDataMaskingFillValue": anueStageDataMaskingFillValue,
       "anueStageDataMaskingModPkts": anueStageDataMaskingModPkts,
       "anueStageDataMaskingModPktPct": anueStageDataMaskingModPktPct,
       "anueStageDataMaskingRstModPkts": anueStageDataMaskingRstModPkts,
       "anueStageDataMaskingRstModPktPct": anueStageDataMaskingRstModPktPct,
       "anueNtoStageGscNetworkFilterTable": anueNtoStageGscNetworkFilterTable,
       "anueNtoStageGscNetworkFilterEntry": anueNtoStageGscNetworkFilterEntry,
       "anueNtoStageGscNetworkFilterType": anueNtoStageGscNetworkFilterType,
       "anueNtoStageGscNetworkFilterNumber": anueNtoStageGscNetworkFilterNumber,
       "anueGscNWFltrExcSess": anueGscNWFltrExcSess,
       "anueNtoStageGscNetworkFilterFeature": anueNtoStageGscNetworkFilterFeature,
       "anueGscNWFltrAvgGscPktFrag": anueGscNWFltrAvgGscPktFrag,
       "anueGscNWFltrAvgTdoutFrag": anueGscNWFltrAvgTdoutFrag,
       "anueGscNWFltrCurPacketFrag": anueGscNWFltrCurPacketFrag,
       "anueGscNWFltrCurTdoutFrag": anueGscNWFltrCurTdoutFrag,
       "anueGscNWFltrPkPacketFrag": anueGscNWFltrPkPacketFrag,
       "anueGscNWFltrPkPacketFragT": anueGscNWFltrPkPacketFragT,
       "anueGscNWFltrPkTdOutFrag": anueGscNWFltrPkTdOutFrag,
       "anueGscNWFltrPkTdOutFragT": anueGscNWFltrPkTdOutFragT,
       "anueGscNWFltrTotFrag": anueGscNWFltrTotFrag,
       "anueGscNWFltrTotRxCountFrag": anueGscNWFltrTotRxCountFrag,
       "anueGscNWFltrTotTdOutFrag": anueGscNWFltrTotTdOutFrag,
       "anueGscNWFltrAvgCompFragPkts": anueGscNWFltrAvgCompFragPkts,
       "anueGscNWFltrAvgCompFragPktsPerc": anueGscNWFltrAvgCompFragPktsPerc,
       "anueGscNWFltrAvgIncomFragPkts": anueGscNWFltrAvgIncomFragPkts,
       "anueGscNWFltrCurCompFragPkts": anueGscNWFltrCurCompFragPkts,
       "anueGscNWFltrCurCompFragPktsPerc": anueGscNWFltrCurCompFragPktsPerc,
       "anueGscNWFltrCurIncomFragPkts": anueGscNWFltrCurIncomFragPkts,
       "anueGscNWFltrPkCompFragPkts": anueGscNWFltrPkCompFragPkts,
       "anueGscNWFltrPkCompFragPktsT": anueGscNWFltrPkCompFragPktsT,
       "anueGscNWFltrPkCompFragPktsPerc": anueGscNWFltrPkCompFragPktsPerc,
       "anueGscNWFltrPkCompFragPktsPercT": anueGscNWFltrPkCompFragPktsPercT,
       "anueGscNWFltrPkIncomFragPkts": anueGscNWFltrPkIncomFragPkts,
       "anueGscNWFltrPkIncomFragPktsT": anueGscNWFltrPkIncomFragPktsT,
       "anueGscNWFltrPkTotCompFragPkts": anueGscNWFltrPkTotCompFragPkts,
       "anueGscNWFltrAvgActiveUsers": anueGscNWFltrAvgActiveUsers,
       "anueGscNWFltrCurActiveUsers": anueGscNWFltrCurActiveUsers,
       "anueGscNWFltrPkActiveUsers": anueGscNWFltrPkActiveUsers,
       "anueGscNWFltrPkActiveUsersT": anueGscNWFltrPkActiveUsersT,
       "anueGscNWFltrAvgExcSess": anueGscNWFltrAvgExcSess,
       "anueGscNWFltrCurExcSess": anueGscNWFltrCurExcSess,
       "anueGscNWFltrPkExcSess": anueGscNWFltrPkExcSess,
       "anueGscNWFltrPkExcSessT": anueGscNWFltrPkExcSessT,
       "anueGscNWFltrTotExcSess": anueGscNWFltrTotExcSess,
       "anueGscNWFltrTotGtpV0CrSess": anueGscNWFltrTotGtpV0CrSess,
       "anueGscNWFltrTotGtpV1CrSess": anueGscNWFltrTotGtpV1CrSess,
       "anueGscNWFltrTotGtpV2CrSess": anueGscNWFltrTotGtpV2CrSess,
       "anueGscNWFltrTotGtpTotCrSess": anueGscNWFltrTotGtpTotCrSess,
       "anueGscNWFltrAvgGtpV0CrSess": anueGscNWFltrAvgGtpV0CrSess,
       "anueGscNWFltrAvgGtpV1CrSess": anueGscNWFltrAvgGtpV1CrSess,
       "anueGscNWFltrAvgGtpV2CrSess": anueGscNWFltrAvgGtpV2CrSess,
       "anueGscNWFltrAvgGtpTotCrSess": anueGscNWFltrAvgGtpTotCrSess,
       "anueGscNWFltrCurGtpV0CrSess": anueGscNWFltrCurGtpV0CrSess,
       "anueGscNWFltrCurGtpV1CrSess": anueGscNWFltrCurGtpV1CrSess,
       "anueGscNWFltrCurGtpV2CrSess": anueGscNWFltrCurGtpV2CrSess,
       "anueGscNWFltrCurGtpTotCrSess": anueGscNWFltrCurGtpTotCrSess,
       "anueGscNWFltrPkGtpV0CrSess": anueGscNWFltrPkGtpV0CrSess,
       "anueGscNWFltrPkGtpV1CrSess": anueGscNWFltrPkGtpV1CrSess,
       "anueGscNWFltrPkGtpV2CrSess": anueGscNWFltrPkGtpV2CrSess,
       "anueGscNWFltrPkGtpTotCrSess": anueGscNWFltrPkGtpTotCrSess,
       "anueGscNWFltrPkGtpV0CrSessT": anueGscNWFltrPkGtpV0CrSessT,
       "anueGscNWFltrPkGtpV1CrSessT": anueGscNWFltrPkGtpV1CrSessT,
       "anueGscNWFltrPkGtpV2CrSessT": anueGscNWFltrPkGtpV2CrSessT,
       "anueGscNWFltrPkGtpTotCrSessT": anueGscNWFltrPkGtpTotCrSessT,
       "anueGscNWFltrTotGtpV0DelSess": anueGscNWFltrTotGtpV0DelSess,
       "anueGscNWFltrTotGtpV1DelSess": anueGscNWFltrTotGtpV1DelSess,
       "anueGscNWFltrTotGtpV2DelSess": anueGscNWFltrTotGtpV2DelSess,
       "anueGscNWFltrTotGtpTotDelSess": anueGscNWFltrTotGtpTotDelSess,
       "anueGscNWFltrAvgGtpV0DelSess": anueGscNWFltrAvgGtpV0DelSess,
       "anueGscNWFltrAvgGtpV1DelSess": anueGscNWFltrAvgGtpV1DelSess,
       "anueGscNWFltrAvgGtpV2DelSess": anueGscNWFltrAvgGtpV2DelSess,
       "anueGscNWFltrAvgGtpTotDelSess": anueGscNWFltrAvgGtpTotDelSess,
       "anueGscNWFltrCurGtpV0DelSess": anueGscNWFltrCurGtpV0DelSess,
       "anueGscNWFltrCurGtpV1DelSess": anueGscNWFltrCurGtpV1DelSess,
       "anueGscNWFltrCurGtpV2DelSess": anueGscNWFltrCurGtpV2DelSess,
       "anueGscNWFltrCurGtpTotDelSess": anueGscNWFltrCurGtpTotDelSess,
       "anueGscNWFltrPkGtpV0DelSess": anueGscNWFltrPkGtpV0DelSess,
       "anueGscNWFltrPkGtpV1DelSess": anueGscNWFltrPkGtpV1DelSess,
       "anueGscNWFltrPkGtpV2DelSess": anueGscNWFltrPkGtpV2DelSess,
       "anueGscNWFltrPkGtpTotDelSess": anueGscNWFltrPkGtpTotDelSess,
       "anueGscNWFltrPkGtpV0DelSessT": anueGscNWFltrPkGtpV0DelSessT,
       "anueGscNWFltrPkGtpV1DelSessT": anueGscNWFltrPkGtpV1DelSessT,
       "anueGscNWFltrPkGtpV2DelSessT": anueGscNWFltrPkGtpV2DelSessT,
       "anueGscNWFltrPkGtpTotDelSessT": anueGscNWFltrPkGtpTotDelSessT,
       "anueGscNWFltrAvgGtpV0Bearers": anueGscNWFltrAvgGtpV0Bearers,
       "anueGscNWFltrAvgGtpV1Bearers": anueGscNWFltrAvgGtpV1Bearers,
       "anueGscNWFltrAvgGtpV2Bearers": anueGscNWFltrAvgGtpV2Bearers,
       "anueGscNWFltrAvgGtpTotBearers": anueGscNWFltrAvgGtpTotBearers,
       "anueGscNWFltrCurGtpV0Bearers": anueGscNWFltrCurGtpV0Bearers,
       "anueGscNWFltrCurGtpV1Bearers": anueGscNWFltrCurGtpV1Bearers,
       "anueGscNWFltrCurGtpV2Bearers": anueGscNWFltrCurGtpV2Bearers,
       "anueGscNWFltrCurGtpTotBearers": anueGscNWFltrCurGtpTotBearers,
       "anueGscNWFltrPkGtpV0Bearers": anueGscNWFltrPkGtpV0Bearers,
       "anueGscNWFltrPkGtpV1Bearers": anueGscNWFltrPkGtpV1Bearers,
       "anueGscNWFltrPkGtpV2Bearers": anueGscNWFltrPkGtpV2Bearers,
       "anueGscNWFltrPkGtpTotBearers": anueGscNWFltrPkGtpTotBearers,
       "anueGscNWFltrPkGtpV0BearersT": anueGscNWFltrPkGtpV0BearersT,
       "anueGscNWFltrPkGtpV1BearersT": anueGscNWFltrPkGtpV1BearersT,
       "anueGscNWFltrPkGtpV2BearersT": anueGscNWFltrPkGtpV2BearersT,
       "anueGscNWFltrPkGtpTotBearersT": anueGscNWFltrPkGtpTotBearersT,
       "anueGscNWFltrAvgGtpV0Pkts": anueGscNWFltrAvgGtpV0Pkts,
       "anueGscNWFltrAvgGtpV1Pkts": anueGscNWFltrAvgGtpV1Pkts,
       "anueGscNWFltrAvgGtpV2Pkts": anueGscNWFltrAvgGtpV2Pkts,
       "anueGscNWFltrAvgGtpTotPkts": anueGscNWFltrAvgGtpTotPkts,
       "anueGscNWFltrCurGtpV0Pkts": anueGscNWFltrCurGtpV0Pkts,
       "anueGscNWFltrCurGtpV1Pkts": anueGscNWFltrCurGtpV1Pkts,
       "anueGscNWFltrCurGtpV2Pkts": anueGscNWFltrCurGtpV2Pkts,
       "anueGscNWFltrCurGtpTotPkts": anueGscNWFltrCurGtpTotPkts,
       "anueGscNWFltrTotGtpV1Pkts": anueGscNWFltrTotGtpV1Pkts,
       "anueGscNWFltrTotGtpV0Pkts": anueGscNWFltrTotGtpV0Pkts,
       "anueGscNWFltrTotGtpV2Pkts": anueGscNWFltrTotGtpV2Pkts,
       "anueGscNWFltrTotGtpTotPkts": anueGscNWFltrTotGtpTotPkts,
       "anueGscNWFltrPkGtpV0Pkts": anueGscNWFltrPkGtpV0Pkts,
       "anueGscNWFltrPkGtpV1Pkts": anueGscNWFltrPkGtpV1Pkts,
       "anueGscNWFltrPkGtpV2Pkts": anueGscNWFltrPkGtpV2Pkts,
       "anueGscNWFltrPkGtpTotPkts": anueGscNWFltrPkGtpTotPkts,
       "anueGscNWFltrPkGtpV0PktsT": anueGscNWFltrPkGtpV0PktsT,
       "anueGscNWFltrPkGtpV1PktsT": anueGscNWFltrPkGtpV1PktsT,
       "anueGscNWFltrPkGtpV2PktsT": anueGscNWFltrPkGtpV2PktsT,
       "anueGscNWFltrPkGtpTotPktsT": anueGscNWFltrPkGtpTotPktsT,
       "anueGscNWFltrTotGtpV0ToutSess": anueGscNWFltrTotGtpV0ToutSess,
       "anueGscNWFltrTotGtpV1ToutSess": anueGscNWFltrTotGtpV1ToutSess,
       "anueGscNWFltrTotGtpV2ToutSess": anueGscNWFltrTotGtpV2ToutSess,
       "anueGscNWFltrTotGtpTotToutSess": anueGscNWFltrTotGtpTotToutSess,
       "anueGscNWFltrAvgGtpV0ToutSess": anueGscNWFltrAvgGtpV0ToutSess,
       "anueGscNWFltrAvgGtpV1ToutSess": anueGscNWFltrAvgGtpV1ToutSess,
       "anueGscNWFltrAvgGtpV2ToutSess": anueGscNWFltrAvgGtpV2ToutSess,
       "anueGscNWFltrAvgGtpTotToutSess": anueGscNWFltrAvgGtpTotToutSess,
       "anueGscNWFltrCurGtpV0ToutSess": anueGscNWFltrCurGtpV0ToutSess,
       "anueGscNWFltrCurGtpV1ToutSess": anueGscNWFltrCurGtpV1ToutSess,
       "anueGscNWFltrCurGtpV2ToutSess": anueGscNWFltrCurGtpV2ToutSess,
       "anueGscNWFltrCurGtpTotToutSess": anueGscNWFltrCurGtpTotToutSess,
       "anueGscNWFltrPkGtpV0ToutSess": anueGscNWFltrPkGtpV0ToutSess,
       "anueGscNWFltrPkGtpV1ToutSess": anueGscNWFltrPkGtpV1ToutSess,
       "anueGscNWFltrPkGtpV2ToutSess": anueGscNWFltrPkGtpV2ToutSess,
       "anueGscNWFltrPkGtpTotToutSess": anueGscNWFltrPkGtpTotToutSess,
       "anueGscNWFltrPkGtpV0ToutSessT": anueGscNWFltrPkGtpV0ToutSessT,
       "anueGscNWFltrPkGtpV1ToutSessT": anueGscNWFltrPkGtpV1ToutSessT,
       "anueGscNWFltrPkGtpV2ToutSessT": anueGscNWFltrPkGtpV2ToutSessT,
       "anueGscNWFltrPkGtpTotToutSessT": anueGscNWFltrPkGtpTotToutSessT,
       "anueGscNWFltrAvgGtpCPkts": anueGscNWFltrAvgGtpCPkts,
       "anueGscNWFltrAvgGtpUPkts": anueGscNWFltrAvgGtpUPkts,
       "anueGscNWFltrAvgDiameterPkts": anueGscNWFltrAvgDiameterPkts,
       "anueGscNWFltrAvgDnsPkts": anueGscNWFltrAvgDnsPkts,
       "anueGscNWFltrAvgRadiusPkts": anueGscNWFltrAvgRadiusPkts,
       "anueGscNWFltrAvgNonGtpPkts": anueGscNWFltrAvgNonGtpPkts,
       "anueGscNWFltrCurGtpCPkts": anueGscNWFltrCurGtpCPkts,
       "anueGscNWFltrCurGtpUPkts": anueGscNWFltrCurGtpUPkts,
       "anueGscNWFltrCurDiameterPkts": anueGscNWFltrCurDiameterPkts,
       "anueGscNWFltrCurDnsPkts": anueGscNWFltrCurDnsPkts,
       "anueGscNWFltrCurRadiusPkts": anueGscNWFltrCurRadiusPkts,
       "anueGscNWFltrCurNonGtpPkts": anueGscNWFltrCurNonGtpPkts,
       "anueGscNWFltrPkGtpCPkts": anueGscNWFltrPkGtpCPkts,
       "anueGscNWFltrPkGtpUPkts": anueGscNWFltrPkGtpUPkts,
       "anueGscNWFltrPkDiameterPkts": anueGscNWFltrPkDiameterPkts,
       "anueGscNWFltrPkDnsPkts": anueGscNWFltrPkDnsPkts,
       "anueGscNWFltrPkRadiusPkts": anueGscNWFltrPkRadiusPkts,
       "anueGscNWFltrPkNonGtpPkts": anueGscNWFltrPkNonGtpPkts,
       "anueGscNWFltrPkGtpCPktsT": anueGscNWFltrPkGtpCPktsT,
       "anueGscNWFltrPkGtpUPktsT": anueGscNWFltrPkGtpUPktsT,
       "anueGscNWFltrPkDiameterPktsT": anueGscNWFltrPkDiameterPktsT,
       "anueGscNWFltrPkDnsPktsT": anueGscNWFltrPkDnsPktsT,
       "anueGscNWFltrPkRadiusPktsT": anueGscNWFltrPkRadiusPktsT,
       "anueGscNWFltrPkNonGtpPktsT": anueGscNWFltrPkNonGtpPktsT,
       "anueGscNWFltrTotGtpCPkts": anueGscNWFltrTotGtpCPkts,
       "anueGscNWFltrTotGtpUPkts": anueGscNWFltrTotGtpUPkts,
       "anueGscNWFltrTotDiameterPkts": anueGscNWFltrTotDiameterPkts,
       "anueGscNWFltrTotDnsPkts": anueGscNWFltrTotDnsPkts,
       "anueGscNWFltrTotRadiusPkts": anueGscNWFltrTotRadiusPkts,
       "anueGscNWFltrTotNonGtpPkts": anueGscNWFltrTotNonGtpPkts,
       "anueGscNWFltrTotGscDropPkts": anueGscNWFltrTotGscDropPkts,
       "anueGscNWFltrCurGscSessLoad": anueGscNWFltrCurGscSessLoad,
       "anueGscNWFltrAvgGscSessLoad": anueGscNWFltrAvgGscSessLoad,
       "anueGscNWFltrPeakGscSessLoad": anueGscNWFltrPeakGscSessLoad,
       "anueGscNWFltrPeakGscSessLoadT": anueGscNWFltrPeakGscSessLoadT,
       "anueGscNWFltrCurNetwElemLoad": anueGscNWFltrCurNetwElemLoad,
       "anueGscNWFltrPeakNetwElemLoad": anueGscNWFltrPeakNetwElemLoad,
       "anueGscNWFltrPeakNetwElemLoadT": anueGscNWFltrPeakNetwElemLoadT,
       "anueGscNWFltrCurReqRespLoad": anueGscNWFltrCurReqRespLoad,
       "anueGscNWFltrPeakReqRespLoad": anueGscNWFltrPeakReqRespLoad,
       "anueGscNWFltrPeakReqRespLoadT": anueGscNWFltrPeakReqRespLoadT,
       "anueGscNWFltrCurFragLoad": anueGscNWFltrCurFragLoad,
       "anueGscNWFltrPeakFragLoad": anueGscNWFltrPeakFragLoad,
       "anueGscNWFltrPeakFragLoadT": anueGscNWFltrPeakFragLoadT,
       "anueGscNWFltrAvgGscUnassignedSess": anueGscNWFltrAvgGscUnassignedSess,
       "anueGscNWFltrCurGscUnassignedSess": anueGscNWFltrCurGscUnassignedSess,
       "anueGscNWFltrPkGscUnassignedSess": anueGscNWFltrPkGscUnassignedSess,
       "anueGscNWFltrPkGscUnassignedSessT": anueGscNWFltrPkGscUnassignedSessT,
       "anueGscNWFltrTotGscUnassignedSess": anueGscNWFltrTotGscUnassignedSess,
       "anueGscNWFltrAvgUnprocReq": anueGscNWFltrAvgUnprocReq,
       "anueGscNWFltrCurUnprocReq": anueGscNWFltrCurUnprocReq,
       "anueGscNWFltrPkUnprocReq": anueGscNWFltrPkUnprocReq,
       "anueGscNWFltrPkUnprocReqT": anueGscNWFltrPkUnprocReqT,
       "anueGscNWFltrTotUnprocReq": anueGscNWFltrTotUnprocReq,
       "anueGscNWFltrAvgTdOutReq": anueGscNWFltrAvgTdOutReq,
       "anueGscNWFltrCurTdOutReq": anueGscNWFltrCurTdOutReq,
       "anueGscNWFltrPkTdOutReq": anueGscNWFltrPkTdOutReq,
       "anueGscNWFltrPkTdOutReqT": anueGscNWFltrPkTdOutReqT,
       "anueGscNWFltrTotTdOutReq": anueGscNWFltrTotTdOutReq,
       "anueGscNWFltrAvgUnmatchedResp": anueGscNWFltrAvgUnmatchedResp,
       "anueGscNWFltrCurUnmatchedResp": anueGscNWFltrCurUnmatchedResp,
       "anueGscNWFltrPkUnmatchedResp": anueGscNWFltrPkUnmatchedResp,
       "anueGscNWFltrPkUnmatchedRespT": anueGscNWFltrPkUnmatchedRespT,
       "anueGscNWFltrTotUnmatchedResp": anueGscNWFltrTotUnmatchedResp,
       "anueGscNWFltrOverloadErrCode": anueGscNWFltrOverloadErrCode,
       "anueGscNWFltrOverloadT": anueGscNWFltrOverloadT,
       "anueNtoStageGscToolFilterTable": anueNtoStageGscToolFilterTable,
       "anueNtoStageGscToolFilterEntry": anueNtoStageGscToolFilterEntry,
       "anueNtoStageGscToolFilterType": anueNtoStageGscToolFilterType,
       "anueNtoStageGscToolFilterNumber": anueNtoStageGscToolFilterNumber,
       "anueNtoStageGscToolFilterFeature": anueNtoStageGscToolFilterFeature,
       "anueGscTFltrCurGtpV0ActSess": anueGscTFltrCurGtpV0ActSess,
       "anueGscTFltrCurGtpV1ActSess": anueGscTFltrCurGtpV1ActSess,
       "anueGscTFltrCurGtpV2ActSess": anueGscTFltrCurGtpV2ActSess,
       "anueGscTFltrCurGtpTotActSess": anueGscTFltrCurGtpTotActSess,
       "anueGscTFltrAvgGtpV0ActSess": anueGscTFltrAvgGtpV0ActSess,
       "anueGscTFltrAvgGtpV1ActSess": anueGscTFltrAvgGtpV1ActSess,
       "anueGscTFltrAvgGtpV2ActSess": anueGscTFltrAvgGtpV2ActSess,
       "anueGscTFltrAvgGtpTotActSess": anueGscTFltrAvgGtpTotActSess,
       "anueGscTFltrPeakGtpV0ActSess": anueGscTFltrPeakGtpV0ActSess,
       "anueGscTFltrPeakGtpV1ActSess": anueGscTFltrPeakGtpV1ActSess,
       "anueGscTFltrPeakGtpV2ActSess": anueGscTFltrPeakGtpV2ActSess,
       "anueGscTFltrPeakGtpTotActSess": anueGscTFltrPeakGtpTotActSess,
       "anueGscTFltrPeakGtpV0ActSessT": anueGscTFltrPeakGtpV0ActSessT,
       "anueGscTFltrPeakGtpV1ActSessT": anueGscTFltrPeakGtpV1ActSessT,
       "anueGscTFltrPeakGtpV2ActSessT": anueGscTFltrPeakGtpV2ActSessT,
       "anueGscTFltrPeakGtpTotActSessT": anueGscTFltrPeakGtpTotActSessT,
       "anueGscTFltrAvgGtpCPkts": anueGscTFltrAvgGtpCPkts,
       "anueGscTFltrAvgGtpUPkts": anueGscTFltrAvgGtpUPkts,
       "anueGscTFltrAvgDiameterPkts": anueGscTFltrAvgDiameterPkts,
       "anueGscTFltrAvgDnsPkts": anueGscTFltrAvgDnsPkts,
       "anueGscTFltrAvgRadiusPkts": anueGscTFltrAvgRadiusPkts,
       "anueGscTFltrPeakGtpCPkts": anueGscTFltrPeakGtpCPkts,
       "anueGscTFltrPeakGtpUPkts": anueGscTFltrPeakGtpUPkts,
       "anueGscTFltrPeakDiameterPkts": anueGscTFltrPeakDiameterPkts,
       "anueGscTFltrPeakDnsPkts": anueGscTFltrPeakDnsPkts,
       "anueGscTFltrPeakRadiusPkts": anueGscTFltrPeakRadiusPkts,
       "anueGscTFltrPeakGtpCPktsT": anueGscTFltrPeakGtpCPktsT,
       "anueGscTFltrPeakGtpUPktsT": anueGscTFltrPeakGtpUPktsT,
       "anueGscTFltrPeakDiameterPktsT": anueGscTFltrPeakDiameterPktsT,
       "anueGscTFltrPeakDnsPktsT": anueGscTFltrPeakDnsPktsT,
       "anueGscTFltrPeakRadiusPktsT": anueGscTFltrPeakRadiusPktsT,
       "anueGscTFltrTotGtpCPkts": anueGscTFltrTotGtpCPkts,
       "anueGscTFltrTotGtpUPkts": anueGscTFltrTotGtpUPkts,
       "anueGscTFltrTotDiameterPkts": anueGscTFltrTotDiameterPkts,
       "anueGscTFltrTotDnsPkts": anueGscTFltrTotDnsPkts,
       "anueGscTFltrTotRadiusPkts": anueGscTFltrTotRadiusPkts,
       "anueGscTFltrCurGtpCPkts": anueGscTFltrCurGtpCPkts,
       "anueGscTFltrCurGtpUPkts": anueGscTFltrCurGtpUPkts,
       "anueGscTFltrCurDiameterPkts": anueGscTFltrCurDiameterPkts,
       "anueGscTFltrCurDnsPkts": anueGscTFltrCurDnsPkts,
       "anueGscTFltrCurRadiusPkts": anueGscTFltrCurRadiusPkts,
       "anueNtoPayload": anueNtoPayload,
       "anueNtoEventMonData": anueNtoEventMonData,
       "anueNtoEventMonDataDateAndTime": anueNtoEventMonDataDateAndTime,
       "anueNtoEventMonDataTriggerCause": anueNtoEventMonDataTriggerCause,
       "anueNtoEventMonDataTriggerValue": anueNtoEventMonDataTriggerValue,
       "anueNtoEventMonDataDirection": anueNtoEventMonDataDirection,
       "anueNtoEventMonDataStatName": anueNtoEventMonDataStatName,
       "anueNtoEventMonDataEntityName": anueNtoEventMonDataEntityName,
       "anueNtoEventMonDataNotSent": anueNtoEventMonDataNotSent,
       "anueNtoEventMonDataTriggerDescr": anueNtoEventMonDataTriggerDescr,
       "anueNtoEventMonDataThreshold": anueNtoEventMonDataThreshold,
       "anueNtoEventMonDataInterval": anueNtoEventMonDataInterval,
       "anueNtoEventMonDataWindowSize": anueNtoEventMonDataWindowSize,
       "anueNtoEventMonDataWindowCount": anueNtoEventMonDataWindowCount,
       "anueNtoEventTestData": anueNtoEventTestData,
       "anueNtoEventTestTime": anueNtoEventTestTime,
       "anueNtoEventTestMessage": anueNtoEventTestMessage,
       "anueMemberActionData": anueMemberActionData,
       "anueMemberActionDataMemberName": anueMemberActionDataMemberName,
       "anueMemberActionDataType": anueMemberActionDataType,
       "anueNtoCapture": anueNtoCapture,
       "anueNtoCaptureTable": anueNtoCaptureTable,
       "anueNtoCaptureEntry": anueNtoCaptureEntry,
       "anueCaptureNumber": anueCaptureNumber,
       "anueCaptureDefaultName": anueCaptureDefaultName,
       "anueCaptureName": anueCaptureName,
       "anueCaptureDesc": anueCaptureDesc,
       "anueCaptureStatus": anueCaptureStatus,
       "anueCaptureBufferSize": anueCaptureBufferSize,
       "anueCaptureBufferType": anueCaptureBufferType,
       "anueCaptureTriggerMode": anueCaptureTriggerMode,
       "anueCaptureTriggerPosition": anueCaptureTriggerPosition,
       "anueCaptureFillBufferToTrigger": anueCaptureFillBufferToTrigger,
       "anueCaptureEnableTrailerStripping": anueCaptureEnableTrailerStripping,
       "anueCaptureTriggerCriteria": anueCaptureTriggerCriteria,
       "anueCaptureConnection": anueCaptureConnection,
       "anueNtoCaptureStatsTable": anueNtoCaptureStatsTable,
       "anueNtoCaptureStatsEntry": anueNtoCaptureStatsEntry,
       "anueCaptureTransBytesTotal": anueCaptureTransBytesTotal,
       "anueCaptureTransBytesCur": anueCaptureTransBytesCur,
       "anueCaptureTransBytesAvg": anueCaptureTransBytesAvg,
       "anueCaptureTransBytesPeak": anueCaptureTransBytesPeak,
       "anueCaptureTransBytesPeakTime": anueCaptureTransBytesPeakTime,
       "anueCaptureTransBytesTimeSincePeak": anueCaptureTransBytesTimeSincePeak,
       "anueCaptureTransPktsTotal": anueCaptureTransPktsTotal,
       "anueCaptureTransPktsCur": anueCaptureTransPktsCur,
       "anueCaptureTransPktsAvg": anueCaptureTransPktsAvg,
       "anueCaptureTransPktsPeak": anueCaptureTransPktsPeak,
       "anueCaptureTransPktsPeakTime": anueCaptureTransPktsPeakTime,
       "anueCaptureTransPktsTimeSincePeak": anueCaptureTransPktsTimeSincePeak,
       "anueCaptureDropPktsTotal": anueCaptureDropPktsTotal,
       "anueCaptureDropPktsCur": anueCaptureDropPktsCur,
       "anueCaptureDropPktsAvg": anueCaptureDropPktsAvg,
       "anueCaptureDropPktsPeak": anueCaptureDropPktsPeak,
       "anueCaptureDropPktsPeakTime": anueCaptureDropPktsPeakTime,
       "anueCaptureDropPktsTimeSincePeak": anueCaptureDropPktsTimeSincePeak,
       "anueCaptureBufferUtilizationPerc": anueCaptureBufferUtilizationPerc,
       "anueCaptureTimeSinceReset": anueCaptureTimeSinceReset,
       "anueCaptureResetById": anueCaptureResetById,
       "anueNtoResource": anueNtoResource,
       "anueNtoResourceTable": anueNtoResourceTable,
       "anueNtoResourceEntry": anueNtoResourceEntry,
       "anueResourceFilterType": anueResourceFilterType,
       "anueResourceNumber": anueResourceNumber,
       "anueResourceDefaultName": anueResourceDefaultName,
       "anueResourceName": anueResourceName,
       "anueResourceDesc": anueResourceDesc,
       "anueResourceStatus": anueResourceStatus,
       "anueGscObjects": anueGscObjects,
       "anueGscSystem": anueGscSystem,
       "anueGscLastCriticalFailure": anueGscLastCriticalFailure,
       "anueCriticalFailureDateAndTime": anueCriticalFailureDateAndTime,
       "anueCriticalFailureType": anueCriticalFailureType,
       "anueGscData": anueGscData,
       "anueGscPortProbeTable": anueGscPortProbeTable,
       "anueGscPortProbeEntry": anueGscPortProbeEntry,
       "anueGscPortIfIndex": anueGscPortIfIndex,
       "anueGscPortProbeId": anueGscPortProbeId,
       "anueGscProbeTable": anueGscProbeTable,
       "anueGscProbeEntry": anueGscProbeEntry,
       "anueGscProbeId": anueGscProbeId,
       "anueGscProbePgIfIndex": anueGscProbePgIfIndex,
       "anueGscProbeName": anueGscProbeName,
       "anueGscProbeIp": anueGscProbeIp,
       "anueGscProbeIsActive": anueGscProbeIsActive,
       "anueGscProbeIsRedundant": anueGscProbeIsRedundant,
       "anueGscProbeLastRxHeartbeatTime": anueGscProbeLastRxHeartbeatTime,
       "anueGscProbeLastRxFailMsgTime": anueGscProbeLastRxFailMsgTime,
       "anueGscProbeFailoverId": anueGscProbeFailoverId,
       "anueGscPayload": anueGscPayload,
       "anueGscEventFailedProbeData": anueGscEventFailedProbeData,
       "anueGscEvFailedPbDateAndTime": anueGscEvFailedPbDateAndTime,
       "anueGscEvFailedPbId": anueGscEvFailedPbId,
       "anueGscEvFailedPbName": anueGscEvFailedPbName,
       "anueGscEvFailedPbIP": anueGscEvFailedPbIP,
       "anueGscEvFailedPbPortList": anueGscEvFailedPbPortList,
       "anueGscEvFailedPbLastRxHeartbeat": anueGscEvFailedPbLastRxHeartbeat,
       "anueGscEvFailedPbLastRxFailMsg": anueGscEvFailedPbLastRxFailMsg,
       "anueGscEvFailoverPbId": anueGscEvFailoverPbId,
       "anueGscEvFailoverPbName": anueGscEvFailoverPbName,
       "anueGscEvFailoverPbIP": anueGscEvFailoverPbIP,
       "anueGscEvFailoverPbPortList": anueGscEvFailoverPbPortList,
       "anueEvents": anueEvents,
       "anueNtoEvents": anueNtoEvents,
       "anueSnmpAuthenticationFailure": anueSnmpAuthenticationFailure,
       "anueClientLoginFailure": anueClientLoginFailure,
       "anueNtoEventMonStatInvalidCount": anueNtoEventMonStatInvalidCount,
       "anueNtoEventMonStatDropCount": anueNtoEventMonStatDropCount,
       "anueNtoEventMonStatRxUtilization": anueNtoEventMonStatRxUtilization,
       "anueNtoEventMonStatTxUtilization": anueNtoEventMonStatTxUtilization,
       "anueNtoEventTest": anueNtoEventTest,
       "anueNtoEventUnionMemberAction": anueNtoEventUnionMemberAction,
       "anueNtoEventMonStatLoadDistribution": anueNtoEventMonStatLoadDistribution,
       "anueGscEvents": anueGscEvents,
       "anueGscEventMonStatOverflowPkts": anueGscEventMonStatOverflowPkts,
       "anueGscEventMonStatControlPlanePktRate": anueGscEventMonStatControlPlanePktRate,
       "anueGscEventMonStatExcessSessions": anueGscEventMonStatExcessSessions,
       "anueGscEventMonStatIngressPktDrops": anueGscEventMonStatIngressPktDrops,
       "anueGscEventMonStatSessionsTableLoad": anueGscEventMonStatSessionsTableLoad,
       "anueGscEventMonStatNetworkElemLoad": anueGscEventMonStatNetworkElemLoad,
       "anueGscEventMonStatReqRespLoad": anueGscEventMonStatReqRespLoad,
       "anueGscEventMonStatFragmentationLoad": anueGscEventMonStatFragmentationLoad,
       "anueGscCriticalFailure": anueGscCriticalFailure,
       "anueGscProbeFailure": anueGscProbeFailure,
       "anueConformance": anueConformance,
       "anueNtoConformance": anueNtoConformance,
       "anueGroups": anueGroups,
       "anueNtoGroups": anueNtoGroups,
       "anueNtoSystemGroup": anueNtoSystemGroup,
       "anueNtoIfExtGroup": anueNtoIfExtGroup,
       "anueNtoFilterGroup": anueNtoFilterGroup,
       "anueNtoPayloadGroup": anueNtoPayloadGroup,
       "anueNtoCaptureGroup": anueNtoCaptureGroup,
       "anueNtoCaptureStatsGroup": anueNtoCaptureStatsGroup,
       "anueNtoEventGroup": anueNtoEventGroup,
       "anueNtoStageGroup": anueNtoStageGroup,
       "anueNtoResourceGroup": anueNtoResourceGroup,
       "anueGscGroups": anueGscGroups,
       "anueGscEventGroup": anueGscEventGroup,
       "anueGscDataGroup": anueGscDataGroup,
       "anueGscPayloadGroup": anueGscPayloadGroup,
       "anueCompliances": anueCompliances,
       "anueMIBCompliances": anueMIBCompliances}
)
