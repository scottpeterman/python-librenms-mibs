# SNMP MIB module (CIENA-CES-DATAPLANE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-DATAPLANE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:32 2025
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

(cienaCesLogicalPortConfigPortName,
 cienaCesPortPgIdMappingNotifChassisIndex,
 cienaCesPortPgIdMappingNotifPortNumber,
 cienaCesPortPgIdMappingNotifShelfIndex,
 cienaCesPortPgIdMappingNotifSlotIndex) = mibBuilder.importSymbols(
    "CIENA-CES-PORT-MIB",
    "cienaCesLogicalPortConfigPortName",
    "cienaCesPortPgIdMappingNotifChassisIndex",
    "cienaCesPortPgIdMappingNotifPortNumber",
    "cienaCesPortPgIdMappingNotifShelfIndex",
    "cienaCesPortPgIdMappingNotifSlotIndex")

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesDataplaneMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7)
)
if mibBuilder.loadTexts:
    cienaCesDataplaneMIB.setRevisions(
        ("2017-06-07 00:00",
         "2017-04-11 00:00",
         "2016-03-06 00:00",
         "2015-11-03 00:00",
         "2015-10-27 00:00",
         "2015-10-10 00:00",
         "2015-09-22 00:00",
         "2015-08-21 00:00",
         "2015-06-25 00:00",
         "2015-05-08 00:00",
         "2014-08-28 00:00",
         "2014-06-03 00:00",
         "2014-04-14 00:00",
         "2014-02-07 00:00",
         "2013-09-13 00:00",
         "2013-09-04 00:00",
         "2013-08-12 00:00",
         "2013-08-07 00:00",
         "2013-08-06 00:00",
         "2013-07-26 00:00",
         "2013-07-25 00:00",
         "2011-01-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DpTsAttachType(TextualConvention, Integer32):
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("tunnelEncapPbt", 2),
          ("tunnelDecapPbt", 3),
          ("tunnelGroupPbt", 4),
          ("transitPbt", 5),
          ("tunnelEncapMpls", 6),
          ("tunnelDecapMpls", 7),
          ("tunnelGroupMpls", 8),
          ("transitMpls", 9),
          ("subPort", 10),
          ("qosFlow", 11),
          ("accessFlow", 12),
          ("servicePbt", 13),
          ("servicePbb", 14),
          ("vcMpls", 15),
          ("serviceMplsMesh", 16),
          ("cpuInterface", 17),
          ("cpuSubInterface", 18),
          ("ettp", 19),
          ("lspEncapMpls", 20),
          ("lspDecapMpls", 21),
          ("l3Interface", 22),
          ("l3Adjacency", 23),
          ("unknown", 99))
    )



class PrivateForwardGroupPolicy(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("talkToA", 1),
          ("talkToB", 2),
          ("talkToC", 3),
          ("talkToAB", 4),
          ("talkToAC", 5),
          ("talkToBC", 6),
          ("talkToABC", 7))
    )



class DpCouplingFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class DpIngressMeterPolicy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonhierarchical", 1),
          ("hierarchical", 2))
    )



class DpSchedulingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("mdrr", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesDpMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesDpMIBObjects = _CienaCesDpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1)
)
_CienaCesDpTsMeterFloodContainerNotifAttrs_ObjectIdentity = ObjectIdentity
cienaCesDpTsMeterFloodContainerNotifAttrs = _CienaCesDpTsMeterFloodContainerNotifAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1)
)
_CienaCesDpTsMeterFloodContainerProfileTable_Object = MibTable
cienaCesDpTsMeterFloodContainerProfileTable = _CienaCesDpTsMeterFloodContainerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileTable.setStatus("current")
_CienaCesDpTsMeterFloodContainerProfileEntry_Object = MibTableRow
cienaCesDpTsMeterFloodContainerProfileEntry = _CienaCesDpTsMeterFloodContainerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1)
)
cienaCesDpTsMeterFloodContainerProfileEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileEntry.setStatus("current")


class _CienaCesDpTsMeterFloodContainerProfileIndex_Type(Integer32):
    """Custom type cienaCesDpTsMeterFloodContainerProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsMeterFloodContainerProfileIndex_Type.__name__ = "Integer32"
_CienaCesDpTsMeterFloodContainerProfileIndex_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerProfileIndex = _CienaCesDpTsMeterFloodContainerProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1, 1),
    _CienaCesDpTsMeterFloodContainerProfileIndex_Type()
)
cienaCesDpTsMeterFloodContainerProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileIndex.setStatus("current")
_CienaCesDpTsMeterFloodContainerProfileName_Type = DisplayString
_CienaCesDpTsMeterFloodContainerProfileName_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerProfileName = _CienaCesDpTsMeterFloodContainerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1, 2),
    _CienaCesDpTsMeterFloodContainerProfileName_Type()
)
cienaCesDpTsMeterFloodContainerProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileName.setStatus("current")


class _CienaCesDpTsMeterFloodContainerNotifProfileIndex_Type(Integer32):
    """Custom type cienaCesDpTsMeterFloodContainerNotifProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsMeterFloodContainerNotifProfileIndex_Type.__name__ = "Integer32"
_CienaCesDpTsMeterFloodContainerNotifProfileIndex_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerNotifProfileIndex = _CienaCesDpTsMeterFloodContainerNotifProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1, 3),
    _CienaCesDpTsMeterFloodContainerNotifProfileIndex_Type()
)
cienaCesDpTsMeterFloodContainerNotifProfileIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerNotifProfileIndex.setStatus("current")
_CienaCesDpTsMeterFloodContainerProfileRate1_Type = Unsigned32
_CienaCesDpTsMeterFloodContainerProfileRate1_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerProfileRate1 = _CienaCesDpTsMeterFloodContainerProfileRate1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1, 4),
    _CienaCesDpTsMeterFloodContainerProfileRate1_Type()
)
cienaCesDpTsMeterFloodContainerProfileRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileRate1.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileRate1.setUnits("kilobits/sec")
_CienaCesDpTsMeterFloodContainerProfileRate2_Type = Unsigned32
_CienaCesDpTsMeterFloodContainerProfileRate2_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerProfileRate2 = _CienaCesDpTsMeterFloodContainerProfileRate2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1, 5),
    _CienaCesDpTsMeterFloodContainerProfileRate2_Type()
)
cienaCesDpTsMeterFloodContainerProfileRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileRate2.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileRate2.setUnits("kilobits/sec")
_CienaCesDpTsMeterFloodContainerProfileRate3_Type = Unsigned32
_CienaCesDpTsMeterFloodContainerProfileRate3_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerProfileRate3 = _CienaCesDpTsMeterFloodContainerProfileRate3_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1, 6),
    _CienaCesDpTsMeterFloodContainerProfileRate3_Type()
)
cienaCesDpTsMeterFloodContainerProfileRate3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileRate3.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileRate3.setUnits("kilobits/sec")


class _CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Type(Integer32):
    """Custom type cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId based on Integer32"""
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
        *(("noLimit", 1),
          ("rateId1", 2),
          ("rateId2", 3),
          ("rateId3", 4))
    )


_CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Type.__name__ = "Integer32"
_CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId = _CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1, 7),
    _CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Type()
)
cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId.setStatus("current")


class _CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Type(Integer32):
    """Custom type cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId based on Integer32"""
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
        *(("noLimit", 1),
          ("rateId1", 2),
          ("rateId2", 3),
          ("rateId3", 4))
    )


_CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Type.__name__ = "Integer32"
_CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId = _CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1, 8),
    _CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Type()
)
cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId.setStatus("current")


class _CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Type(Integer32):
    """Custom type cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId based on Integer32"""
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
        *(("noLimit", 1),
          ("rateId1", 2),
          ("rateId2", 3),
          ("rateId3", 4))
    )


_CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Type.__name__ = "Integer32"
_CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId = _CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 1, 1, 9),
    _CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Type()
)
cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentTable_Object = MibTable
cienaCesDpTsMeterFloodContainerAttachmentTable = _CienaCesDpTsMeterFloodContainerAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentTable.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentEntry_Object = MibTableRow
cienaCesDpTsMeterFloodContainerAttachmentEntry = _CienaCesDpTsMeterFloodContainerAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1)
)
cienaCesDpTsMeterFloodContainerAttachmentEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileIndex"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentLiType"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentLiIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentEntry.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentLiType_Type = DpTsAttachType
_CienaCesDpTsMeterFloodContainerAttachmentLiType_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentLiType = _CienaCesDpTsMeterFloodContainerAttachmentLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 1),
    _CienaCesDpTsMeterFloodContainerAttachmentLiType_Type()
)
cienaCesDpTsMeterFloodContainerAttachmentLiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentLiType.setStatus("current")


class _CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Type(Integer32):
    """Custom type cienaCesDpTsMeterFloodContainerAttachmentLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Type.__name__ = "Integer32"
_CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentLiIndex = _CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 2),
    _CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Type()
)
cienaCesDpTsMeterFloodContainerAttachmentLiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentLiIndex.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentInterfaceName_Type = DisplayString
_CienaCesDpTsMeterFloodContainerAttachmentInterfaceName_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentInterfaceName = _CienaCesDpTsMeterFloodContainerAttachmentInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 3),
    _CienaCesDpTsMeterFloodContainerAttachmentInterfaceName_Type()
)
cienaCesDpTsMeterFloodContainerAttachmentInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentInterfaceName.setStatus("current")
_CienaCesDpTsMeterFloodContainerNotifAttachmentLiType_Type = DpTsAttachType
_CienaCesDpTsMeterFloodContainerNotifAttachmentLiType_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerNotifAttachmentLiType = _CienaCesDpTsMeterFloodContainerNotifAttachmentLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 4),
    _CienaCesDpTsMeterFloodContainerNotifAttachmentLiType_Type()
)
cienaCesDpTsMeterFloodContainerNotifAttachmentLiType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerNotifAttachmentLiType.setStatus("current")
_CienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex_Type = Integer32
_CienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex = _CienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 5),
    _CienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex_Type()
)
cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentUcastRateState_Type = CienaGlobalState
_CienaCesDpTsMeterFloodContainerAttachmentUcastRateState_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentUcastRateState = _CienaCesDpTsMeterFloodContainerAttachmentUcastRateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 6),
    _CienaCesDpTsMeterFloodContainerAttachmentUcastRateState_Type()
)
cienaCesDpTsMeterFloodContainerAttachmentUcastRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentUcastRateState.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState_Type = CienaGlobalState
_CienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState = _CienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 7),
    _CienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState_Type()
)
cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentL2McastRateState_Type = CienaGlobalState
_CienaCesDpTsMeterFloodContainerAttachmentL2McastRateState_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState = _CienaCesDpTsMeterFloodContainerAttachmentL2McastRateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 8),
    _CienaCesDpTsMeterFloodContainerAttachmentL2McastRateState_Type()
)
cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth_Type = Unsigned32
_CienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth = _CienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 9),
    _CienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth_Type()
)
cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth_Type = Unsigned32
_CienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth = _CienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 10),
    _CienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth_Type()
)
cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth.setStatus("current")
_CienaCesDpTsMeterFloodContainerAttachmentTotalRateState_Type = CienaGlobalState
_CienaCesDpTsMeterFloodContainerAttachmentTotalRateState_Object = MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentTotalRateState = _CienaCesDpTsMeterFloodContainerAttachmentTotalRateState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 1, 2, 1, 11),
    _CienaCesDpTsMeterFloodContainerAttachmentTotalRateState_Type()
)
cienaCesDpTsMeterFloodContainerAttachmentTotalRateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerAttachmentTotalRateState.setStatus("current")
_CienaCesDpTsMeter_ObjectIdentity = ObjectIdentity
cienaCesDpTsMeter = _CienaCesDpTsMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2)
)
_CienaCesDpTsMeterProfile_ObjectIdentity = ObjectIdentity
cienaCesDpTsMeterProfile = _CienaCesDpTsMeterProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1)
)
_CienaCesDpTsMeterProfileTable_Object = MibTable
cienaCesDpTsMeterProfileTable = _CienaCesDpTsMeterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileTable.setStatus("current")
_CienaCesDpTsMeterProfileEntry_Object = MibTableRow
cienaCesDpTsMeterProfileEntry = _CienaCesDpTsMeterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1, 1)
)
cienaCesDpTsMeterProfileEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileEntry.setStatus("current")


class _CienaCesDpTsMeterProfileIndex_Type(Integer32):
    """Custom type cienaCesDpTsMeterProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsMeterProfileIndex_Type.__name__ = "Integer32"
_CienaCesDpTsMeterProfileIndex_Object = MibTableColumn
cienaCesDpTsMeterProfileIndex = _CienaCesDpTsMeterProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1, 1, 1),
    _CienaCesDpTsMeterProfileIndex_Type()
)
cienaCesDpTsMeterProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileIndex.setStatus("current")
_CienaCesDpTsMeterProfileName_Type = DisplayString
_CienaCesDpTsMeterProfileName_Object = MibTableColumn
cienaCesDpTsMeterProfileName = _CienaCesDpTsMeterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1, 1, 2),
    _CienaCesDpTsMeterProfileName_Type()
)
cienaCesDpTsMeterProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileName.setStatus("current")
_CienaCesDpTsMeterProfileCIR_Type = Unsigned32
_CienaCesDpTsMeterProfileCIR_Object = MibTableColumn
cienaCesDpTsMeterProfileCIR = _CienaCesDpTsMeterProfileCIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1, 1, 3),
    _CienaCesDpTsMeterProfileCIR_Type()
)
cienaCesDpTsMeterProfileCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileCIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileCIR.setUnits("kilobits/sec")
_CienaCesDpTsMeterProfileCBS_Type = Unsigned32
_CienaCesDpTsMeterProfileCBS_Object = MibTableColumn
cienaCesDpTsMeterProfileCBS = _CienaCesDpTsMeterProfileCBS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1, 1, 4),
    _CienaCesDpTsMeterProfileCBS_Type()
)
cienaCesDpTsMeterProfileCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileCBS.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileCBS.setUnits("kilobytes")
_CienaCesDpTsMeterProfileEIR_Type = Unsigned32
_CienaCesDpTsMeterProfileEIR_Object = MibTableColumn
cienaCesDpTsMeterProfileEIR = _CienaCesDpTsMeterProfileEIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1, 1, 5),
    _CienaCesDpTsMeterProfileEIR_Type()
)
cienaCesDpTsMeterProfileEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileEIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileEIR.setUnits("kilobits/sec")
_CienaCesDpTsMeterProfileEBS_Type = Unsigned32
_CienaCesDpTsMeterProfileEBS_Object = MibTableColumn
cienaCesDpTsMeterProfileEBS = _CienaCesDpTsMeterProfileEBS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1, 1, 6),
    _CienaCesDpTsMeterProfileEBS_Type()
)
cienaCesDpTsMeterProfileEBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileEBS.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileEBS.setUnits("kilobytes")


class _CienaCesDpTsMeterProfileColorMode_Type(Integer32):
    """Custom type cienaCesDpTsMeterProfileColorMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-mode-none", 0),
          ("color-blind", 1),
          ("color-aware", 2))
    )


_CienaCesDpTsMeterProfileColorMode_Type.__name__ = "Integer32"
_CienaCesDpTsMeterProfileColorMode_Object = MibTableColumn
cienaCesDpTsMeterProfileColorMode = _CienaCesDpTsMeterProfileColorMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1, 1, 7),
    _CienaCesDpTsMeterProfileColorMode_Type()
)
cienaCesDpTsMeterProfileColorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileColorMode.setStatus("current")


class _CienaCesDpTsMeterProfileCouplingFlag_Type(DpCouplingFlag):
    """Custom type cienaCesDpTsMeterProfileCouplingFlag based on DpCouplingFlag"""
    defaultValue = 0


_CienaCesDpTsMeterProfileCouplingFlag_Type.__name__ = "DpCouplingFlag"
_CienaCesDpTsMeterProfileCouplingFlag_Object = MibTableColumn
cienaCesDpTsMeterProfileCouplingFlag = _CienaCesDpTsMeterProfileCouplingFlag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 1, 1, 8),
    _CienaCesDpTsMeterProfileCouplingFlag_Type()
)
cienaCesDpTsMeterProfileCouplingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileCouplingFlag.setStatus("current")
_CienaCesDpTsMeterProfileAttachmentTable_Object = MibTable
cienaCesDpTsMeterProfileAttachmentTable = _CienaCesDpTsMeterProfileAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentTable.setStatus("current")
_CienaCesDpTsMeterProfileAttachmentEntry_Object = MibTableRow
cienaCesDpTsMeterProfileAttachmentEntry = _CienaCesDpTsMeterProfileAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 2, 1)
)
cienaCesDpTsMeterProfileAttachmentEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterProfileIndex"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterProfileAttachmentLiType"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterProfileAttachmentLiIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentEntry.setStatus("current")
_CienaCesDpTsMeterProfileAttachmentLiType_Type = DpTsAttachType
_CienaCesDpTsMeterProfileAttachmentLiType_Object = MibTableColumn
cienaCesDpTsMeterProfileAttachmentLiType = _CienaCesDpTsMeterProfileAttachmentLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 2, 1, 1),
    _CienaCesDpTsMeterProfileAttachmentLiType_Type()
)
cienaCesDpTsMeterProfileAttachmentLiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentLiType.setStatus("current")


class _CienaCesDpTsMeterProfileAttachmentLiIndex_Type(Integer32):
    """Custom type cienaCesDpTsMeterProfileAttachmentLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CienaCesDpTsMeterProfileAttachmentLiIndex_Type.__name__ = "Integer32"
_CienaCesDpTsMeterProfileAttachmentLiIndex_Object = MibTableColumn
cienaCesDpTsMeterProfileAttachmentLiIndex = _CienaCesDpTsMeterProfileAttachmentLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 2, 1, 2),
    _CienaCesDpTsMeterProfileAttachmentLiIndex_Type()
)
cienaCesDpTsMeterProfileAttachmentLiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentLiIndex.setStatus("current")
_CienaCesDpTsMeterProfileAttachmentTotalCIR_Type = Unsigned32
_CienaCesDpTsMeterProfileAttachmentTotalCIR_Object = MibTableColumn
cienaCesDpTsMeterProfileAttachmentTotalCIR = _CienaCesDpTsMeterProfileAttachmentTotalCIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 2, 1, 3),
    _CienaCesDpTsMeterProfileAttachmentTotalCIR_Type()
)
cienaCesDpTsMeterProfileAttachmentTotalCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentTotalCIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentTotalCIR.setUnits("kilobits/sec")
_CienaCesDpTsMeterProfileAttachmentTotalEIR_Type = Unsigned32
_CienaCesDpTsMeterProfileAttachmentTotalEIR_Object = MibTableColumn
cienaCesDpTsMeterProfileAttachmentTotalEIR = _CienaCesDpTsMeterProfileAttachmentTotalEIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 2, 1, 4),
    _CienaCesDpTsMeterProfileAttachmentTotalEIR_Type()
)
cienaCesDpTsMeterProfileAttachmentTotalEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentTotalEIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentTotalEIR.setUnits("kilobits/sec")
_CienaCesDpTsMeterProfileAttachmentUsedCIR_Type = Unsigned32
_CienaCesDpTsMeterProfileAttachmentUsedCIR_Object = MibTableColumn
cienaCesDpTsMeterProfileAttachmentUsedCIR = _CienaCesDpTsMeterProfileAttachmentUsedCIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 2, 1, 5),
    _CienaCesDpTsMeterProfileAttachmentUsedCIR_Type()
)
cienaCesDpTsMeterProfileAttachmentUsedCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentUsedCIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentUsedCIR.setUnits("kilobits/sec")
_CienaCesDpTsMeterProfileAttachmentMaxUsedEIR_Type = Unsigned32
_CienaCesDpTsMeterProfileAttachmentMaxUsedEIR_Object = MibTableColumn
cienaCesDpTsMeterProfileAttachmentMaxUsedEIR = _CienaCesDpTsMeterProfileAttachmentMaxUsedEIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 2, 1, 2, 1, 6),
    _CienaCesDpTsMeterProfileAttachmentMaxUsedEIR_Type()
)
cienaCesDpTsMeterProfileAttachmentMaxUsedEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentMaxUsedEIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsMeterProfileAttachmentMaxUsedEIR.setUnits("kilobits/sec")
_CienaCesDpTsCosMap_ObjectIdentity = ObjectIdentity
cienaCesDpTsCosMap = _CienaCesDpTsCosMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3)
)
_CienaCesDpTsCosMapRcos_ObjectIdentity = ObjectIdentity
cienaCesDpTsCosMapRcos = _CienaCesDpTsCosMapRcos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1)
)
_CienaCesDpTsCosMapRcosProfileTable_Object = MibTable
cienaCesDpTsCosMapRcosProfileTable = _CienaCesDpTsCosMapRcosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosProfileTable.setStatus("current")
_CienaCesDpTsCosMapRcosProfileEntry_Object = MibTableRow
cienaCesDpTsCosMapRcosProfileEntry = _CienaCesDpTsCosMapRcosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 1, 1)
)
cienaCesDpTsCosMapRcosProfileEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsCosMapRcosProfileId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosProfileEntry.setStatus("current")


class _CienaCesDpTsCosMapRcosProfileId_Type(Integer32):
    """Custom type cienaCesDpTsCosMapRcosProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsCosMapRcosProfileId_Type.__name__ = "Integer32"
_CienaCesDpTsCosMapRcosProfileId_Object = MibTableColumn
cienaCesDpTsCosMapRcosProfileId = _CienaCesDpTsCosMapRcosProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 1, 1, 1),
    _CienaCesDpTsCosMapRcosProfileId_Type()
)
cienaCesDpTsCosMapRcosProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosProfileId.setStatus("current")
_CienaCesDpTsCosMapRcosProfileName_Type = DisplayString
_CienaCesDpTsCosMapRcosProfileName_Object = MibTableColumn
cienaCesDpTsCosMapRcosProfileName = _CienaCesDpTsCosMapRcosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 1, 1, 2),
    _CienaCesDpTsCosMapRcosProfileName_Type()
)
cienaCesDpTsCosMapRcosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosProfileName.setStatus("current")
_CienaCesDpTsCosMapRcosFixedRCoSValue_Type = Integer32
_CienaCesDpTsCosMapRcosFixedRCoSValue_Object = MibTableColumn
cienaCesDpTsCosMapRcosFixedRCoSValue = _CienaCesDpTsCosMapRcosFixedRCoSValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 1, 1, 3),
    _CienaCesDpTsCosMapRcosFixedRCoSValue_Type()
)
cienaCesDpTsCosMapRcosFixedRCoSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosFixedRCoSValue.setStatus("current")


class _CienaCesDpTsCosMapRcosFixedRcolour_Type(Integer32):
    """Custom type cienaCesDpTsCosMapRcosFixedRcolour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_CienaCesDpTsCosMapRcosFixedRcolour_Type.__name__ = "Integer32"
_CienaCesDpTsCosMapRcosFixedRcolour_Object = MibTableColumn
cienaCesDpTsCosMapRcosFixedRcolour = _CienaCesDpTsCosMapRcosFixedRcolour_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 1, 1, 4),
    _CienaCesDpTsCosMapRcosFixedRcolour_Type()
)
cienaCesDpTsCosMapRcosFixedRcolour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosFixedRcolour.setStatus("current")


class _CienaCesDpTsCosMapRcosCosMapId_Type(Integer32):
    """Custom type cienaCesDpTsCosMapRcosCosMapId based on Integer32"""
    defaultValue = 0


_CienaCesDpTsCosMapRcosCosMapId_Type.__name__ = "Integer32"
_CienaCesDpTsCosMapRcosCosMapId_Object = MibTableColumn
cienaCesDpTsCosMapRcosCosMapId = _CienaCesDpTsCosMapRcosCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 1, 1, 5),
    _CienaCesDpTsCosMapRcosCosMapId_Type()
)
cienaCesDpTsCosMapRcosCosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosCosMapId.setStatus("current")
_CienaCesDpTsCosMapRcosCosMapName_Type = OctetString
_CienaCesDpTsCosMapRcosCosMapName_Object = MibTableColumn
cienaCesDpTsCosMapRcosCosMapName = _CienaCesDpTsCosMapRcosCosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 1, 1, 6),
    _CienaCesDpTsCosMapRcosCosMapName_Type()
)
cienaCesDpTsCosMapRcosCosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosCosMapName.setStatus("current")
_CienaCesDpTsCosMapRcosMapTable_Object = MibTable
cienaCesDpTsCosMapRcosMapTable = _CienaCesDpTsCosMapRcosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapTable.setStatus("current")
_CienaCesDpTsCosMapRcosMapEntry_Object = MibTableRow
cienaCesDpTsCosMapRcosMapEntry = _CienaCesDpTsCosMapRcosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2, 1)
)
cienaCesDpTsCosMapRcosMapEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsCosMapRcosMapId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapEntry.setStatus("current")


class _CienaCesDpTsCosMapRcosMapId_Type(Integer32):
    """Custom type cienaCesDpTsCosMapRcosMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsCosMapRcosMapId_Type.__name__ = "Integer32"
_CienaCesDpTsCosMapRcosMapId_Object = MibTableColumn
cienaCesDpTsCosMapRcosMapId = _CienaCesDpTsCosMapRcosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2, 1, 1),
    _CienaCesDpTsCosMapRcosMapId_Type()
)
cienaCesDpTsCosMapRcosMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapId.setStatus("current")
_CienaCesDpTsCosMapRcosMapName_Type = DisplayString
_CienaCesDpTsCosMapRcosMapName_Object = MibTableColumn
cienaCesDpTsCosMapRcosMapName = _CienaCesDpTsCosMapRcosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2, 1, 2),
    _CienaCesDpTsCosMapRcosMapName_Type()
)
cienaCesDpTsCosMapRcosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapName.setStatus("current")
_CienaCesDpTsCosMapRcosMapL2RCoS_Type = OctetString
_CienaCesDpTsCosMapRcosMapL2RCoS_Object = MibTableColumn
cienaCesDpTsCosMapRcosMapL2RCoS = _CienaCesDpTsCosMapRcosMapL2RCoS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2, 1, 3),
    _CienaCesDpTsCosMapRcosMapL2RCoS_Type()
)
cienaCesDpTsCosMapRcosMapL2RCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapL2RCoS.setStatus("current")
_CienaCesDpTsCosMapRcosMapL2RColour_Type = OctetString
_CienaCesDpTsCosMapRcosMapL2RColour_Object = MibTableColumn
cienaCesDpTsCosMapRcosMapL2RColour = _CienaCesDpTsCosMapRcosMapL2RColour_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2, 1, 4),
    _CienaCesDpTsCosMapRcosMapL2RColour_Type()
)
cienaCesDpTsCosMapRcosMapL2RColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapL2RColour.setStatus("current")
_CienaCesDpTsCosMapRcosMapL3DscpRCoS_Type = OctetString
_CienaCesDpTsCosMapRcosMapL3DscpRCoS_Object = MibTableColumn
cienaCesDpTsCosMapRcosMapL3DscpRCoS = _CienaCesDpTsCosMapRcosMapL3DscpRCoS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2, 1, 5),
    _CienaCesDpTsCosMapRcosMapL3DscpRCoS_Type()
)
cienaCesDpTsCosMapRcosMapL3DscpRCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapL3DscpRCoS.setStatus("current")
_CienaCesDpTsCosMapRcosMapL3DscpRColour_Type = OctetString
_CienaCesDpTsCosMapRcosMapL3DscpRColour_Object = MibTableColumn
cienaCesDpTsCosMapRcosMapL3DscpRColour = _CienaCesDpTsCosMapRcosMapL3DscpRColour_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2, 1, 6),
    _CienaCesDpTsCosMapRcosMapL3DscpRColour_Type()
)
cienaCesDpTsCosMapRcosMapL3DscpRColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapL3DscpRColour.setStatus("current")
_CienaCesDpTsCosMapRcosMapExpRCoS_Type = OctetString
_CienaCesDpTsCosMapRcosMapExpRCoS_Object = MibTableColumn
cienaCesDpTsCosMapRcosMapExpRCoS = _CienaCesDpTsCosMapRcosMapExpRCoS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2, 1, 7),
    _CienaCesDpTsCosMapRcosMapExpRCoS_Type()
)
cienaCesDpTsCosMapRcosMapExpRCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapExpRCoS.setStatus("current")
_CienaCesDpTsCosMapRcosMapExpRColour_Type = OctetString
_CienaCesDpTsCosMapRcosMapExpRColour_Object = MibTableColumn
cienaCesDpTsCosMapRcosMapExpRColour = _CienaCesDpTsCosMapRcosMapExpRColour_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 1, 2, 1, 8),
    _CienaCesDpTsCosMapRcosMapExpRColour_Type()
)
cienaCesDpTsCosMapRcosMapExpRColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapRcosMapExpRColour.setStatus("current")
_CienaCesDpTsCosMapFcos_ObjectIdentity = ObjectIdentity
cienaCesDpTsCosMapFcos = _CienaCesDpTsCosMapFcos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 2)
)
_CienaCesDpTsCosMapFcosMapTable_Object = MibTable
cienaCesDpTsCosMapFcosMapTable = _CienaCesDpTsCosMapFcosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapFcosMapTable.setStatus("current")
_CienaCesDpTsCosMapFcosMapEntry_Object = MibTableRow
cienaCesDpTsCosMapFcosMapEntry = _CienaCesDpTsCosMapFcosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 2, 1, 1)
)
cienaCesDpTsCosMapFcosMapEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsCosMapFcosMapId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapFcosMapEntry.setStatus("current")


class _CienaCesDpTsCosMapFcosMapId_Type(Integer32):
    """Custom type cienaCesDpTsCosMapFcosMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsCosMapFcosMapId_Type.__name__ = "Integer32"
_CienaCesDpTsCosMapFcosMapId_Object = MibTableColumn
cienaCesDpTsCosMapFcosMapId = _CienaCesDpTsCosMapFcosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 2, 1, 1, 1),
    _CienaCesDpTsCosMapFcosMapId_Type()
)
cienaCesDpTsCosMapFcosMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapFcosMapId.setStatus("current")
_CienaCesDpTsCosMapFcosMapName_Type = DisplayString
_CienaCesDpTsCosMapFcosMapName_Object = MibTableColumn
cienaCesDpTsCosMapFcosMapName = _CienaCesDpTsCosMapFcosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 2, 1, 1, 2),
    _CienaCesDpTsCosMapFcosMapName_Type()
)
cienaCesDpTsCosMapFcosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapFcosMapName.setStatus("current")
_CienaCesDpTsCosMapFcosL2CoS_Type = OctetString
_CienaCesDpTsCosMapFcosL2CoS_Object = MibTableColumn
cienaCesDpTsCosMapFcosL2CoS = _CienaCesDpTsCosMapFcosL2CoS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 2, 1, 1, 3),
    _CienaCesDpTsCosMapFcosL2CoS_Type()
)
cienaCesDpTsCosMapFcosL2CoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapFcosL2CoS.setStatus("current")
_CienaCesDpTsCosMapFcosL2Dei_Type = OctetString
_CienaCesDpTsCosMapFcosL2Dei_Object = MibTableColumn
cienaCesDpTsCosMapFcosL2Dei = _CienaCesDpTsCosMapFcosL2Dei_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 2, 1, 1, 4),
    _CienaCesDpTsCosMapFcosL2Dei_Type()
)
cienaCesDpTsCosMapFcosL2Dei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapFcosL2Dei.setStatus("current")
_CienaCesDpTsCosMapFcosL3Dscp_Type = OctetString
_CienaCesDpTsCosMapFcosL3Dscp_Object = MibTableColumn
cienaCesDpTsCosMapFcosL3Dscp = _CienaCesDpTsCosMapFcosL3Dscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 2, 1, 1, 5),
    _CienaCesDpTsCosMapFcosL3Dscp_Type()
)
cienaCesDpTsCosMapFcosL3Dscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapFcosL3Dscp.setStatus("current")
_CienaCesDpTsCosMapFcosExp_Type = OctetString
_CienaCesDpTsCosMapFcosExp_Object = MibTableColumn
cienaCesDpTsCosMapFcosExp = _CienaCesDpTsCosMapFcosExp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 3, 2, 1, 1, 6),
    _CienaCesDpTsCosMapFcosExp_Type()
)
cienaCesDpTsCosMapFcosExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsCosMapFcosExp.setStatus("current")
_CienaCesDpTsShaper_ObjectIdentity = ObjectIdentity
cienaCesDpTsShaper = _CienaCesDpTsShaper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4)
)
_CienaCesDpTsShaperProfile_ObjectIdentity = ObjectIdentity
cienaCesDpTsShaperProfile = _CienaCesDpTsShaperProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1)
)
_CienaCesDpTsShaperProfileTable_Object = MibTable
cienaCesDpTsShaperProfileTable = _CienaCesDpTsShaperProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileTable.setStatus("current")
_CienaCesDpTsShaperProfileEntry_Object = MibTableRow
cienaCesDpTsShaperProfileEntry = _CienaCesDpTsShaperProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 1, 1)
)
cienaCesDpTsShaperProfileEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsShaperProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileEntry.setStatus("current")


class _CienaCesDpTsShaperProfileIndex_Type(Integer32):
    """Custom type cienaCesDpTsShaperProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsShaperProfileIndex_Type.__name__ = "Integer32"
_CienaCesDpTsShaperProfileIndex_Object = MibTableColumn
cienaCesDpTsShaperProfileIndex = _CienaCesDpTsShaperProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 1, 1, 1),
    _CienaCesDpTsShaperProfileIndex_Type()
)
cienaCesDpTsShaperProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileIndex.setStatus("current")
_CienaCesDpTsShaperProfileName_Type = DisplayString
_CienaCesDpTsShaperProfileName_Object = MibTableColumn
cienaCesDpTsShaperProfileName = _CienaCesDpTsShaperProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 1, 1, 2),
    _CienaCesDpTsShaperProfileName_Type()
)
cienaCesDpTsShaperProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileName.setStatus("current")
_CienaCesDpTsShaperProfileCIR_Type = Unsigned32
_CienaCesDpTsShaperProfileCIR_Object = MibTableColumn
cienaCesDpTsShaperProfileCIR = _CienaCesDpTsShaperProfileCIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 1, 1, 3),
    _CienaCesDpTsShaperProfileCIR_Type()
)
cienaCesDpTsShaperProfileCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileCIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileCIR.setUnits("kilobits/sec")
_CienaCesDpTsShaperProfileCBS_Type = Unsigned32
_CienaCesDpTsShaperProfileCBS_Object = MibTableColumn
cienaCesDpTsShaperProfileCBS = _CienaCesDpTsShaperProfileCBS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 1, 1, 4),
    _CienaCesDpTsShaperProfileCBS_Type()
)
cienaCesDpTsShaperProfileCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileCBS.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileCBS.setUnits("kilobytes")
_CienaCesDpTsShaperProfileAttachmentTable_Object = MibTable
cienaCesDpTsShaperProfileAttachmentTable = _CienaCesDpTsShaperProfileAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentTable.setStatus("current")
_CienaCesDpTsShaperProfileAttachmentEntry_Object = MibTableRow
cienaCesDpTsShaperProfileAttachmentEntry = _CienaCesDpTsShaperProfileAttachmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 2, 1)
)
cienaCesDpTsShaperProfileAttachmentEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsShaperProfileIndex"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsShaperProfileAttachmentLiType"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsShaperProfileAttachmentLiIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentEntry.setStatus("current")
_CienaCesDpTsShaperProfileAttachmentLiType_Type = DpTsAttachType
_CienaCesDpTsShaperProfileAttachmentLiType_Object = MibTableColumn
cienaCesDpTsShaperProfileAttachmentLiType = _CienaCesDpTsShaperProfileAttachmentLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 2, 1, 1),
    _CienaCesDpTsShaperProfileAttachmentLiType_Type()
)
cienaCesDpTsShaperProfileAttachmentLiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentLiType.setStatus("current")


class _CienaCesDpTsShaperProfileAttachmentLiIndex_Type(Integer32):
    """Custom type cienaCesDpTsShaperProfileAttachmentLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CienaCesDpTsShaperProfileAttachmentLiIndex_Type.__name__ = "Integer32"
_CienaCesDpTsShaperProfileAttachmentLiIndex_Object = MibTableColumn
cienaCesDpTsShaperProfileAttachmentLiIndex = _CienaCesDpTsShaperProfileAttachmentLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 2, 1, 2),
    _CienaCesDpTsShaperProfileAttachmentLiIndex_Type()
)
cienaCesDpTsShaperProfileAttachmentLiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentLiIndex.setStatus("current")
_CienaCesDpTsShaperProfileAttachmentTotalCIR_Type = Unsigned32
_CienaCesDpTsShaperProfileAttachmentTotalCIR_Object = MibTableColumn
cienaCesDpTsShaperProfileAttachmentTotalCIR = _CienaCesDpTsShaperProfileAttachmentTotalCIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 2, 1, 3),
    _CienaCesDpTsShaperProfileAttachmentTotalCIR_Type()
)
cienaCesDpTsShaperProfileAttachmentTotalCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentTotalCIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentTotalCIR.setUnits("kilobits/sec")
_CienaCesDpTsShaperProfileAttachmentTotalEIR_Type = Unsigned32
_CienaCesDpTsShaperProfileAttachmentTotalEIR_Object = MibTableColumn
cienaCesDpTsShaperProfileAttachmentTotalEIR = _CienaCesDpTsShaperProfileAttachmentTotalEIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 2, 1, 4),
    _CienaCesDpTsShaperProfileAttachmentTotalEIR_Type()
)
cienaCesDpTsShaperProfileAttachmentTotalEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentTotalEIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentTotalEIR.setUnits("kilobits/sec")
_CienaCesDpTsShaperProfileAttachmentUsedCIR_Type = Unsigned32
_CienaCesDpTsShaperProfileAttachmentUsedCIR_Object = MibTableColumn
cienaCesDpTsShaperProfileAttachmentUsedCIR = _CienaCesDpTsShaperProfileAttachmentUsedCIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 2, 1, 5),
    _CienaCesDpTsShaperProfileAttachmentUsedCIR_Type()
)
cienaCesDpTsShaperProfileAttachmentUsedCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentUsedCIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentUsedCIR.setUnits("kilobits/sec")
_CienaCesDpTsShaperProfileAttachmentMaxUsedEIR_Type = Unsigned32
_CienaCesDpTsShaperProfileAttachmentMaxUsedEIR_Object = MibTableColumn
cienaCesDpTsShaperProfileAttachmentMaxUsedEIR = _CienaCesDpTsShaperProfileAttachmentMaxUsedEIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 4, 1, 2, 1, 6),
    _CienaCesDpTsShaperProfileAttachmentMaxUsedEIR_Type()
)
cienaCesDpTsShaperProfileAttachmentMaxUsedEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentMaxUsedEIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsShaperProfileAttachmentMaxUsedEIR.setUnits("kilobits/sec")
_CienaCesDpTsQ_ObjectIdentity = ObjectIdentity
cienaCesDpTsQ = _CienaCesDpTsQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5)
)
_CienaCesDpTsQCongestionAvoidanceProfile_ObjectIdentity = ObjectIdentity
cienaCesDpTsQCongestionAvoidanceProfile = _CienaCesDpTsQCongestionAvoidanceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1)
)
_CienaCesDpTsQCAProfileWREDTable_Object = MibTable
cienaCesDpTsQCAProfileWREDTable = _CienaCesDpTsQCAProfileWREDTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDTable.setStatus("current")
_CienaCesDpTsQCAProfileWREDEntry_Object = MibTableRow
cienaCesDpTsQCAProfileWREDEntry = _CienaCesDpTsQCAProfileWREDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 1, 1)
)
cienaCesDpTsQCAProfileWREDEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQCAProfileWREDId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDEntry.setStatus("current")


class _CienaCesDpTsQCAProfileWREDId_Type(Integer32):
    """Custom type cienaCesDpTsQCAProfileWREDId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsQCAProfileWREDId_Type.__name__ = "Integer32"
_CienaCesDpTsQCAProfileWREDId_Object = MibTableColumn
cienaCesDpTsQCAProfileWREDId = _CienaCesDpTsQCAProfileWREDId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 1, 1, 1),
    _CienaCesDpTsQCAProfileWREDId_Type()
)
cienaCesDpTsQCAProfileWREDId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDId.setStatus("current")
_CienaCesDpTsQCAProfileWREDName_Type = DisplayString
_CienaCesDpTsQCAProfileWREDName_Object = MibTableColumn
cienaCesDpTsQCAProfileWREDName = _CienaCesDpTsQCAProfileWREDName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 1, 1, 2),
    _CienaCesDpTsQCAProfileWREDName_Type()
)
cienaCesDpTsQCAProfileWREDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDName.setStatus("current")
_CienaCesDpTsQCAProfileWREDDropRateExponent_Type = Unsigned32
_CienaCesDpTsQCAProfileWREDDropRateExponent_Object = MibTableColumn
cienaCesDpTsQCAProfileWREDDropRateExponent = _CienaCesDpTsQCAProfileWREDDropRateExponent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 1, 1, 3),
    _CienaCesDpTsQCAProfileWREDDropRateExponent_Type()
)
cienaCesDpTsQCAProfileWREDDropRateExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDDropRateExponent.setStatus("current")
_CienaCesDpTsQCAProfileWREDMaxQueueSize_Type = Integer32
_CienaCesDpTsQCAProfileWREDMaxQueueSize_Object = MibTableColumn
cienaCesDpTsQCAProfileWREDMaxQueueSize = _CienaCesDpTsQCAProfileWREDMaxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 1, 1, 4),
    _CienaCesDpTsQCAProfileWREDMaxQueueSize_Type()
)
cienaCesDpTsQCAProfileWREDMaxQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDMaxQueueSize.setStatus("current")
_CienaCesDpTsQCAProfileWREDMinQueueGuarantee_Type = Integer32
_CienaCesDpTsQCAProfileWREDMinQueueGuarantee_Object = MibTableColumn
cienaCesDpTsQCAProfileWREDMinQueueGuarantee = _CienaCesDpTsQCAProfileWREDMinQueueGuarantee_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 1, 1, 5),
    _CienaCesDpTsQCAProfileWREDMinQueueGuarantee_Type()
)
cienaCesDpTsQCAProfileWREDMinQueueGuarantee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDMinQueueGuarantee.setStatus("current")
_CienaCesDpTsQCAProfileWREDCurveTable_Object = MibTable
cienaCesDpTsQCAProfileWREDCurveTable = _CienaCesDpTsQCAProfileWREDCurveTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDCurveTable.setStatus("current")
_CienaCesDpTsQCAProfileWREDCurveEntry_Object = MibTableRow
cienaCesDpTsQCAProfileWREDCurveEntry = _CienaCesDpTsQCAProfileWREDCurveEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 2, 1)
)
cienaCesDpTsQCAProfileWREDCurveEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQCAProfileWREDId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQCAProfileWREDCurveId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDCurveEntry.setStatus("current")


class _CienaCesDpTsQCAProfileWREDCurveId_Type(Integer32):
    """Custom type cienaCesDpTsQCAProfileWREDCurveId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CienaCesDpTsQCAProfileWREDCurveId_Type.__name__ = "Integer32"
_CienaCesDpTsQCAProfileWREDCurveId_Object = MibTableColumn
cienaCesDpTsQCAProfileWREDCurveId = _CienaCesDpTsQCAProfileWREDCurveId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 2, 1, 1),
    _CienaCesDpTsQCAProfileWREDCurveId_Type()
)
cienaCesDpTsQCAProfileWREDCurveId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDCurveId.setStatus("current")
_CienaCesDpTsQCAProfileWREDCurveLowerThreshold_Type = Unsigned32
_CienaCesDpTsQCAProfileWREDCurveLowerThreshold_Object = MibTableColumn
cienaCesDpTsQCAProfileWREDCurveLowerThreshold = _CienaCesDpTsQCAProfileWREDCurveLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 2, 1, 2),
    _CienaCesDpTsQCAProfileWREDCurveLowerThreshold_Type()
)
cienaCesDpTsQCAProfileWREDCurveLowerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDCurveLowerThreshold.setStatus("current")
_CienaCesDpTsQCAProfileWREDCurveUpperThreshold_Type = Unsigned32
_CienaCesDpTsQCAProfileWREDCurveUpperThreshold_Object = MibTableColumn
cienaCesDpTsQCAProfileWREDCurveUpperThreshold = _CienaCesDpTsQCAProfileWREDCurveUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 2, 1, 3),
    _CienaCesDpTsQCAProfileWREDCurveUpperThreshold_Type()
)
cienaCesDpTsQCAProfileWREDCurveUpperThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDCurveUpperThreshold.setStatus("current")
_CienaCesDpTsQCAProfileWREDCurveMaxDropProbability_Type = Unsigned32
_CienaCesDpTsQCAProfileWREDCurveMaxDropProbability_Object = MibTableColumn
cienaCesDpTsQCAProfileWREDCurveMaxDropProbability = _CienaCesDpTsQCAProfileWREDCurveMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 1, 2, 1, 4),
    _CienaCesDpTsQCAProfileWREDCurveMaxDropProbability_Type()
)
cienaCesDpTsQCAProfileWREDCurveMaxDropProbability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQCAProfileWREDCurveMaxDropProbability.setStatus("current")
_CienaCesDpTsQRCOSQMap_ObjectIdentity = ObjectIdentity
cienaCesDpTsQRCOSQMap = _CienaCesDpTsQRCOSQMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2)
)
_CienaCesDpTsQRCOSQMapTable_Object = MibTable
cienaCesDpTsQRCOSQMapTable = _CienaCesDpTsQRCOSQMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapTable.setStatus("current")
_CienaCesDpTsQRCOSQMapEntry_Object = MibTableRow
cienaCesDpTsQRCOSQMapEntry = _CienaCesDpTsQRCOSQMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 1, 1)
)
cienaCesDpTsQRCOSQMapEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQRCOSQMapId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapEntry.setStatus("current")


class _CienaCesDpTsQRCOSQMapId_Type(Integer32):
    """Custom type cienaCesDpTsQRCOSQMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsQRCOSQMapId_Type.__name__ = "Integer32"
_CienaCesDpTsQRCOSQMapId_Object = MibTableColumn
cienaCesDpTsQRCOSQMapId = _CienaCesDpTsQRCOSQMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 1, 1, 1),
    _CienaCesDpTsQRCOSQMapId_Type()
)
cienaCesDpTsQRCOSQMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapId.setStatus("current")
_CienaCesDpTsQRCOSQMapName_Type = DisplayString
_CienaCesDpTsQRCOSQMapName_Object = MibTableColumn
cienaCesDpTsQRCOSQMapName = _CienaCesDpTsQRCOSQMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 1, 1, 2),
    _CienaCesDpTsQRCOSQMapName_Type()
)
cienaCesDpTsQRCOSQMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapName.setStatus("current")
_CienaCesDpTsQRCOSQMapQueueTable_Object = MibTable
cienaCesDpTsQRCOSQMapQueueTable = _CienaCesDpTsQRCOSQMapQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapQueueTable.setStatus("current")
_CienaCesDpTsQRCOSQMapQueueEntry_Object = MibTableRow
cienaCesDpTsQRCOSQMapQueueEntry = _CienaCesDpTsQRCOSQMapQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 2, 1)
)
cienaCesDpTsQRCOSQMapQueueEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQRCOSQMapId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQRCOSQMapQueueId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapQueueEntry.setStatus("current")


class _CienaCesDpTsQRCOSQMapQueueId_Type(Integer32):
    """Custom type cienaCesDpTsQRCOSQMapQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsQRCOSQMapQueueId_Type.__name__ = "Integer32"
_CienaCesDpTsQRCOSQMapQueueId_Object = MibTableColumn
cienaCesDpTsQRCOSQMapQueueId = _CienaCesDpTsQRCOSQMapQueueId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 2, 1, 1),
    _CienaCesDpTsQRCOSQMapQueueId_Type()
)
cienaCesDpTsQRCOSQMapQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapQueueId.setStatus("current")


class _CienaCesDpTsQRCOSQMapQueueNumber_Type(Integer32):
    """Custom type cienaCesDpTsQRCOSQMapQueueNumber based on Integer32"""
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
        *(("queue-0", 0),
          ("queue-1", 1),
          ("queue-2", 2),
          ("queue-3", 3),
          ("queue-4", 4),
          ("queue-5", 5),
          ("queue-6", 6),
          ("queue-7", 7))
    )


_CienaCesDpTsQRCOSQMapQueueNumber_Type.__name__ = "Integer32"
_CienaCesDpTsQRCOSQMapQueueNumber_Object = MibTableColumn
cienaCesDpTsQRCOSQMapQueueNumber = _CienaCesDpTsQRCOSQMapQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 2, 1, 2),
    _CienaCesDpTsQRCOSQMapQueueNumber_Type()
)
cienaCesDpTsQRCOSQMapQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapQueueNumber.setStatus("current")
_CienaCesDpTsQRCOSQMapGreenCurveTable_Object = MibTable
cienaCesDpTsQRCOSQMapGreenCurveTable = _CienaCesDpTsQRCOSQMapGreenCurveTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapGreenCurveTable.setStatus("current")
_CienaCesDpTsQRCOSQMapGreenCurveEntry_Object = MibTableRow
cienaCesDpTsQRCOSQMapGreenCurveEntry = _CienaCesDpTsQRCOSQMapGreenCurveEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 3, 1)
)
cienaCesDpTsQRCOSQMapGreenCurveEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQRCOSQMapId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQRCOSQMapGreenCurveId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapGreenCurveEntry.setStatus("current")


class _CienaCesDpTsQRCOSQMapGreenCurveId_Type(Integer32):
    """Custom type cienaCesDpTsQRCOSQMapGreenCurveId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CienaCesDpTsQRCOSQMapGreenCurveId_Type.__name__ = "Integer32"
_CienaCesDpTsQRCOSQMapGreenCurveId_Object = MibTableColumn
cienaCesDpTsQRCOSQMapGreenCurveId = _CienaCesDpTsQRCOSQMapGreenCurveId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 3, 1, 1),
    _CienaCesDpTsQRCOSQMapGreenCurveId_Type()
)
cienaCesDpTsQRCOSQMapGreenCurveId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapGreenCurveId.setStatus("current")


class _CienaCesDpTsQRCOSQMapGreenCurveNumber_Type(Integer32):
    """Custom type cienaCesDpTsQRCOSQMapGreenCurveNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wred-curve-1", 1),
          ("wred-curve-2", 2))
    )


_CienaCesDpTsQRCOSQMapGreenCurveNumber_Type.__name__ = "Integer32"
_CienaCesDpTsQRCOSQMapGreenCurveNumber_Object = MibTableColumn
cienaCesDpTsQRCOSQMapGreenCurveNumber = _CienaCesDpTsQRCOSQMapGreenCurveNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 3, 1, 2),
    _CienaCesDpTsQRCOSQMapGreenCurveNumber_Type()
)
cienaCesDpTsQRCOSQMapGreenCurveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapGreenCurveNumber.setStatus("current")
_CienaCesDpTsQRCOSQMapYellowCurveTable_Object = MibTable
cienaCesDpTsQRCOSQMapYellowCurveTable = _CienaCesDpTsQRCOSQMapYellowCurveTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapYellowCurveTable.setStatus("current")
_CienaCesDpTsQRCOSQMapYellowCurveEntry_Object = MibTableRow
cienaCesDpTsQRCOSQMapYellowCurveEntry = _CienaCesDpTsQRCOSQMapYellowCurveEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 4, 1)
)
cienaCesDpTsQRCOSQMapYellowCurveEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQRCOSQMapId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQRCOSQMapYellowCurveId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapYellowCurveEntry.setStatus("current")


class _CienaCesDpTsQRCOSQMapYellowCurveId_Type(Integer32):
    """Custom type cienaCesDpTsQRCOSQMapYellowCurveId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CienaCesDpTsQRCOSQMapYellowCurveId_Type.__name__ = "Integer32"
_CienaCesDpTsQRCOSQMapYellowCurveId_Object = MibTableColumn
cienaCesDpTsQRCOSQMapYellowCurveId = _CienaCesDpTsQRCOSQMapYellowCurveId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 4, 1, 1),
    _CienaCesDpTsQRCOSQMapYellowCurveId_Type()
)
cienaCesDpTsQRCOSQMapYellowCurveId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapYellowCurveId.setStatus("current")


class _CienaCesDpTsQRCOSQMapYellowCurveNumber_Type(Integer32):
    """Custom type cienaCesDpTsQRCOSQMapYellowCurveNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wred-curve-1", 1),
          ("wred-curve-2", 2))
    )


_CienaCesDpTsQRCOSQMapYellowCurveNumber_Type.__name__ = "Integer32"
_CienaCesDpTsQRCOSQMapYellowCurveNumber_Object = MibTableColumn
cienaCesDpTsQRCOSQMapYellowCurveNumber = _CienaCesDpTsQRCOSQMapYellowCurveNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 2, 4, 1, 2),
    _CienaCesDpTsQRCOSQMapYellowCurveNumber_Type()
)
cienaCesDpTsQRCOSQMapYellowCurveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQRCOSQMapYellowCurveNumber.setStatus("current")
_CienaCesDpTsQGroupProfile_ObjectIdentity = ObjectIdentity
cienaCesDpTsQGroupProfile = _CienaCesDpTsQGroupProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3)
)
_CienaCesDpTsQGroupProfileTable_Object = MibTable
cienaCesDpTsQGroupProfileTable = _CienaCesDpTsQGroupProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileTable.setStatus("current")
_CienaCesDpTsQGroupProfileEntry_Object = MibTableRow
cienaCesDpTsQGroupProfileEntry = _CienaCesDpTsQGroupProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 1, 1)
)
cienaCesDpTsQGroupProfileEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQGroupProfileId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileEntry.setStatus("current")


class _CienaCesDpTsQGroupProfileId_Type(Integer32):
    """Custom type cienaCesDpTsQGroupProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsQGroupProfileId_Type.__name__ = "Integer32"
_CienaCesDpTsQGroupProfileId_Object = MibTableColumn
cienaCesDpTsQGroupProfileId = _CienaCesDpTsQGroupProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 1, 1, 1),
    _CienaCesDpTsQGroupProfileId_Type()
)
cienaCesDpTsQGroupProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileId.setStatus("current")
_CienaCesDpTsQGroupProfileName_Type = DisplayString
_CienaCesDpTsQGroupProfileName_Object = MibTableColumn
cienaCesDpTsQGroupProfileName = _CienaCesDpTsQGroupProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 1, 1, 2),
    _CienaCesDpTsQGroupProfileName_Type()
)
cienaCesDpTsQGroupProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileName.setStatus("current")
_CienaCesDpTsQGroupProfileQueueCount_Type = Integer32
_CienaCesDpTsQGroupProfileQueueCount_Object = MibTableColumn
cienaCesDpTsQGroupProfileQueueCount = _CienaCesDpTsQGroupProfileQueueCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 1, 1, 3),
    _CienaCesDpTsQGroupProfileQueueCount_Type()
)
cienaCesDpTsQGroupProfileQueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueCount.setStatus("current")
_CienaCesDpTsQGroupProfileRCOSQMapId_Type = Unsigned32
_CienaCesDpTsQGroupProfileRCOSQMapId_Object = MibTableColumn
cienaCesDpTsQGroupProfileRCOSQMapId = _CienaCesDpTsQGroupProfileRCOSQMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 1, 1, 4),
    _CienaCesDpTsQGroupProfileRCOSQMapId_Type()
)
cienaCesDpTsQGroupProfileRCOSQMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileRCOSQMapId.setStatus("current")
_CienaCesDpTsQGroupProfileShaperCompensation_Type = Integer32
_CienaCesDpTsQGroupProfileShaperCompensation_Object = MibTableColumn
cienaCesDpTsQGroupProfileShaperCompensation = _CienaCesDpTsQGroupProfileShaperCompensation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 1, 1, 5),
    _CienaCesDpTsQGroupProfileShaperCompensation_Type()
)
cienaCesDpTsQGroupProfileShaperCompensation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileShaperCompensation.setStatus("current")
_CienaCesDpTsQGroupProfileQueueTable_Object = MibTable
cienaCesDpTsQGroupProfileQueueTable = _CienaCesDpTsQGroupProfileQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueTable.setStatus("current")
_CienaCesDpTsQGroupProfileQueueEntry_Object = MibTableRow
cienaCesDpTsQGroupProfileQueueEntry = _CienaCesDpTsQGroupProfileQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2, 1)
)
cienaCesDpTsQGroupProfileQueueEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQGroupProfileId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQGroupProfileQueueIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueEntry.setStatus("current")


class _CienaCesDpTsQGroupProfileQueueIndex_Type(Integer32):
    """Custom type cienaCesDpTsQGroupProfileQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsQGroupProfileQueueIndex_Type.__name__ = "Integer32"
_CienaCesDpTsQGroupProfileQueueIndex_Object = MibTableColumn
cienaCesDpTsQGroupProfileQueueIndex = _CienaCesDpTsQGroupProfileQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2, 1, 1),
    _CienaCesDpTsQGroupProfileQueueIndex_Type()
)
cienaCesDpTsQGroupProfileQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueIndex.setStatus("current")
_CienaCesDpTsQGroupProfileQueueCAPId_Type = Unsigned32
_CienaCesDpTsQGroupProfileQueueCAPId_Object = MibTableColumn
cienaCesDpTsQGroupProfileQueueCAPId = _CienaCesDpTsQGroupProfileQueueCAPId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2, 1, 2),
    _CienaCesDpTsQGroupProfileQueueCAPId_Type()
)
cienaCesDpTsQGroupProfileQueueCAPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueCAPId.setStatus("current")
_CienaCesDpTsQGroupProfileQueueCIR_Type = Unsigned32
_CienaCesDpTsQGroupProfileQueueCIR_Object = MibTableColumn
cienaCesDpTsQGroupProfileQueueCIR = _CienaCesDpTsQGroupProfileQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2, 1, 3),
    _CienaCesDpTsQGroupProfileQueueCIR_Type()
)
cienaCesDpTsQGroupProfileQueueCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueCIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueCIR.setUnits("kilobits/sec")
_CienaCesDpTsQGroupProfileQueueCBS_Type = Unsigned32
_CienaCesDpTsQGroupProfileQueueCBS_Object = MibTableColumn
cienaCesDpTsQGroupProfileQueueCBS = _CienaCesDpTsQGroupProfileQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2, 1, 4),
    _CienaCesDpTsQGroupProfileQueueCBS_Type()
)
cienaCesDpTsQGroupProfileQueueCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueCBS.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueCBS.setUnits("kilobytes")
_CienaCesDpTsQGroupProfileQueueEIR_Type = Unsigned32
_CienaCesDpTsQGroupProfileQueueEIR_Object = MibTableColumn
cienaCesDpTsQGroupProfileQueueEIR = _CienaCesDpTsQGroupProfileQueueEIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2, 1, 5),
    _CienaCesDpTsQGroupProfileQueueEIR_Type()
)
cienaCesDpTsQGroupProfileQueueEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueEIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueEIR.setUnits("kilobits/sec")
_CienaCesDpTsQGroupProfileQueueEBS_Type = Unsigned32
_CienaCesDpTsQGroupProfileQueueEBS_Object = MibTableColumn
cienaCesDpTsQGroupProfileQueueEBS = _CienaCesDpTsQGroupProfileQueueEBS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2, 1, 6),
    _CienaCesDpTsQGroupProfileQueueEBS_Type()
)
cienaCesDpTsQGroupProfileQueueEBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueEBS.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueEBS.setUnits("kilobytes")
_CienaCesDpTsQGroupProfileQueueCirPercent_Type = Unsigned32
_CienaCesDpTsQGroupProfileQueueCirPercent_Object = MibTableColumn
cienaCesDpTsQGroupProfileQueueCirPercent = _CienaCesDpTsQGroupProfileQueueCirPercent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2, 1, 7),
    _CienaCesDpTsQGroupProfileQueueCirPercent_Type()
)
cienaCesDpTsQGroupProfileQueueCirPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueCirPercent.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueCirPercent.setUnits("percent")
_CienaCesDpTsQGroupProfileQueueEirPercent_Type = Unsigned32
_CienaCesDpTsQGroupProfileQueueEirPercent_Object = MibTableColumn
cienaCesDpTsQGroupProfileQueueEirPercent = _CienaCesDpTsQGroupProfileQueueEirPercent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 3, 2, 1, 8),
    _CienaCesDpTsQGroupProfileQueueEirPercent_Type()
)
cienaCesDpTsQGroupProfileQueueEirPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueEirPercent.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupProfileQueueEirPercent.setUnits("percent")
_CienaCesDpTsQGroupInstance_ObjectIdentity = ObjectIdentity
cienaCesDpTsQGroupInstance = _CienaCesDpTsQGroupInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 4)
)
_CienaCesDpTsQGroupInstanceTable_Object = MibTable
cienaCesDpTsQGroupInstanceTable = _CienaCesDpTsQGroupInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupInstanceTable.setStatus("current")
_CienaCesDpTsQGroupInstanceEntry_Object = MibTableRow
cienaCesDpTsQGroupInstanceEntry = _CienaCesDpTsQGroupInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 4, 1, 1)
)
cienaCesDpTsQGroupInstanceEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQGroupInstancePgid"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQGroupProfileId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQGroupInstanceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupInstanceEntry.setStatus("current")
_CienaCesDpTsQGroupInstancePgid_Type = Unsigned32
_CienaCesDpTsQGroupInstancePgid_Object = MibTableColumn
cienaCesDpTsQGroupInstancePgid = _CienaCesDpTsQGroupInstancePgid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 4, 1, 1, 1),
    _CienaCesDpTsQGroupInstancePgid_Type()
)
cienaCesDpTsQGroupInstancePgid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupInstancePgid.setStatus("current")


class _CienaCesDpTsQGroupInstanceIndex_Type(Integer32):
    """Custom type cienaCesDpTsQGroupInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsQGroupInstanceIndex_Type.__name__ = "Integer32"
_CienaCesDpTsQGroupInstanceIndex_Object = MibTableColumn
cienaCesDpTsQGroupInstanceIndex = _CienaCesDpTsQGroupInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 4, 1, 1, 2),
    _CienaCesDpTsQGroupInstanceIndex_Type()
)
cienaCesDpTsQGroupInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupInstanceIndex.setStatus("current")
_CienaCesDpTsQGroupInstanceParentSchedId_Type = Integer32
_CienaCesDpTsQGroupInstanceParentSchedId_Object = MibTableColumn
cienaCesDpTsQGroupInstanceParentSchedId = _CienaCesDpTsQGroupInstanceParentSchedId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 4, 1, 1, 3),
    _CienaCesDpTsQGroupInstanceParentSchedId_Type()
)
cienaCesDpTsQGroupInstanceParentSchedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupInstanceParentSchedId.setStatus("current")
_CienaCesDpTsQGroupInstanceParentInstanceId_Type = Integer32
_CienaCesDpTsQGroupInstanceParentInstanceId_Object = MibTableColumn
cienaCesDpTsQGroupInstanceParentInstanceId = _CienaCesDpTsQGroupInstanceParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 4, 1, 1, 4),
    _CienaCesDpTsQGroupInstanceParentInstanceId_Type()
)
cienaCesDpTsQGroupInstanceParentInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQGroupInstanceParentInstanceId.setStatus("current")
_CienaCesDpTsQSchedulerProfile_ObjectIdentity = ObjectIdentity
cienaCesDpTsQSchedulerProfile = _CienaCesDpTsQSchedulerProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5)
)
_CienaCesDpTsQSchedulerProfileTable_Object = MibTable
cienaCesDpTsQSchedulerProfileTable = _CienaCesDpTsQSchedulerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileTable.setStatus("current")
_CienaCesDpTsQSchedulerProfileEntry_Object = MibTableRow
cienaCesDpTsQSchedulerProfileEntry = _CienaCesDpTsQSchedulerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1)
)
cienaCesDpTsQSchedulerProfileEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQSchedulerProfileId"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileEntry.setStatus("current")


class _CienaCesDpTsQSchedulerProfileId_Type(Integer32):
    """Custom type cienaCesDpTsQSchedulerProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsQSchedulerProfileId_Type.__name__ = "Integer32"
_CienaCesDpTsQSchedulerProfileId_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileId = _CienaCesDpTsQSchedulerProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 1),
    _CienaCesDpTsQSchedulerProfileId_Type()
)
cienaCesDpTsQSchedulerProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileId.setStatus("current")
_CienaCesDpTsQSchedulerProfileName_Type = DisplayString
_CienaCesDpTsQSchedulerProfileName_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileName = _CienaCesDpTsQSchedulerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 2),
    _CienaCesDpTsQSchedulerProfileName_Type()
)
cienaCesDpTsQSchedulerProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileName.setStatus("current")


class _CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Type(Integer32):
    """Custom type cienaCesDpTsQSchedulerProfileSchedulerAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("strictPriority", 1),
          ("weightedFairQueuing", 2),
          ("roundRobin", 3))
    )


_CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Type.__name__ = "Integer32"
_CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileSchedulerAlgorithm = _CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 3),
    _CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Type()
)
cienaCesDpTsQSchedulerProfileSchedulerAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileSchedulerAlgorithm.setStatus("current")
_CienaCesDpTsQSchedulerProfileCIR_Type = Unsigned32
_CienaCesDpTsQSchedulerProfileCIR_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileCIR = _CienaCesDpTsQSchedulerProfileCIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 4),
    _CienaCesDpTsQSchedulerProfileCIR_Type()
)
cienaCesDpTsQSchedulerProfileCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileCIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileCIR.setUnits("kilobits/sec")
_CienaCesDpTsQSchedulerProfileCBS_Type = Unsigned32
_CienaCesDpTsQSchedulerProfileCBS_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileCBS = _CienaCesDpTsQSchedulerProfileCBS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 5),
    _CienaCesDpTsQSchedulerProfileCBS_Type()
)
cienaCesDpTsQSchedulerProfileCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileCBS.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileCBS.setUnits("kilobytes")
_CienaCesDpTsQSchedulerProfileEIR_Type = Unsigned32
_CienaCesDpTsQSchedulerProfileEIR_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileEIR = _CienaCesDpTsQSchedulerProfileEIR_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 6),
    _CienaCesDpTsQSchedulerProfileEIR_Type()
)
cienaCesDpTsQSchedulerProfileEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileEIR.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileEIR.setUnits("kilobits/sec")


class _CienaCesDpTsQSchedulerProfileEBS_Type(Unsigned32):
    """Custom type cienaCesDpTsQSchedulerProfileEBS based on Unsigned32"""
    defaultValue = 32


_CienaCesDpTsQSchedulerProfileEBS_Type.__name__ = "Unsigned32"
_CienaCesDpTsQSchedulerProfileEBS_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileEBS = _CienaCesDpTsQSchedulerProfileEBS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 7),
    _CienaCesDpTsQSchedulerProfileEBS_Type()
)
cienaCesDpTsQSchedulerProfileEBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileEBS.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileEBS.setUnits("kilobytes")


class _CienaCesDpTsQSchedulerProfileScheduledUcastWt_Type(Integer32):
    """Custom type cienaCesDpTsQSchedulerProfileScheduledUcastWt based on Integer32"""
    defaultValue = 80


_CienaCesDpTsQSchedulerProfileScheduledUcastWt_Type.__name__ = "Integer32"
_CienaCesDpTsQSchedulerProfileScheduledUcastWt_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileScheduledUcastWt = _CienaCesDpTsQSchedulerProfileScheduledUcastWt_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 8),
    _CienaCesDpTsQSchedulerProfileScheduledUcastWt_Type()
)
cienaCesDpTsQSchedulerProfileScheduledUcastWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileScheduledUcastWt.setStatus("current")


class _CienaCesDpTsQSchedulerProfileScheduledMcastWt_Type(Integer32):
    """Custom type cienaCesDpTsQSchedulerProfileScheduledMcastWt based on Integer32"""
    defaultValue = 20


_CienaCesDpTsQSchedulerProfileScheduledMcastWt_Type.__name__ = "Integer32"
_CienaCesDpTsQSchedulerProfileScheduledMcastWt_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileScheduledMcastWt = _CienaCesDpTsQSchedulerProfileScheduledMcastWt_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 9),
    _CienaCesDpTsQSchedulerProfileScheduledMcastWt_Type()
)
cienaCesDpTsQSchedulerProfileScheduledMcastWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileScheduledMcastWt.setStatus("current")
_CienaCesDpTsQSchedulerProfileTapPointCount_Type = Integer32
_CienaCesDpTsQSchedulerProfileTapPointCount_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileTapPointCount = _CienaCesDpTsQSchedulerProfileTapPointCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 10),
    _CienaCesDpTsQSchedulerProfileTapPointCount_Type()
)
cienaCesDpTsQSchedulerProfileTapPointCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileTapPointCount.setStatus("current")
_CienaCesDpTsQSchedulerProfileShaperOverSpeed_Type = Integer32
_CienaCesDpTsQSchedulerProfileShaperOverSpeed_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileShaperOverSpeed = _CienaCesDpTsQSchedulerProfileShaperOverSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 11),
    _CienaCesDpTsQSchedulerProfileShaperOverSpeed_Type()
)
cienaCesDpTsQSchedulerProfileShaperOverSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileShaperOverSpeed.setStatus("current")


class _CienaCesDpTsQSchedulerProfileCirPolicy_Type(Integer32):
    """Custom type cienaCesDpTsQSchedulerProfileCirPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("autoAdjustDisabled", 1),
          ("cirAsPercent", 2),
          ("childCirAsPercent", 3),
          ("childCirSum", 4))
    )


_CienaCesDpTsQSchedulerProfileCirPolicy_Type.__name__ = "Integer32"
_CienaCesDpTsQSchedulerProfileCirPolicy_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileCirPolicy = _CienaCesDpTsQSchedulerProfileCirPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 12),
    _CienaCesDpTsQSchedulerProfileCirPolicy_Type()
)
cienaCesDpTsQSchedulerProfileCirPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileCirPolicy.setStatus("current")


class _CienaCesDpTsQSchedulerProfileEirPolicy_Type(Integer32):
    """Custom type cienaCesDpTsQSchedulerProfileEirPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("autoAdjustDisabled", 1),
          ("eirAsPercent", 2),
          ("childEirAsPercent", 3))
    )


_CienaCesDpTsQSchedulerProfileEirPolicy_Type.__name__ = "Integer32"
_CienaCesDpTsQSchedulerProfileEirPolicy_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileEirPolicy = _CienaCesDpTsQSchedulerProfileEirPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 13),
    _CienaCesDpTsQSchedulerProfileEirPolicy_Type()
)
cienaCesDpTsQSchedulerProfileEirPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileEirPolicy.setStatus("current")
_CienaCesDpTsQSchedulerProfileCirPercent_Type = Unsigned32
_CienaCesDpTsQSchedulerProfileCirPercent_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileCirPercent = _CienaCesDpTsQSchedulerProfileCirPercent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 14),
    _CienaCesDpTsQSchedulerProfileCirPercent_Type()
)
cienaCesDpTsQSchedulerProfileCirPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileCirPercent.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileCirPercent.setUnits("percent")
_CienaCesDpTsQSchedulerProfileEirPercent_Type = Unsigned32
_CienaCesDpTsQSchedulerProfileEirPercent_Object = MibTableColumn
cienaCesDpTsQSchedulerProfileEirPercent = _CienaCesDpTsQSchedulerProfileEirPercent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 1, 1, 15),
    _CienaCesDpTsQSchedulerProfileEirPercent_Type()
)
cienaCesDpTsQSchedulerProfileEirPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileEirPercent.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerProfileEirPercent.setUnits("percent")
_CienaCesDpTsQSchedulerTapPointTable_Object = MibTable
cienaCesDpTsQSchedulerTapPointTable = _CienaCesDpTsQSchedulerTapPointTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerTapPointTable.setStatus("current")
_CienaCesDpTsQSchedulerTapPointEntry_Object = MibTableRow
cienaCesDpTsQSchedulerTapPointEntry = _CienaCesDpTsQSchedulerTapPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 2, 1)
)
cienaCesDpTsQSchedulerTapPointEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQSchedulerProfileId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQSchedulerTapPointIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerTapPointEntry.setStatus("current")


class _CienaCesDpTsQSchedulerTapPointIndex_Type(Integer32):
    """Custom type cienaCesDpTsQSchedulerTapPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesDpTsQSchedulerTapPointIndex_Type.__name__ = "Integer32"
_CienaCesDpTsQSchedulerTapPointIndex_Object = MibTableColumn
cienaCesDpTsQSchedulerTapPointIndex = _CienaCesDpTsQSchedulerTapPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 2, 1, 1),
    _CienaCesDpTsQSchedulerTapPointIndex_Type()
)
cienaCesDpTsQSchedulerTapPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerTapPointIndex.setStatus("current")
_CienaCesDpTsQSchedulerTapPointPriority_Type = Integer32
_CienaCesDpTsQSchedulerTapPointPriority_Object = MibTableColumn
cienaCesDpTsQSchedulerTapPointPriority = _CienaCesDpTsQSchedulerTapPointPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 2, 1, 2),
    _CienaCesDpTsQSchedulerTapPointPriority_Type()
)
cienaCesDpTsQSchedulerTapPointPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerTapPointPriority.setStatus("current")
_CienaCesDpTsQSchedulerTapPointWeight_Type = Integer32
_CienaCesDpTsQSchedulerTapPointWeight_Object = MibTableColumn
cienaCesDpTsQSchedulerTapPointWeight = _CienaCesDpTsQSchedulerTapPointWeight_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 5, 2, 1, 3),
    _CienaCesDpTsQSchedulerTapPointWeight_Type()
)
cienaCesDpTsQSchedulerTapPointWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerTapPointWeight.setStatus("current")
_CienaCesDpTsQSchedulerInstance_ObjectIdentity = ObjectIdentity
cienaCesDpTsQSchedulerInstance = _CienaCesDpTsQSchedulerInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 6)
)
_CienaCesDpTsQSchedulerInstanceTable_Object = MibTable
cienaCesDpTsQSchedulerInstanceTable = _CienaCesDpTsQSchedulerInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerInstanceTable.setStatus("current")
_CienaCesDpTsQSchedulerInstanceEntry_Object = MibTableRow
cienaCesDpTsQSchedulerInstanceEntry = _CienaCesDpTsQSchedulerInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 6, 1, 1)
)
cienaCesDpTsQSchedulerInstanceEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQSchedulerInstancePgid"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQSchedulerProfileId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsQSchedulerInstanceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerInstanceEntry.setStatus("current")
_CienaCesDpTsQSchedulerInstancePgid_Type = Unsigned32
_CienaCesDpTsQSchedulerInstancePgid_Object = MibTableColumn
cienaCesDpTsQSchedulerInstancePgid = _CienaCesDpTsQSchedulerInstancePgid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 6, 1, 1, 1),
    _CienaCesDpTsQSchedulerInstancePgid_Type()
)
cienaCesDpTsQSchedulerInstancePgid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerInstancePgid.setStatus("current")


class _CienaCesDpTsQSchedulerInstanceIndex_Type(Integer32):
    """Custom type cienaCesDpTsQSchedulerInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTsQSchedulerInstanceIndex_Type.__name__ = "Integer32"
_CienaCesDpTsQSchedulerInstanceIndex_Object = MibTableColumn
cienaCesDpTsQSchedulerInstanceIndex = _CienaCesDpTsQSchedulerInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 6, 1, 1, 2),
    _CienaCesDpTsQSchedulerInstanceIndex_Type()
)
cienaCesDpTsQSchedulerInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerInstanceIndex.setStatus("current")
_CienaCesDpTsQSchedulerInstanceParentSchedId_Type = Integer32
_CienaCesDpTsQSchedulerInstanceParentSchedId_Object = MibTableColumn
cienaCesDpTsQSchedulerInstanceParentSchedId = _CienaCesDpTsQSchedulerInstanceParentSchedId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 6, 1, 1, 3),
    _CienaCesDpTsQSchedulerInstanceParentSchedId_Type()
)
cienaCesDpTsQSchedulerInstanceParentSchedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerInstanceParentSchedId.setStatus("current")
_CienaCesDpTsQSchedulerInstanceParentInstanceId_Type = Integer32
_CienaCesDpTsQSchedulerInstanceParentInstanceId_Object = MibTableColumn
cienaCesDpTsQSchedulerInstanceParentInstanceId = _CienaCesDpTsQSchedulerInstanceParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 6, 1, 1, 4),
    _CienaCesDpTsQSchedulerInstanceParentInstanceId_Type()
)
cienaCesDpTsQSchedulerInstanceParentInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerInstanceParentInstanceId.setStatus("current")
_CienaCesDpTsQSchedulerInstanceParentTapPoint_Type = Integer32
_CienaCesDpTsQSchedulerInstanceParentTapPoint_Object = MibTableColumn
cienaCesDpTsQSchedulerInstanceParentTapPoint = _CienaCesDpTsQSchedulerInstanceParentTapPoint_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 6, 1, 1, 5),
    _CienaCesDpTsQSchedulerInstanceParentTapPoint_Type()
)
cienaCesDpTsQSchedulerInstanceParentTapPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerInstanceParentTapPoint.setStatus("current")
_CienaCesDpTsQSchedulerInstanceControlPlaneUsedCir_Type = Unsigned32
_CienaCesDpTsQSchedulerInstanceControlPlaneUsedCir_Object = MibTableColumn
cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir = _CienaCesDpTsQSchedulerInstanceControlPlaneUsedCir_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 5, 6, 1, 1, 6),
    _CienaCesDpTsQSchedulerInstanceControlPlaneUsedCir_Type()
)
cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir.setUnits("kilobits/sec")
_CienaCesDpTrafficClassTerm_ObjectIdentity = ObjectIdentity
cienaCesDpTrafficClassTerm = _CienaCesDpTrafficClassTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6)
)
_CienaCesDpTrafficClassTermTable_Object = MibTable
cienaCesDpTrafficClassTermTable = _CienaCesDpTrafficClassTermTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassTermTable.setStatus("current")
_CienaCesDpTrafficClassTermEntry_Object = MibTableRow
cienaCesDpTrafficClassTermEntry = _CienaCesDpTrafficClassTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1)
)
cienaCesDpTrafficClassTermEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTrafficClassType"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTrafficClassId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTrafficClassElemId"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpTrafficClassTermPresentType"),
)
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassTermEntry.setStatus("current")


class _CienaCesDpTrafficClassType_Type(Integer32):
    """Custom type cienaCesDpTrafficClassType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("subPort", 1),
          ("qosFlow", 2),
          ("accessFlow", 3),
          ("transitPbt", 4),
          ("servicePbt", 5),
          ("tunnelDecapPbt", 6),
          ("vcMpls", 7),
          ("named", 8))
    )


_CienaCesDpTrafficClassType_Type.__name__ = "Integer32"
_CienaCesDpTrafficClassType_Object = MibTableColumn
cienaCesDpTrafficClassType = _CienaCesDpTrafficClassType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 1),
    _CienaCesDpTrafficClassType_Type()
)
cienaCesDpTrafficClassType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassType.setStatus("current")


class _CienaCesDpTrafficClassId_Type(Integer32):
    """Custom type cienaCesDpTrafficClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTrafficClassId_Type.__name__ = "Integer32"
_CienaCesDpTrafficClassId_Object = MibTableColumn
cienaCesDpTrafficClassId = _CienaCesDpTrafficClassId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 2),
    _CienaCesDpTrafficClassId_Type()
)
cienaCesDpTrafficClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassId.setStatus("current")


class _CienaCesDpTrafficClassElemId_Type(Integer32):
    """Custom type cienaCesDpTrafficClassElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesDpTrafficClassElemId_Type.__name__ = "Integer32"
_CienaCesDpTrafficClassElemId_Object = MibTableColumn
cienaCesDpTrafficClassElemId = _CienaCesDpTrafficClassElemId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 3),
    _CienaCesDpTrafficClassElemId_Type()
)
cienaCesDpTrafficClassElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassElemId.setStatus("current")


class _CienaCesDpTrafficClassTermPresentType_Type(Integer32):
    """Custom type cienaCesDpTrafficClassTermPresentType based on Integer32"""
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("trafficClassElement", 1),
          ("vid1", 2),
          ("l2Pcp1", 3),
          ("vid2", 4),
          ("l2Pcp2", 5),
          ("vlanUntaggedData", 6),
          ("l2Control", 7),
          ("cMacSa", 8),
          ("cMacDa", 9),
          ("ipSrcIp", 10),
          ("ipDstIp", 11),
          ("ipProtoType", 12),
          ("ipDscp", 13),
          ("ipL4SrcPort", 14),
          ("ipL4DstPort", 15),
          ("mplsVcLabel", 16),
          ("mplsVcExp", 17),
          ("mplsTunLabel", 18),
          ("mplsTunExp", 19),
          ("baseEtype", 20),
          ("bvid", 21),
          ("bPcp", 22),
          ("isid", 23),
          ("isidPcp", 24),
          ("any", 25),
          ("l2Rcos", 26),
          ("ipL4Application", 27))
    )


_CienaCesDpTrafficClassTermPresentType_Type.__name__ = "Integer32"
_CienaCesDpTrafficClassTermPresentType_Object = MibTableColumn
cienaCesDpTrafficClassTermPresentType = _CienaCesDpTrafficClassTermPresentType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 4),
    _CienaCesDpTrafficClassTermPresentType_Type()
)
cienaCesDpTrafficClassTermPresentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassTermPresentType.setStatus("current")


class _CienaCesDpTrafficClassTermStartValue32_Type(Unsigned32):
    """Custom type cienaCesDpTrafficClassTermStartValue32 based on Unsigned32"""
    defaultValue = 0


_CienaCesDpTrafficClassTermStartValue32_Type.__name__ = "Unsigned32"
_CienaCesDpTrafficClassTermStartValue32_Object = MibTableColumn
cienaCesDpTrafficClassTermStartValue32 = _CienaCesDpTrafficClassTermStartValue32_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 5),
    _CienaCesDpTrafficClassTermStartValue32_Type()
)
cienaCesDpTrafficClassTermStartValue32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassTermStartValue32.setStatus("current")


class _CienaCesDpTrafficClassTermEndOrMaskValue32_Type(Unsigned32):
    """Custom type cienaCesDpTrafficClassTermEndOrMaskValue32 based on Unsigned32"""
    defaultValue = 0


_CienaCesDpTrafficClassTermEndOrMaskValue32_Type.__name__ = "Unsigned32"
_CienaCesDpTrafficClassTermEndOrMaskValue32_Object = MibTableColumn
cienaCesDpTrafficClassTermEndOrMaskValue32 = _CienaCesDpTrafficClassTermEndOrMaskValue32_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 6),
    _CienaCesDpTrafficClassTermEndOrMaskValue32_Type()
)
cienaCesDpTrafficClassTermEndOrMaskValue32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassTermEndOrMaskValue32.setStatus("current")


class _CienaCesDpTrafficClassTermStartValueMac_Type(MacAddress):
    """Custom type cienaCesDpTrafficClassTermStartValueMac based on MacAddress"""
    defaultHexValue = "000000000000"


_CienaCesDpTrafficClassTermStartValueMac_Type.__name__ = "MacAddress"
_CienaCesDpTrafficClassTermStartValueMac_Object = MibTableColumn
cienaCesDpTrafficClassTermStartValueMac = _CienaCesDpTrafficClassTermStartValueMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 7),
    _CienaCesDpTrafficClassTermStartValueMac_Type()
)
cienaCesDpTrafficClassTermStartValueMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassTermStartValueMac.setStatus("current")


class _CienaCesDpTrafficClassTermMaskValueMac_Type(MacAddress):
    """Custom type cienaCesDpTrafficClassTermMaskValueMac based on MacAddress"""
    defaultHexValue = "000000000000"


_CienaCesDpTrafficClassTermMaskValueMac_Type.__name__ = "MacAddress"
_CienaCesDpTrafficClassTermMaskValueMac_Object = MibTableColumn
cienaCesDpTrafficClassTermMaskValueMac = _CienaCesDpTrafficClassTermMaskValueMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 8),
    _CienaCesDpTrafficClassTermMaskValueMac_Type()
)
cienaCesDpTrafficClassTermMaskValueMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassTermMaskValueMac.setStatus("current")


class _CienaCesDpTrafficClassTermStartValueIp_Type(IpAddress):
    """Custom type cienaCesDpTrafficClassTermStartValueIp based on IpAddress"""
    defaultHexValue = "00000000"


_CienaCesDpTrafficClassTermStartValueIp_Type.__name__ = "IpAddress"
_CienaCesDpTrafficClassTermStartValueIp_Object = MibTableColumn
cienaCesDpTrafficClassTermStartValueIp = _CienaCesDpTrafficClassTermStartValueIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 9),
    _CienaCesDpTrafficClassTermStartValueIp_Type()
)
cienaCesDpTrafficClassTermStartValueIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassTermStartValueIp.setStatus("current")


class _CienaCesDpTrafficClassTermMaskValueIp_Type(IpAddress):
    """Custom type cienaCesDpTrafficClassTermMaskValueIp based on IpAddress"""
    defaultHexValue = "00000000"


_CienaCesDpTrafficClassTermMaskValueIp_Type.__name__ = "IpAddress"
_CienaCesDpTrafficClassTermMaskValueIp_Object = MibTableColumn
cienaCesDpTrafficClassTermMaskValueIp = _CienaCesDpTrafficClassTermMaskValueIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 6, 1, 1, 10),
    _CienaCesDpTrafficClassTermMaskValueIp_Type()
)
cienaCesDpTrafficClassTermMaskValueIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpTrafficClassTermMaskValueIp.setStatus("current")
_CienaCesDpSubPort_ObjectIdentity = ObjectIdentity
cienaCesDpSubPort = _CienaCesDpSubPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7)
)
_CienaCesDpSubPortTable_Object = MibTable
cienaCesDpSubPortTable = _CienaCesDpSubPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpSubPortTable.setStatus("current")
_CienaCesDpSubPortEntry_Object = MibTableRow
cienaCesDpSubPortEntry = _CienaCesDpSubPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1)
)
cienaCesDpSubPortEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpSubPortLiIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpSubPortEntry.setStatus("current")


class _CienaCesDpSubPortLiIndex_Type(Integer32):
    """Custom type cienaCesDpSubPortLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CienaCesDpSubPortLiIndex_Type.__name__ = "Integer32"
_CienaCesDpSubPortLiIndex_Object = MibTableColumn
cienaCesDpSubPortLiIndex = _CienaCesDpSubPortLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 1),
    _CienaCesDpSubPortLiIndex_Type()
)
cienaCesDpSubPortLiIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesDpSubPortLiIndex.setStatus("current")
_CienaCesDpSubPortName_Type = DisplayString
_CienaCesDpSubPortName_Object = MibTableColumn
cienaCesDpSubPortName = _CienaCesDpSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 2),
    _CienaCesDpSubPortName_Type()
)
cienaCesDpSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortName.setStatus("current")
_CienaCesDpSubPortClassifierPrecedence_Type = Unsigned32
_CienaCesDpSubPortClassifierPrecedence_Object = MibTableColumn
cienaCesDpSubPortClassifierPrecedence = _CienaCesDpSubPortClassifierPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 3),
    _CienaCesDpSubPortClassifierPrecedence_Type()
)
cienaCesDpSubPortClassifierPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortClassifierPrecedence.setStatus("current")
_CienaCesDpSubPortParentIfId_Type = Integer32
_CienaCesDpSubPortParentIfId_Object = MibTableColumn
cienaCesDpSubPortParentIfId = _CienaCesDpSubPortParentIfId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 4),
    _CienaCesDpSubPortParentIfId_Type()
)
cienaCesDpSubPortParentIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortParentIfId.setStatus("current")


class _CienaCesDpSubPortVirtualSwitchIndex_Type(Integer32):
    """Custom type cienaCesDpSubPortVirtualSwitchIndex based on Integer32"""
    defaultValue = 0


_CienaCesDpSubPortVirtualSwitchIndex_Type.__name__ = "Integer32"
_CienaCesDpSubPortVirtualSwitchIndex_Object = MibTableColumn
cienaCesDpSubPortVirtualSwitchIndex = _CienaCesDpSubPortVirtualSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 5),
    _CienaCesDpSubPortVirtualSwitchIndex_Type()
)
cienaCesDpSubPortVirtualSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortVirtualSwitchIndex.setStatus("current")


class _CienaCesDpSubPortRlanIndex_Type(Integer32):
    """Custom type cienaCesDpSubPortRlanIndex based on Integer32"""
    defaultValue = 0


_CienaCesDpSubPortRlanIndex_Type.__name__ = "Integer32"
_CienaCesDpSubPortRlanIndex_Object = MibTableColumn
cienaCesDpSubPortRlanIndex = _CienaCesDpSubPortRlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 6),
    _CienaCesDpSubPortRlanIndex_Type()
)
cienaCesDpSubPortRlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortRlanIndex.setStatus("current")
_CienaCesDpSubPortVirtualSwitchName_Type = OctetString
_CienaCesDpSubPortVirtualSwitchName_Object = MibTableColumn
cienaCesDpSubPortVirtualSwitchName = _CienaCesDpSubPortVirtualSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 7),
    _CienaCesDpSubPortVirtualSwitchName_Type()
)
cienaCesDpSubPortVirtualSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortVirtualSwitchName.setStatus("current")
_CienaCesDpSubPortIngressMeterProfileId_Type = Integer32
_CienaCesDpSubPortIngressMeterProfileId_Object = MibTableColumn
cienaCesDpSubPortIngressMeterProfileId = _CienaCesDpSubPortIngressMeterProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 8),
    _CienaCesDpSubPortIngressMeterProfileId_Type()
)
cienaCesDpSubPortIngressMeterProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressMeterProfileId.setStatus("current")
_CienaCesDpSubPortIngressMeterProfileName_Type = OctetString
_CienaCesDpSubPortIngressMeterProfileName_Object = MibTableColumn
cienaCesDpSubPortIngressMeterProfileName = _CienaCesDpSubPortIngressMeterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 9),
    _CienaCesDpSubPortIngressMeterProfileName_Type()
)
cienaCesDpSubPortIngressMeterProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressMeterProfileName.setStatus("current")


class _CienaCesDpSubportIngressMeterPolicy_Type(DpIngressMeterPolicy):
    """Custom type cienaCesDpSubportIngressMeterPolicy based on DpIngressMeterPolicy"""
    defaultValue = 1


_CienaCesDpSubportIngressMeterPolicy_Type.__name__ = "DpIngressMeterPolicy"
_CienaCesDpSubportIngressMeterPolicy_Object = MibTableColumn
cienaCesDpSubportIngressMeterPolicy = _CienaCesDpSubportIngressMeterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 10),
    _CienaCesDpSubportIngressMeterPolicy_Type()
)
cienaCesDpSubportIngressMeterPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubportIngressMeterPolicy.setStatus("current")
_CienaCesDpSubPortIngressFloodContainerId_Type = Integer32
_CienaCesDpSubPortIngressFloodContainerId_Object = MibTableColumn
cienaCesDpSubPortIngressFloodContainerId = _CienaCesDpSubPortIngressFloodContainerId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 11),
    _CienaCesDpSubPortIngressFloodContainerId_Type()
)
cienaCesDpSubPortIngressFloodContainerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressFloodContainerId.setStatus("current")
_CienaCesDpSubPortIngressFloodContainerName_Type = OctetString
_CienaCesDpSubPortIngressFloodContainerName_Object = MibTableColumn
cienaCesDpSubPortIngressFloodContainerName = _CienaCesDpSubPortIngressFloodContainerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 12),
    _CienaCesDpSubPortIngressFloodContainerName_Type()
)
cienaCesDpSubPortIngressFloodContainerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressFloodContainerName.setStatus("current")
_CienaCesDpSubPortIngressRcosProfileId_Type = Integer32
_CienaCesDpSubPortIngressRcosProfileId_Object = MibTableColumn
cienaCesDpSubPortIngressRcosProfileId = _CienaCesDpSubPortIngressRcosProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 13),
    _CienaCesDpSubPortIngressRcosProfileId_Type()
)
cienaCesDpSubPortIngressRcosProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressRcosProfileId.setStatus("current")
_CienaCesDpSubPortIngressRcosProfileName_Type = OctetString
_CienaCesDpSubPortIngressRcosProfileName_Object = MibTableColumn
cienaCesDpSubPortIngressRcosProfileName = _CienaCesDpSubPortIngressRcosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 14),
    _CienaCesDpSubPortIngressRcosProfileName_Type()
)
cienaCesDpSubPortIngressRcosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressRcosProfileName.setStatus("current")


class _CienaCesDpSubPortIngressRcosPolicy_Type(Integer32):
    """Custom type cienaCesDpSubPortIngressRcosPolicy based on Integer32"""
    defaultValue = 3

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
        *(("ignore", 1),
          ("fixed", 2),
          ("dot1dToRcosTag1", 3),
          ("dot1dToRcosTag2", 4),
          ("dscpToRcos", 5),
          ("dscpMplsTcToRcos", 6))
    )


_CienaCesDpSubPortIngressRcosPolicy_Type.__name__ = "Integer32"
_CienaCesDpSubPortIngressRcosPolicy_Object = MibTableColumn
cienaCesDpSubPortIngressRcosPolicy = _CienaCesDpSubPortIngressRcosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 15),
    _CienaCesDpSubPortIngressRcosPolicy_Type()
)
cienaCesDpSubPortIngressRcosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressRcosPolicy.setStatus("current")


class _CienaCesDpSubPortIngressFcosMapId_Type(Integer32):
    """Custom type cienaCesDpSubPortIngressFcosMapId based on Integer32"""
    defaultValue = 0


_CienaCesDpSubPortIngressFcosMapId_Type.__name__ = "Integer32"
_CienaCesDpSubPortIngressFcosMapId_Object = MibTableColumn
cienaCesDpSubPortIngressFcosMapId = _CienaCesDpSubPortIngressFcosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 16),
    _CienaCesDpSubPortIngressFcosMapId_Type()
)
cienaCesDpSubPortIngressFcosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressFcosMapId.setStatus("current")
_CienaCesDpSubPortIngressFcosMapName_Type = OctetString
_CienaCesDpSubPortIngressFcosMapName_Object = MibTableColumn
cienaCesDpSubPortIngressFcosMapName = _CienaCesDpSubPortIngressFcosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 17),
    _CienaCesDpSubPortIngressFcosMapName_Type()
)
cienaCesDpSubPortIngressFcosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressFcosMapName.setStatus("current")


class _CienaCesDpSubPortEgressFcosMapId_Type(Integer32):
    """Custom type cienaCesDpSubPortEgressFcosMapId based on Integer32"""
    defaultValue = 0


_CienaCesDpSubPortEgressFcosMapId_Type.__name__ = "Integer32"
_CienaCesDpSubPortEgressFcosMapId_Object = MibTableColumn
cienaCesDpSubPortEgressFcosMapId = _CienaCesDpSubPortEgressFcosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 18),
    _CienaCesDpSubPortEgressFcosMapId_Type()
)
cienaCesDpSubPortEgressFcosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortEgressFcosMapId.setStatus("current")
_CienaCesDpSubPortEgressFcosMapName_Type = OctetString
_CienaCesDpSubPortEgressFcosMapName_Object = MibTableColumn
cienaCesDpSubPortEgressFcosMapName = _CienaCesDpSubPortEgressFcosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 19),
    _CienaCesDpSubPortEgressFcosMapName_Type()
)
cienaCesDpSubPortEgressFcosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortEgressFcosMapName.setStatus("current")


class _CienaCesDpSubPortEgressL2PtTransform_Type(TruthValue):
    """Custom type cienaCesDpSubPortEgressL2PtTransform based on TruthValue"""
    defaultValue = 2


_CienaCesDpSubPortEgressL2PtTransform_Type.__name__ = "TruthValue"
_CienaCesDpSubPortEgressL2PtTransform_Object = MibTableColumn
cienaCesDpSubPortEgressL2PtTransform = _CienaCesDpSubPortEgressL2PtTransform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 20),
    _CienaCesDpSubPortEgressL2PtTransform_Type()
)
cienaCesDpSubPortEgressL2PtTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortEgressL2PtTransform.setStatus("current")
_CienaCesDpSubPortIngressL2Transform_Type = OctetString
_CienaCesDpSubPortIngressL2Transform_Object = MibTableColumn
cienaCesDpSubPortIngressL2Transform = _CienaCesDpSubPortIngressL2Transform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 21),
    _CienaCesDpSubPortIngressL2Transform_Type()
)
cienaCesDpSubPortIngressL2Transform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressL2Transform.setStatus("current")
_CienaCesDpSubPortEgressL2Transform_Type = OctetString
_CienaCesDpSubPortEgressL2Transform_Object = MibTableColumn
cienaCesDpSubPortEgressL2Transform = _CienaCesDpSubPortEgressL2Transform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 22),
    _CienaCesDpSubPortEgressL2Transform_Type()
)
cienaCesDpSubPortEgressL2Transform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortEgressL2Transform.setStatus("current")


class _CienaCesDpSubPortIngressL3TransformPolicy_Type(Integer32):
    """Custom type cienaCesDpSubPortIngressL3TransformPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leave", 1),
          ("mappedDscp", 2))
    )


_CienaCesDpSubPortIngressL3TransformPolicy_Type.__name__ = "Integer32"
_CienaCesDpSubPortIngressL3TransformPolicy_Object = MibTableColumn
cienaCesDpSubPortIngressL3TransformPolicy = _CienaCesDpSubPortIngressL3TransformPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 23),
    _CienaCesDpSubPortIngressL3TransformPolicy_Type()
)
cienaCesDpSubPortIngressL3TransformPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortIngressL3TransformPolicy.setStatus("current")


class _CienaCesDpSubPortEgressL3TransformPolicy_Type(Integer32):
    """Custom type cienaCesDpSubPortEgressL3TransformPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leave", 1),
          ("mappedDscp", 2))
    )


_CienaCesDpSubPortEgressL3TransformPolicy_Type.__name__ = "Integer32"
_CienaCesDpSubPortEgressL3TransformPolicy_Object = MibTableColumn
cienaCesDpSubPortEgressL3TransformPolicy = _CienaCesDpSubPortEgressL3TransformPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 24),
    _CienaCesDpSubPortEgressL3TransformPolicy_Type()
)
cienaCesDpSubPortEgressL3TransformPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortEgressL3TransformPolicy.setStatus("current")


class _CienaCesDpSubPortPrivateFwdGroup_Type(Integer32):
    """Custom type cienaCesDpSubPortPrivateFwdGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("groupA", 1),
          ("groupB", 2),
          ("groupC", 3))
    )


_CienaCesDpSubPortPrivateFwdGroup_Type.__name__ = "Integer32"
_CienaCesDpSubPortPrivateFwdGroup_Object = MibTableColumn
cienaCesDpSubPortPrivateFwdGroup = _CienaCesDpSubPortPrivateFwdGroup_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 25),
    _CienaCesDpSubPortPrivateFwdGroup_Type()
)
cienaCesDpSubPortPrivateFwdGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortPrivateFwdGroup.setStatus("current")


class _CienaCesDpSubPortFilterPolicy_Type(Integer32):
    """Custom type cienaCesDpSubPortFilterPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_CienaCesDpSubPortFilterPolicy_Type.__name__ = "Integer32"
_CienaCesDpSubPortFilterPolicy_Object = MibTableColumn
cienaCesDpSubPortFilterPolicy = _CienaCesDpSubPortFilterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 26),
    _CienaCesDpSubPortFilterPolicy_Type()
)
cienaCesDpSubPortFilterPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortFilterPolicy.setStatus("current")
_CienaCesDpSubPortLogicalRingIndex_Type = Integer32
_CienaCesDpSubPortLogicalRingIndex_Object = MibTableColumn
cienaCesDpSubPortLogicalRingIndex = _CienaCesDpSubPortLogicalRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 27),
    _CienaCesDpSubPortLogicalRingIndex_Type()
)
cienaCesDpSubPortLogicalRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortLogicalRingIndex.setStatus("current")
_CienaCesDpSubPortVirtualRingIndex_Type = Integer32
_CienaCesDpSubPortVirtualRingIndex_Object = MibTableColumn
cienaCesDpSubPortVirtualRingIndex = _CienaCesDpSubPortVirtualRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 28),
    _CienaCesDpSubPortVirtualRingIndex_Type()
)
cienaCesDpSubPortVirtualRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortVirtualRingIndex.setStatus("current")
_CienaCesDpSubPortEgressReflectorMac_Type = MacAddress
_CienaCesDpSubPortEgressReflectorMac_Object = MibTableColumn
cienaCesDpSubPortEgressReflectorMac = _CienaCesDpSubPortEgressReflectorMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 29),
    _CienaCesDpSubPortEgressReflectorMac_Type()
)
cienaCesDpSubPortEgressReflectorMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortEgressReflectorMac.setStatus("current")
_CienaCesDpSubPortEgressGeneratorMac_Type = MacAddress
_CienaCesDpSubPortEgressGeneratorMac_Object = MibTableColumn
cienaCesDpSubPortEgressGeneratorMac = _CienaCesDpSubPortEgressGeneratorMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 30),
    _CienaCesDpSubPortEgressGeneratorMac_Type()
)
cienaCesDpSubPortEgressGeneratorMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortEgressGeneratorMac.setStatus("current")
_CienaCesDpSubPortQueueGroupProfileId_Type = Integer32
_CienaCesDpSubPortQueueGroupProfileId_Object = MibTableColumn
cienaCesDpSubPortQueueGroupProfileId = _CienaCesDpSubPortQueueGroupProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 31),
    _CienaCesDpSubPortQueueGroupProfileId_Type()
)
cienaCesDpSubPortQueueGroupProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortQueueGroupProfileId.setStatus("current")
_CienaCesDpSubPortQueueGroupProfileName_Type = OctetString
_CienaCesDpSubPortQueueGroupProfileName_Object = MibTableColumn
cienaCesDpSubPortQueueGroupProfileName = _CienaCesDpSubPortQueueGroupProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 32),
    _CienaCesDpSubPortQueueGroupProfileName_Type()
)
cienaCesDpSubPortQueueGroupProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortQueueGroupProfileName.setStatus("current")
_CienaCesDpSubPortQueueGroupInstanceId_Type = Integer32
_CienaCesDpSubPortQueueGroupInstanceId_Object = MibTableColumn
cienaCesDpSubPortQueueGroupInstanceId = _CienaCesDpSubPortQueueGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 7, 1, 1, 33),
    _CienaCesDpSubPortQueueGroupInstanceId_Type()
)
cienaCesDpSubPortQueueGroupInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpSubPortQueueGroupInstanceId.setStatus("current")
_CienaCesDpVirtualSwitch_ObjectIdentity = ObjectIdentity
cienaCesDpVirtualSwitch = _CienaCesDpVirtualSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8)
)
_CienaCesDpVirtualSwitchTable_Object = MibTable
cienaCesDpVirtualSwitchTable = _CienaCesDpVirtualSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchTable.setStatus("current")
_CienaCesDpVirtualSwitchEntry_Object = MibTableRow
cienaCesDpVirtualSwitchEntry = _CienaCesDpVirtualSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 1, 1)
)
cienaCesDpVirtualSwitchEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchEntry.setStatus("current")


class _CienaCesDpVirtualSwitchIndex_Type(Integer32):
    """Custom type cienaCesDpVirtualSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_CienaCesDpVirtualSwitchIndex_Type.__name__ = "Integer32"
_CienaCesDpVirtualSwitchIndex_Object = MibTableColumn
cienaCesDpVirtualSwitchIndex = _CienaCesDpVirtualSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 1, 1, 1),
    _CienaCesDpVirtualSwitchIndex_Type()
)
cienaCesDpVirtualSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchIndex.setStatus("current")


class _CienaCesDpVirtualSwitchRlanIndex_Type(Integer32):
    """Custom type cienaCesDpVirtualSwitchRlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CienaCesDpVirtualSwitchRlanIndex_Type.__name__ = "Integer32"
_CienaCesDpVirtualSwitchRlanIndex_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanIndex = _CienaCesDpVirtualSwitchRlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 1, 1, 2),
    _CienaCesDpVirtualSwitchRlanIndex_Type()
)
cienaCesDpVirtualSwitchRlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanIndex.setStatus("current")
_CienaCesDpVirtualSwitchRlanTable_Object = MibTable
cienaCesDpVirtualSwitchRlanTable = _CienaCesDpVirtualSwitchRlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanTable.setStatus("current")
_CienaCesDpVirtualSwitchRlanEntry_Object = MibTableRow
cienaCesDpVirtualSwitchRlanEntry = _CienaCesDpVirtualSwitchRlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1)
)
cienaCesDpVirtualSwitchRlanEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchIndex"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchRlanIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanEntry.setStatus("current")
_CienaCesDpVirtualSwitchRlanName_Type = DisplayString
_CienaCesDpVirtualSwitchRlanName_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanName = _CienaCesDpVirtualSwitchRlanName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 1),
    _CienaCesDpVirtualSwitchRlanName_Type()
)
cienaCesDpVirtualSwitchRlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanName.setStatus("current")


class _CienaCesDpVirtualSwitchRlanMcastForwardingMode_Type(Integer32):
    """Custom type cienaCesDpVirtualSwitchRlanMcastForwardingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("l2Enhanced", 2))
    )


_CienaCesDpVirtualSwitchRlanMcastForwardingMode_Type.__name__ = "Integer32"
_CienaCesDpVirtualSwitchRlanMcastForwardingMode_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanMcastForwardingMode = _CienaCesDpVirtualSwitchRlanMcastForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 2),
    _CienaCesDpVirtualSwitchRlanMcastForwardingMode_Type()
)
cienaCesDpVirtualSwitchRlanMcastForwardingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanMcastForwardingMode.setStatus("current")


class _CienaCesDpVirtualSwitchRlanL2CftStatus_Type(CienaGlobalState):
    """Custom type cienaCesDpVirtualSwitchRlanL2CftStatus based on CienaGlobalState"""
    defaultValue = 2


_CienaCesDpVirtualSwitchRlanL2CftStatus_Type.__name__ = "CienaGlobalState"
_CienaCesDpVirtualSwitchRlanL2CftStatus_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftStatus = _CienaCesDpVirtualSwitchRlanL2CftStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 3),
    _CienaCesDpVirtualSwitchRlanL2CftStatus_Type()
)
cienaCesDpVirtualSwitchRlanL2CftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanL2CftStatus.setStatus("current")


class _CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Type(Integer32):
    """Custom type cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos based on Integer32"""
    defaultValue = 48


_CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Type.__name__ = "Integer32"
_CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos = _CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 4),
    _CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Type()
)
cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos.setStatus("current")


class _CienaCesDpVirtualSwitchRlanMacLearningStatus_Type(CienaGlobalState):
    """Custom type cienaCesDpVirtualSwitchRlanMacLearningStatus based on CienaGlobalState"""
    defaultValue = 1


_CienaCesDpVirtualSwitchRlanMacLearningStatus_Type.__name__ = "CienaGlobalState"
_CienaCesDpVirtualSwitchRlanMacLearningStatus_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanMacLearningStatus = _CienaCesDpVirtualSwitchRlanMacLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 5),
    _CienaCesDpVirtualSwitchRlanMacLearningStatus_Type()
)
cienaCesDpVirtualSwitchRlanMacLearningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanMacLearningStatus.setStatus("current")


class _CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Type(CienaGlobalState):
    """Custom type cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus based on CienaGlobalState"""
    defaultValue = 2


_CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Type.__name__ = "CienaGlobalState"
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus = _CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 6),
    _CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Type()
)
cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus.setStatus("current")


class _CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Type(PrivateForwardGroupPolicy):
    """Custom type cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy based on PrivateForwardGroupPolicy"""
    defaultValue = 7


_CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Type.__name__ = "PrivateForwardGroupPolicy"
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy = _CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 7),
    _CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Type()
)
cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy.setStatus("current")


class _CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Type(PrivateForwardGroupPolicy):
    """Custom type cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy based on PrivateForwardGroupPolicy"""
    defaultValue = 7


_CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Type.__name__ = "PrivateForwardGroupPolicy"
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy = _CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 8),
    _CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Type()
)
cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy.setStatus("current")


class _CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Type(PrivateForwardGroupPolicy):
    """Custom type cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy based on PrivateForwardGroupPolicy"""
    defaultValue = 7


_CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Type.__name__ = "PrivateForwardGroupPolicy"
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy = _CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 9),
    _CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Type()
)
cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy.setStatus("current")
_CienaCesDpVirtualSwitchRlanDescription_Type = DisplayString
_CienaCesDpVirtualSwitchRlanDescription_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanDescription = _CienaCesDpVirtualSwitchRlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 10),
    _CienaCesDpVirtualSwitchRlanDescription_Type()
)
cienaCesDpVirtualSwitchRlanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanDescription.setStatus("current")
_CienaCesDpVirtualSwitchRlanPfgProfileId_Type = Integer32
_CienaCesDpVirtualSwitchRlanPfgProfileId_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanPfgProfileId = _CienaCesDpVirtualSwitchRlanPfgProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 11),
    _CienaCesDpVirtualSwitchRlanPfgProfileId_Type()
)
cienaCesDpVirtualSwitchRlanPfgProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanPfgProfileId.setStatus("current")
_CienaCesDpVirtualSwitchRlanPfgProfileName_Type = OctetString
_CienaCesDpVirtualSwitchRlanPfgProfileName_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanPfgProfileName = _CienaCesDpVirtualSwitchRlanPfgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 12),
    _CienaCesDpVirtualSwitchRlanPfgProfileName_Type()
)
cienaCesDpVirtualSwitchRlanPfgProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanPfgProfileName.setStatus("current")
_CienaCesDpVirtualSwitchRlanL2CftProfileId_Type = Integer32
_CienaCesDpVirtualSwitchRlanL2CftProfileId_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftProfileId = _CienaCesDpVirtualSwitchRlanL2CftProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 13),
    _CienaCesDpVirtualSwitchRlanL2CftProfileId_Type()
)
cienaCesDpVirtualSwitchRlanL2CftProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanL2CftProfileId.setStatus("current")
_CienaCesDpVirtualSwitchRlanL2CftProfileName_Type = OctetString
_CienaCesDpVirtualSwitchRlanL2CftProfileName_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftProfileName = _CienaCesDpVirtualSwitchRlanL2CftProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 14),
    _CienaCesDpVirtualSwitchRlanL2CftProfileName_Type()
)
cienaCesDpVirtualSwitchRlanL2CftProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanL2CftProfileName.setStatus("current")


class _CienaCesDpVirtualSwitchRlanLearnLimit_Type(Integer32):
    """Custom type cienaCesDpVirtualSwitchRlanLearnLimit based on Integer32"""
    defaultValue = 64000


_CienaCesDpVirtualSwitchRlanLearnLimit_Type.__name__ = "Integer32"
_CienaCesDpVirtualSwitchRlanLearnLimit_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanLearnLimit = _CienaCesDpVirtualSwitchRlanLearnLimit_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 2, 1, 15),
    _CienaCesDpVirtualSwitchRlanLearnLimit_Type()
)
cienaCesDpVirtualSwitchRlanLearnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanLearnLimit.setStatus("current")
_CienaCesDpVirtualSwitchRlanIfTable_Object = MibTable
cienaCesDpVirtualSwitchRlanIfTable = _CienaCesDpVirtualSwitchRlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 3)
)
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanIfTable.setStatus("current")
_CienaCesDpVirtualSwitchRlanIfEntry_Object = MibTableRow
cienaCesDpVirtualSwitchRlanIfEntry = _CienaCesDpVirtualSwitchRlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 3, 1)
)
cienaCesDpVirtualSwitchRlanIfEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchIndex"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchRlanIndex"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchRlanIfLiType"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchRlanIfLiIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanIfEntry.setStatus("current")
_CienaCesDpVirtualSwitchRlanIfLiType_Type = DpTsAttachType
_CienaCesDpVirtualSwitchRlanIfLiType_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanIfLiType = _CienaCesDpVirtualSwitchRlanIfLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 3, 1, 1),
    _CienaCesDpVirtualSwitchRlanIfLiType_Type()
)
cienaCesDpVirtualSwitchRlanIfLiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanIfLiType.setStatus("current")


class _CienaCesDpVirtualSwitchRlanIfLiIndex_Type(Integer32):
    """Custom type cienaCesDpVirtualSwitchRlanIfLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CienaCesDpVirtualSwitchRlanIfLiIndex_Type.__name__ = "Integer32"
_CienaCesDpVirtualSwitchRlanIfLiIndex_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanIfLiIndex = _CienaCesDpVirtualSwitchRlanIfLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 3, 1, 2),
    _CienaCesDpVirtualSwitchRlanIfLiIndex_Type()
)
cienaCesDpVirtualSwitchRlanIfLiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanIfLiIndex.setStatus("current")
_CienaCesDpVirtualSwitchRlanIfLportIngress_Type = Integer32
_CienaCesDpVirtualSwitchRlanIfLportIngress_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanIfLportIngress = _CienaCesDpVirtualSwitchRlanIfLportIngress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 3, 1, 3),
    _CienaCesDpVirtualSwitchRlanIfLportIngress_Type()
)
cienaCesDpVirtualSwitchRlanIfLportIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanIfLportIngress.setStatus("current")
_CienaCesDpVirtualSwitchRlanIfLportEgress_Type = Integer32
_CienaCesDpVirtualSwitchRlanIfLportEgress_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanIfLportEgress = _CienaCesDpVirtualSwitchRlanIfLportEgress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 3, 1, 4),
    _CienaCesDpVirtualSwitchRlanIfLportEgress_Type()
)
cienaCesDpVirtualSwitchRlanIfLportEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanIfLportEgress.setStatus("current")
_CienaCesDpVirtualSwitchRlanL2CftProtocolTable_Object = MibTable
cienaCesDpVirtualSwitchRlanL2CftProtocolTable = _CienaCesDpVirtualSwitchRlanL2CftProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 4)
)
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanL2CftProtocolTable.setStatus("current")
_CienaCesDpVirtualSwitchRlanL2CftProtocolEntry_Object = MibTableRow
cienaCesDpVirtualSwitchRlanL2CftProtocolEntry = _CienaCesDpVirtualSwitchRlanL2CftProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 4, 1)
)
cienaCesDpVirtualSwitchRlanL2CftProtocolEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchIndex"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchRlanIndex"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpVirtualSwitchRlanL2CftProtocolType"),
)
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanL2CftProtocolEntry.setStatus("current")


class _CienaCesDpVirtualSwitchRlanL2CftProtocolType_Type(Integer32):
    """Custom type cienaCesDpVirtualSwitchRlanL2CftProtocolType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ciscoCdp", 1),
          ("ciscoDtp", 2),
          ("ciscoPagp", 3),
          ("ciscoUdld", 4),
          ("ciscoVtp", 5),
          ("ciscoPvst", 6),
          ("ciscoStpUplinkFast", 7),
          ("vlanBridge", 8),
          ("rstp", 9),
          ("lacp", 10),
          ("lacpMarker", 11),
          ("oam", 12),
          ("lldp", 13),
          ("i8021x", 14),
          ("gmrp", 15),
          ("gvrp", 16),
          ("brigeBlock", 17),
          ("allBridgesBlock", 18),
          ("garpBlock", 19),
          ("elmi", 20),
          ("ptpPeerDelay", 21))
    )


_CienaCesDpVirtualSwitchRlanL2CftProtocolType_Type.__name__ = "Integer32"
_CienaCesDpVirtualSwitchRlanL2CftProtocolType_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftProtocolType = _CienaCesDpVirtualSwitchRlanL2CftProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 4, 1, 1),
    _CienaCesDpVirtualSwitchRlanL2CftProtocolType_Type()
)
cienaCesDpVirtualSwitchRlanL2CftProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanL2CftProtocolType.setStatus("current")


class _CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Type(Integer32):
    """Custom type cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Type.__name__ = "Integer32"
_CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Object = MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition = _CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 8, 4, 1, 2),
    _CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Type()
)
cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition.setStatus("current")
_CienaCesDpQosFlow_ObjectIdentity = ObjectIdentity
cienaCesDpQosFlow = _CienaCesDpQosFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9)
)
_CienaCesDpQosFlowTable_Object = MibTable
cienaCesDpQosFlowTable = _CienaCesDpQosFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpQosFlowTable.setStatus("current")
_CienaCesDpQosFlowEntry_Object = MibTableRow
cienaCesDpQosFlowEntry = _CienaCesDpQosFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1)
)
cienaCesDpQosFlowEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpQosFlowLiIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpQosFlowEntry.setStatus("current")


class _CienaCesDpQosFlowLiIndex_Type(Integer32):
    """Custom type cienaCesDpQosFlowLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CienaCesDpQosFlowLiIndex_Type.__name__ = "Integer32"
_CienaCesDpQosFlowLiIndex_Object = MibTableColumn
cienaCesDpQosFlowLiIndex = _CienaCesDpQosFlowLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 1),
    _CienaCesDpQosFlowLiIndex_Type()
)
cienaCesDpQosFlowLiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowLiIndex.setStatus("current")
_CienaCesDpQosFlowName_Type = DisplayString
_CienaCesDpQosFlowName_Object = MibTableColumn
cienaCesDpQosFlowName = _CienaCesDpQosFlowName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 2),
    _CienaCesDpQosFlowName_Type()
)
cienaCesDpQosFlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowName.setStatus("current")
_CienaCesDpQosFlowClassifierPrecedence_Type = Unsigned32
_CienaCesDpQosFlowClassifierPrecedence_Object = MibTableColumn
cienaCesDpQosFlowClassifierPrecedence = _CienaCesDpQosFlowClassifierPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 3),
    _CienaCesDpQosFlowClassifierPrecedence_Type()
)
cienaCesDpQosFlowClassifierPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowClassifierPrecedence.setStatus("current")
_CienaCesDpQosFlowParentIfId_Type = Integer32
_CienaCesDpQosFlowParentIfId_Object = MibTableColumn
cienaCesDpQosFlowParentIfId = _CienaCesDpQosFlowParentIfId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 4),
    _CienaCesDpQosFlowParentIfId_Type()
)
cienaCesDpQosFlowParentIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowParentIfId.setStatus("current")
_CienaCesDpQosFlowParentIfType_Type = DpTsAttachType
_CienaCesDpQosFlowParentIfType_Object = MibTableColumn
cienaCesDpQosFlowParentIfType = _CienaCesDpQosFlowParentIfType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 5),
    _CienaCesDpQosFlowParentIfType_Type()
)
cienaCesDpQosFlowParentIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowParentIfType.setStatus("current")
_CienaCesDpQosFlowIngressMeterProfileId_Type = Integer32
_CienaCesDpQosFlowIngressMeterProfileId_Object = MibTableColumn
cienaCesDpQosFlowIngressMeterProfileId = _CienaCesDpQosFlowIngressMeterProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 6),
    _CienaCesDpQosFlowIngressMeterProfileId_Type()
)
cienaCesDpQosFlowIngressMeterProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowIngressMeterProfileId.setStatus("current")
_CienaCesDpQosFlowIngressMeterProfileName_Type = OctetString
_CienaCesDpQosFlowIngressMeterProfileName_Object = MibTableColumn
cienaCesDpQosFlowIngressMeterProfileName = _CienaCesDpQosFlowIngressMeterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 7),
    _CienaCesDpQosFlowIngressMeterProfileName_Type()
)
cienaCesDpQosFlowIngressMeterProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowIngressMeterProfileName.setStatus("current")


class _CienaCesDpQosFlowIngressMeterPolicy_Type(DpIngressMeterPolicy):
    """Custom type cienaCesDpQosFlowIngressMeterPolicy based on DpIngressMeterPolicy"""
    defaultValue = 1


_CienaCesDpQosFlowIngressMeterPolicy_Type.__name__ = "DpIngressMeterPolicy"
_CienaCesDpQosFlowIngressMeterPolicy_Object = MibTableColumn
cienaCesDpQosFlowIngressMeterPolicy = _CienaCesDpQosFlowIngressMeterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 8),
    _CienaCesDpQosFlowIngressMeterPolicy_Type()
)
cienaCesDpQosFlowIngressMeterPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowIngressMeterPolicy.setStatus("current")
_CienaCesDpQosFlowIngressRcosProfileId_Type = Integer32
_CienaCesDpQosFlowIngressRcosProfileId_Object = MibTableColumn
cienaCesDpQosFlowIngressRcosProfileId = _CienaCesDpQosFlowIngressRcosProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 9),
    _CienaCesDpQosFlowIngressRcosProfileId_Type()
)
cienaCesDpQosFlowIngressRcosProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowIngressRcosProfileId.setStatus("current")
_CienaCesDpQosFlowIngressRcosProfileName_Type = OctetString
_CienaCesDpQosFlowIngressRcosProfileName_Object = MibTableColumn
cienaCesDpQosFlowIngressRcosProfileName = _CienaCesDpQosFlowIngressRcosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 10),
    _CienaCesDpQosFlowIngressRcosProfileName_Type()
)
cienaCesDpQosFlowIngressRcosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowIngressRcosProfileName.setStatus("current")


class _CienaCesDpQosFlowIngressRcosPolicy_Type(Integer32):
    """Custom type cienaCesDpQosFlowIngressRcosPolicy based on Integer32"""
    defaultValue = 3

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
        *(("ignore", 1),
          ("fixed", 2),
          ("dot1dToRcosTag1", 3),
          ("dot1dToRcosTag2", 4),
          ("dscpToRcos", 5),
          ("dscpMplsTcToRcos", 6))
    )


_CienaCesDpQosFlowIngressRcosPolicy_Type.__name__ = "Integer32"
_CienaCesDpQosFlowIngressRcosPolicy_Object = MibTableColumn
cienaCesDpQosFlowIngressRcosPolicy = _CienaCesDpQosFlowIngressRcosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 9, 1, 1, 11),
    _CienaCesDpQosFlowIngressRcosPolicy_Type()
)
cienaCesDpQosFlowIngressRcosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpQosFlowIngressRcosPolicy.setStatus("current")
_CienaCesDpAccessFlow_ObjectIdentity = ObjectIdentity
cienaCesDpAccessFlow = _CienaCesDpAccessFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 10)
)
_CienaCesDpAccessFlowTable_Object = MibTable
cienaCesDpAccessFlowTable = _CienaCesDpAccessFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpAccessFlowTable.setStatus("current")
_CienaCesDpAccessFlowEntry_Object = MibTableRow
cienaCesDpAccessFlowEntry = _CienaCesDpAccessFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 10, 1, 1)
)
cienaCesDpAccessFlowEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpAccessFlowLiIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpAccessFlowEntry.setStatus("current")


class _CienaCesDpAccessFlowLiIndex_Type(Integer32):
    """Custom type cienaCesDpAccessFlowLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CienaCesDpAccessFlowLiIndex_Type.__name__ = "Integer32"
_CienaCesDpAccessFlowLiIndex_Object = MibTableColumn
cienaCesDpAccessFlowLiIndex = _CienaCesDpAccessFlowLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 10, 1, 1, 1),
    _CienaCesDpAccessFlowLiIndex_Type()
)
cienaCesDpAccessFlowLiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpAccessFlowLiIndex.setStatus("current")
_CienaCesDpAccessFlowName_Type = DisplayString
_CienaCesDpAccessFlowName_Object = MibTableColumn
cienaCesDpAccessFlowName = _CienaCesDpAccessFlowName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 10, 1, 1, 2),
    _CienaCesDpAccessFlowName_Type()
)
cienaCesDpAccessFlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpAccessFlowName.setStatus("current")
_CienaCesDpAccessFlowClassifierPrecedence_Type = Unsigned32
_CienaCesDpAccessFlowClassifierPrecedence_Object = MibTableColumn
cienaCesDpAccessFlowClassifierPrecedence = _CienaCesDpAccessFlowClassifierPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 10, 1, 1, 3),
    _CienaCesDpAccessFlowClassifierPrecedence_Type()
)
cienaCesDpAccessFlowClassifierPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpAccessFlowClassifierPrecedence.setStatus("current")
_CienaCesDpAccessFlowParentIfId_Type = Integer32
_CienaCesDpAccessFlowParentIfId_Object = MibTableColumn
cienaCesDpAccessFlowParentIfId = _CienaCesDpAccessFlowParentIfId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 10, 1, 1, 4),
    _CienaCesDpAccessFlowParentIfId_Type()
)
cienaCesDpAccessFlowParentIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpAccessFlowParentIfId.setStatus("current")
_CienaCesDpAccessFlowParentIfType_Type = DpTsAttachType
_CienaCesDpAccessFlowParentIfType_Object = MibTableColumn
cienaCesDpAccessFlowParentIfType = _CienaCesDpAccessFlowParentIfType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 10, 1, 1, 5),
    _CienaCesDpAccessFlowParentIfType_Type()
)
cienaCesDpAccessFlowParentIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpAccessFlowParentIfType.setStatus("current")


class _CienaCesDpAccessFlowFilterPolicy_Type(Integer32):
    """Custom type cienaCesDpAccessFlowFilterPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("l2ptmactranslation", 3))
    )


_CienaCesDpAccessFlowFilterPolicy_Type.__name__ = "Integer32"
_CienaCesDpAccessFlowFilterPolicy_Object = MibTableColumn
cienaCesDpAccessFlowFilterPolicy = _CienaCesDpAccessFlowFilterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 10, 1, 1, 6),
    _CienaCesDpAccessFlowFilterPolicy_Type()
)
cienaCesDpAccessFlowFilterPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpAccessFlowFilterPolicy.setStatus("current")
_CienaCesDpPbtTransit_ObjectIdentity = ObjectIdentity
cienaCesDpPbtTransit = _CienaCesDpPbtTransit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11)
)
_CienaCesDpPbtTransitTable_Object = MibTable
cienaCesDpPbtTransitTable = _CienaCesDpPbtTransitTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitTable.setStatus("current")
_CienaCesDpPbtTransitEntry_Object = MibTableRow
cienaCesDpPbtTransitEntry = _CienaCesDpPbtTransitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1)
)
cienaCesDpPbtTransitEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpPbtTransitLiIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitEntry.setStatus("current")


class _CienaCesDpPbtTransitLiIndex_Type(Integer32):
    """Custom type cienaCesDpPbtTransitLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CienaCesDpPbtTransitLiIndex_Type.__name__ = "Integer32"
_CienaCesDpPbtTransitLiIndex_Object = MibTableColumn
cienaCesDpPbtTransitLiIndex = _CienaCesDpPbtTransitLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 1),
    _CienaCesDpPbtTransitLiIndex_Type()
)
cienaCesDpPbtTransitLiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitLiIndex.setStatus("current")
_CienaCesDpPbtTransitName_Type = DisplayString
_CienaCesDpPbtTransitName_Object = MibTableColumn
cienaCesDpPbtTransitName = _CienaCesDpPbtTransitName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 2),
    _CienaCesDpPbtTransitName_Type()
)
cienaCesDpPbtTransitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitName.setStatus("current")
_CienaCesDpPbtTransitParentIfId_Type = Integer32
_CienaCesDpPbtTransitParentIfId_Object = MibTableColumn
cienaCesDpPbtTransitParentIfId = _CienaCesDpPbtTransitParentIfId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 3),
    _CienaCesDpPbtTransitParentIfId_Type()
)
cienaCesDpPbtTransitParentIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitParentIfId.setStatus("current")
_CienaCesDpPbtTransitIngressMeterProfileId_Type = Integer32
_CienaCesDpPbtTransitIngressMeterProfileId_Object = MibTableColumn
cienaCesDpPbtTransitIngressMeterProfileId = _CienaCesDpPbtTransitIngressMeterProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 4),
    _CienaCesDpPbtTransitIngressMeterProfileId_Type()
)
cienaCesDpPbtTransitIngressMeterProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressMeterProfileId.setStatus("current")
_CienaCesDpPbtTransitIngressMeterProfileName_Type = OctetString
_CienaCesDpPbtTransitIngressMeterProfileName_Object = MibTableColumn
cienaCesDpPbtTransitIngressMeterProfileName = _CienaCesDpPbtTransitIngressMeterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 5),
    _CienaCesDpPbtTransitIngressMeterProfileName_Type()
)
cienaCesDpPbtTransitIngressMeterProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressMeterProfileName.setStatus("current")
_CienaCesDpPbtTransitIngressFloodContainerId_Type = Integer32
_CienaCesDpPbtTransitIngressFloodContainerId_Object = MibTableColumn
cienaCesDpPbtTransitIngressFloodContainerId = _CienaCesDpPbtTransitIngressFloodContainerId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 6),
    _CienaCesDpPbtTransitIngressFloodContainerId_Type()
)
cienaCesDpPbtTransitIngressFloodContainerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressFloodContainerId.setStatus("current")
_CienaCesDpPbtTransitIngressFloodContainerName_Type = OctetString
_CienaCesDpPbtTransitIngressFloodContainerName_Object = MibTableColumn
cienaCesDpPbtTransitIngressFloodContainerName = _CienaCesDpPbtTransitIngressFloodContainerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 7),
    _CienaCesDpPbtTransitIngressFloodContainerName_Type()
)
cienaCesDpPbtTransitIngressFloodContainerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressFloodContainerName.setStatus("current")
_CienaCesDpPbtTransitIngressRcosProfileId_Type = Integer32
_CienaCesDpPbtTransitIngressRcosProfileId_Object = MibTableColumn
cienaCesDpPbtTransitIngressRcosProfileId = _CienaCesDpPbtTransitIngressRcosProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 8),
    _CienaCesDpPbtTransitIngressRcosProfileId_Type()
)
cienaCesDpPbtTransitIngressRcosProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressRcosProfileId.setStatus("current")
_CienaCesDpPbtTransitIngressRcosProfileName_Type = OctetString
_CienaCesDpPbtTransitIngressRcosProfileName_Object = MibTableColumn
cienaCesDpPbtTransitIngressRcosProfileName = _CienaCesDpPbtTransitIngressRcosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 9),
    _CienaCesDpPbtTransitIngressRcosProfileName_Type()
)
cienaCesDpPbtTransitIngressRcosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressRcosProfileName.setStatus("current")


class _CienaCesDpPbtTransitIngressRcosPolicy_Type(Integer32):
    """Custom type cienaCesDpPbtTransitIngressRcosPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("fixed", 2),
          ("bvidPcpToRcos", 3))
    )


_CienaCesDpPbtTransitIngressRcosPolicy_Type.__name__ = "Integer32"
_CienaCesDpPbtTransitIngressRcosPolicy_Object = MibTableColumn
cienaCesDpPbtTransitIngressRcosPolicy = _CienaCesDpPbtTransitIngressRcosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 10),
    _CienaCesDpPbtTransitIngressRcosPolicy_Type()
)
cienaCesDpPbtTransitIngressRcosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressRcosPolicy.setStatus("current")


class _CienaCesDpPbtTransitIngressFcosMapId_Type(Integer32):
    """Custom type cienaCesDpPbtTransitIngressFcosMapId based on Integer32"""
    defaultValue = 0


_CienaCesDpPbtTransitIngressFcosMapId_Type.__name__ = "Integer32"
_CienaCesDpPbtTransitIngressFcosMapId_Object = MibTableColumn
cienaCesDpPbtTransitIngressFcosMapId = _CienaCesDpPbtTransitIngressFcosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 11),
    _CienaCesDpPbtTransitIngressFcosMapId_Type()
)
cienaCesDpPbtTransitIngressFcosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressFcosMapId.setStatus("current")
_CienaCesDpPbtTransitIngressFcosMapName_Type = OctetString
_CienaCesDpPbtTransitIngressFcosMapName_Object = MibTableColumn
cienaCesDpPbtTransitIngressFcosMapName = _CienaCesDpPbtTransitIngressFcosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 12),
    _CienaCesDpPbtTransitIngressFcosMapName_Type()
)
cienaCesDpPbtTransitIngressFcosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressFcosMapName.setStatus("current")


class _CienaCesDpPbtTransitEgressFcosMapId_Type(Integer32):
    """Custom type cienaCesDpPbtTransitEgressFcosMapId based on Integer32"""
    defaultValue = 0


_CienaCesDpPbtTransitEgressFcosMapId_Type.__name__ = "Integer32"
_CienaCesDpPbtTransitEgressFcosMapId_Object = MibTableColumn
cienaCesDpPbtTransitEgressFcosMapId = _CienaCesDpPbtTransitEgressFcosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 13),
    _CienaCesDpPbtTransitEgressFcosMapId_Type()
)
cienaCesDpPbtTransitEgressFcosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitEgressFcosMapId.setStatus("current")
_CienaCesDpPbtTransitEgressFcosMapName_Type = OctetString
_CienaCesDpPbtTransitEgressFcosMapName_Object = MibTableColumn
cienaCesDpPbtTransitEgressFcosMapName = _CienaCesDpPbtTransitEgressFcosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 14),
    _CienaCesDpPbtTransitEgressFcosMapName_Type()
)
cienaCesDpPbtTransitEgressFcosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitEgressFcosMapName.setStatus("current")
_CienaCesDpPbtTransitIngressBvidTransform_Type = OctetString
_CienaCesDpPbtTransitIngressBvidTransform_Object = MibTableColumn
cienaCesDpPbtTransitIngressBvidTransform = _CienaCesDpPbtTransitIngressBvidTransform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 15),
    _CienaCesDpPbtTransitIngressBvidTransform_Type()
)
cienaCesDpPbtTransitIngressBvidTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressBvidTransform.setStatus("current")
_CienaCesDpPbtTransitEgressBvidTransform_Type = OctetString
_CienaCesDpPbtTransitEgressBvidTransform_Object = MibTableColumn
cienaCesDpPbtTransitEgressBvidTransform = _CienaCesDpPbtTransitEgressBvidTransform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 16),
    _CienaCesDpPbtTransitEgressBvidTransform_Type()
)
cienaCesDpPbtTransitEgressBvidTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitEgressBvidTransform.setStatus("current")


class _CienaCesDpPbtTransitVirtualSwitchId_Type(Integer32):
    """Custom type cienaCesDpPbtTransitVirtualSwitchId based on Integer32"""
    defaultValue = 0


_CienaCesDpPbtTransitVirtualSwitchId_Type.__name__ = "Integer32"
_CienaCesDpPbtTransitVirtualSwitchId_Object = MibTableColumn
cienaCesDpPbtTransitVirtualSwitchId = _CienaCesDpPbtTransitVirtualSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 17),
    _CienaCesDpPbtTransitVirtualSwitchId_Type()
)
cienaCesDpPbtTransitVirtualSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitVirtualSwitchId.setStatus("current")


class _CienaCesDpPbtTransitRlanId_Type(Integer32):
    """Custom type cienaCesDpPbtTransitRlanId based on Integer32"""
    defaultValue = 0


_CienaCesDpPbtTransitRlanId_Type.__name__ = "Integer32"
_CienaCesDpPbtTransitRlanId_Object = MibTableColumn
cienaCesDpPbtTransitRlanId = _CienaCesDpPbtTransitRlanId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 18),
    _CienaCesDpPbtTransitRlanId_Type()
)
cienaCesDpPbtTransitRlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitRlanId.setStatus("current")
_CienaCesDpPbtTransitVirtualSwitchName_Type = OctetString
_CienaCesDpPbtTransitVirtualSwitchName_Object = MibTableColumn
cienaCesDpPbtTransitVirtualSwitchName = _CienaCesDpPbtTransitVirtualSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 19),
    _CienaCesDpPbtTransitVirtualSwitchName_Type()
)
cienaCesDpPbtTransitVirtualSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitVirtualSwitchName.setStatus("current")


class _CienaCesDpPbtTransitPrivateFwdGroup_Type(Integer32):
    """Custom type cienaCesDpPbtTransitPrivateFwdGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("groupA", 1),
          ("groupB", 2),
          ("groupC", 3))
    )


_CienaCesDpPbtTransitPrivateFwdGroup_Type.__name__ = "Integer32"
_CienaCesDpPbtTransitPrivateFwdGroup_Object = MibTableColumn
cienaCesDpPbtTransitPrivateFwdGroup = _CienaCesDpPbtTransitPrivateFwdGroup_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 20),
    _CienaCesDpPbtTransitPrivateFwdGroup_Type()
)
cienaCesDpPbtTransitPrivateFwdGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitPrivateFwdGroup.setStatus("current")


class _CienaCesDpPbtTransitIngressMeterPolicy_Type(DpIngressMeterPolicy):
    """Custom type cienaCesDpPbtTransitIngressMeterPolicy based on DpIngressMeterPolicy"""
    defaultValue = 1


_CienaCesDpPbtTransitIngressMeterPolicy_Type.__name__ = "DpIngressMeterPolicy"
_CienaCesDpPbtTransitIngressMeterPolicy_Object = MibTableColumn
cienaCesDpPbtTransitIngressMeterPolicy = _CienaCesDpPbtTransitIngressMeterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 11, 1, 1, 21),
    _CienaCesDpPbtTransitIngressMeterPolicy_Type()
)
cienaCesDpPbtTransitIngressMeterPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPbtTransitIngressMeterPolicy.setStatus("current")
_CienaCesDpCpuSubInterface_ObjectIdentity = ObjectIdentity
cienaCesDpCpuSubInterface = _CienaCesDpCpuSubInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12)
)
_CienaCesDpCpuSubInterfaceTable_Object = MibTable
cienaCesDpCpuSubInterfaceTable = _CienaCesDpCpuSubInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceTable.setStatus("current")
_CienaCesDpCpuSubInterfaceEntry_Object = MibTableRow
cienaCesDpCpuSubInterfaceEntry = _CienaCesDpCpuSubInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1)
)
cienaCesDpCpuSubInterfaceEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpCpuSubInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceEntry.setStatus("current")
_CienaCesDpCpuSubInterfaceIndex_Type = Unsigned32
_CienaCesDpCpuSubInterfaceIndex_Object = MibTableColumn
cienaCesDpCpuSubInterfaceIndex = _CienaCesDpCpuSubInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 1),
    _CienaCesDpCpuSubInterfaceIndex_Type()
)
cienaCesDpCpuSubInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceIndex.setStatus("current")
_CienaCesDpCpuSubInterfaceName_Type = OctetString
_CienaCesDpCpuSubInterfaceName_Object = MibTableColumn
cienaCesDpCpuSubInterfaceName = _CienaCesDpCpuSubInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 2),
    _CienaCesDpCpuSubInterfaceName_Type()
)
cienaCesDpCpuSubInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceName.setStatus("current")
_CienaCesDpCpuSubInterfaceEgressL2Transform_Type = OctetString
_CienaCesDpCpuSubInterfaceEgressL2Transform_Object = MibTableColumn
cienaCesDpCpuSubInterfaceEgressL2Transform = _CienaCesDpCpuSubInterfaceEgressL2Transform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 3),
    _CienaCesDpCpuSubInterfaceEgressL2Transform_Type()
)
cienaCesDpCpuSubInterfaceEgressL2Transform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceEgressL2Transform.setStatus("current")
_CienaCesDpCpuSubInterfaceIngressL2Transform_Type = OctetString
_CienaCesDpCpuSubInterfaceIngressL2Transform_Object = MibTableColumn
cienaCesDpCpuSubInterfaceIngressL2Transform = _CienaCesDpCpuSubInterfaceIngressL2Transform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 4),
    _CienaCesDpCpuSubInterfaceIngressL2Transform_Type()
)
cienaCesDpCpuSubInterfaceIngressL2Transform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceIngressL2Transform.setStatus("current")


class _CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Type(Integer32):
    """Custom type cienaCesDpCpuSubInterfaceEgressL3TransformPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leave", 1),
          ("mappedDscp", 2))
    )


_CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Type.__name__ = "Integer32"
_CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Object = MibTableColumn
cienaCesDpCpuSubInterfaceEgressL3TransformPolicy = _CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 5),
    _CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Type()
)
cienaCesDpCpuSubInterfaceEgressL3TransformPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceEgressL3TransformPolicy.setStatus("current")


class _CienaCesDpCpuSubInterfaceEgressRCosPolicy_Type(Integer32):
    """Custom type cienaCesDpCpuSubInterfaceEgressRCosPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("fixed-cos", 1),
          ("none", 99))
    )


_CienaCesDpCpuSubInterfaceEgressRCosPolicy_Type.__name__ = "Integer32"
_CienaCesDpCpuSubInterfaceEgressRCosPolicy_Object = MibTableColumn
cienaCesDpCpuSubInterfaceEgressRCosPolicy = _CienaCesDpCpuSubInterfaceEgressRCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 6),
    _CienaCesDpCpuSubInterfaceEgressRCosPolicy_Type()
)
cienaCesDpCpuSubInterfaceEgressRCosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceEgressRCosPolicy.setStatus("current")
_CienaCesDpCpuSubInterfaceEgressRCosProfileIndex_Type = Unsigned32
_CienaCesDpCpuSubInterfaceEgressRCosProfileIndex_Object = MibTableColumn
cienaCesDpCpuSubInterfaceEgressRCosProfileIndex = _CienaCesDpCpuSubInterfaceEgressRCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 7),
    _CienaCesDpCpuSubInterfaceEgressRCosProfileIndex_Type()
)
cienaCesDpCpuSubInterfaceEgressRCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceEgressRCosProfileIndex.setStatus("current")
_CienaCesDpCpuSubInterfaceEgressRCosProfile_Type = OctetString
_CienaCesDpCpuSubInterfaceEgressRCosProfile_Object = MibTableColumn
cienaCesDpCpuSubInterfaceEgressRCosProfile = _CienaCesDpCpuSubInterfaceEgressRCosProfile_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 8),
    _CienaCesDpCpuSubInterfaceEgressRCosProfile_Type()
)
cienaCesDpCpuSubInterfaceEgressRCosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceEgressRCosProfile.setStatus("current")


class _CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Type(Unsigned32):
    """Custom type cienaCesDpCpuSubInterfaceVirtualSwitchIndex based on Unsigned32"""
    defaultValue = 0


_CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Type.__name__ = "Unsigned32"
_CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Object = MibTableColumn
cienaCesDpCpuSubInterfaceVirtualSwitchIndex = _CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 9),
    _CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Type()
)
cienaCesDpCpuSubInterfaceVirtualSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceVirtualSwitchIndex.setStatus("current")
_CienaCesDpCpuSubInterfaceRlanIndex_Type = Unsigned32
_CienaCesDpCpuSubInterfaceRlanIndex_Object = MibTableColumn
cienaCesDpCpuSubInterfaceRlanIndex = _CienaCesDpCpuSubInterfaceRlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 10),
    _CienaCesDpCpuSubInterfaceRlanIndex_Type()
)
cienaCesDpCpuSubInterfaceRlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceRlanIndex.setStatus("current")
_CienaCesDpCpuSubInterfaceVirtualSwitchName_Type = OctetString
_CienaCesDpCpuSubInterfaceVirtualSwitchName_Object = MibTableColumn
cienaCesDpCpuSubInterfaceVirtualSwitchName = _CienaCesDpCpuSubInterfaceVirtualSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 12, 1, 1, 11),
    _CienaCesDpCpuSubInterfaceVirtualSwitchName_Type()
)
cienaCesDpCpuSubInterfaceVirtualSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpCpuSubInterfaceVirtualSwitchName.setStatus("current")
_CienaCesDpPfgProfile_ObjectIdentity = ObjectIdentity
cienaCesDpPfgProfile = _CienaCesDpPfgProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 13)
)
_CienaCesDpPfgProfileTable_Object = MibTable
cienaCesDpPfgProfileTable = _CienaCesDpPfgProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 13, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpPfgProfileTable.setStatus("current")
_CienaCesDpPfgProfileEntry_Object = MibTableRow
cienaCesDpPfgProfileEntry = _CienaCesDpPfgProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 13, 1, 1)
)
cienaCesDpPfgProfileEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpPfgProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpPfgProfileEntry.setStatus("current")


class _CienaCesDpPfgProfileIndex_Type(Integer32):
    """Custom type cienaCesDpPfgProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesDpPfgProfileIndex_Type.__name__ = "Integer32"
_CienaCesDpPfgProfileIndex_Object = MibTableColumn
cienaCesDpPfgProfileIndex = _CienaCesDpPfgProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 13, 1, 1, 1),
    _CienaCesDpPfgProfileIndex_Type()
)
cienaCesDpPfgProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpPfgProfileIndex.setStatus("current")
_CienaCesDpPfgProfileName_Type = DisplayString
_CienaCesDpPfgProfileName_Object = MibTableColumn
cienaCesDpPfgProfileName = _CienaCesDpPfgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 13, 1, 1, 2),
    _CienaCesDpPfgProfileName_Type()
)
cienaCesDpPfgProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPfgProfileName.setStatus("current")


class _CienaCesDpPfgProfileAPolicy_Type(PrivateForwardGroupPolicy):
    """Custom type cienaCesDpPfgProfileAPolicy based on PrivateForwardGroupPolicy"""
    defaultValue = 7


_CienaCesDpPfgProfileAPolicy_Type.__name__ = "PrivateForwardGroupPolicy"
_CienaCesDpPfgProfileAPolicy_Object = MibTableColumn
cienaCesDpPfgProfileAPolicy = _CienaCesDpPfgProfileAPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 13, 1, 1, 3),
    _CienaCesDpPfgProfileAPolicy_Type()
)
cienaCesDpPfgProfileAPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPfgProfileAPolicy.setStatus("current")


class _CienaCesDpPfgProfileBPolicy_Type(PrivateForwardGroupPolicy):
    """Custom type cienaCesDpPfgProfileBPolicy based on PrivateForwardGroupPolicy"""
    defaultValue = 7


_CienaCesDpPfgProfileBPolicy_Type.__name__ = "PrivateForwardGroupPolicy"
_CienaCesDpPfgProfileBPolicy_Object = MibTableColumn
cienaCesDpPfgProfileBPolicy = _CienaCesDpPfgProfileBPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 13, 1, 1, 4),
    _CienaCesDpPfgProfileBPolicy_Type()
)
cienaCesDpPfgProfileBPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPfgProfileBPolicy.setStatus("current")


class _CienaCesDpPfgProfileCPolicy_Type(PrivateForwardGroupPolicy):
    """Custom type cienaCesDpPfgProfileCPolicy based on PrivateForwardGroupPolicy"""
    defaultValue = 7


_CienaCesDpPfgProfileCPolicy_Type.__name__ = "PrivateForwardGroupPolicy"
_CienaCesDpPfgProfileCPolicy_Object = MibTableColumn
cienaCesDpPfgProfileCPolicy = _CienaCesDpPfgProfileCPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 13, 1, 1, 5),
    _CienaCesDpPfgProfileCPolicy_Type()
)
cienaCesDpPfgProfileCPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpPfgProfileCPolicy.setStatus("current")
_CienaCesDpL2CftProfile_ObjectIdentity = ObjectIdentity
cienaCesDpL2CftProfile = _CienaCesDpL2CftProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14)
)
_CienaCesDpL2CftProfileTable_Object = MibTable
cienaCesDpL2CftProfileTable = _CienaCesDpL2CftProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cienaCesDpL2CftProfileTable.setStatus("current")
_CienaCesDpL2CftProfileEntry_Object = MibTableRow
cienaCesDpL2CftProfileEntry = _CienaCesDpL2CftProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14, 1, 1)
)
cienaCesDpL2CftProfileEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpL2CftProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesDpL2CftProfileEntry.setStatus("current")
_CienaCesDpL2CftProfileIndex_Type = Integer32
_CienaCesDpL2CftProfileIndex_Object = MibTableColumn
cienaCesDpL2CftProfileIndex = _CienaCesDpL2CftProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14, 1, 1, 1),
    _CienaCesDpL2CftProfileIndex_Type()
)
cienaCesDpL2CftProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpL2CftProfileIndex.setStatus("current")
_CienaCesDpL2CftProfileName_Type = DisplayString
_CienaCesDpL2CftProfileName_Object = MibTableColumn
cienaCesDpL2CftProfileName = _CienaCesDpL2CftProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14, 1, 1, 2),
    _CienaCesDpL2CftProfileName_Type()
)
cienaCesDpL2CftProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpL2CftProfileName.setStatus("current")


class _CienaCesDpL2CftProfileL2ControlRcos_Type(Integer32):
    """Custom type cienaCesDpL2CftProfileL2ControlRcos based on Integer32"""
    defaultValue = 48


_CienaCesDpL2CftProfileL2ControlRcos_Type.__name__ = "Integer32"
_CienaCesDpL2CftProfileL2ControlRcos_Object = MibTableColumn
cienaCesDpL2CftProfileL2ControlRcos = _CienaCesDpL2CftProfileL2ControlRcos_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14, 1, 1, 3),
    _CienaCesDpL2CftProfileL2ControlRcos_Type()
)
cienaCesDpL2CftProfileL2ControlRcos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpL2CftProfileL2ControlRcos.setStatus("current")
_CienaCesDpL2CftProfileL2CftProtocolTable_Object = MibTable
cienaCesDpL2CftProfileL2CftProtocolTable = _CienaCesDpL2CftProfileL2CftProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14, 2)
)
if mibBuilder.loadTexts:
    cienaCesDpL2CftProfileL2CftProtocolTable.setStatus("current")
_CienaCesDpL2CftProfileL2CftProtocolEntry_Object = MibTableRow
cienaCesDpL2CftProfileL2CftProtocolEntry = _CienaCesDpL2CftProfileL2CftProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14, 2, 1)
)
cienaCesDpL2CftProfileL2CftProtocolEntry.setIndexNames(
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpL2CftProfileIndex"),
    (0, "CIENA-CES-DATAPLANE-MIB", "cienaCesDpL2CftProfileL2CftProtocolType"),
)
if mibBuilder.loadTexts:
    cienaCesDpL2CftProfileL2CftProtocolEntry.setStatus("current")


class _CienaCesDpL2CftProfileL2CftProtocolType_Type(Integer32):
    """Custom type cienaCesDpL2CftProfileL2CftProtocolType based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ciscoCdp", 1),
          ("ciscoDtp", 2),
          ("ciscoPagp", 3),
          ("ciscoUdld", 4),
          ("ciscoVtp", 5),
          ("ciscoPvst", 6),
          ("ciscoStpUplinkFast", 7),
          ("vlanBridge", 8),
          ("rstp", 9),
          ("lacp", 10),
          ("lacpMarker", 11),
          ("oam", 12),
          ("lldp", 13),
          ("i8021x", 14),
          ("gmrp", 15),
          ("gvrp", 16),
          ("isis", 17),
          ("esmc", 18),
          ("bridgeReserved0C0D", 19),
          ("bridgeReserved0B0F", 20),
          ("brigeBlock", 21),
          ("allBridgesBlock", 22),
          ("garpBlock", 23))
    )


_CienaCesDpL2CftProfileL2CftProtocolType_Type.__name__ = "Integer32"
_CienaCesDpL2CftProfileL2CftProtocolType_Object = MibTableColumn
cienaCesDpL2CftProfileL2CftProtocolType = _CienaCesDpL2CftProfileL2CftProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14, 2, 1, 1),
    _CienaCesDpL2CftProfileL2CftProtocolType_Type()
)
cienaCesDpL2CftProfileL2CftProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesDpL2CftProfileL2CftProtocolType.setStatus("current")


class _CienaCesDpL2CftProfileL2CftProtocolDisposition_Type(Integer32):
    """Custom type cienaCesDpL2CftProfileL2CftProtocolDisposition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_CienaCesDpL2CftProfileL2CftProtocolDisposition_Type.__name__ = "Integer32"
_CienaCesDpL2CftProfileL2CftProtocolDisposition_Object = MibTableColumn
cienaCesDpL2CftProfileL2CftProtocolDisposition = _CienaCesDpL2CftProfileL2CftProtocolDisposition_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 7, 1, 14, 2, 1, 2),
    _CienaCesDpL2CftProfileL2CftProtocolDisposition_Type()
)
cienaCesDpL2CftProfileL2CftProtocolDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesDpL2CftProfileL2CftProtocolDisposition.setStatus("current")
_CienaCesDpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesDpMIBNotificationPrefix = _CienaCesDpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7)
)
_CienaCesDpMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesDpMIBNotifications = _CienaCesDpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0)
)

# Managed Objects groups


# Notification objects

cienaCesDpTsMeterFloodContainerUcastThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 1)
)
cienaCesDpTsMeterFloodContainerUcastThresholdExceeded.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifProfileIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiType"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerUcastThresholdExceeded.setStatus(
        "current"
    )

cienaCesDpTsMeterFloodContainerUcastThresholdNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 2)
)
cienaCesDpTsMeterFloodContainerUcastThresholdNormal.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifProfileIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiType"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerUcastThresholdNormal.setStatus(
        "current"
    )

cienaCesDpTsMeterFloodContainerBcastThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 3)
)
cienaCesDpTsMeterFloodContainerBcastThresholdExceeded.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifProfileIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiType"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerBcastThresholdExceeded.setStatus(
        "current"
    )

cienaCesDpTsMeterFloodContainerBcastThresholdNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 4)
)
cienaCesDpTsMeterFloodContainerBcastThresholdNormal.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifProfileIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiType"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerBcastThresholdNormal.setStatus(
        "current"
    )

cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 5)
)
cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifProfileIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiType"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded.setStatus(
        "current"
    )

cienaCesDpTsMeterFloodContainerL2McastThresholdNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 6)
)
cienaCesDpTsMeterFloodContainerL2McastThresholdNormal.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifProfileIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiType"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerL2McastThresholdNormal.setStatus(
        "current"
    )

cienaCesDataplaneEgressReflectorEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 7)
)
cienaCesDataplaneEgressReflectorEnabled.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpSubPortName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpSubPortLiIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpSubPortEgressReflectorMac"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpSubPortEgressGeneratorMac"))
)
if mibBuilder.loadTexts:
    cienaCesDataplaneEgressReflectorEnabled.setStatus(
        "current"
    )

cienaCesDataplaneEgressReflectorDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 8)
)
cienaCesDataplaneEgressReflectorDisabled.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpSubPortName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpSubPortLiIndex"))
)
if mibBuilder.loadTexts:
    cienaCesDataplaneEgressReflectorDisabled.setStatus(
        "current"
    )

cienaCesDpPortShapingSubscriptionExceedsOperSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 9)
)
cienaCesDpPortShapingSubscriptionExceedsOperSpeed.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortName"))
)
if mibBuilder.loadTexts:
    cienaCesDpPortShapingSubscriptionExceedsOperSpeed.setStatus(
        "current"
    )

cienaCesDpPortShapingSubscriptionWithinOperSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 10)
)
cienaCesDpPortShapingSubscriptionWithinOperSpeed.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortName"))
)
if mibBuilder.loadTexts:
    cienaCesDpPortShapingSubscriptionWithinOperSpeed.setStatus(
        "current"
    )

cienaCesDpTsMeterFloodContainerTotalThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 11)
)
cienaCesDpTsMeterFloodContainerTotalThresholdExceeded.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifProfileIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiType"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerTotalThresholdExceeded.setStatus(
        "current"
    )

cienaCesDpTsMeterFloodContainerTotalThresholdNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 7, 0, 12)
)
cienaCesDpTsMeterFloodContainerTotalThresholdNormal.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifProfileIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiType"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerProfileName"),
        ("CIENA-CES-DATAPLANE-MIB", "cienaCesDpTsMeterFloodContainerAttachmentInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesDpTsMeterFloodContainerTotalThresholdNormal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-DATAPLANE-MIB",
    **{"DpTsAttachType": DpTsAttachType,
       "PrivateForwardGroupPolicy": PrivateForwardGroupPolicy,
       "DpCouplingFlag": DpCouplingFlag,
       "DpIngressMeterPolicy": DpIngressMeterPolicy,
       "DpSchedulingType": DpSchedulingType,
       "cienaCesDataplaneMIB": cienaCesDataplaneMIB,
       "cienaCesDpMIBObjects": cienaCesDpMIBObjects,
       "cienaCesDpTsMeterFloodContainerNotifAttrs": cienaCesDpTsMeterFloodContainerNotifAttrs,
       "cienaCesDpTsMeterFloodContainerProfileTable": cienaCesDpTsMeterFloodContainerProfileTable,
       "cienaCesDpTsMeterFloodContainerProfileEntry": cienaCesDpTsMeterFloodContainerProfileEntry,
       "cienaCesDpTsMeterFloodContainerProfileIndex": cienaCesDpTsMeterFloodContainerProfileIndex,
       "cienaCesDpTsMeterFloodContainerProfileName": cienaCesDpTsMeterFloodContainerProfileName,
       "cienaCesDpTsMeterFloodContainerNotifProfileIndex": cienaCesDpTsMeterFloodContainerNotifProfileIndex,
       "cienaCesDpTsMeterFloodContainerProfileRate1": cienaCesDpTsMeterFloodContainerProfileRate1,
       "cienaCesDpTsMeterFloodContainerProfileRate2": cienaCesDpTsMeterFloodContainerProfileRate2,
       "cienaCesDpTsMeterFloodContainerProfileRate3": cienaCesDpTsMeterFloodContainerProfileRate3,
       "cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId": cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId,
       "cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId": cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId,
       "cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId": cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId,
       "cienaCesDpTsMeterFloodContainerAttachmentTable": cienaCesDpTsMeterFloodContainerAttachmentTable,
       "cienaCesDpTsMeterFloodContainerAttachmentEntry": cienaCesDpTsMeterFloodContainerAttachmentEntry,
       "cienaCesDpTsMeterFloodContainerAttachmentLiType": cienaCesDpTsMeterFloodContainerAttachmentLiType,
       "cienaCesDpTsMeterFloodContainerAttachmentLiIndex": cienaCesDpTsMeterFloodContainerAttachmentLiIndex,
       "cienaCesDpTsMeterFloodContainerAttachmentInterfaceName": cienaCesDpTsMeterFloodContainerAttachmentInterfaceName,
       "cienaCesDpTsMeterFloodContainerNotifAttachmentLiType": cienaCesDpTsMeterFloodContainerNotifAttachmentLiType,
       "cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex": cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex,
       "cienaCesDpTsMeterFloodContainerAttachmentUcastRateState": cienaCesDpTsMeterFloodContainerAttachmentUcastRateState,
       "cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState": cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState,
       "cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState": cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState,
       "cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth": cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth,
       "cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth": cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth,
       "cienaCesDpTsMeterFloodContainerAttachmentTotalRateState": cienaCesDpTsMeterFloodContainerAttachmentTotalRateState,
       "cienaCesDpTsMeter": cienaCesDpTsMeter,
       "cienaCesDpTsMeterProfile": cienaCesDpTsMeterProfile,
       "cienaCesDpTsMeterProfileTable": cienaCesDpTsMeterProfileTable,
       "cienaCesDpTsMeterProfileEntry": cienaCesDpTsMeterProfileEntry,
       "cienaCesDpTsMeterProfileIndex": cienaCesDpTsMeterProfileIndex,
       "cienaCesDpTsMeterProfileName": cienaCesDpTsMeterProfileName,
       "cienaCesDpTsMeterProfileCIR": cienaCesDpTsMeterProfileCIR,
       "cienaCesDpTsMeterProfileCBS": cienaCesDpTsMeterProfileCBS,
       "cienaCesDpTsMeterProfileEIR": cienaCesDpTsMeterProfileEIR,
       "cienaCesDpTsMeterProfileEBS": cienaCesDpTsMeterProfileEBS,
       "cienaCesDpTsMeterProfileColorMode": cienaCesDpTsMeterProfileColorMode,
       "cienaCesDpTsMeterProfileCouplingFlag": cienaCesDpTsMeterProfileCouplingFlag,
       "cienaCesDpTsMeterProfileAttachmentTable": cienaCesDpTsMeterProfileAttachmentTable,
       "cienaCesDpTsMeterProfileAttachmentEntry": cienaCesDpTsMeterProfileAttachmentEntry,
       "cienaCesDpTsMeterProfileAttachmentLiType": cienaCesDpTsMeterProfileAttachmentLiType,
       "cienaCesDpTsMeterProfileAttachmentLiIndex": cienaCesDpTsMeterProfileAttachmentLiIndex,
       "cienaCesDpTsMeterProfileAttachmentTotalCIR": cienaCesDpTsMeterProfileAttachmentTotalCIR,
       "cienaCesDpTsMeterProfileAttachmentTotalEIR": cienaCesDpTsMeterProfileAttachmentTotalEIR,
       "cienaCesDpTsMeterProfileAttachmentUsedCIR": cienaCesDpTsMeterProfileAttachmentUsedCIR,
       "cienaCesDpTsMeterProfileAttachmentMaxUsedEIR": cienaCesDpTsMeterProfileAttachmentMaxUsedEIR,
       "cienaCesDpTsCosMap": cienaCesDpTsCosMap,
       "cienaCesDpTsCosMapRcos": cienaCesDpTsCosMapRcos,
       "cienaCesDpTsCosMapRcosProfileTable": cienaCesDpTsCosMapRcosProfileTable,
       "cienaCesDpTsCosMapRcosProfileEntry": cienaCesDpTsCosMapRcosProfileEntry,
       "cienaCesDpTsCosMapRcosProfileId": cienaCesDpTsCosMapRcosProfileId,
       "cienaCesDpTsCosMapRcosProfileName": cienaCesDpTsCosMapRcosProfileName,
       "cienaCesDpTsCosMapRcosFixedRCoSValue": cienaCesDpTsCosMapRcosFixedRCoSValue,
       "cienaCesDpTsCosMapRcosFixedRcolour": cienaCesDpTsCosMapRcosFixedRcolour,
       "cienaCesDpTsCosMapRcosCosMapId": cienaCesDpTsCosMapRcosCosMapId,
       "cienaCesDpTsCosMapRcosCosMapName": cienaCesDpTsCosMapRcosCosMapName,
       "cienaCesDpTsCosMapRcosMapTable": cienaCesDpTsCosMapRcosMapTable,
       "cienaCesDpTsCosMapRcosMapEntry": cienaCesDpTsCosMapRcosMapEntry,
       "cienaCesDpTsCosMapRcosMapId": cienaCesDpTsCosMapRcosMapId,
       "cienaCesDpTsCosMapRcosMapName": cienaCesDpTsCosMapRcosMapName,
       "cienaCesDpTsCosMapRcosMapL2RCoS": cienaCesDpTsCosMapRcosMapL2RCoS,
       "cienaCesDpTsCosMapRcosMapL2RColour": cienaCesDpTsCosMapRcosMapL2RColour,
       "cienaCesDpTsCosMapRcosMapL3DscpRCoS": cienaCesDpTsCosMapRcosMapL3DscpRCoS,
       "cienaCesDpTsCosMapRcosMapL3DscpRColour": cienaCesDpTsCosMapRcosMapL3DscpRColour,
       "cienaCesDpTsCosMapRcosMapExpRCoS": cienaCesDpTsCosMapRcosMapExpRCoS,
       "cienaCesDpTsCosMapRcosMapExpRColour": cienaCesDpTsCosMapRcosMapExpRColour,
       "cienaCesDpTsCosMapFcos": cienaCesDpTsCosMapFcos,
       "cienaCesDpTsCosMapFcosMapTable": cienaCesDpTsCosMapFcosMapTable,
       "cienaCesDpTsCosMapFcosMapEntry": cienaCesDpTsCosMapFcosMapEntry,
       "cienaCesDpTsCosMapFcosMapId": cienaCesDpTsCosMapFcosMapId,
       "cienaCesDpTsCosMapFcosMapName": cienaCesDpTsCosMapFcosMapName,
       "cienaCesDpTsCosMapFcosL2CoS": cienaCesDpTsCosMapFcosL2CoS,
       "cienaCesDpTsCosMapFcosL2Dei": cienaCesDpTsCosMapFcosL2Dei,
       "cienaCesDpTsCosMapFcosL3Dscp": cienaCesDpTsCosMapFcosL3Dscp,
       "cienaCesDpTsCosMapFcosExp": cienaCesDpTsCosMapFcosExp,
       "cienaCesDpTsShaper": cienaCesDpTsShaper,
       "cienaCesDpTsShaperProfile": cienaCesDpTsShaperProfile,
       "cienaCesDpTsShaperProfileTable": cienaCesDpTsShaperProfileTable,
       "cienaCesDpTsShaperProfileEntry": cienaCesDpTsShaperProfileEntry,
       "cienaCesDpTsShaperProfileIndex": cienaCesDpTsShaperProfileIndex,
       "cienaCesDpTsShaperProfileName": cienaCesDpTsShaperProfileName,
       "cienaCesDpTsShaperProfileCIR": cienaCesDpTsShaperProfileCIR,
       "cienaCesDpTsShaperProfileCBS": cienaCesDpTsShaperProfileCBS,
       "cienaCesDpTsShaperProfileAttachmentTable": cienaCesDpTsShaperProfileAttachmentTable,
       "cienaCesDpTsShaperProfileAttachmentEntry": cienaCesDpTsShaperProfileAttachmentEntry,
       "cienaCesDpTsShaperProfileAttachmentLiType": cienaCesDpTsShaperProfileAttachmentLiType,
       "cienaCesDpTsShaperProfileAttachmentLiIndex": cienaCesDpTsShaperProfileAttachmentLiIndex,
       "cienaCesDpTsShaperProfileAttachmentTotalCIR": cienaCesDpTsShaperProfileAttachmentTotalCIR,
       "cienaCesDpTsShaperProfileAttachmentTotalEIR": cienaCesDpTsShaperProfileAttachmentTotalEIR,
       "cienaCesDpTsShaperProfileAttachmentUsedCIR": cienaCesDpTsShaperProfileAttachmentUsedCIR,
       "cienaCesDpTsShaperProfileAttachmentMaxUsedEIR": cienaCesDpTsShaperProfileAttachmentMaxUsedEIR,
       "cienaCesDpTsQ": cienaCesDpTsQ,
       "cienaCesDpTsQCongestionAvoidanceProfile": cienaCesDpTsQCongestionAvoidanceProfile,
       "cienaCesDpTsQCAProfileWREDTable": cienaCesDpTsQCAProfileWREDTable,
       "cienaCesDpTsQCAProfileWREDEntry": cienaCesDpTsQCAProfileWREDEntry,
       "cienaCesDpTsQCAProfileWREDId": cienaCesDpTsQCAProfileWREDId,
       "cienaCesDpTsQCAProfileWREDName": cienaCesDpTsQCAProfileWREDName,
       "cienaCesDpTsQCAProfileWREDDropRateExponent": cienaCesDpTsQCAProfileWREDDropRateExponent,
       "cienaCesDpTsQCAProfileWREDMaxQueueSize": cienaCesDpTsQCAProfileWREDMaxQueueSize,
       "cienaCesDpTsQCAProfileWREDMinQueueGuarantee": cienaCesDpTsQCAProfileWREDMinQueueGuarantee,
       "cienaCesDpTsQCAProfileWREDCurveTable": cienaCesDpTsQCAProfileWREDCurveTable,
       "cienaCesDpTsQCAProfileWREDCurveEntry": cienaCesDpTsQCAProfileWREDCurveEntry,
       "cienaCesDpTsQCAProfileWREDCurveId": cienaCesDpTsQCAProfileWREDCurveId,
       "cienaCesDpTsQCAProfileWREDCurveLowerThreshold": cienaCesDpTsQCAProfileWREDCurveLowerThreshold,
       "cienaCesDpTsQCAProfileWREDCurveUpperThreshold": cienaCesDpTsQCAProfileWREDCurveUpperThreshold,
       "cienaCesDpTsQCAProfileWREDCurveMaxDropProbability": cienaCesDpTsQCAProfileWREDCurveMaxDropProbability,
       "cienaCesDpTsQRCOSQMap": cienaCesDpTsQRCOSQMap,
       "cienaCesDpTsQRCOSQMapTable": cienaCesDpTsQRCOSQMapTable,
       "cienaCesDpTsQRCOSQMapEntry": cienaCesDpTsQRCOSQMapEntry,
       "cienaCesDpTsQRCOSQMapId": cienaCesDpTsQRCOSQMapId,
       "cienaCesDpTsQRCOSQMapName": cienaCesDpTsQRCOSQMapName,
       "cienaCesDpTsQRCOSQMapQueueTable": cienaCesDpTsQRCOSQMapQueueTable,
       "cienaCesDpTsQRCOSQMapQueueEntry": cienaCesDpTsQRCOSQMapQueueEntry,
       "cienaCesDpTsQRCOSQMapQueueId": cienaCesDpTsQRCOSQMapQueueId,
       "cienaCesDpTsQRCOSQMapQueueNumber": cienaCesDpTsQRCOSQMapQueueNumber,
       "cienaCesDpTsQRCOSQMapGreenCurveTable": cienaCesDpTsQRCOSQMapGreenCurveTable,
       "cienaCesDpTsQRCOSQMapGreenCurveEntry": cienaCesDpTsQRCOSQMapGreenCurveEntry,
       "cienaCesDpTsQRCOSQMapGreenCurveId": cienaCesDpTsQRCOSQMapGreenCurveId,
       "cienaCesDpTsQRCOSQMapGreenCurveNumber": cienaCesDpTsQRCOSQMapGreenCurveNumber,
       "cienaCesDpTsQRCOSQMapYellowCurveTable": cienaCesDpTsQRCOSQMapYellowCurveTable,
       "cienaCesDpTsQRCOSQMapYellowCurveEntry": cienaCesDpTsQRCOSQMapYellowCurveEntry,
       "cienaCesDpTsQRCOSQMapYellowCurveId": cienaCesDpTsQRCOSQMapYellowCurveId,
       "cienaCesDpTsQRCOSQMapYellowCurveNumber": cienaCesDpTsQRCOSQMapYellowCurveNumber,
       "cienaCesDpTsQGroupProfile": cienaCesDpTsQGroupProfile,
       "cienaCesDpTsQGroupProfileTable": cienaCesDpTsQGroupProfileTable,
       "cienaCesDpTsQGroupProfileEntry": cienaCesDpTsQGroupProfileEntry,
       "cienaCesDpTsQGroupProfileId": cienaCesDpTsQGroupProfileId,
       "cienaCesDpTsQGroupProfileName": cienaCesDpTsQGroupProfileName,
       "cienaCesDpTsQGroupProfileQueueCount": cienaCesDpTsQGroupProfileQueueCount,
       "cienaCesDpTsQGroupProfileRCOSQMapId": cienaCesDpTsQGroupProfileRCOSQMapId,
       "cienaCesDpTsQGroupProfileShaperCompensation": cienaCesDpTsQGroupProfileShaperCompensation,
       "cienaCesDpTsQGroupProfileQueueTable": cienaCesDpTsQGroupProfileQueueTable,
       "cienaCesDpTsQGroupProfileQueueEntry": cienaCesDpTsQGroupProfileQueueEntry,
       "cienaCesDpTsQGroupProfileQueueIndex": cienaCesDpTsQGroupProfileQueueIndex,
       "cienaCesDpTsQGroupProfileQueueCAPId": cienaCesDpTsQGroupProfileQueueCAPId,
       "cienaCesDpTsQGroupProfileQueueCIR": cienaCesDpTsQGroupProfileQueueCIR,
       "cienaCesDpTsQGroupProfileQueueCBS": cienaCesDpTsQGroupProfileQueueCBS,
       "cienaCesDpTsQGroupProfileQueueEIR": cienaCesDpTsQGroupProfileQueueEIR,
       "cienaCesDpTsQGroupProfileQueueEBS": cienaCesDpTsQGroupProfileQueueEBS,
       "cienaCesDpTsQGroupProfileQueueCirPercent": cienaCesDpTsQGroupProfileQueueCirPercent,
       "cienaCesDpTsQGroupProfileQueueEirPercent": cienaCesDpTsQGroupProfileQueueEirPercent,
       "cienaCesDpTsQGroupInstance": cienaCesDpTsQGroupInstance,
       "cienaCesDpTsQGroupInstanceTable": cienaCesDpTsQGroupInstanceTable,
       "cienaCesDpTsQGroupInstanceEntry": cienaCesDpTsQGroupInstanceEntry,
       "cienaCesDpTsQGroupInstancePgid": cienaCesDpTsQGroupInstancePgid,
       "cienaCesDpTsQGroupInstanceIndex": cienaCesDpTsQGroupInstanceIndex,
       "cienaCesDpTsQGroupInstanceParentSchedId": cienaCesDpTsQGroupInstanceParentSchedId,
       "cienaCesDpTsQGroupInstanceParentInstanceId": cienaCesDpTsQGroupInstanceParentInstanceId,
       "cienaCesDpTsQSchedulerProfile": cienaCesDpTsQSchedulerProfile,
       "cienaCesDpTsQSchedulerProfileTable": cienaCesDpTsQSchedulerProfileTable,
       "cienaCesDpTsQSchedulerProfileEntry": cienaCesDpTsQSchedulerProfileEntry,
       "cienaCesDpTsQSchedulerProfileId": cienaCesDpTsQSchedulerProfileId,
       "cienaCesDpTsQSchedulerProfileName": cienaCesDpTsQSchedulerProfileName,
       "cienaCesDpTsQSchedulerProfileSchedulerAlgorithm": cienaCesDpTsQSchedulerProfileSchedulerAlgorithm,
       "cienaCesDpTsQSchedulerProfileCIR": cienaCesDpTsQSchedulerProfileCIR,
       "cienaCesDpTsQSchedulerProfileCBS": cienaCesDpTsQSchedulerProfileCBS,
       "cienaCesDpTsQSchedulerProfileEIR": cienaCesDpTsQSchedulerProfileEIR,
       "cienaCesDpTsQSchedulerProfileEBS": cienaCesDpTsQSchedulerProfileEBS,
       "cienaCesDpTsQSchedulerProfileScheduledUcastWt": cienaCesDpTsQSchedulerProfileScheduledUcastWt,
       "cienaCesDpTsQSchedulerProfileScheduledMcastWt": cienaCesDpTsQSchedulerProfileScheduledMcastWt,
       "cienaCesDpTsQSchedulerProfileTapPointCount": cienaCesDpTsQSchedulerProfileTapPointCount,
       "cienaCesDpTsQSchedulerProfileShaperOverSpeed": cienaCesDpTsQSchedulerProfileShaperOverSpeed,
       "cienaCesDpTsQSchedulerProfileCirPolicy": cienaCesDpTsQSchedulerProfileCirPolicy,
       "cienaCesDpTsQSchedulerProfileEirPolicy": cienaCesDpTsQSchedulerProfileEirPolicy,
       "cienaCesDpTsQSchedulerProfileCirPercent": cienaCesDpTsQSchedulerProfileCirPercent,
       "cienaCesDpTsQSchedulerProfileEirPercent": cienaCesDpTsQSchedulerProfileEirPercent,
       "cienaCesDpTsQSchedulerTapPointTable": cienaCesDpTsQSchedulerTapPointTable,
       "cienaCesDpTsQSchedulerTapPointEntry": cienaCesDpTsQSchedulerTapPointEntry,
       "cienaCesDpTsQSchedulerTapPointIndex": cienaCesDpTsQSchedulerTapPointIndex,
       "cienaCesDpTsQSchedulerTapPointPriority": cienaCesDpTsQSchedulerTapPointPriority,
       "cienaCesDpTsQSchedulerTapPointWeight": cienaCesDpTsQSchedulerTapPointWeight,
       "cienaCesDpTsQSchedulerInstance": cienaCesDpTsQSchedulerInstance,
       "cienaCesDpTsQSchedulerInstanceTable": cienaCesDpTsQSchedulerInstanceTable,
       "cienaCesDpTsQSchedulerInstanceEntry": cienaCesDpTsQSchedulerInstanceEntry,
       "cienaCesDpTsQSchedulerInstancePgid": cienaCesDpTsQSchedulerInstancePgid,
       "cienaCesDpTsQSchedulerInstanceIndex": cienaCesDpTsQSchedulerInstanceIndex,
       "cienaCesDpTsQSchedulerInstanceParentSchedId": cienaCesDpTsQSchedulerInstanceParentSchedId,
       "cienaCesDpTsQSchedulerInstanceParentInstanceId": cienaCesDpTsQSchedulerInstanceParentInstanceId,
       "cienaCesDpTsQSchedulerInstanceParentTapPoint": cienaCesDpTsQSchedulerInstanceParentTapPoint,
       "cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir": cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir,
       "cienaCesDpTrafficClassTerm": cienaCesDpTrafficClassTerm,
       "cienaCesDpTrafficClassTermTable": cienaCesDpTrafficClassTermTable,
       "cienaCesDpTrafficClassTermEntry": cienaCesDpTrafficClassTermEntry,
       "cienaCesDpTrafficClassType": cienaCesDpTrafficClassType,
       "cienaCesDpTrafficClassId": cienaCesDpTrafficClassId,
       "cienaCesDpTrafficClassElemId": cienaCesDpTrafficClassElemId,
       "cienaCesDpTrafficClassTermPresentType": cienaCesDpTrafficClassTermPresentType,
       "cienaCesDpTrafficClassTermStartValue32": cienaCesDpTrafficClassTermStartValue32,
       "cienaCesDpTrafficClassTermEndOrMaskValue32": cienaCesDpTrafficClassTermEndOrMaskValue32,
       "cienaCesDpTrafficClassTermStartValueMac": cienaCesDpTrafficClassTermStartValueMac,
       "cienaCesDpTrafficClassTermMaskValueMac": cienaCesDpTrafficClassTermMaskValueMac,
       "cienaCesDpTrafficClassTermStartValueIp": cienaCesDpTrafficClassTermStartValueIp,
       "cienaCesDpTrafficClassTermMaskValueIp": cienaCesDpTrafficClassTermMaskValueIp,
       "cienaCesDpSubPort": cienaCesDpSubPort,
       "cienaCesDpSubPortTable": cienaCesDpSubPortTable,
       "cienaCesDpSubPortEntry": cienaCesDpSubPortEntry,
       "cienaCesDpSubPortLiIndex": cienaCesDpSubPortLiIndex,
       "cienaCesDpSubPortName": cienaCesDpSubPortName,
       "cienaCesDpSubPortClassifierPrecedence": cienaCesDpSubPortClassifierPrecedence,
       "cienaCesDpSubPortParentIfId": cienaCesDpSubPortParentIfId,
       "cienaCesDpSubPortVirtualSwitchIndex": cienaCesDpSubPortVirtualSwitchIndex,
       "cienaCesDpSubPortRlanIndex": cienaCesDpSubPortRlanIndex,
       "cienaCesDpSubPortVirtualSwitchName": cienaCesDpSubPortVirtualSwitchName,
       "cienaCesDpSubPortIngressMeterProfileId": cienaCesDpSubPortIngressMeterProfileId,
       "cienaCesDpSubPortIngressMeterProfileName": cienaCesDpSubPortIngressMeterProfileName,
       "cienaCesDpSubportIngressMeterPolicy": cienaCesDpSubportIngressMeterPolicy,
       "cienaCesDpSubPortIngressFloodContainerId": cienaCesDpSubPortIngressFloodContainerId,
       "cienaCesDpSubPortIngressFloodContainerName": cienaCesDpSubPortIngressFloodContainerName,
       "cienaCesDpSubPortIngressRcosProfileId": cienaCesDpSubPortIngressRcosProfileId,
       "cienaCesDpSubPortIngressRcosProfileName": cienaCesDpSubPortIngressRcosProfileName,
       "cienaCesDpSubPortIngressRcosPolicy": cienaCesDpSubPortIngressRcosPolicy,
       "cienaCesDpSubPortIngressFcosMapId": cienaCesDpSubPortIngressFcosMapId,
       "cienaCesDpSubPortIngressFcosMapName": cienaCesDpSubPortIngressFcosMapName,
       "cienaCesDpSubPortEgressFcosMapId": cienaCesDpSubPortEgressFcosMapId,
       "cienaCesDpSubPortEgressFcosMapName": cienaCesDpSubPortEgressFcosMapName,
       "cienaCesDpSubPortEgressL2PtTransform": cienaCesDpSubPortEgressL2PtTransform,
       "cienaCesDpSubPortIngressL2Transform": cienaCesDpSubPortIngressL2Transform,
       "cienaCesDpSubPortEgressL2Transform": cienaCesDpSubPortEgressL2Transform,
       "cienaCesDpSubPortIngressL3TransformPolicy": cienaCesDpSubPortIngressL3TransformPolicy,
       "cienaCesDpSubPortEgressL3TransformPolicy": cienaCesDpSubPortEgressL3TransformPolicy,
       "cienaCesDpSubPortPrivateFwdGroup": cienaCesDpSubPortPrivateFwdGroup,
       "cienaCesDpSubPortFilterPolicy": cienaCesDpSubPortFilterPolicy,
       "cienaCesDpSubPortLogicalRingIndex": cienaCesDpSubPortLogicalRingIndex,
       "cienaCesDpSubPortVirtualRingIndex": cienaCesDpSubPortVirtualRingIndex,
       "cienaCesDpSubPortEgressReflectorMac": cienaCesDpSubPortEgressReflectorMac,
       "cienaCesDpSubPortEgressGeneratorMac": cienaCesDpSubPortEgressGeneratorMac,
       "cienaCesDpSubPortQueueGroupProfileId": cienaCesDpSubPortQueueGroupProfileId,
       "cienaCesDpSubPortQueueGroupProfileName": cienaCesDpSubPortQueueGroupProfileName,
       "cienaCesDpSubPortQueueGroupInstanceId": cienaCesDpSubPortQueueGroupInstanceId,
       "cienaCesDpVirtualSwitch": cienaCesDpVirtualSwitch,
       "cienaCesDpVirtualSwitchTable": cienaCesDpVirtualSwitchTable,
       "cienaCesDpVirtualSwitchEntry": cienaCesDpVirtualSwitchEntry,
       "cienaCesDpVirtualSwitchIndex": cienaCesDpVirtualSwitchIndex,
       "cienaCesDpVirtualSwitchRlanIndex": cienaCesDpVirtualSwitchRlanIndex,
       "cienaCesDpVirtualSwitchRlanTable": cienaCesDpVirtualSwitchRlanTable,
       "cienaCesDpVirtualSwitchRlanEntry": cienaCesDpVirtualSwitchRlanEntry,
       "cienaCesDpVirtualSwitchRlanName": cienaCesDpVirtualSwitchRlanName,
       "cienaCesDpVirtualSwitchRlanMcastForwardingMode": cienaCesDpVirtualSwitchRlanMcastForwardingMode,
       "cienaCesDpVirtualSwitchRlanL2CftStatus": cienaCesDpVirtualSwitchRlanL2CftStatus,
       "cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos": cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos,
       "cienaCesDpVirtualSwitchRlanMacLearningStatus": cienaCesDpVirtualSwitchRlanMacLearningStatus,
       "cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus": cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus,
       "cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy": cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy,
       "cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy": cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy,
       "cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy": cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy,
       "cienaCesDpVirtualSwitchRlanDescription": cienaCesDpVirtualSwitchRlanDescription,
       "cienaCesDpVirtualSwitchRlanPfgProfileId": cienaCesDpVirtualSwitchRlanPfgProfileId,
       "cienaCesDpVirtualSwitchRlanPfgProfileName": cienaCesDpVirtualSwitchRlanPfgProfileName,
       "cienaCesDpVirtualSwitchRlanL2CftProfileId": cienaCesDpVirtualSwitchRlanL2CftProfileId,
       "cienaCesDpVirtualSwitchRlanL2CftProfileName": cienaCesDpVirtualSwitchRlanL2CftProfileName,
       "cienaCesDpVirtualSwitchRlanLearnLimit": cienaCesDpVirtualSwitchRlanLearnLimit,
       "cienaCesDpVirtualSwitchRlanIfTable": cienaCesDpVirtualSwitchRlanIfTable,
       "cienaCesDpVirtualSwitchRlanIfEntry": cienaCesDpVirtualSwitchRlanIfEntry,
       "cienaCesDpVirtualSwitchRlanIfLiType": cienaCesDpVirtualSwitchRlanIfLiType,
       "cienaCesDpVirtualSwitchRlanIfLiIndex": cienaCesDpVirtualSwitchRlanIfLiIndex,
       "cienaCesDpVirtualSwitchRlanIfLportIngress": cienaCesDpVirtualSwitchRlanIfLportIngress,
       "cienaCesDpVirtualSwitchRlanIfLportEgress": cienaCesDpVirtualSwitchRlanIfLportEgress,
       "cienaCesDpVirtualSwitchRlanL2CftProtocolTable": cienaCesDpVirtualSwitchRlanL2CftProtocolTable,
       "cienaCesDpVirtualSwitchRlanL2CftProtocolEntry": cienaCesDpVirtualSwitchRlanL2CftProtocolEntry,
       "cienaCesDpVirtualSwitchRlanL2CftProtocolType": cienaCesDpVirtualSwitchRlanL2CftProtocolType,
       "cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition": cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition,
       "cienaCesDpQosFlow": cienaCesDpQosFlow,
       "cienaCesDpQosFlowTable": cienaCesDpQosFlowTable,
       "cienaCesDpQosFlowEntry": cienaCesDpQosFlowEntry,
       "cienaCesDpQosFlowLiIndex": cienaCesDpQosFlowLiIndex,
       "cienaCesDpQosFlowName": cienaCesDpQosFlowName,
       "cienaCesDpQosFlowClassifierPrecedence": cienaCesDpQosFlowClassifierPrecedence,
       "cienaCesDpQosFlowParentIfId": cienaCesDpQosFlowParentIfId,
       "cienaCesDpQosFlowParentIfType": cienaCesDpQosFlowParentIfType,
       "cienaCesDpQosFlowIngressMeterProfileId": cienaCesDpQosFlowIngressMeterProfileId,
       "cienaCesDpQosFlowIngressMeterProfileName": cienaCesDpQosFlowIngressMeterProfileName,
       "cienaCesDpQosFlowIngressMeterPolicy": cienaCesDpQosFlowIngressMeterPolicy,
       "cienaCesDpQosFlowIngressRcosProfileId": cienaCesDpQosFlowIngressRcosProfileId,
       "cienaCesDpQosFlowIngressRcosProfileName": cienaCesDpQosFlowIngressRcosProfileName,
       "cienaCesDpQosFlowIngressRcosPolicy": cienaCesDpQosFlowIngressRcosPolicy,
       "cienaCesDpAccessFlow": cienaCesDpAccessFlow,
       "cienaCesDpAccessFlowTable": cienaCesDpAccessFlowTable,
       "cienaCesDpAccessFlowEntry": cienaCesDpAccessFlowEntry,
       "cienaCesDpAccessFlowLiIndex": cienaCesDpAccessFlowLiIndex,
       "cienaCesDpAccessFlowName": cienaCesDpAccessFlowName,
       "cienaCesDpAccessFlowClassifierPrecedence": cienaCesDpAccessFlowClassifierPrecedence,
       "cienaCesDpAccessFlowParentIfId": cienaCesDpAccessFlowParentIfId,
       "cienaCesDpAccessFlowParentIfType": cienaCesDpAccessFlowParentIfType,
       "cienaCesDpAccessFlowFilterPolicy": cienaCesDpAccessFlowFilterPolicy,
       "cienaCesDpPbtTransit": cienaCesDpPbtTransit,
       "cienaCesDpPbtTransitTable": cienaCesDpPbtTransitTable,
       "cienaCesDpPbtTransitEntry": cienaCesDpPbtTransitEntry,
       "cienaCesDpPbtTransitLiIndex": cienaCesDpPbtTransitLiIndex,
       "cienaCesDpPbtTransitName": cienaCesDpPbtTransitName,
       "cienaCesDpPbtTransitParentIfId": cienaCesDpPbtTransitParentIfId,
       "cienaCesDpPbtTransitIngressMeterProfileId": cienaCesDpPbtTransitIngressMeterProfileId,
       "cienaCesDpPbtTransitIngressMeterProfileName": cienaCesDpPbtTransitIngressMeterProfileName,
       "cienaCesDpPbtTransitIngressFloodContainerId": cienaCesDpPbtTransitIngressFloodContainerId,
       "cienaCesDpPbtTransitIngressFloodContainerName": cienaCesDpPbtTransitIngressFloodContainerName,
       "cienaCesDpPbtTransitIngressRcosProfileId": cienaCesDpPbtTransitIngressRcosProfileId,
       "cienaCesDpPbtTransitIngressRcosProfileName": cienaCesDpPbtTransitIngressRcosProfileName,
       "cienaCesDpPbtTransitIngressRcosPolicy": cienaCesDpPbtTransitIngressRcosPolicy,
       "cienaCesDpPbtTransitIngressFcosMapId": cienaCesDpPbtTransitIngressFcosMapId,
       "cienaCesDpPbtTransitIngressFcosMapName": cienaCesDpPbtTransitIngressFcosMapName,
       "cienaCesDpPbtTransitEgressFcosMapId": cienaCesDpPbtTransitEgressFcosMapId,
       "cienaCesDpPbtTransitEgressFcosMapName": cienaCesDpPbtTransitEgressFcosMapName,
       "cienaCesDpPbtTransitIngressBvidTransform": cienaCesDpPbtTransitIngressBvidTransform,
       "cienaCesDpPbtTransitEgressBvidTransform": cienaCesDpPbtTransitEgressBvidTransform,
       "cienaCesDpPbtTransitVirtualSwitchId": cienaCesDpPbtTransitVirtualSwitchId,
       "cienaCesDpPbtTransitRlanId": cienaCesDpPbtTransitRlanId,
       "cienaCesDpPbtTransitVirtualSwitchName": cienaCesDpPbtTransitVirtualSwitchName,
       "cienaCesDpPbtTransitPrivateFwdGroup": cienaCesDpPbtTransitPrivateFwdGroup,
       "cienaCesDpPbtTransitIngressMeterPolicy": cienaCesDpPbtTransitIngressMeterPolicy,
       "cienaCesDpCpuSubInterface": cienaCesDpCpuSubInterface,
       "cienaCesDpCpuSubInterfaceTable": cienaCesDpCpuSubInterfaceTable,
       "cienaCesDpCpuSubInterfaceEntry": cienaCesDpCpuSubInterfaceEntry,
       "cienaCesDpCpuSubInterfaceIndex": cienaCesDpCpuSubInterfaceIndex,
       "cienaCesDpCpuSubInterfaceName": cienaCesDpCpuSubInterfaceName,
       "cienaCesDpCpuSubInterfaceEgressL2Transform": cienaCesDpCpuSubInterfaceEgressL2Transform,
       "cienaCesDpCpuSubInterfaceIngressL2Transform": cienaCesDpCpuSubInterfaceIngressL2Transform,
       "cienaCesDpCpuSubInterfaceEgressL3TransformPolicy": cienaCesDpCpuSubInterfaceEgressL3TransformPolicy,
       "cienaCesDpCpuSubInterfaceEgressRCosPolicy": cienaCesDpCpuSubInterfaceEgressRCosPolicy,
       "cienaCesDpCpuSubInterfaceEgressRCosProfileIndex": cienaCesDpCpuSubInterfaceEgressRCosProfileIndex,
       "cienaCesDpCpuSubInterfaceEgressRCosProfile": cienaCesDpCpuSubInterfaceEgressRCosProfile,
       "cienaCesDpCpuSubInterfaceVirtualSwitchIndex": cienaCesDpCpuSubInterfaceVirtualSwitchIndex,
       "cienaCesDpCpuSubInterfaceRlanIndex": cienaCesDpCpuSubInterfaceRlanIndex,
       "cienaCesDpCpuSubInterfaceVirtualSwitchName": cienaCesDpCpuSubInterfaceVirtualSwitchName,
       "cienaCesDpPfgProfile": cienaCesDpPfgProfile,
       "cienaCesDpPfgProfileTable": cienaCesDpPfgProfileTable,
       "cienaCesDpPfgProfileEntry": cienaCesDpPfgProfileEntry,
       "cienaCesDpPfgProfileIndex": cienaCesDpPfgProfileIndex,
       "cienaCesDpPfgProfileName": cienaCesDpPfgProfileName,
       "cienaCesDpPfgProfileAPolicy": cienaCesDpPfgProfileAPolicy,
       "cienaCesDpPfgProfileBPolicy": cienaCesDpPfgProfileBPolicy,
       "cienaCesDpPfgProfileCPolicy": cienaCesDpPfgProfileCPolicy,
       "cienaCesDpL2CftProfile": cienaCesDpL2CftProfile,
       "cienaCesDpL2CftProfileTable": cienaCesDpL2CftProfileTable,
       "cienaCesDpL2CftProfileEntry": cienaCesDpL2CftProfileEntry,
       "cienaCesDpL2CftProfileIndex": cienaCesDpL2CftProfileIndex,
       "cienaCesDpL2CftProfileName": cienaCesDpL2CftProfileName,
       "cienaCesDpL2CftProfileL2ControlRcos": cienaCesDpL2CftProfileL2ControlRcos,
       "cienaCesDpL2CftProfileL2CftProtocolTable": cienaCesDpL2CftProfileL2CftProtocolTable,
       "cienaCesDpL2CftProfileL2CftProtocolEntry": cienaCesDpL2CftProfileL2CftProtocolEntry,
       "cienaCesDpL2CftProfileL2CftProtocolType": cienaCesDpL2CftProfileL2CftProtocolType,
       "cienaCesDpL2CftProfileL2CftProtocolDisposition": cienaCesDpL2CftProfileL2CftProtocolDisposition,
       "cienaCesDpMIBNotificationPrefix": cienaCesDpMIBNotificationPrefix,
       "cienaCesDpMIBNotifications": cienaCesDpMIBNotifications,
       "cienaCesDpTsMeterFloodContainerUcastThresholdExceeded": cienaCesDpTsMeterFloodContainerUcastThresholdExceeded,
       "cienaCesDpTsMeterFloodContainerUcastThresholdNormal": cienaCesDpTsMeterFloodContainerUcastThresholdNormal,
       "cienaCesDpTsMeterFloodContainerBcastThresholdExceeded": cienaCesDpTsMeterFloodContainerBcastThresholdExceeded,
       "cienaCesDpTsMeterFloodContainerBcastThresholdNormal": cienaCesDpTsMeterFloodContainerBcastThresholdNormal,
       "cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded": cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded,
       "cienaCesDpTsMeterFloodContainerL2McastThresholdNormal": cienaCesDpTsMeterFloodContainerL2McastThresholdNormal,
       "cienaCesDataplaneEgressReflectorEnabled": cienaCesDataplaneEgressReflectorEnabled,
       "cienaCesDataplaneEgressReflectorDisabled": cienaCesDataplaneEgressReflectorDisabled,
       "cienaCesDpPortShapingSubscriptionExceedsOperSpeed": cienaCesDpPortShapingSubscriptionExceedsOperSpeed,
       "cienaCesDpPortShapingSubscriptionWithinOperSpeed": cienaCesDpPortShapingSubscriptionWithinOperSpeed,
       "cienaCesDpTsMeterFloodContainerTotalThresholdExceeded": cienaCesDpTsMeterFloodContainerTotalThresholdExceeded,
       "cienaCesDpTsMeterFloodContainerTotalThresholdNormal": cienaCesDpTsMeterFloodContainerTotalThresholdNormal}
)
