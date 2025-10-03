# SNMP MIB module (TN-EVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-EVC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:30 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(PortList,
 VlanId,
 VlanIdOrAny,
 VlanIdOrAnyOrNone,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "VlanIdOrAny",
    "VlanIdOrAnyOrNone",
    "VlanIdOrNone")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnEvcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106)
)
if mibBuilder.loadTexts:
    tnEvcMib.setRevisions(
        ("2012-04-20 00:00",
         "2012-07-06 00:00",
         "2014-01-09 00:00",
         "2014-05-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnEvcObjects_ObjectIdentity = ObjectIdentity
tnEvcObjects = _TnEvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1)
)
_TnEvcCfgMgmtGroup_ObjectIdentity = ObjectIdentity
tnEvcCfgMgmtGroup = _TnEvcCfgMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1)
)
_TnEvcPortTable_Object = MibTable
tnEvcPortTable = _TnEvcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnEvcPortTable.setStatus("current")
_TnEvcPortEntry_Object = MibTableRow
tnEvcPortEntry = _TnEvcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 1, 1)
)
tnEvcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnEvcPortEntry.setStatus("current")


class _TnEvcPortDEIMode_Type(Integer32):
    """Custom type tnEvcPortDEIMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coloured", 1),
          ("fixed", 2))
    )


_TnEvcPortDEIMode_Type.__name__ = "Integer32"
_TnEvcPortDEIMode_Object = MibTableColumn
tnEvcPortDEIMode = _TnEvcPortDEIMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 1, 1, 1),
    _TnEvcPortDEIMode_Type()
)
tnEvcPortDEIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcPortDEIMode.setStatus("current")


class _TnEvcPortTagMode_Type(Integer32):
    """Custom type tnEvcPortTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inner", 1),
          ("outer", 2))
    )


_TnEvcPortTagMode_Type.__name__ = "Integer32"
_TnEvcPortTagMode_Object = MibTableColumn
tnEvcPortTagMode = _TnEvcPortTagMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 1, 1, 2),
    _TnEvcPortTagMode_Type()
)
tnEvcPortTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcPortTagMode.setStatus("current")


class _TnEvcPortAddressMode_Type(Integer32):
    """Custom type tnEvcPortAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("destination", 2))
    )


_TnEvcPortAddressMode_Type.__name__ = "Integer32"
_TnEvcPortAddressMode_Object = MibTableColumn
tnEvcPortAddressMode = _TnEvcPortAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 1, 1, 3),
    _TnEvcPortAddressMode_Type()
)
tnEvcPortAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcPortAddressMode.setStatus("current")
_TnEvcTable_Object = MibTable
tnEvcTable = _TnEvcTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnEvcTable.setStatus("current")
_TnEvcEntry_Object = MibTableRow
tnEvcEntry = _TnEvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1)
)
tnEvcEntry.setIndexNames(
    (0, "TN-EVC-MIB", "tnEvcIndex"),
)
if mibBuilder.loadTexts:
    tnEvcEntry.setStatus("current")


class _TnEvcIndex_Type(Integer32):
    """Custom type tnEvcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnEvcIndex_Type.__name__ = "Integer32"
_TnEvcIndex_Object = MibTableColumn
tnEvcIndex = _TnEvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 1),
    _TnEvcIndex_Type()
)
tnEvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEvcIndex.setStatus("current")
_TnEvcNNIPortlist_Type = PortList
_TnEvcNNIPortlist_Object = MibTableColumn
tnEvcNNIPortlist = _TnEvcNNIPortlist_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 2),
    _TnEvcNNIPortlist_Type()
)
tnEvcNNIPortlist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcNNIPortlist.setStatus("current")
_TnEvcVid_Type = VlanIdOrAny
_TnEvcVid_Object = MibTableColumn
tnEvcVid = _TnEvcVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 3),
    _TnEvcVid_Type()
)
tnEvcVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcVid.setStatus("current")
_TnEvcIVid_Type = VlanIdOrAny
_TnEvcIVid_Object = MibTableColumn
tnEvcIVid = _TnEvcIVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 4),
    _TnEvcIVid_Type()
)
tnEvcIVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcIVid.setStatus("current")


class _TnEvcLearning_Type(Integer32):
    """Custom type tnEvcLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnEvcLearning_Type.__name__ = "Integer32"
_TnEvcLearning_Object = MibTableColumn
tnEvcLearning = _TnEvcLearning_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 5),
    _TnEvcLearning_Type()
)
tnEvcLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcLearning.setStatus("current")


class _TnEvcInnerTagType_Type(Integer32):
    """Custom type tnEvcInnerTagType based on Integer32"""
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
        *(("none", 1),
          ("cTag", 2),
          ("sTag", 3),
          ("sCustomTag", 4))
    )


_TnEvcInnerTagType_Type.__name__ = "Integer32"
_TnEvcInnerTagType_Object = MibTableColumn
tnEvcInnerTagType = _TnEvcInnerTagType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 6),
    _TnEvcInnerTagType_Type()
)
tnEvcInnerTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcInnerTagType.setStatus("current")


class _TnEvcInnerVidMode_Type(Integer32):
    """Custom type tnEvcInnerVidMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("tunnel", 2))
    )


_TnEvcInnerVidMode_Type.__name__ = "Integer32"
_TnEvcInnerVidMode_Object = MibTableColumn
tnEvcInnerVidMode = _TnEvcInnerVidMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 7),
    _TnEvcInnerVidMode_Type()
)
tnEvcInnerVidMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcInnerVidMode.setStatus("current")
_TnEvcInnerVid_Type = VlanIdOrAnyOrNone
_TnEvcInnerVid_Object = MibTableColumn
tnEvcInnerVid = _TnEvcInnerVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 8),
    _TnEvcInnerVid_Type()
)
tnEvcInnerVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcInnerVid.setStatus("current")


class _TnEvcInnerPCPDEIPreservation_Type(Integer32):
    """Custom type tnEvcInnerPCPDEIPreservation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preserved", 1),
          ("fixed", 2))
    )


_TnEvcInnerPCPDEIPreservation_Type.__name__ = "Integer32"
_TnEvcInnerPCPDEIPreservation_Object = MibTableColumn
tnEvcInnerPCPDEIPreservation = _TnEvcInnerPCPDEIPreservation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 9),
    _TnEvcInnerPCPDEIPreservation_Type()
)
tnEvcInnerPCPDEIPreservation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcInnerPCPDEIPreservation.setStatus("current")


class _TnEvcInnerPCP_Type(Integer32):
    """Custom type tnEvcInnerPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnEvcInnerPCP_Type.__name__ = "Integer32"
_TnEvcInnerPCP_Object = MibTableColumn
tnEvcInnerPCP = _TnEvcInnerPCP_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 10),
    _TnEvcInnerPCP_Type()
)
tnEvcInnerPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcInnerPCP.setStatus("current")


class _TnEvcInnerDEI_Type(Integer32):
    """Custom type tnEvcInnerDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnEvcInnerDEI_Type.__name__ = "Integer32"
_TnEvcInnerDEI_Object = MibTableColumn
tnEvcInnerDEI = _TnEvcInnerDEI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 11),
    _TnEvcInnerDEI_Type()
)
tnEvcInnerDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcInnerDEI.setStatus("current")
_TnEvcOuterVid_Type = VlanIdOrAnyOrNone
_TnEvcOuterVid_Object = MibTableColumn
tnEvcOuterVid = _TnEvcOuterVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 12),
    _TnEvcOuterVid_Type()
)
tnEvcOuterVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcOuterVid.setStatus("current")
_TnEvcStatus_Type = RowStatus
_TnEvcStatus_Object = MibTableColumn
tnEvcStatus = _TnEvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 13),
    _TnEvcStatus_Type()
)
tnEvcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcStatus.setStatus("current")


class _TnEvcPolicerID_Type(Integer32):
    """Custom type tnEvcPolicerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TnEvcPolicerID_Type.__name__ = "Integer32"
_TnEvcPolicerID_Object = MibTableColumn
tnEvcPolicerID = _TnEvcPolicerID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 14),
    _TnEvcPolicerID_Type()
)
tnEvcPolicerID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcPolicerID.setStatus("current")


class _TnEvcName_Type(OctetString):
    """Custom type tnEvcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TnEvcName_Type.__name__ = "OctetString"
_TnEvcName_Object = MibTableColumn
tnEvcName = _TnEvcName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 2, 1, 15),
    _TnEvcName_Type()
)
tnEvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcName.setStatus("current")
_TnEvcEceTable_Object = MibTable
tnEvcEceTable = _TnEvcEceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnEvcEceTable.setStatus("current")
_TnEvcEceEntry_Object = MibTableRow
tnEvcEceEntry = _TnEvcEceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1)
)
tnEvcEceEntry.setIndexNames(
    (0, "TN-EVC-MIB", "tnEvcEceId"),
)
if mibBuilder.loadTexts:
    tnEvcEceEntry.setStatus("current")


class _TnEvcEceId_Type(Integer32):
    """Custom type tnEvcEceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnEvcEceId_Type.__name__ = "Integer32"
_TnEvcEceId_Object = MibTableColumn
tnEvcEceId = _TnEvcEceId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 1),
    _TnEvcEceId_Type()
)
tnEvcEceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEvcEceId.setStatus("current")
_TnEvcEceNextEceId_Type = Integer32
_TnEvcEceNextEceId_Object = MibTableColumn
tnEvcEceNextEceId = _TnEvcEceNextEceId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 2),
    _TnEvcEceNextEceId_Type()
)
tnEvcEceNextEceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceNextEceId.setStatus("current")
_TnEvcEceUNIPortlist_Type = PortList
_TnEvcEceUNIPortlist_Object = MibTableColumn
tnEvcEceUNIPortlist = _TnEvcEceUNIPortlist_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 3),
    _TnEvcEceUNIPortlist_Type()
)
tnEvcEceUNIPortlist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceUNIPortlist.setStatus("current")


class _TnEvcEceTagType_Type(Integer32):
    """Custom type tnEvcEceTagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2),
          ("any", 3))
    )


_TnEvcEceTagType_Type.__name__ = "Integer32"
_TnEvcEceTagType_Object = MibTableColumn
tnEvcEceTagType = _TnEvcEceTagType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 4),
    _TnEvcEceTagType_Type()
)
tnEvcEceTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceTagType.setStatus("current")


class _TnEvcEceTagVIDFilterType_Type(Integer32):
    """Custom type tnEvcEceTagVIDFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnEvcEceTagVIDFilterType_Type.__name__ = "Integer32"
_TnEvcEceTagVIDFilterType_Object = MibTableColumn
tnEvcEceTagVIDFilterType = _TnEvcEceTagVIDFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 5),
    _TnEvcEceTagVIDFilterType_Type()
)
tnEvcEceTagVIDFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceTagVIDFilterType.setStatus("current")
_TnEvcEceTagVIDFilterVal_Type = VlanIdOrAnyOrNone
_TnEvcEceTagVIDFilterVal_Object = MibTableColumn
tnEvcEceTagVIDFilterVal = _TnEvcEceTagVIDFilterVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 6),
    _TnEvcEceTagVIDFilterVal_Type()
)
tnEvcEceTagVIDFilterVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceTagVIDFilterVal.setStatus("current")
_TnEvcEceTagVIDFilterStart_Type = VlanIdOrAnyOrNone
_TnEvcEceTagVIDFilterStart_Object = MibTableColumn
tnEvcEceTagVIDFilterStart = _TnEvcEceTagVIDFilterStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 7),
    _TnEvcEceTagVIDFilterStart_Type()
)
tnEvcEceTagVIDFilterStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceTagVIDFilterStart.setStatus("current")
_TnEvcEceTagVIDFilterEnd_Type = VlanIdOrAnyOrNone
_TnEvcEceTagVIDFilterEnd_Object = MibTableColumn
tnEvcEceTagVIDFilterEnd = _TnEvcEceTagVIDFilterEnd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 8),
    _TnEvcEceTagVIDFilterEnd_Type()
)
tnEvcEceTagVIDFilterEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceTagVIDFilterEnd.setStatus("current")


class _TnEvcEceTagPCP_Type(Bits):
    """Custom type tnEvcEceTagPCP based on Bits"""
    namedValues = NamedValues(
        ("none", 0)
    )

_TnEvcEceTagPCP_Type.__name__ = "Bits"
_TnEvcEceTagPCP_Object = MibTableColumn
tnEvcEceTagPCP = _TnEvcEceTagPCP_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 9),
    _TnEvcEceTagPCP_Type()
)
tnEvcEceTagPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceTagPCP.setStatus("current")


class _TnEvcEceTagDEI_Type(Integer32):
    """Custom type tnEvcEceTagDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dei0", 2),
          ("dei1", 3))
    )


_TnEvcEceTagDEI_Type.__name__ = "Integer32"
_TnEvcEceTagDEI_Object = MibTableColumn
tnEvcEceTagDEI = _TnEvcEceTagDEI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 10),
    _TnEvcEceTagDEI_Type()
)
tnEvcEceTagDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceTagDEI.setStatus("current")


class _TnEvcEceTagFrameType_Type(Integer32):
    """Custom type tnEvcEceTagFrameType based on Integer32"""
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
        *(("any", 1),
          ("etype", 2),
          ("llc", 3),
          ("snap", 4),
          ("ipv4", 5),
          ("ipv6", 6),
          ("l2cp", 7))
    )


_TnEvcEceTagFrameType_Type.__name__ = "Integer32"
_TnEvcEceTagFrameType_Object = MibTableColumn
tnEvcEceTagFrameType = _TnEvcEceTagFrameType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 11),
    _TnEvcEceTagFrameType_Type()
)
tnEvcEceTagFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceTagFrameType.setStatus("current")


class _TnEvcEceProtoType_Type(Integer32):
    """Custom type tnEvcEceProtoType based on Integer32"""
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
        *(("any", 1),
          ("udp", 2),
          ("tcp", 3),
          ("other", 4))
    )


_TnEvcEceProtoType_Type.__name__ = "Integer32"
_TnEvcEceProtoType_Object = MibTableColumn
tnEvcEceProtoType = _TnEvcEceProtoType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 12),
    _TnEvcEceProtoType_Type()
)
tnEvcEceProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceProtoType.setStatus("current")


class _TnEvcEceProtoVal_Type(Integer32):
    """Custom type tnEvcEceProtoVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnEvcEceProtoVal_Type.__name__ = "Integer32"
_TnEvcEceProtoVal_Object = MibTableColumn
tnEvcEceProtoVal = _TnEvcEceProtoVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 13),
    _TnEvcEceProtoVal_Type()
)
tnEvcEceProtoVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceProtoVal.setStatus("current")


class _TnEvcEceDscpFilterType_Type(Integer32):
    """Custom type tnEvcEceDscpFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnEvcEceDscpFilterType_Type.__name__ = "Integer32"
_TnEvcEceDscpFilterType_Object = MibTableColumn
tnEvcEceDscpFilterType = _TnEvcEceDscpFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 14),
    _TnEvcEceDscpFilterType_Type()
)
tnEvcEceDscpFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDscpFilterType.setStatus("current")


class _TnEvcEceDscpFilterVal_Type(Integer32):
    """Custom type tnEvcEceDscpFilterVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnEvcEceDscpFilterVal_Type.__name__ = "Integer32"
_TnEvcEceDscpFilterVal_Object = MibTableColumn
tnEvcEceDscpFilterVal = _TnEvcEceDscpFilterVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 15),
    _TnEvcEceDscpFilterVal_Type()
)
tnEvcEceDscpFilterVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDscpFilterVal.setStatus("current")


class _TnEvcEceDscpRangeStart_Type(Integer32):
    """Custom type tnEvcEceDscpRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnEvcEceDscpRangeStart_Type.__name__ = "Integer32"
_TnEvcEceDscpRangeStart_Object = MibTableColumn
tnEvcEceDscpRangeStart = _TnEvcEceDscpRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 16),
    _TnEvcEceDscpRangeStart_Type()
)
tnEvcEceDscpRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDscpRangeStart.setStatus("current")


class _TnEvcEceDscpRangeEnd_Type(Integer32):
    """Custom type tnEvcEceDscpRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnEvcEceDscpRangeEnd_Type.__name__ = "Integer32"
_TnEvcEceDscpRangeEnd_Object = MibTableColumn
tnEvcEceDscpRangeEnd = _TnEvcEceDscpRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 17),
    _TnEvcEceDscpRangeEnd_Type()
)
tnEvcEceDscpRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDscpRangeEnd.setStatus("current")


class _TnEvcEceSrcPortFilterType_Type(Integer32):
    """Custom type tnEvcEceSrcPortFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnEvcEceSrcPortFilterType_Type.__name__ = "Integer32"
_TnEvcEceSrcPortFilterType_Object = MibTableColumn
tnEvcEceSrcPortFilterType = _TnEvcEceSrcPortFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 18),
    _TnEvcEceSrcPortFilterType_Type()
)
tnEvcEceSrcPortFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceSrcPortFilterType.setStatus("current")


class _TnEvcEceSrcPortFilterNo_Type(Integer32):
    """Custom type tnEvcEceSrcPortFilterNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnEvcEceSrcPortFilterNo_Type.__name__ = "Integer32"
_TnEvcEceSrcPortFilterNo_Object = MibTableColumn
tnEvcEceSrcPortFilterNo = _TnEvcEceSrcPortFilterNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 19),
    _TnEvcEceSrcPortFilterNo_Type()
)
tnEvcEceSrcPortFilterNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceSrcPortFilterNo.setStatus("current")


class _TnEvcEceSrcPortRangeStart_Type(Integer32):
    """Custom type tnEvcEceSrcPortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnEvcEceSrcPortRangeStart_Type.__name__ = "Integer32"
_TnEvcEceSrcPortRangeStart_Object = MibTableColumn
tnEvcEceSrcPortRangeStart = _TnEvcEceSrcPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 20),
    _TnEvcEceSrcPortRangeStart_Type()
)
tnEvcEceSrcPortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceSrcPortRangeStart.setStatus("current")


class _TnEvcEceSrcPortRangeEnd_Type(Integer32):
    """Custom type tnEvcEceSrcPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnEvcEceSrcPortRangeEnd_Type.__name__ = "Integer32"
_TnEvcEceSrcPortRangeEnd_Object = MibTableColumn
tnEvcEceSrcPortRangeEnd = _TnEvcEceSrcPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 21),
    _TnEvcEceSrcPortRangeEnd_Type()
)
tnEvcEceSrcPortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceSrcPortRangeEnd.setStatus("current")


class _TnEvcEceDstPortFilterType_Type(Integer32):
    """Custom type tnEvcEceDstPortFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnEvcEceDstPortFilterType_Type.__name__ = "Integer32"
_TnEvcEceDstPortFilterType_Object = MibTableColumn
tnEvcEceDstPortFilterType = _TnEvcEceDstPortFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 22),
    _TnEvcEceDstPortFilterType_Type()
)
tnEvcEceDstPortFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDstPortFilterType.setStatus("current")


class _TnEvcEceDstPortFilterNo_Type(Integer32):
    """Custom type tnEvcEceDstPortFilterNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnEvcEceDstPortFilterNo_Type.__name__ = "Integer32"
_TnEvcEceDstPortFilterNo_Object = MibTableColumn
tnEvcEceDstPortFilterNo = _TnEvcEceDstPortFilterNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 23),
    _TnEvcEceDstPortFilterNo_Type()
)
tnEvcEceDstPortFilterNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDstPortFilterNo.setStatus("current")


class _TnEvcEceDstPortRangeStart_Type(Integer32):
    """Custom type tnEvcEceDstPortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnEvcEceDstPortRangeStart_Type.__name__ = "Integer32"
_TnEvcEceDstPortRangeStart_Object = MibTableColumn
tnEvcEceDstPortRangeStart = _TnEvcEceDstPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 24),
    _TnEvcEceDstPortRangeStart_Type()
)
tnEvcEceDstPortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDstPortRangeStart.setStatus("current")


class _TnEvcEceDstPortRangeEnd_Type(Integer32):
    """Custom type tnEvcEceDstPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnEvcEceDstPortRangeEnd_Type.__name__ = "Integer32"
_TnEvcEceDstPortRangeEnd_Object = MibTableColumn
tnEvcEceDstPortRangeEnd = _TnEvcEceDstPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 25),
    _TnEvcEceDstPortRangeEnd_Type()
)
tnEvcEceDstPortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDstPortRangeEnd.setStatus("current")


class _TnEvcEceIpv4DipSipFilter_Type(Integer32):
    """Custom type tnEvcEceIpv4DipSipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("host", 2),
          ("network", 3))
    )


_TnEvcEceIpv4DipSipFilter_Type.__name__ = "Integer32"
_TnEvcEceIpv4DipSipFilter_Object = MibTableColumn
tnEvcEceIpv4DipSipFilter = _TnEvcEceIpv4DipSipFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 26),
    _TnEvcEceIpv4DipSipFilter_Type()
)
tnEvcEceIpv4DipSipFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceIpv4DipSipFilter.setStatus("current")
_TnEvcEceIpv4DipSipAddr_Type = InetAddress
_TnEvcEceIpv4DipSipAddr_Object = MibTableColumn
tnEvcEceIpv4DipSipAddr = _TnEvcEceIpv4DipSipAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 27),
    _TnEvcEceIpv4DipSipAddr_Type()
)
tnEvcEceIpv4DipSipAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceIpv4DipSipAddr.setStatus("current")
_TnEvcEceIpv4DipSipMask_Type = InetAddress
_TnEvcEceIpv4DipSipMask_Object = MibTableColumn
tnEvcEceIpv4DipSipMask = _TnEvcEceIpv4DipSipMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 28),
    _TnEvcEceIpv4DipSipMask_Type()
)
tnEvcEceIpv4DipSipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceIpv4DipSipMask.setStatus("current")


class _TnEvcEceIpv4Fragment_Type(Integer32):
    """Custom type tnEvcEceIpv4Fragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("fragment", 2),
          ("nonfragment", 3))
    )


_TnEvcEceIpv4Fragment_Type.__name__ = "Integer32"
_TnEvcEceIpv4Fragment_Object = MibTableColumn
tnEvcEceIpv4Fragment = _TnEvcEceIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 29),
    _TnEvcEceIpv4Fragment_Type()
)
tnEvcEceIpv4Fragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceIpv4Fragment.setStatus("current")


class _TnEvcEceIpv6DipSipFilter_Type(Integer32):
    """Custom type tnEvcEceIpv6DipSipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceIpv6DipSipFilter_Type.__name__ = "Integer32"
_TnEvcEceIpv6DipSipFilter_Object = MibTableColumn
tnEvcEceIpv6DipSipFilter = _TnEvcEceIpv6DipSipFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 30),
    _TnEvcEceIpv6DipSipFilter_Type()
)
tnEvcEceIpv6DipSipFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceIpv6DipSipFilter.setStatus("current")
_TnEvcEceIpv6DipSipAddr_Type = Unsigned32
_TnEvcEceIpv6DipSipAddr_Object = MibTableColumn
tnEvcEceIpv6DipSipAddr = _TnEvcEceIpv6DipSipAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 31),
    _TnEvcEceIpv6DipSipAddr_Type()
)
tnEvcEceIpv6DipSipAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceIpv6DipSipAddr.setStatus("current")
_TnEvcEceIpv6DipSipMask_Type = Unsigned32
_TnEvcEceIpv6DipSipMask_Object = MibTableColumn
tnEvcEceIpv6DipSipMask = _TnEvcEceIpv6DipSipMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 32),
    _TnEvcEceIpv6DipSipMask_Type()
)
tnEvcEceIpv6DipSipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceIpv6DipSipMask.setStatus("current")


class _TnEvcEceOuterMode_Type(Integer32):
    """Custom type tnEvcEceOuterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnEvcEceOuterMode_Type.__name__ = "Integer32"
_TnEvcEceOuterMode_Object = MibTableColumn
tnEvcEceOuterMode = _TnEvcEceOuterMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 33),
    _TnEvcEceOuterMode_Type()
)
tnEvcEceOuterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceOuterMode.setStatus("current")


class _TnEvcEceOuterPCPDEIPreserve_Type(Integer32):
    """Custom type tnEvcEceOuterPCPDEIPreserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preserved", 1),
          ("fixed", 2))
    )


_TnEvcEceOuterPCPDEIPreserve_Type.__name__ = "Integer32"
_TnEvcEceOuterPCPDEIPreserve_Object = MibTableColumn
tnEvcEceOuterPCPDEIPreserve = _TnEvcEceOuterPCPDEIPreserve_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 34),
    _TnEvcEceOuterPCPDEIPreserve_Type()
)
tnEvcEceOuterPCPDEIPreserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceOuterPCPDEIPreserve.setStatus("current")


class _TnEvcEceOuterPCP_Type(Integer32):
    """Custom type tnEvcEceOuterPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnEvcEceOuterPCP_Type.__name__ = "Integer32"
_TnEvcEceOuterPCP_Object = MibTableColumn
tnEvcEceOuterPCP = _TnEvcEceOuterPCP_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 35),
    _TnEvcEceOuterPCP_Type()
)
tnEvcEceOuterPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceOuterPCP.setStatus("current")


class _TnEvcEceOuterDEI_Type(Integer32):
    """Custom type tnEvcEceOuterDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnEvcEceOuterDEI_Type.__name__ = "Integer32"
_TnEvcEceOuterDEI_Object = MibTableColumn
tnEvcEceOuterDEI = _TnEvcEceOuterDEI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 36),
    _TnEvcEceOuterDEI_Type()
)
tnEvcEceOuterDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceOuterDEI.setStatus("current")


class _TnEvcEceActDirection_Type(Integer32):
    """Custom type tnEvcEceActDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("uni2nni", 2),
          ("nni2uni", 3))
    )


_TnEvcEceActDirection_Type.__name__ = "Integer32"
_TnEvcEceActDirection_Object = MibTableColumn
tnEvcEceActDirection = _TnEvcEceActDirection_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 37),
    _TnEvcEceActDirection_Type()
)
tnEvcEceActDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceActDirection.setStatus("current")


class _TnEvcEceActEvcidFilterType_Type(Integer32):
    """Custom type tnEvcEceActEvcidFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceActEvcidFilterType_Type.__name__ = "Integer32"
_TnEvcEceActEvcidFilterType_Object = MibTableColumn
tnEvcEceActEvcidFilterType = _TnEvcEceActEvcidFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 38),
    _TnEvcEceActEvcidFilterType_Type()
)
tnEvcEceActEvcidFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceActEvcidFilterType.setStatus("current")


class _TnEvcEceActEvcidVal_Type(Integer32):
    """Custom type tnEvcEceActEvcidVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnEvcEceActEvcidVal_Type.__name__ = "Integer32"
_TnEvcEceActEvcidVal_Object = MibTableColumn
tnEvcEceActEvcidVal = _TnEvcEceActEvcidVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 39),
    _TnEvcEceActEvcidVal_Type()
)
tnEvcEceActEvcidVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceActEvcidVal.setStatus("current")


class _TnEvcEceActTagPopCount_Type(Integer32):
    """Custom type tnEvcEceActTagPopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TnEvcEceActTagPopCount_Type.__name__ = "Integer32"
_TnEvcEceActTagPopCount_Object = MibTableColumn
tnEvcEceActTagPopCount = _TnEvcEceActTagPopCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 40),
    _TnEvcEceActTagPopCount_Type()
)
tnEvcEceActTagPopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceActTagPopCount.setStatus("current")


class _TnEvcEceActPolicyId_Type(Integer32):
    """Custom type tnEvcEceActPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnEvcEceActPolicyId_Type.__name__ = "Integer32"
_TnEvcEceActPolicyId_Object = MibTableColumn
tnEvcEceActPolicyId = _TnEvcEceActPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 41),
    _TnEvcEceActPolicyId_Type()
)
tnEvcEceActPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceActPolicyId.setStatus("current")


class _TnEvcEceActClass_Type(Integer32):
    """Custom type tnEvcEceActClass based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 1),
          ("tc1", 2),
          ("tc2", 3),
          ("tc3", 4),
          ("tc4", 5),
          ("tc5", 6),
          ("tc6", 7),
          ("tc7", 8),
          ("disabled", 9))
    )


_TnEvcEceActClass_Type.__name__ = "Integer32"
_TnEvcEceActClass_Object = MibTableColumn
tnEvcEceActClass = _TnEvcEceActClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 42),
    _TnEvcEceActClass_Type()
)
tnEvcEceActClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceActClass.setStatus("current")


class _TnEvcEceDMacSMacFilterType_Type(Integer32):
    """Custom type tnEvcEceDMacSMacFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceDMacSMacFilterType_Type.__name__ = "Integer32"
_TnEvcEceDMacSMacFilterType_Object = MibTableColumn
tnEvcEceDMacSMacFilterType = _TnEvcEceDMacSMacFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 43),
    _TnEvcEceDMacSMacFilterType_Type()
)
tnEvcEceDMacSMacFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDMacSMacFilterType.setStatus("current")
_TnEvcEceDMacSMacVal_Type = MacAddress
_TnEvcEceDMacSMacVal_Object = MibTableColumn
tnEvcEceDMacSMacVal = _TnEvcEceDMacSMacVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 44),
    _TnEvcEceDMacSMacVal_Type()
)
tnEvcEceDMacSMacVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDMacSMacVal.setStatus("current")


class _TnEvcEceDMacType_Type(Integer32):
    """Custom type tnEvcEceDMacType based on Integer32"""
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
        *(("any", 1),
          ("unicast", 2),
          ("multicast", 3),
          ("broadcast", 4),
          ("specific", 5))
    )


_TnEvcEceDMacType_Type.__name__ = "Integer32"
_TnEvcEceDMacType_Object = MibTableColumn
tnEvcEceDMacType = _TnEvcEceDMacType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 45),
    _TnEvcEceDMacType_Type()
)
tnEvcEceDMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceDMacType.setStatus("current")


class _TnEvcEceConflict_Type(Integer32):
    """Custom type tnEvcEceConflict based on Integer32"""
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


_TnEvcEceConflict_Type.__name__ = "Integer32"
_TnEvcEceConflict_Object = MibTableColumn
tnEvcEceConflict = _TnEvcEceConflict_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 46),
    _TnEvcEceConflict_Type()
)
tnEvcEceConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcEceConflict.setStatus("current")
_TnEvcEceStatus_Type = RowStatus
_TnEvcEceStatus_Object = MibTableColumn
tnEvcEceStatus = _TnEvcEceStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 3, 1, 47),
    _TnEvcEceStatus_Type()
)
tnEvcEceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceStatus.setStatus("current")
_TnEvcBandwidthProfilesTable_Object = MibTable
tnEvcBandwidthProfilesTable = _TnEvcBandwidthProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tnEvcBandwidthProfilesTable.setStatus("current")
_TnEvcBandwidthProfilesEntry_Object = MibTableRow
tnEvcBandwidthProfilesEntry = _TnEvcBandwidthProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 4, 1)
)
tnEvcBandwidthProfilesEntry.setIndexNames(
    (0, "TN-EVC-MIB", "tnEvcBandwidthProfilesIndex"),
)
if mibBuilder.loadTexts:
    tnEvcBandwidthProfilesEntry.setStatus("current")


class _TnEvcBandwidthProfilesIndex_Type(Integer32):
    """Custom type tnEvcBandwidthProfilesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnEvcBandwidthProfilesIndex_Type.__name__ = "Integer32"
_TnEvcBandwidthProfilesIndex_Object = MibTableColumn
tnEvcBandwidthProfilesIndex = _TnEvcBandwidthProfilesIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 4, 1, 1),
    _TnEvcBandwidthProfilesIndex_Type()
)
tnEvcBandwidthProfilesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEvcBandwidthProfilesIndex.setStatus("current")


class _TnEvcBandwidthProfilesPolicerMode_Type(Integer32):
    """Custom type tnEvcBandwidthProfilesPolicerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coupled", 1),
          ("aware", 2),
          ("blind", 3))
    )


_TnEvcBandwidthProfilesPolicerMode_Type.__name__ = "Integer32"
_TnEvcBandwidthProfilesPolicerMode_Object = MibTableColumn
tnEvcBandwidthProfilesPolicerMode = _TnEvcBandwidthProfilesPolicerMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 4, 1, 2),
    _TnEvcBandwidthProfilesPolicerMode_Type()
)
tnEvcBandwidthProfilesPolicerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcBandwidthProfilesPolicerMode.setStatus("current")


class _TnEvcBandwidthProfilesCIR_Type(Integer32):
    """Custom type tnEvcBandwidthProfilesCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_TnEvcBandwidthProfilesCIR_Type.__name__ = "Integer32"
_TnEvcBandwidthProfilesCIR_Object = MibTableColumn
tnEvcBandwidthProfilesCIR = _TnEvcBandwidthProfilesCIR_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 4, 1, 3),
    _TnEvcBandwidthProfilesCIR_Type()
)
tnEvcBandwidthProfilesCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcBandwidthProfilesCIR.setStatus("current")


class _TnEvcBandwidthProfilesCBS_Type(Integer32):
    """Custom type tnEvcBandwidthProfilesCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TnEvcBandwidthProfilesCBS_Type.__name__ = "Integer32"
_TnEvcBandwidthProfilesCBS_Object = MibTableColumn
tnEvcBandwidthProfilesCBS = _TnEvcBandwidthProfilesCBS_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 4, 1, 4),
    _TnEvcBandwidthProfilesCBS_Type()
)
tnEvcBandwidthProfilesCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcBandwidthProfilesCBS.setStatus("current")


class _TnEvcBandwidthProfilesEIR_Type(Integer32):
    """Custom type tnEvcBandwidthProfilesEIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_TnEvcBandwidthProfilesEIR_Type.__name__ = "Integer32"
_TnEvcBandwidthProfilesEIR_Object = MibTableColumn
tnEvcBandwidthProfilesEIR = _TnEvcBandwidthProfilesEIR_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 4, 1, 5),
    _TnEvcBandwidthProfilesEIR_Type()
)
tnEvcBandwidthProfilesEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcBandwidthProfilesEIR.setStatus("current")


class _TnEvcBandwidthProfilesEBS_Type(Integer32):
    """Custom type tnEvcBandwidthProfilesEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TnEvcBandwidthProfilesEBS_Type.__name__ = "Integer32"
_TnEvcBandwidthProfilesEBS_Object = MibTableColumn
tnEvcBandwidthProfilesEBS = _TnEvcBandwidthProfilesEBS_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 4, 1, 6),
    _TnEvcBandwidthProfilesEBS_Type()
)
tnEvcBandwidthProfilesEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcBandwidthProfilesEBS.setStatus("current")


class _TnEvcBandwidthProfilesState_Type(Integer32):
    """Custom type tnEvcBandwidthProfilesState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnEvcBandwidthProfilesState_Type.__name__ = "Integer32"
_TnEvcBandwidthProfilesState_Object = MibTableColumn
tnEvcBandwidthProfilesState = _TnEvcBandwidthProfilesState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 4, 1, 7),
    _TnEvcBandwidthProfilesState_Type()
)
tnEvcBandwidthProfilesState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcBandwidthProfilesState.setStatus("current")
_TnEvcExtEceTable_Object = MibTable
tnEvcExtEceTable = _TnEvcExtEceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tnEvcExtEceTable.setStatus("current")
_TnEvcExtEceEntry_Object = MibTableRow
tnEvcExtEceEntry = _TnEvcExtEceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnEvcExtEceEntry.setStatus("current")


class _TnEvcEceInnerTagType_Type(Integer32):
    """Custom type tnEvcEceInnerTagType based on Integer32"""
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
        *(("any", 1),
          ("untagged", 2),
          ("tagged", 3),
          ("c-tag", 4),
          ("s-tag", 5))
    )


_TnEvcEceInnerTagType_Type.__name__ = "Integer32"
_TnEvcEceInnerTagType_Object = MibTableColumn
tnEvcEceInnerTagType = _TnEvcEceInnerTagType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 1),
    _TnEvcEceInnerTagType_Type()
)
tnEvcEceInnerTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerTagType.setStatus("current")


class _TnEvcEceInnerTagVIDFilterType_Type(Integer32):
    """Custom type tnEvcEceInnerTagVIDFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnEvcEceInnerTagVIDFilterType_Type.__name__ = "Integer32"
_TnEvcEceInnerTagVIDFilterType_Object = MibTableColumn
tnEvcEceInnerTagVIDFilterType = _TnEvcEceInnerTagVIDFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 2),
    _TnEvcEceInnerTagVIDFilterType_Type()
)
tnEvcEceInnerTagVIDFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerTagVIDFilterType.setStatus("current")
_TnEvcEceInnerTagVIDFilterVal_Type = VlanIdOrNone
_TnEvcEceInnerTagVIDFilterVal_Object = MibTableColumn
tnEvcEceInnerTagVIDFilterVal = _TnEvcEceInnerTagVIDFilterVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 3),
    _TnEvcEceInnerTagVIDFilterVal_Type()
)
tnEvcEceInnerTagVIDFilterVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerTagVIDFilterVal.setStatus("current")
_TnEvcEceInnerTagVIDFilterStart_Type = VlanIdOrNone
_TnEvcEceInnerTagVIDFilterStart_Object = MibTableColumn
tnEvcEceInnerTagVIDFilterStart = _TnEvcEceInnerTagVIDFilterStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 4),
    _TnEvcEceInnerTagVIDFilterStart_Type()
)
tnEvcEceInnerTagVIDFilterStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerTagVIDFilterStart.setStatus("current")
_TnEvcEceInnerTagVIDFilterEnd_Type = VlanIdOrNone
_TnEvcEceInnerTagVIDFilterEnd_Object = MibTableColumn
tnEvcEceInnerTagVIDFilterEnd = _TnEvcEceInnerTagVIDFilterEnd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 5),
    _TnEvcEceInnerTagVIDFilterEnd_Type()
)
tnEvcEceInnerTagVIDFilterEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerTagVIDFilterEnd.setStatus("current")


class _TnEvcEceInnerTagPCP_Type(Bits):
    """Custom type tnEvcEceInnerTagPCP based on Bits"""
    namedValues = NamedValues(
        ("none", 0)
    )

_TnEvcEceInnerTagPCP_Type.__name__ = "Bits"
_TnEvcEceInnerTagPCP_Object = MibTableColumn
tnEvcEceInnerTagPCP = _TnEvcEceInnerTagPCP_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 6),
    _TnEvcEceInnerTagPCP_Type()
)
tnEvcEceInnerTagPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerTagPCP.setStatus("current")


class _TnEvcEceInnerTagDEI_Type(Integer32):
    """Custom type tnEvcEceInnerTagDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dei0", 2),
          ("dei1", 3))
    )


_TnEvcEceInnerTagDEI_Type.__name__ = "Integer32"
_TnEvcEceInnerTagDEI_Object = MibTableColumn
tnEvcEceInnerTagDEI = _TnEvcEceInnerTagDEI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 7),
    _TnEvcEceInnerTagDEI_Type()
)
tnEvcEceInnerTagDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerTagDEI.setStatus("current")


class _TnEvcEcePolicer_Type(Integer32):
    """Custom type tnEvcEcePolicer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_TnEvcEcePolicer_Type.__name__ = "Integer32"
_TnEvcEcePolicer_Object = MibTableColumn
tnEvcEcePolicer = _TnEvcEcePolicer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 8),
    _TnEvcEcePolicer_Type()
)
tnEvcEcePolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEcePolicer.setStatus("current")
_TnEvcEceOuterVid_Type = VlanIdOrNone
_TnEvcEceOuterVid_Object = MibTableColumn
tnEvcEceOuterVid = _TnEvcEceOuterVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 9),
    _TnEvcEceOuterVid_Type()
)
tnEvcEceOuterVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceOuterVid.setStatus("current")


class _TnEvcEceNNIInnerTagType_Type(Integer32):
    """Custom type tnEvcEceNNIInnerTagType based on Integer32"""
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
          ("ctag", 1),
          ("stag", 2),
          ("sctag", 3))
    )


_TnEvcEceNNIInnerTagType_Type.__name__ = "Integer32"
_TnEvcEceNNIInnerTagType_Object = MibTableColumn
tnEvcEceNNIInnerTagType = _TnEvcEceNNIInnerTagType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 10),
    _TnEvcEceNNIInnerTagType_Type()
)
tnEvcEceNNIInnerTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceNNIInnerTagType.setStatus("current")
_TnEvcEceInnerVid_Type = VlanIdOrNone
_TnEvcEceInnerVid_Object = MibTableColumn
tnEvcEceInnerVid = _TnEvcEceInnerVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 11),
    _TnEvcEceInnerVid_Type()
)
tnEvcEceInnerVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerVid.setStatus("current")


class _TnEvcEceInnerPCPDEIPreserve_Type(Integer32):
    """Custom type tnEvcEceInnerPCPDEIPreserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preserved", 1),
          ("fixed", 2))
    )


_TnEvcEceInnerPCPDEIPreserve_Type.__name__ = "Integer32"
_TnEvcEceInnerPCPDEIPreserve_Object = MibTableColumn
tnEvcEceInnerPCPDEIPreserve = _TnEvcEceInnerPCPDEIPreserve_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 12),
    _TnEvcEceInnerPCPDEIPreserve_Type()
)
tnEvcEceInnerPCPDEIPreserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerPCPDEIPreserve.setStatus("current")


class _TnEvcEceInnerPCP_Type(Integer32):
    """Custom type tnEvcEceInnerPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnEvcEceInnerPCP_Type.__name__ = "Integer32"
_TnEvcEceInnerPCP_Object = MibTableColumn
tnEvcEceInnerPCP = _TnEvcEceInnerPCP_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 13),
    _TnEvcEceInnerPCP_Type()
)
tnEvcEceInnerPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerPCP.setStatus("current")


class _TnEvcEceInnerDEI_Type(Integer32):
    """Custom type tnEvcEceInnerDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnEvcEceInnerDEI_Type.__name__ = "Integer32"
_TnEvcEceInnerDEI_Object = MibTableColumn
tnEvcEceInnerDEI = _TnEvcEceInnerDEI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 14),
    _TnEvcEceInnerDEI_Type()
)
tnEvcEceInnerDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcEceInnerDEI.setStatus("current")
_TnEvcEceDMacVal_Type = MacAddress
_TnEvcEceDMacVal_Object = MibTableColumn
tnEvcEceDMacVal = _TnEvcEceDMacVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 15),
    _TnEvcEceDMacVal_Type()
)
tnEvcEceDMacVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceDMacVal.setStatus("current")


class _TnEvcEceOuterPCPMode_Type(Integer32):
    """Custom type tnEvcEceOuterPCPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classified", 1),
          ("fixed", 2),
          ("mapped", 3))
    )


_TnEvcEceOuterPCPMode_Type.__name__ = "Integer32"
_TnEvcEceOuterPCPMode_Object = MibTableColumn
tnEvcEceOuterPCPMode = _TnEvcEceOuterPCPMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 16),
    _TnEvcEceOuterPCPMode_Type()
)
tnEvcEceOuterPCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceOuterPCPMode.setStatus("current")


class _TnEvcEceOuterDEIMode_Type(Integer32):
    """Custom type tnEvcEceOuterDEIMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classified", 1),
          ("fixed", 2),
          ("dropPrec", 3))
    )


_TnEvcEceOuterDEIMode_Type.__name__ = "Integer32"
_TnEvcEceOuterDEIMode_Object = MibTableColumn
tnEvcEceOuterDEIMode = _TnEvcEceOuterDEIMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 17),
    _TnEvcEceOuterDEIMode_Type()
)
tnEvcEceOuterDEIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceOuterDEIMode.setStatus("current")


class _TnEvcEceActRuleType_Type(Integer32):
    """Custom type tnEvcEceActRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("rx", 2),
          ("tx", 3))
    )


_TnEvcEceActRuleType_Type.__name__ = "Integer32"
_TnEvcEceActRuleType_Object = MibTableColumn
tnEvcEceActRuleType = _TnEvcEceActRuleType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 18),
    _TnEvcEceActRuleType_Type()
)
tnEvcEceActRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceActRuleType.setStatus("current")


class _TnEvcEceActTxLookupType_Type(Integer32):
    """Custom type tnEvcEceActTxLookupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vidLookup", 1),
          ("vidPCP", 2),
          ("isdx", 3))
    )


_TnEvcEceActTxLookupType_Type.__name__ = "Integer32"
_TnEvcEceActTxLookupType_Object = MibTableColumn
tnEvcEceActTxLookupType = _TnEvcEceActTxLookupType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 19),
    _TnEvcEceActTxLookupType_Type()
)
tnEvcEceActTxLookupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceActTxLookupType.setStatus("current")


class _TnEvcEceActDropPrecType_Type(Integer32):
    """Custom type tnEvcEceActDropPrecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp0", 1),
          ("dp1", 2),
          ("disabled", 3))
    )


_TnEvcEceActDropPrecType_Type.__name__ = "Integer32"
_TnEvcEceActDropPrecType_Object = MibTableColumn
tnEvcEceActDropPrecType = _TnEvcEceActDropPrecType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 20),
    _TnEvcEceActDropPrecType_Type()
)
tnEvcEceActDropPrecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceActDropPrecType.setStatus("current")


class _TnEvcEceInnerPcpMode_Type(Integer32):
    """Custom type tnEvcEceInnerPcpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classified", 1),
          ("fixed", 2),
          ("mapped", 3))
    )


_TnEvcEceInnerPcpMode_Type.__name__ = "Integer32"
_TnEvcEceInnerPcpMode_Object = MibTableColumn
tnEvcEceInnerPcpMode = _TnEvcEceInnerPcpMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 21),
    _TnEvcEceInnerPcpMode_Type()
)
tnEvcEceInnerPcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceInnerPcpMode.setStatus("current")


class _TnEvcEceIInnerDeiMode_Type(Integer32):
    """Custom type tnEvcEceIInnerDeiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classified", 1),
          ("fixed", 2),
          ("dropPrecedence", 3))
    )


_TnEvcEceIInnerDeiMode_Type.__name__ = "Integer32"
_TnEvcEceIInnerDeiMode_Object = MibTableColumn
tnEvcEceIInnerDeiMode = _TnEvcEceIInnerDeiMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 22),
    _TnEvcEceIInnerDeiMode_Type()
)
tnEvcEceIInnerDeiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceIInnerDeiMode.setStatus("current")


class _TnEvcEceIpv4DipFilter_Type(Integer32):
    """Custom type tnEvcEceIpv4DipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("host", 2),
          ("network", 3))
    )


_TnEvcEceIpv4DipFilter_Type.__name__ = "Integer32"
_TnEvcEceIpv4DipFilter_Object = MibTableColumn
tnEvcEceIpv4DipFilter = _TnEvcEceIpv4DipFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 23),
    _TnEvcEceIpv4DipFilter_Type()
)
tnEvcEceIpv4DipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceIpv4DipFilter.setStatus("current")
_TnEvcEceIpv4DipAddr_Type = InetAddress
_TnEvcEceIpv4DipAddr_Object = MibTableColumn
tnEvcEceIpv4DipAddr = _TnEvcEceIpv4DipAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 24),
    _TnEvcEceIpv4DipAddr_Type()
)
tnEvcEceIpv4DipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceIpv4DipAddr.setStatus("current")
_TnEvcEceIpv4DipMask_Type = InetAddress
_TnEvcEceIpv4DipMask_Object = MibTableColumn
tnEvcEceIpv4DipMask = _TnEvcEceIpv4DipMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 25),
    _TnEvcEceIpv4DipMask_Type()
)
tnEvcEceIpv4DipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceIpv4DipMask.setStatus("current")


class _TnEvcEceIpv6DipFilter_Type(Integer32):
    """Custom type tnEvcEceIpv6DipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("host", 2),
          ("network", 3))
    )


_TnEvcEceIpv6DipFilter_Type.__name__ = "Integer32"
_TnEvcEceIpv6DipFilter_Object = MibTableColumn
tnEvcEceIpv6DipFilter = _TnEvcEceIpv6DipFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 26),
    _TnEvcEceIpv6DipFilter_Type()
)
tnEvcEceIpv6DipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceIpv6DipFilter.setStatus("current")
_TnEvcEceIpv6DipAddr_Type = Unsigned32
_TnEvcEceIpv6DipAddr_Object = MibTableColumn
tnEvcEceIpv6DipAddr = _TnEvcEceIpv6DipAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 27),
    _TnEvcEceIpv6DipAddr_Type()
)
tnEvcEceIpv6DipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceIpv6DipAddr.setStatus("current")
_TnEvcEceIpv6DipMask_Type = Unsigned32
_TnEvcEceIpv6DipMask_Object = MibTableColumn
tnEvcEceIpv6DipMask = _TnEvcEceIpv6DipMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 28),
    _TnEvcEceIpv6DipMask_Type()
)
tnEvcEceIpv6DipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceIpv6DipMask.setStatus("current")


class _TnEvcEceLookup_Type(Integer32):
    """Custom type tnEvcEceLookup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("advanced", 2))
    )


_TnEvcEceLookup_Type.__name__ = "Integer32"
_TnEvcEceLookup_Object = MibTableColumn
tnEvcEceLookup = _TnEvcEceLookup_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 29),
    _TnEvcEceLookup_Type()
)
tnEvcEceLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLookup.setStatus("current")


class _TnEvcEceEtypeFilter_Type(Integer32):
    """Custom type tnEvcEceEtypeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceEtypeFilter_Type.__name__ = "Integer32"
_TnEvcEceEtypeFilter_Object = MibTableColumn
tnEvcEceEtypeFilter = _TnEvcEceEtypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 30),
    _TnEvcEceEtypeFilter_Type()
)
tnEvcEceEtypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceEtypeFilter.setStatus("current")
_TnEvcEceEtypeValue_Type = Unsigned32
_TnEvcEceEtypeValue_Object = MibTableColumn
tnEvcEceEtypeValue = _TnEvcEceEtypeValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 31),
    _TnEvcEceEtypeValue_Type()
)
tnEvcEceEtypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceEtypeValue.setStatus("current")


class _TnEvcEceEtypeDataFilter_Type(Integer32):
    """Custom type tnEvcEceEtypeDataFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceEtypeDataFilter_Type.__name__ = "Integer32"
_TnEvcEceEtypeDataFilter_Object = MibTableColumn
tnEvcEceEtypeDataFilter = _TnEvcEceEtypeDataFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 32),
    _TnEvcEceEtypeDataFilter_Type()
)
tnEvcEceEtypeDataFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceEtypeDataFilter.setStatus("current")
_TnEvcEceEtypeData_Type = Unsigned32
_TnEvcEceEtypeData_Object = MibTableColumn
tnEvcEceEtypeData = _TnEvcEceEtypeData_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 33),
    _TnEvcEceEtypeData_Type()
)
tnEvcEceEtypeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceEtypeData.setStatus("current")
_TnEvcEceEtypeDataMask_Type = Unsigned32
_TnEvcEceEtypeDataMask_Object = MibTableColumn
tnEvcEceEtypeDataMask = _TnEvcEceEtypeDataMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 34),
    _TnEvcEceEtypeDataMask_Type()
)
tnEvcEceEtypeDataMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceEtypeDataMask.setStatus("current")


class _TnEvcEceLlcDSAPFilter_Type(Integer32):
    """Custom type tnEvcEceLlcDSAPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceLlcDSAPFilter_Type.__name__ = "Integer32"
_TnEvcEceLlcDSAPFilter_Object = MibTableColumn
tnEvcEceLlcDSAPFilter = _TnEvcEceLlcDSAPFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 35),
    _TnEvcEceLlcDSAPFilter_Type()
)
tnEvcEceLlcDSAPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLlcDSAPFilter.setStatus("current")
_TnEvcEceLlcDSAPValue_Type = Unsigned32
_TnEvcEceLlcDSAPValue_Object = MibTableColumn
tnEvcEceLlcDSAPValue = _TnEvcEceLlcDSAPValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 36),
    _TnEvcEceLlcDSAPValue_Type()
)
tnEvcEceLlcDSAPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLlcDSAPValue.setStatus("current")


class _TnEvcEceLlcSSAPFilter_Type(Integer32):
    """Custom type tnEvcEceLlcSSAPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceLlcSSAPFilter_Type.__name__ = "Integer32"
_TnEvcEceLlcSSAPFilter_Object = MibTableColumn
tnEvcEceLlcSSAPFilter = _TnEvcEceLlcSSAPFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 37),
    _TnEvcEceLlcSSAPFilter_Type()
)
tnEvcEceLlcSSAPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLlcSSAPFilter.setStatus("current")
_TnEvcEceLlcSSAPValue_Type = Unsigned32
_TnEvcEceLlcSSAPValue_Object = MibTableColumn
tnEvcEceLlcSSAPValue = _TnEvcEceLlcSSAPValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 38),
    _TnEvcEceLlcSSAPValue_Type()
)
tnEvcEceLlcSSAPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLlcSSAPValue.setStatus("current")


class _TnEvcEceLlcCtrlFilter_Type(Integer32):
    """Custom type tnEvcEceLlcCtrlFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceLlcCtrlFilter_Type.__name__ = "Integer32"
_TnEvcEceLlcCtrlFilter_Object = MibTableColumn
tnEvcEceLlcCtrlFilter = _TnEvcEceLlcCtrlFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 39),
    _TnEvcEceLlcCtrlFilter_Type()
)
tnEvcEceLlcCtrlFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLlcCtrlFilter.setStatus("current")
_TnEvcEceLlcCtrlValue_Type = Unsigned32
_TnEvcEceLlcCtrlValue_Object = MibTableColumn
tnEvcEceLlcCtrlValue = _TnEvcEceLlcCtrlValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 40),
    _TnEvcEceLlcCtrlValue_Type()
)
tnEvcEceLlcCtrlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLlcCtrlValue.setStatus("current")


class _TnEvcEceLlcDataFilter_Type(Integer32):
    """Custom type tnEvcEceLlcDataFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceLlcDataFilter_Type.__name__ = "Integer32"
_TnEvcEceLlcDataFilter_Object = MibTableColumn
tnEvcEceLlcDataFilter = _TnEvcEceLlcDataFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 41),
    _TnEvcEceLlcDataFilter_Type()
)
tnEvcEceLlcDataFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLlcDataFilter.setStatus("current")
_TnEvcEceLlcDataValue_Type = Unsigned32
_TnEvcEceLlcDataValue_Object = MibTableColumn
tnEvcEceLlcDataValue = _TnEvcEceLlcDataValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 42),
    _TnEvcEceLlcDataValue_Type()
)
tnEvcEceLlcDataValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLlcDataValue.setStatus("current")
_TnEvcEceLlcDataMask_Type = Unsigned32
_TnEvcEceLlcDataMask_Object = MibTableColumn
tnEvcEceLlcDataMask = _TnEvcEceLlcDataMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 43),
    _TnEvcEceLlcDataMask_Type()
)
tnEvcEceLlcDataMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceLlcDataMask.setStatus("current")


class _TnEvcEceSnapOuiFilter_Type(Integer32):
    """Custom type tnEvcEceSnapOuiFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceSnapOuiFilter_Type.__name__ = "Integer32"
_TnEvcEceSnapOuiFilter_Object = MibTableColumn
tnEvcEceSnapOuiFilter = _TnEvcEceSnapOuiFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 44),
    _TnEvcEceSnapOuiFilter_Type()
)
tnEvcEceSnapOuiFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceSnapOuiFilter.setStatus("current")
_TnEvcEceSnapOuiValue_Type = Unsigned32
_TnEvcEceSnapOuiValue_Object = MibTableColumn
tnEvcEceSnapOuiValue = _TnEvcEceSnapOuiValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 45),
    _TnEvcEceSnapOuiValue_Type()
)
tnEvcEceSnapOuiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceSnapOuiValue.setStatus("current")


class _TnEvcEceSnapPidFilter_Type(Integer32):
    """Custom type tnEvcEceSnapPidFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnEvcEceSnapPidFilter_Type.__name__ = "Integer32"
_TnEvcEceSnapPidFilter_Object = MibTableColumn
tnEvcEceSnapPidFilter = _TnEvcEceSnapPidFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 46),
    _TnEvcEceSnapPidFilter_Type()
)
tnEvcEceSnapPidFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceSnapPidFilter.setStatus("current")
_TnEvcEceSnapPidValue_Type = Unsigned32
_TnEvcEceSnapPidValue_Object = MibTableColumn
tnEvcEceSnapPidValue = _TnEvcEceSnapPidValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 47),
    _TnEvcEceSnapPidValue_Type()
)
tnEvcEceSnapPidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceSnapPidValue.setStatus("current")


class _TnEvcEceL2cpProtoType_Type(Integer32):
    """Custom type tnEvcEceL2cpProtoType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("stpRstpMstp", 1),
          ("pause", 2),
          ("lacp", 3),
          ("lamp", 4),
          ("linkOam", 5),
          ("portAuth8021x", 6),
          ("elmi", 7),
          ("pbGroupAddr", 8),
          ("pbGvrp", 9),
          ("lldp", 10),
          ("gmrp", 11),
          ("gvrp", 12),
          ("uld", 13),
          ("pagp", 14),
          ("pvstPvstP", 15),
          ("ciscoBpdu", 16),
          ("cdp", 17),
          ("vtp", 18),
          ("dtp", 19),
          ("stpUplinkFast", 20),
          ("ciscoCfm", 21))
    )


_TnEvcEceL2cpProtoType_Type.__name__ = "Integer32"
_TnEvcEceL2cpProtoType_Object = MibTableColumn
tnEvcEceL2cpProtoType = _TnEvcEceL2cpProtoType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 1, 5, 1, 48),
    _TnEvcEceL2cpProtoType_Type()
)
tnEvcEceL2cpProtoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcEceL2cpProtoType.setStatus("current")
_TnEvcStatGroup_ObjectIdentity = ObjectIdentity
tnEvcStatGroup = _TnEvcStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2)
)
_TnEvcStatTable_Object = MibTable
tnEvcStatTable = _TnEvcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnEvcStatTable.setStatus("current")
_TnEvcStatEntry_Object = MibTableRow
tnEvcStatEntry = _TnEvcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1)
)
tnEvcStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-EVC-MIB", "tnEvcStatClass"),
)
if mibBuilder.loadTexts:
    tnEvcStatEntry.setStatus("current")


class _TnEvcStatClass_Type(Integer32):
    """Custom type tnEvcStatClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnEvcStatClass_Type.__name__ = "Integer32"
_TnEvcStatClass_Object = MibTableColumn
tnEvcStatClass = _TnEvcStatClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1, 1),
    _TnEvcStatClass_Type()
)
tnEvcStatClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEvcStatClass.setStatus("current")
_TnEvcStatGreenFrameRx_Type = Counter64
_TnEvcStatGreenFrameRx_Object = MibTableColumn
tnEvcStatGreenFrameRx = _TnEvcStatGreenFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1, 2),
    _TnEvcStatGreenFrameRx_Type()
)
tnEvcStatGreenFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcStatGreenFrameRx.setStatus("current")
_TnEvcStatGreenFrameTx_Type = Counter64
_TnEvcStatGreenFrameTx_Object = MibTableColumn
tnEvcStatGreenFrameTx = _TnEvcStatGreenFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1, 3),
    _TnEvcStatGreenFrameTx_Type()
)
tnEvcStatGreenFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcStatGreenFrameTx.setStatus("current")
_TnEvcStatYellowFrameRx_Type = Counter64
_TnEvcStatYellowFrameRx_Object = MibTableColumn
tnEvcStatYellowFrameRx = _TnEvcStatYellowFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1, 4),
    _TnEvcStatYellowFrameRx_Type()
)
tnEvcStatYellowFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcStatYellowFrameRx.setStatus("current")
_TnEvcStatYellowFrameTx_Type = Counter64
_TnEvcStatYellowFrameTx_Object = MibTableColumn
tnEvcStatYellowFrameTx = _TnEvcStatYellowFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1, 5),
    _TnEvcStatYellowFrameTx_Type()
)
tnEvcStatYellowFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcStatYellowFrameTx.setStatus("current")
_TnEvcStatRedFrameRx_Type = Counter64
_TnEvcStatRedFrameRx_Object = MibTableColumn
tnEvcStatRedFrameRx = _TnEvcStatRedFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1, 6),
    _TnEvcStatRedFrameRx_Type()
)
tnEvcStatRedFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcStatRedFrameRx.setStatus("current")
_TnEvcStatDiscardGreenFrame_Type = Counter64
_TnEvcStatDiscardGreenFrame_Object = MibTableColumn
tnEvcStatDiscardGreenFrame = _TnEvcStatDiscardGreenFrame_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1, 7),
    _TnEvcStatDiscardGreenFrame_Type()
)
tnEvcStatDiscardGreenFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcStatDiscardGreenFrame.setStatus("current")
_TnEvcStatDiscardYellowFrame_Type = Counter64
_TnEvcStatDiscardYellowFrame_Object = MibTableColumn
tnEvcStatDiscardYellowFrame = _TnEvcStatDiscardYellowFrame_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1, 8),
    _TnEvcStatDiscardYellowFrame_Type()
)
tnEvcStatDiscardYellowFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcStatDiscardYellowFrame.setStatus("current")
_TnEvcStatClear_Type = TruthValue
_TnEvcStatClear_Object = MibTableColumn
tnEvcStatClear = _TnEvcStatClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 1, 1, 9),
    _TnEvcStatClear_Type()
)
tnEvcStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcStatClear.setStatus("current")
_TnEvcExtStatTable_Object = MibTable
tnEvcExtStatTable = _TnEvcExtStatTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnEvcExtStatTable.setStatus("current")
_TnEvcExtStatEntry_Object = MibTableRow
tnEvcExtStatEntry = _TnEvcExtStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1)
)
tnEvcExtStatEntry.setIndexNames(
    (0, "TN-EVC-MIB", "tnEvcExtStatType"),
    (0, "TN-EVC-MIB", "tnEvcExtStatIndex"),
    (0, "TN-EVC-MIB", "tnEvcExtStatPort"),
)
if mibBuilder.loadTexts:
    tnEvcExtStatEntry.setStatus("current")


class _TnEvcExtStatType_Type(Integer32):
    """Custom type tnEvcExtStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("evc", 1),
          ("ece", 2))
    )


_TnEvcExtStatType_Type.__name__ = "Integer32"
_TnEvcExtStatType_Object = MibTableColumn
tnEvcExtStatType = _TnEvcExtStatType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 1),
    _TnEvcExtStatType_Type()
)
tnEvcExtStatType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEvcExtStatType.setStatus("current")


class _TnEvcExtStatIndex_Type(Integer32):
    """Custom type tnEvcExtStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnEvcExtStatIndex_Type.__name__ = "Integer32"
_TnEvcExtStatIndex_Object = MibTableColumn
tnEvcExtStatIndex = _TnEvcExtStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 2),
    _TnEvcExtStatIndex_Type()
)
tnEvcExtStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEvcExtStatIndex.setStatus("current")


class _TnEvcExtStatPort_Type(Integer32):
    """Custom type tnEvcExtStatPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnEvcExtStatPort_Type.__name__ = "Integer32"
_TnEvcExtStatPort_Object = MibTableColumn
tnEvcExtStatPort = _TnEvcExtStatPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 3),
    _TnEvcExtStatPort_Type()
)
tnEvcExtStatPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEvcExtStatPort.setStatus("current")
_TnEvcExtStatGreenFrameRx_Type = Counter64
_TnEvcExtStatGreenFrameRx_Object = MibTableColumn
tnEvcExtStatGreenFrameRx = _TnEvcExtStatGreenFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 4),
    _TnEvcExtStatGreenFrameRx_Type()
)
tnEvcExtStatGreenFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatGreenFrameRx.setStatus("current")
_TnEvcExtStatGreenFrameTx_Type = Counter64
_TnEvcExtStatGreenFrameTx_Object = MibTableColumn
tnEvcExtStatGreenFrameTx = _TnEvcExtStatGreenFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 5),
    _TnEvcExtStatGreenFrameTx_Type()
)
tnEvcExtStatGreenFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatGreenFrameTx.setStatus("current")
_TnEvcExtStatGreenBytesRx_Type = Counter64
_TnEvcExtStatGreenBytesRx_Object = MibTableColumn
tnEvcExtStatGreenBytesRx = _TnEvcExtStatGreenBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 6),
    _TnEvcExtStatGreenBytesRx_Type()
)
tnEvcExtStatGreenBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatGreenBytesRx.setStatus("current")
_TnEvcExtStatGreenBytesTx_Type = Counter64
_TnEvcExtStatGreenBytesTx_Object = MibTableColumn
tnEvcExtStatGreenBytesTx = _TnEvcExtStatGreenBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 7),
    _TnEvcExtStatGreenBytesTx_Type()
)
tnEvcExtStatGreenBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatGreenBytesTx.setStatus("current")
_TnEvcExtStatYellowFrameRx_Type = Counter64
_TnEvcExtStatYellowFrameRx_Object = MibTableColumn
tnEvcExtStatYellowFrameRx = _TnEvcExtStatYellowFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 8),
    _TnEvcExtStatYellowFrameRx_Type()
)
tnEvcExtStatYellowFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatYellowFrameRx.setStatus("current")
_TnEvcExtStatYellowFrameTx_Type = Counter64
_TnEvcExtStatYellowFrameTx_Object = MibTableColumn
tnEvcExtStatYellowFrameTx = _TnEvcExtStatYellowFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 9),
    _TnEvcExtStatYellowFrameTx_Type()
)
tnEvcExtStatYellowFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatYellowFrameTx.setStatus("current")
_TnEvcExtStatYellowBytesRx_Type = Counter64
_TnEvcExtStatYellowBytesRx_Object = MibTableColumn
tnEvcExtStatYellowBytesRx = _TnEvcExtStatYellowBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 10),
    _TnEvcExtStatYellowBytesRx_Type()
)
tnEvcExtStatYellowBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatYellowBytesRx.setStatus("current")
_TnEvcExtStatYellowBytesTx_Type = Counter64
_TnEvcExtStatYellowBytesTx_Object = MibTableColumn
tnEvcExtStatYellowBytesTx = _TnEvcExtStatYellowBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 11),
    _TnEvcExtStatYellowBytesTx_Type()
)
tnEvcExtStatYellowBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatYellowBytesTx.setStatus("current")
_TnEvcExtStatRedFrameRx_Type = Counter64
_TnEvcExtStatRedFrameRx_Object = MibTableColumn
tnEvcExtStatRedFrameRx = _TnEvcExtStatRedFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 12),
    _TnEvcExtStatRedFrameRx_Type()
)
tnEvcExtStatRedFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatRedFrameRx.setStatus("current")
_TnEvcExtStatRedBytesRx_Type = Counter64
_TnEvcExtStatRedBytesRx_Object = MibTableColumn
tnEvcExtStatRedBytesRx = _TnEvcExtStatRedBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 13),
    _TnEvcExtStatRedBytesRx_Type()
)
tnEvcExtStatRedBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatRedBytesRx.setStatus("current")
_TnEvcExtStatDiscardFrameRx_Type = Counter64
_TnEvcExtStatDiscardFrameRx_Object = MibTableColumn
tnEvcExtStatDiscardFrameRx = _TnEvcExtStatDiscardFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 14),
    _TnEvcExtStatDiscardFrameRx_Type()
)
tnEvcExtStatDiscardFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatDiscardFrameRx.setStatus("current")
_TnEvcExtStatDiscardFrameTx_Type = Counter64
_TnEvcExtStatDiscardFrameTx_Object = MibTableColumn
tnEvcExtStatDiscardFrameTx = _TnEvcExtStatDiscardFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 15),
    _TnEvcExtStatDiscardFrameTx_Type()
)
tnEvcExtStatDiscardFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatDiscardFrameTx.setStatus("current")
_TnEvcExtStatDiscardBytesRx_Type = Counter64
_TnEvcExtStatDiscardBytesRx_Object = MibTableColumn
tnEvcExtStatDiscardBytesRx = _TnEvcExtStatDiscardBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 16),
    _TnEvcExtStatDiscardBytesRx_Type()
)
tnEvcExtStatDiscardBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatDiscardBytesRx.setStatus("current")
_TnEvcExtStatDiscardBytesTx_Type = Counter64
_TnEvcExtStatDiscardBytesTx_Object = MibTableColumn
tnEvcExtStatDiscardBytesTx = _TnEvcExtStatDiscardBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 17),
    _TnEvcExtStatDiscardBytesTx_Type()
)
tnEvcExtStatDiscardBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEvcExtStatDiscardBytesTx.setStatus("current")
_TnEvcExtStatclear_Type = TruthValue
_TnEvcExtStatclear_Object = MibTableColumn
tnEvcExtStatclear = _TnEvcExtStatclear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 2, 2, 1, 18),
    _TnEvcExtStatclear_Type()
)
tnEvcExtStatclear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEvcExtStatclear.setStatus("current")
_TnEvcL2cpMgmtGroup_ObjectIdentity = ObjectIdentity
tnEvcL2cpMgmtGroup = _TnEvcL2cpMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3)
)
_TnEvcL2cpCfgTable_Object = MibTable
tnEvcL2cpCfgTable = _TnEvcL2cpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tnEvcL2cpCfgTable.setStatus("current")
_TnEvcL2cpCfgEntry_Object = MibTableRow
tnEvcL2cpCfgEntry = _TnEvcL2cpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1)
)
tnEvcL2cpCfgEntry.setIndexNames(
    (0, "TN-EVC-MIB", "tnEvcL2cpCfgInterfaceNumber"),
    (0, "TN-EVC-MIB", "tnEvcL2cpCfgIndex"),
)
if mibBuilder.loadTexts:
    tnEvcL2cpCfgEntry.setStatus("current")
_TnEvcL2cpCfgInterfaceNumber_Type = Unsigned32
_TnEvcL2cpCfgInterfaceNumber_Object = MibTableColumn
tnEvcL2cpCfgInterfaceNumber = _TnEvcL2cpCfgInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 1),
    _TnEvcL2cpCfgInterfaceNumber_Type()
)
tnEvcL2cpCfgInterfaceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgInterfaceNumber.setStatus("current")
_TnEvcL2cpCfgIndex_Type = Unsigned32
_TnEvcL2cpCfgIndex_Object = MibTableColumn
tnEvcL2cpCfgIndex = _TnEvcL2cpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 2),
    _TnEvcL2cpCfgIndex_Type()
)
tnEvcL2cpCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgIndex.setStatus("current")


class _TnEvcL2cpCfgType_Type(Integer32):
    """Custom type tnEvcL2cpCfgType based on Integer32"""
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
        *(("discard", 1),
          ("tunnel", 2),
          ("peer", 3),
          ("passToEvc", 4),
          ("peerToEvc", 5))
    )


_TnEvcL2cpCfgType_Type.__name__ = "Integer32"
_TnEvcL2cpCfgType_Object = MibTableColumn
tnEvcL2cpCfgType = _TnEvcL2cpCfgType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 3),
    _TnEvcL2cpCfgType_Type()
)
tnEvcL2cpCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgType.setStatus("current")


class _TnEvcL2cpCfgMatchScope_Type(Integer32):
    """Custom type tnEvcL2cpCfgMatchScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destinationAddressOnly", 1),
          ("daPlusProtocol", 2),
          ("daPlusProtocolPlusSubtype", 3))
    )


_TnEvcL2cpCfgMatchScope_Type.__name__ = "Integer32"
_TnEvcL2cpCfgMatchScope_Object = MibTableColumn
tnEvcL2cpCfgMatchScope = _TnEvcL2cpCfgMatchScope_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 4),
    _TnEvcL2cpCfgMatchScope_Type()
)
tnEvcL2cpCfgMatchScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgMatchScope.setStatus("current")
_TnEvcL2cpCfgMacAddress_Type = MacAddress
_TnEvcL2cpCfgMacAddress_Object = MibTableColumn
tnEvcL2cpCfgMacAddress = _TnEvcL2cpCfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 5),
    _TnEvcL2cpCfgMacAddress_Type()
)
tnEvcL2cpCfgMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgMacAddress.setStatus("current")
_TnEvcL2cpCfgProtocol_Type = Unsigned32
_TnEvcL2cpCfgProtocol_Object = MibTableColumn
tnEvcL2cpCfgProtocol = _TnEvcL2cpCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 6),
    _TnEvcL2cpCfgProtocol_Type()
)
tnEvcL2cpCfgProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgProtocol.setStatus("current")
_TnEvcL2cpCfgSubType_Type = Unsigned32
_TnEvcL2cpCfgSubType_Object = MibTableColumn
tnEvcL2cpCfgSubType = _TnEvcL2cpCfgSubType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 7),
    _TnEvcL2cpCfgSubType_Type()
)
tnEvcL2cpCfgSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgSubType.setStatus("current")


class _TnEvcL2cpCfgEvcName_Type(OctetString):
    """Custom type tnEvcL2cpCfgEvcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnEvcL2cpCfgEvcName_Type.__name__ = "OctetString"
_TnEvcL2cpCfgEvcName_Object = MibTableColumn
tnEvcL2cpCfgEvcName = _TnEvcL2cpCfgEvcName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 8),
    _TnEvcL2cpCfgEvcName_Type()
)
tnEvcL2cpCfgEvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgEvcName.setStatus("current")


class _TnEvcL2cpCfgValid_Type(Integer32):
    """Custom type tnEvcL2cpCfgValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_TnEvcL2cpCfgValid_Type.__name__ = "Integer32"
_TnEvcL2cpCfgValid_Object = MibTableColumn
tnEvcL2cpCfgValid = _TnEvcL2cpCfgValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 9),
    _TnEvcL2cpCfgValid_Type()
)
tnEvcL2cpCfgValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgValid.setStatus("current")
_TnEvcL2cpCfgRowStatus_Type = RowStatus
_TnEvcL2cpCfgRowStatus_Object = MibTableColumn
tnEvcL2cpCfgRowStatus = _TnEvcL2cpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 3, 3, 1, 10),
    _TnEvcL2cpCfgRowStatus_Type()
)
tnEvcL2cpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEvcL2cpCfgRowStatus.setStatus("current")
_TnEvcConformance_ObjectIdentity = ObjectIdentity
tnEvcConformance = _TnEvcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 8)
)
_TnEvcGroups_ObjectIdentity = ObjectIdentity
tnEvcGroups = _TnEvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 8, 1)
)
tnEvcEceEntry.registerAugmentions(
    ("TN-EVC-MIB",
     "tnEvcExtEceEntry")
)
tnEvcExtEceEntry.setIndexNames(*tnEvcEceEntry.getIndexNames())

# Managed Objects groups

tnEvcPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 8, 1, 1)
)
tnEvcPortConfigGroup.setObjects(
      *(("TN-EVC-MIB", "tnEvcPortDEIMode"),
        ("TN-EVC-MIB", "tnEvcPortTagMode"),
        ("TN-EVC-MIB", "tnEvcPortAddressMode"))
)
if mibBuilder.loadTexts:
    tnEvcPortConfigGroup.setStatus("current")

tnEvcJaguarPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 8, 1, 2)
)
tnEvcJaguarPortConfigGroup.setObjects(
    ("TN-EVC-MIB", "tnEvcPortDEIMode")
)
if mibBuilder.loadTexts:
    tnEvcJaguarPortConfigGroup.setStatus("current")

tnEvcTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 106, 1, 8, 1, 3)
)
tnEvcTableGroup.setObjects(
      *(("TN-EVC-MIB", "tnEvcNNIPortlist"),
        ("TN-EVC-MIB", "tnEvcVid"),
        ("TN-EVC-MIB", "tnEvcIVid"),
        ("TN-EVC-MIB", "tnEvcLearning"),
        ("TN-EVC-MIB", "tnEvcPolicerID"))
)
if mibBuilder.loadTexts:
    tnEvcTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-EVC-MIB",
    **{"tnEvcMib": tnEvcMib,
       "tnEvcObjects": tnEvcObjects,
       "tnEvcCfgMgmtGroup": tnEvcCfgMgmtGroup,
       "tnEvcPortTable": tnEvcPortTable,
       "tnEvcPortEntry": tnEvcPortEntry,
       "tnEvcPortDEIMode": tnEvcPortDEIMode,
       "tnEvcPortTagMode": tnEvcPortTagMode,
       "tnEvcPortAddressMode": tnEvcPortAddressMode,
       "tnEvcTable": tnEvcTable,
       "tnEvcEntry": tnEvcEntry,
       "tnEvcIndex": tnEvcIndex,
       "tnEvcNNIPortlist": tnEvcNNIPortlist,
       "tnEvcVid": tnEvcVid,
       "tnEvcIVid": tnEvcIVid,
       "tnEvcLearning": tnEvcLearning,
       "tnEvcInnerTagType": tnEvcInnerTagType,
       "tnEvcInnerVidMode": tnEvcInnerVidMode,
       "tnEvcInnerVid": tnEvcInnerVid,
       "tnEvcInnerPCPDEIPreservation": tnEvcInnerPCPDEIPreservation,
       "tnEvcInnerPCP": tnEvcInnerPCP,
       "tnEvcInnerDEI": tnEvcInnerDEI,
       "tnEvcOuterVid": tnEvcOuterVid,
       "tnEvcStatus": tnEvcStatus,
       "tnEvcPolicerID": tnEvcPolicerID,
       "tnEvcName": tnEvcName,
       "tnEvcEceTable": tnEvcEceTable,
       "tnEvcEceEntry": tnEvcEceEntry,
       "tnEvcEceId": tnEvcEceId,
       "tnEvcEceNextEceId": tnEvcEceNextEceId,
       "tnEvcEceUNIPortlist": tnEvcEceUNIPortlist,
       "tnEvcEceTagType": tnEvcEceTagType,
       "tnEvcEceTagVIDFilterType": tnEvcEceTagVIDFilterType,
       "tnEvcEceTagVIDFilterVal": tnEvcEceTagVIDFilterVal,
       "tnEvcEceTagVIDFilterStart": tnEvcEceTagVIDFilterStart,
       "tnEvcEceTagVIDFilterEnd": tnEvcEceTagVIDFilterEnd,
       "tnEvcEceTagPCP": tnEvcEceTagPCP,
       "tnEvcEceTagDEI": tnEvcEceTagDEI,
       "tnEvcEceTagFrameType": tnEvcEceTagFrameType,
       "tnEvcEceProtoType": tnEvcEceProtoType,
       "tnEvcEceProtoVal": tnEvcEceProtoVal,
       "tnEvcEceDscpFilterType": tnEvcEceDscpFilterType,
       "tnEvcEceDscpFilterVal": tnEvcEceDscpFilterVal,
       "tnEvcEceDscpRangeStart": tnEvcEceDscpRangeStart,
       "tnEvcEceDscpRangeEnd": tnEvcEceDscpRangeEnd,
       "tnEvcEceSrcPortFilterType": tnEvcEceSrcPortFilterType,
       "tnEvcEceSrcPortFilterNo": tnEvcEceSrcPortFilterNo,
       "tnEvcEceSrcPortRangeStart": tnEvcEceSrcPortRangeStart,
       "tnEvcEceSrcPortRangeEnd": tnEvcEceSrcPortRangeEnd,
       "tnEvcEceDstPortFilterType": tnEvcEceDstPortFilterType,
       "tnEvcEceDstPortFilterNo": tnEvcEceDstPortFilterNo,
       "tnEvcEceDstPortRangeStart": tnEvcEceDstPortRangeStart,
       "tnEvcEceDstPortRangeEnd": tnEvcEceDstPortRangeEnd,
       "tnEvcEceIpv4DipSipFilter": tnEvcEceIpv4DipSipFilter,
       "tnEvcEceIpv4DipSipAddr": tnEvcEceIpv4DipSipAddr,
       "tnEvcEceIpv4DipSipMask": tnEvcEceIpv4DipSipMask,
       "tnEvcEceIpv4Fragment": tnEvcEceIpv4Fragment,
       "tnEvcEceIpv6DipSipFilter": tnEvcEceIpv6DipSipFilter,
       "tnEvcEceIpv6DipSipAddr": tnEvcEceIpv6DipSipAddr,
       "tnEvcEceIpv6DipSipMask": tnEvcEceIpv6DipSipMask,
       "tnEvcEceOuterMode": tnEvcEceOuterMode,
       "tnEvcEceOuterPCPDEIPreserve": tnEvcEceOuterPCPDEIPreserve,
       "tnEvcEceOuterPCP": tnEvcEceOuterPCP,
       "tnEvcEceOuterDEI": tnEvcEceOuterDEI,
       "tnEvcEceActDirection": tnEvcEceActDirection,
       "tnEvcEceActEvcidFilterType": tnEvcEceActEvcidFilterType,
       "tnEvcEceActEvcidVal": tnEvcEceActEvcidVal,
       "tnEvcEceActTagPopCount": tnEvcEceActTagPopCount,
       "tnEvcEceActPolicyId": tnEvcEceActPolicyId,
       "tnEvcEceActClass": tnEvcEceActClass,
       "tnEvcEceDMacSMacFilterType": tnEvcEceDMacSMacFilterType,
       "tnEvcEceDMacSMacVal": tnEvcEceDMacSMacVal,
       "tnEvcEceDMacType": tnEvcEceDMacType,
       "tnEvcEceConflict": tnEvcEceConflict,
       "tnEvcEceStatus": tnEvcEceStatus,
       "tnEvcBandwidthProfilesTable": tnEvcBandwidthProfilesTable,
       "tnEvcBandwidthProfilesEntry": tnEvcBandwidthProfilesEntry,
       "tnEvcBandwidthProfilesIndex": tnEvcBandwidthProfilesIndex,
       "tnEvcBandwidthProfilesPolicerMode": tnEvcBandwidthProfilesPolicerMode,
       "tnEvcBandwidthProfilesCIR": tnEvcBandwidthProfilesCIR,
       "tnEvcBandwidthProfilesCBS": tnEvcBandwidthProfilesCBS,
       "tnEvcBandwidthProfilesEIR": tnEvcBandwidthProfilesEIR,
       "tnEvcBandwidthProfilesEBS": tnEvcBandwidthProfilesEBS,
       "tnEvcBandwidthProfilesState": tnEvcBandwidthProfilesState,
       "tnEvcExtEceTable": tnEvcExtEceTable,
       "tnEvcExtEceEntry": tnEvcExtEceEntry,
       "tnEvcEceInnerTagType": tnEvcEceInnerTagType,
       "tnEvcEceInnerTagVIDFilterType": tnEvcEceInnerTagVIDFilterType,
       "tnEvcEceInnerTagVIDFilterVal": tnEvcEceInnerTagVIDFilterVal,
       "tnEvcEceInnerTagVIDFilterStart": tnEvcEceInnerTagVIDFilterStart,
       "tnEvcEceInnerTagVIDFilterEnd": tnEvcEceInnerTagVIDFilterEnd,
       "tnEvcEceInnerTagPCP": tnEvcEceInnerTagPCP,
       "tnEvcEceInnerTagDEI": tnEvcEceInnerTagDEI,
       "tnEvcEcePolicer": tnEvcEcePolicer,
       "tnEvcEceOuterVid": tnEvcEceOuterVid,
       "tnEvcEceNNIInnerTagType": tnEvcEceNNIInnerTagType,
       "tnEvcEceInnerVid": tnEvcEceInnerVid,
       "tnEvcEceInnerPCPDEIPreserve": tnEvcEceInnerPCPDEIPreserve,
       "tnEvcEceInnerPCP": tnEvcEceInnerPCP,
       "tnEvcEceInnerDEI": tnEvcEceInnerDEI,
       "tnEvcEceDMacVal": tnEvcEceDMacVal,
       "tnEvcEceOuterPCPMode": tnEvcEceOuterPCPMode,
       "tnEvcEceOuterDEIMode": tnEvcEceOuterDEIMode,
       "tnEvcEceActRuleType": tnEvcEceActRuleType,
       "tnEvcEceActTxLookupType": tnEvcEceActTxLookupType,
       "tnEvcEceActDropPrecType": tnEvcEceActDropPrecType,
       "tnEvcEceInnerPcpMode": tnEvcEceInnerPcpMode,
       "tnEvcEceIInnerDeiMode": tnEvcEceIInnerDeiMode,
       "tnEvcEceIpv4DipFilter": tnEvcEceIpv4DipFilter,
       "tnEvcEceIpv4DipAddr": tnEvcEceIpv4DipAddr,
       "tnEvcEceIpv4DipMask": tnEvcEceIpv4DipMask,
       "tnEvcEceIpv6DipFilter": tnEvcEceIpv6DipFilter,
       "tnEvcEceIpv6DipAddr": tnEvcEceIpv6DipAddr,
       "tnEvcEceIpv6DipMask": tnEvcEceIpv6DipMask,
       "tnEvcEceLookup": tnEvcEceLookup,
       "tnEvcEceEtypeFilter": tnEvcEceEtypeFilter,
       "tnEvcEceEtypeValue": tnEvcEceEtypeValue,
       "tnEvcEceEtypeDataFilter": tnEvcEceEtypeDataFilter,
       "tnEvcEceEtypeData": tnEvcEceEtypeData,
       "tnEvcEceEtypeDataMask": tnEvcEceEtypeDataMask,
       "tnEvcEceLlcDSAPFilter": tnEvcEceLlcDSAPFilter,
       "tnEvcEceLlcDSAPValue": tnEvcEceLlcDSAPValue,
       "tnEvcEceLlcSSAPFilter": tnEvcEceLlcSSAPFilter,
       "tnEvcEceLlcSSAPValue": tnEvcEceLlcSSAPValue,
       "tnEvcEceLlcCtrlFilter": tnEvcEceLlcCtrlFilter,
       "tnEvcEceLlcCtrlValue": tnEvcEceLlcCtrlValue,
       "tnEvcEceLlcDataFilter": tnEvcEceLlcDataFilter,
       "tnEvcEceLlcDataValue": tnEvcEceLlcDataValue,
       "tnEvcEceLlcDataMask": tnEvcEceLlcDataMask,
       "tnEvcEceSnapOuiFilter": tnEvcEceSnapOuiFilter,
       "tnEvcEceSnapOuiValue": tnEvcEceSnapOuiValue,
       "tnEvcEceSnapPidFilter": tnEvcEceSnapPidFilter,
       "tnEvcEceSnapPidValue": tnEvcEceSnapPidValue,
       "tnEvcEceL2cpProtoType": tnEvcEceL2cpProtoType,
       "tnEvcStatGroup": tnEvcStatGroup,
       "tnEvcStatTable": tnEvcStatTable,
       "tnEvcStatEntry": tnEvcStatEntry,
       "tnEvcStatClass": tnEvcStatClass,
       "tnEvcStatGreenFrameRx": tnEvcStatGreenFrameRx,
       "tnEvcStatGreenFrameTx": tnEvcStatGreenFrameTx,
       "tnEvcStatYellowFrameRx": tnEvcStatYellowFrameRx,
       "tnEvcStatYellowFrameTx": tnEvcStatYellowFrameTx,
       "tnEvcStatRedFrameRx": tnEvcStatRedFrameRx,
       "tnEvcStatDiscardGreenFrame": tnEvcStatDiscardGreenFrame,
       "tnEvcStatDiscardYellowFrame": tnEvcStatDiscardYellowFrame,
       "tnEvcStatClear": tnEvcStatClear,
       "tnEvcExtStatTable": tnEvcExtStatTable,
       "tnEvcExtStatEntry": tnEvcExtStatEntry,
       "tnEvcExtStatType": tnEvcExtStatType,
       "tnEvcExtStatIndex": tnEvcExtStatIndex,
       "tnEvcExtStatPort": tnEvcExtStatPort,
       "tnEvcExtStatGreenFrameRx": tnEvcExtStatGreenFrameRx,
       "tnEvcExtStatGreenFrameTx": tnEvcExtStatGreenFrameTx,
       "tnEvcExtStatGreenBytesRx": tnEvcExtStatGreenBytesRx,
       "tnEvcExtStatGreenBytesTx": tnEvcExtStatGreenBytesTx,
       "tnEvcExtStatYellowFrameRx": tnEvcExtStatYellowFrameRx,
       "tnEvcExtStatYellowFrameTx": tnEvcExtStatYellowFrameTx,
       "tnEvcExtStatYellowBytesRx": tnEvcExtStatYellowBytesRx,
       "tnEvcExtStatYellowBytesTx": tnEvcExtStatYellowBytesTx,
       "tnEvcExtStatRedFrameRx": tnEvcExtStatRedFrameRx,
       "tnEvcExtStatRedBytesRx": tnEvcExtStatRedBytesRx,
       "tnEvcExtStatDiscardFrameRx": tnEvcExtStatDiscardFrameRx,
       "tnEvcExtStatDiscardFrameTx": tnEvcExtStatDiscardFrameTx,
       "tnEvcExtStatDiscardBytesRx": tnEvcExtStatDiscardBytesRx,
       "tnEvcExtStatDiscardBytesTx": tnEvcExtStatDiscardBytesTx,
       "tnEvcExtStatclear": tnEvcExtStatclear,
       "tnEvcL2cpMgmtGroup": tnEvcL2cpMgmtGroup,
       "tnEvcL2cpCfgTable": tnEvcL2cpCfgTable,
       "tnEvcL2cpCfgEntry": tnEvcL2cpCfgEntry,
       "tnEvcL2cpCfgInterfaceNumber": tnEvcL2cpCfgInterfaceNumber,
       "tnEvcL2cpCfgIndex": tnEvcL2cpCfgIndex,
       "tnEvcL2cpCfgType": tnEvcL2cpCfgType,
       "tnEvcL2cpCfgMatchScope": tnEvcL2cpCfgMatchScope,
       "tnEvcL2cpCfgMacAddress": tnEvcL2cpCfgMacAddress,
       "tnEvcL2cpCfgProtocol": tnEvcL2cpCfgProtocol,
       "tnEvcL2cpCfgSubType": tnEvcL2cpCfgSubType,
       "tnEvcL2cpCfgEvcName": tnEvcL2cpCfgEvcName,
       "tnEvcL2cpCfgValid": tnEvcL2cpCfgValid,
       "tnEvcL2cpCfgRowStatus": tnEvcL2cpCfgRowStatus,
       "tnEvcConformance": tnEvcConformance,
       "tnEvcGroups": tnEvcGroups,
       "tnEvcPortConfigGroup": tnEvcPortConfigGroup,
       "tnEvcJaguarPortConfigGroup": tnEvcJaguarPortConfigGroup,
       "tnEvcTableGroup": tnEvcTableGroup}
)
