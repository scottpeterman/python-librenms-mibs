# SNMP MIB module (MPLS-LSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\MPLS-LSR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:34 2025
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsLsrMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 96)
)
if mibBuilder.loadTexts:
    mplsLsrMIB.setRevisions(
        ("1999-06-16 12:00",
         "2000-02-16 12:00",
         "2000-03-06 12:00",
         "2000-04-21 12:00",
         "2000-04-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsLSPID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class MplsLabel(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class MplsBitRate(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class MplsBurstSize(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class MplsBufferSize(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class MplsObjectOwner(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("snmp", 2),
          ("ldp", 3),
          ("rsvp", 4),
          ("policyAgent", 5),
          ("unknown", 6))
    )



# MIB Managed Objects in the order of their OIDs

_MplsLsrObjects_ObjectIdentity = ObjectIdentity
mplsLsrObjects = _MplsLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 96, 1)
)
_MplsInterfaceConfTable_Object = MibTable
mplsInterfaceConfTable = _MplsInterfaceConfTable_Object(
    (1, 3, 6, 1, 3, 96, 1, 1)
)
if mibBuilder.loadTexts:
    mplsInterfaceConfTable.setStatus("current")
_MplsInterfaceConfEntry_Object = MibTableRow
mplsInterfaceConfEntry = _MplsInterfaceConfEntry_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1)
)
mplsInterfaceConfEntry.setIndexNames(
    (0, "MPLS-LSR-MIB", "mplsInterfaceConfIndex"),
)
if mibBuilder.loadTexts:
    mplsInterfaceConfEntry.setStatus("current")
_MplsInterfaceConfIndex_Type = InterfaceIndexOrZero
_MplsInterfaceConfIndex_Object = MibTableColumn
mplsInterfaceConfIndex = _MplsInterfaceConfIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 1),
    _MplsInterfaceConfIndex_Type()
)
mplsInterfaceConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInterfaceConfIndex.setStatus("current")
_MplsInterfaceLabelMinIn_Type = MplsLabel
_MplsInterfaceLabelMinIn_Object = MibTableColumn
mplsInterfaceLabelMinIn = _MplsInterfaceLabelMinIn_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 2),
    _MplsInterfaceLabelMinIn_Type()
)
mplsInterfaceLabelMinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMinIn.setStatus("current")
_MplsInterfaceLabelMaxIn_Type = MplsLabel
_MplsInterfaceLabelMaxIn_Object = MibTableColumn
mplsInterfaceLabelMaxIn = _MplsInterfaceLabelMaxIn_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 3),
    _MplsInterfaceLabelMaxIn_Type()
)
mplsInterfaceLabelMaxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMaxIn.setStatus("current")
_MplsInterfaceLabelMinOut_Type = MplsLabel
_MplsInterfaceLabelMinOut_Object = MibTableColumn
mplsInterfaceLabelMinOut = _MplsInterfaceLabelMinOut_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 4),
    _MplsInterfaceLabelMinOut_Type()
)
mplsInterfaceLabelMinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMinOut.setStatus("current")
_MplsInterfaceLabelMaxOut_Type = MplsLabel
_MplsInterfaceLabelMaxOut_Object = MibTableColumn
mplsInterfaceLabelMaxOut = _MplsInterfaceLabelMaxOut_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 5),
    _MplsInterfaceLabelMaxOut_Type()
)
mplsInterfaceLabelMaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMaxOut.setStatus("current")
_MplsInterfaceTotalBandwidth_Type = MplsBitRate
_MplsInterfaceTotalBandwidth_Object = MibTableColumn
mplsInterfaceTotalBandwidth = _MplsInterfaceTotalBandwidth_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 6),
    _MplsInterfaceTotalBandwidth_Type()
)
mplsInterfaceTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceTotalBandwidth.setStatus("current")
_MplsInterfaceAvailableBandwidth_Type = MplsBitRate
_MplsInterfaceAvailableBandwidth_Object = MibTableColumn
mplsInterfaceAvailableBandwidth = _MplsInterfaceAvailableBandwidth_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 7),
    _MplsInterfaceAvailableBandwidth_Type()
)
mplsInterfaceAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceAvailableBandwidth.setStatus("current")
_MplsInterfaceTotalBuffer_Type = MplsBufferSize
_MplsInterfaceTotalBuffer_Object = MibTableColumn
mplsInterfaceTotalBuffer = _MplsInterfaceTotalBuffer_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 8),
    _MplsInterfaceTotalBuffer_Type()
)
mplsInterfaceTotalBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceTotalBuffer.setStatus("current")
_MplsInterfaceAvailableBuffer_Type = MplsBufferSize
_MplsInterfaceAvailableBuffer_Object = MibTableColumn
mplsInterfaceAvailableBuffer = _MplsInterfaceAvailableBuffer_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 9),
    _MplsInterfaceAvailableBuffer_Type()
)
mplsInterfaceAvailableBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceAvailableBuffer.setStatus("current")


class _MplsInterfaceLabelParticipationType_Type(Bits):
    """Custom type mplsInterfaceLabelParticipationType based on Bits"""
    namedValues = NamedValues(
        *(("perPlatform", 0),
          ("perInterface", 1))
    )

_MplsInterfaceLabelParticipationType_Type.__name__ = "Bits"
_MplsInterfaceLabelParticipationType_Object = MibTableColumn
mplsInterfaceLabelParticipationType = _MplsInterfaceLabelParticipationType_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 10),
    _MplsInterfaceLabelParticipationType_Type()
)
mplsInterfaceLabelParticipationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelParticipationType.setStatus("current")
_MplsInterfaceConfStorageType_Type = StorageType
_MplsInterfaceConfStorageType_Object = MibTableColumn
mplsInterfaceConfStorageType = _MplsInterfaceConfStorageType_Object(
    (1, 3, 6, 1, 3, 96, 1, 1, 1, 11),
    _MplsInterfaceConfStorageType_Type()
)
mplsInterfaceConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInterfaceConfStorageType.setStatus("current")
_MplsInterfacePerfTable_Object = MibTable
mplsInterfacePerfTable = _MplsInterfacePerfTable_Object(
    (1, 3, 6, 1, 3, 96, 1, 2)
)
if mibBuilder.loadTexts:
    mplsInterfacePerfTable.setStatus("current")
_MplsInterfacePerfEntry_Object = MibTableRow
mplsInterfacePerfEntry = _MplsInterfacePerfEntry_Object(
    (1, 3, 6, 1, 3, 96, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsInterfacePerfEntry.setStatus("current")
_MplsInterfaceInLabelsUsed_Type = Gauge32
_MplsInterfaceInLabelsUsed_Object = MibTableColumn
mplsInterfaceInLabelsUsed = _MplsInterfaceInLabelsUsed_Object(
    (1, 3, 6, 1, 3, 96, 1, 2, 1, 1),
    _MplsInterfaceInLabelsUsed_Type()
)
mplsInterfaceInLabelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceInLabelsUsed.setStatus("current")
_MplsInterfaceInPackets_Type = Counter32
_MplsInterfaceInPackets_Object = MibTableColumn
mplsInterfaceInPackets = _MplsInterfaceInPackets_Object(
    (1, 3, 6, 1, 3, 96, 1, 2, 1, 2),
    _MplsInterfaceInPackets_Type()
)
mplsInterfaceInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceInPackets.setStatus("current")
_MplsInterfaceInDiscards_Type = Counter32
_MplsInterfaceInDiscards_Object = MibTableColumn
mplsInterfaceInDiscards = _MplsInterfaceInDiscards_Object(
    (1, 3, 6, 1, 3, 96, 1, 2, 1, 3),
    _MplsInterfaceInDiscards_Type()
)
mplsInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceInDiscards.setStatus("current")
_MplsInterfaceFailedLabelLookup_Type = Counter32
_MplsInterfaceFailedLabelLookup_Object = MibTableColumn
mplsInterfaceFailedLabelLookup = _MplsInterfaceFailedLabelLookup_Object(
    (1, 3, 6, 1, 3, 96, 1, 2, 1, 4),
    _MplsInterfaceFailedLabelLookup_Type()
)
mplsInterfaceFailedLabelLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceFailedLabelLookup.setStatus("current")
_MplsInterfaceOutLabelsUsed_Type = Gauge32
_MplsInterfaceOutLabelsUsed_Object = MibTableColumn
mplsInterfaceOutLabelsUsed = _MplsInterfaceOutLabelsUsed_Object(
    (1, 3, 6, 1, 3, 96, 1, 2, 1, 5),
    _MplsInterfaceOutLabelsUsed_Type()
)
mplsInterfaceOutLabelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceOutLabelsUsed.setStatus("current")
_MplsInterfaceOutPackets_Type = Counter32
_MplsInterfaceOutPackets_Object = MibTableColumn
mplsInterfaceOutPackets = _MplsInterfaceOutPackets_Object(
    (1, 3, 6, 1, 3, 96, 1, 2, 1, 6),
    _MplsInterfaceOutPackets_Type()
)
mplsInterfaceOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceOutPackets.setStatus("current")
_MplsInterfaceOutDiscards_Type = Counter32
_MplsInterfaceOutDiscards_Object = MibTableColumn
mplsInterfaceOutDiscards = _MplsInterfaceOutDiscards_Object(
    (1, 3, 6, 1, 3, 96, 1, 2, 1, 7),
    _MplsInterfaceOutDiscards_Type()
)
mplsInterfaceOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceOutDiscards.setStatus("current")
_MplsInterfaceOutFragments_Type = Counter32
_MplsInterfaceOutFragments_Object = MibTableColumn
mplsInterfaceOutFragments = _MplsInterfaceOutFragments_Object(
    (1, 3, 6, 1, 3, 96, 1, 2, 1, 8),
    _MplsInterfaceOutFragments_Type()
)
mplsInterfaceOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceOutFragments.setStatus("current")
_MplsInSegmentTable_Object = MibTable
mplsInSegmentTable = _MplsInSegmentTable_Object(
    (1, 3, 6, 1, 3, 96, 1, 3)
)
if mibBuilder.loadTexts:
    mplsInSegmentTable.setStatus("current")
_MplsInSegmentEntry_Object = MibTableRow
mplsInSegmentEntry = _MplsInSegmentEntry_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1)
)
mplsInSegmentEntry.setIndexNames(
    (0, "MPLS-LSR-MIB", "mplsInSegmentIfIndex"),
    (0, "MPLS-LSR-MIB", "mplsInSegmentLabel"),
)
if mibBuilder.loadTexts:
    mplsInSegmentEntry.setStatus("current")
_MplsInSegmentIfIndex_Type = InterfaceIndexOrZero
_MplsInSegmentIfIndex_Object = MibTableColumn
mplsInSegmentIfIndex = _MplsInSegmentIfIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 1),
    _MplsInSegmentIfIndex_Type()
)
mplsInSegmentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentIfIndex.setStatus("current")
_MplsInSegmentLabel_Type = MplsLabel
_MplsInSegmentLabel_Object = MibTableColumn
mplsInSegmentLabel = _MplsInSegmentLabel_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 2),
    _MplsInSegmentLabel_Type()
)
mplsInSegmentLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentLabel.setStatus("current")


class _MplsInSegmentNPop_Type(Integer32):
    """Custom type mplsInSegmentNPop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsInSegmentNPop_Type.__name__ = "Integer32"
_MplsInSegmentNPop_Object = MibTableColumn
mplsInSegmentNPop = _MplsInSegmentNPop_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 3),
    _MplsInSegmentNPop_Type()
)
mplsInSegmentNPop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentNPop.setStatus("current")


class _MplsInSegmentAddrFamily_Type(AddressFamilyNumbers):
    """Custom type mplsInSegmentAddrFamily based on AddressFamilyNumbers"""
    defaultValue = 0


_MplsInSegmentAddrFamily_Type.__name__ = "AddressFamilyNumbers"
_MplsInSegmentAddrFamily_Object = MibTableColumn
mplsInSegmentAddrFamily = _MplsInSegmentAddrFamily_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 4),
    _MplsInSegmentAddrFamily_Type()
)
mplsInSegmentAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentAddrFamily.setStatus("current")


class _MplsInSegmentXCIndex_Type(Integer32):
    """Custom type mplsInSegmentXCIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsInSegmentXCIndex_Type.__name__ = "Integer32"
_MplsInSegmentXCIndex_Object = MibTableColumn
mplsInSegmentXCIndex = _MplsInSegmentXCIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 5),
    _MplsInSegmentXCIndex_Type()
)
mplsInSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentXCIndex.setStatus("current")


class _MplsInSegmentOwner_Type(MplsObjectOwner):
    """Custom type mplsInSegmentOwner based on MplsObjectOwner"""
    defaultValue = 6


_MplsInSegmentOwner_Type.__name__ = "MplsObjectOwner"
_MplsInSegmentOwner_Object = MibTableColumn
mplsInSegmentOwner = _MplsInSegmentOwner_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 6),
    _MplsInSegmentOwner_Type()
)
mplsInSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentOwner.setStatus("current")
_MplsInSegmentTrafficParamPtr_Type = RowPointer
_MplsInSegmentTrafficParamPtr_Object = MibTableColumn
mplsInSegmentTrafficParamPtr = _MplsInSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 7),
    _MplsInSegmentTrafficParamPtr_Type()
)
mplsInSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentTrafficParamPtr.setStatus("current")
_MplsInSegmentRowStatus_Type = RowStatus
_MplsInSegmentRowStatus_Object = MibTableColumn
mplsInSegmentRowStatus = _MplsInSegmentRowStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 8),
    _MplsInSegmentRowStatus_Type()
)
mplsInSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentRowStatus.setStatus("current")
_MplsInSegmentStorageType_Type = StorageType
_MplsInSegmentStorageType_Object = MibTableColumn
mplsInSegmentStorageType = _MplsInSegmentStorageType_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 9),
    _MplsInSegmentStorageType_Type()
)
mplsInSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentStorageType.setStatus("current")


class _MplsInSegmentAdminStatus_Type(Integer32):
    """Custom type mplsInSegmentAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_MplsInSegmentAdminStatus_Type.__name__ = "Integer32"
_MplsInSegmentAdminStatus_Object = MibTableColumn
mplsInSegmentAdminStatus = _MplsInSegmentAdminStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 10),
    _MplsInSegmentAdminStatus_Type()
)
mplsInSegmentAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentAdminStatus.setStatus("current")


class _MplsInSegmentOperStatus_Type(Integer32):
    """Custom type mplsInSegmentOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_MplsInSegmentOperStatus_Type.__name__ = "Integer32"
_MplsInSegmentOperStatus_Object = MibTableColumn
mplsInSegmentOperStatus = _MplsInSegmentOperStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 3, 1, 11),
    _MplsInSegmentOperStatus_Type()
)
mplsInSegmentOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentOperStatus.setStatus("current")
_MplsInSegmentPerfTable_Object = MibTable
mplsInSegmentPerfTable = _MplsInSegmentPerfTable_Object(
    (1, 3, 6, 1, 3, 96, 1, 4)
)
if mibBuilder.loadTexts:
    mplsInSegmentPerfTable.setStatus("current")
_MplsInSegmentPerfEntry_Object = MibTableRow
mplsInSegmentPerfEntry = _MplsInSegmentPerfEntry_Object(
    (1, 3, 6, 1, 3, 96, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mplsInSegmentPerfEntry.setStatus("current")
_MplsInSegmentOctets_Type = Counter32
_MplsInSegmentOctets_Object = MibTableColumn
mplsInSegmentOctets = _MplsInSegmentOctets_Object(
    (1, 3, 6, 1, 3, 96, 1, 4, 1, 1),
    _MplsInSegmentOctets_Type()
)
mplsInSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentOctets.setStatus("current")
_MplsInSegmentPackets_Type = Counter32
_MplsInSegmentPackets_Object = MibTableColumn
mplsInSegmentPackets = _MplsInSegmentPackets_Object(
    (1, 3, 6, 1, 3, 96, 1, 4, 1, 2),
    _MplsInSegmentPackets_Type()
)
mplsInSegmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPackets.setStatus("current")
_MplsInSegmentErrors_Type = Counter32
_MplsInSegmentErrors_Object = MibTableColumn
mplsInSegmentErrors = _MplsInSegmentErrors_Object(
    (1, 3, 6, 1, 3, 96, 1, 4, 1, 3),
    _MplsInSegmentErrors_Type()
)
mplsInSegmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentErrors.setStatus("current")
_MplsInSegmentDiscards_Type = Counter32
_MplsInSegmentDiscards_Object = MibTableColumn
mplsInSegmentDiscards = _MplsInSegmentDiscards_Object(
    (1, 3, 6, 1, 3, 96, 1, 4, 1, 4),
    _MplsInSegmentDiscards_Type()
)
mplsInSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentDiscards.setStatus("current")
_MplsInSegmentHCOctets_Type = Counter64
_MplsInSegmentHCOctets_Object = MibTableColumn
mplsInSegmentHCOctets = _MplsInSegmentHCOctets_Object(
    (1, 3, 6, 1, 3, 96, 1, 4, 1, 5),
    _MplsInSegmentHCOctets_Type()
)
mplsInSegmentHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentHCOctets.setStatus("current")
_MplsInSegmentPerfDiscontinuityTime_Type = TimeStamp
_MplsInSegmentPerfDiscontinuityTime_Object = MibTableColumn
mplsInSegmentPerfDiscontinuityTime = _MplsInSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 3, 96, 1, 4, 1, 6),
    _MplsInSegmentPerfDiscontinuityTime_Type()
)
mplsInSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPerfDiscontinuityTime.setStatus("current")


class _MplsOutSegmentIndexNext_Type(Integer32):
    """Custom type mplsOutSegmentIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsOutSegmentIndexNext_Type.__name__ = "Integer32"
_MplsOutSegmentIndexNext_Object = MibScalar
mplsOutSegmentIndexNext = _MplsOutSegmentIndexNext_Object(
    (1, 3, 6, 1, 3, 96, 1, 5),
    _MplsOutSegmentIndexNext_Type()
)
mplsOutSegmentIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentIndexNext.setStatus("current")
_MplsOutSegmentTable_Object = MibTable
mplsOutSegmentTable = _MplsOutSegmentTable_Object(
    (1, 3, 6, 1, 3, 96, 1, 6)
)
if mibBuilder.loadTexts:
    mplsOutSegmentTable.setStatus("current")
_MplsOutSegmentEntry_Object = MibTableRow
mplsOutSegmentEntry = _MplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1)
)
mplsOutSegmentEntry.setIndexNames(
    (0, "MPLS-LSR-MIB", "mplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    mplsOutSegmentEntry.setStatus("current")


class _MplsOutSegmentIndex_Type(Integer32):
    """Custom type mplsOutSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsOutSegmentIndex_Type.__name__ = "Integer32"
_MplsOutSegmentIndex_Object = MibTableColumn
mplsOutSegmentIndex = _MplsOutSegmentIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 1),
    _MplsOutSegmentIndex_Type()
)
mplsOutSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsOutSegmentIndex.setStatus("current")
_MplsOutSegmentIfIndex_Type = InterfaceIndex
_MplsOutSegmentIfIndex_Object = MibTableColumn
mplsOutSegmentIfIndex = _MplsOutSegmentIfIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 2),
    _MplsOutSegmentIfIndex_Type()
)
mplsOutSegmentIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentIfIndex.setStatus("current")
_MplsOutSegmentPushTopLabel_Type = TruthValue
_MplsOutSegmentPushTopLabel_Object = MibTableColumn
mplsOutSegmentPushTopLabel = _MplsOutSegmentPushTopLabel_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 3),
    _MplsOutSegmentPushTopLabel_Type()
)
mplsOutSegmentPushTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentPushTopLabel.setStatus("current")
_MplsOutSegmentTopLabel_Type = MplsLabel
_MplsOutSegmentTopLabel_Object = MibTableColumn
mplsOutSegmentTopLabel = _MplsOutSegmentTopLabel_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 4),
    _MplsOutSegmentTopLabel_Type()
)
mplsOutSegmentTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentTopLabel.setStatus("current")


class _MplsOutSegmentNextHopIpAddrType_Type(InetAddressType):
    """Custom type mplsOutSegmentNextHopIpAddrType based on InetAddressType"""
    defaultValue = 0


_MplsOutSegmentNextHopIpAddrType_Type.__name__ = "InetAddressType"
_MplsOutSegmentNextHopIpAddrType_Object = MibTableColumn
mplsOutSegmentNextHopIpAddrType = _MplsOutSegmentNextHopIpAddrType_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 5),
    _MplsOutSegmentNextHopIpAddrType_Type()
)
mplsOutSegmentNextHopIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentNextHopIpAddrType.setStatus("current")
_MplsOutSegmentNextHopIpv4Addr_Type = InetAddressIPv4
_MplsOutSegmentNextHopIpv4Addr_Object = MibTableColumn
mplsOutSegmentNextHopIpv4Addr = _MplsOutSegmentNextHopIpv4Addr_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 6),
    _MplsOutSegmentNextHopIpv4Addr_Type()
)
mplsOutSegmentNextHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentNextHopIpv4Addr.setStatus("current")
_MplsOutSegmentNextHopIpv6Addr_Type = InetAddressIPv6
_MplsOutSegmentNextHopIpv6Addr_Object = MibTableColumn
mplsOutSegmentNextHopIpv6Addr = _MplsOutSegmentNextHopIpv6Addr_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 7),
    _MplsOutSegmentNextHopIpv6Addr_Type()
)
mplsOutSegmentNextHopIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentNextHopIpv6Addr.setStatus("current")


class _MplsOutSegmentXCIndex_Type(Integer32):
    """Custom type mplsOutSegmentXCIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsOutSegmentXCIndex_Type.__name__ = "Integer32"
_MplsOutSegmentXCIndex_Object = MibTableColumn
mplsOutSegmentXCIndex = _MplsOutSegmentXCIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 8),
    _MplsOutSegmentXCIndex_Type()
)
mplsOutSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentXCIndex.setStatus("current")


class _MplsOutSegmentOwner_Type(MplsObjectOwner):
    """Custom type mplsOutSegmentOwner based on MplsObjectOwner"""
    defaultValue = 6


_MplsOutSegmentOwner_Type.__name__ = "MplsObjectOwner"
_MplsOutSegmentOwner_Object = MibTableColumn
mplsOutSegmentOwner = _MplsOutSegmentOwner_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 9),
    _MplsOutSegmentOwner_Type()
)
mplsOutSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentOwner.setStatus("current")
_MplsOutSegmentTrafficParamPtr_Type = RowPointer
_MplsOutSegmentTrafficParamPtr_Object = MibTableColumn
mplsOutSegmentTrafficParamPtr = _MplsOutSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 10),
    _MplsOutSegmentTrafficParamPtr_Type()
)
mplsOutSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentTrafficParamPtr.setStatus("current")
_MplsOutSegmentRowStatus_Type = RowStatus
_MplsOutSegmentRowStatus_Object = MibTableColumn
mplsOutSegmentRowStatus = _MplsOutSegmentRowStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 11),
    _MplsOutSegmentRowStatus_Type()
)
mplsOutSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentRowStatus.setStatus("current")
_MplsOutSegmentStorageType_Type = StorageType
_MplsOutSegmentStorageType_Object = MibTableColumn
mplsOutSegmentStorageType = _MplsOutSegmentStorageType_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 12),
    _MplsOutSegmentStorageType_Type()
)
mplsOutSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentStorageType.setStatus("current")


class _MplsOutSegmentAdminStatus_Type(Integer32):
    """Custom type mplsOutSegmentAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_MplsOutSegmentAdminStatus_Type.__name__ = "Integer32"
_MplsOutSegmentAdminStatus_Object = MibTableColumn
mplsOutSegmentAdminStatus = _MplsOutSegmentAdminStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 13),
    _MplsOutSegmentAdminStatus_Type()
)
mplsOutSegmentAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentAdminStatus.setStatus("current")


class _MplsOutSegmentOperStatus_Type(Integer32):
    """Custom type mplsOutSegmentOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_MplsOutSegmentOperStatus_Type.__name__ = "Integer32"
_MplsOutSegmentOperStatus_Object = MibTableColumn
mplsOutSegmentOperStatus = _MplsOutSegmentOperStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 6, 1, 14),
    _MplsOutSegmentOperStatus_Type()
)
mplsOutSegmentOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentOperStatus.setStatus("current")
_MplsOutSegmentPerfTable_Object = MibTable
mplsOutSegmentPerfTable = _MplsOutSegmentPerfTable_Object(
    (1, 3, 6, 1, 3, 96, 1, 7)
)
if mibBuilder.loadTexts:
    mplsOutSegmentPerfTable.setStatus("current")
_MplsOutSegmentPerfEntry_Object = MibTableRow
mplsOutSegmentPerfEntry = _MplsOutSegmentPerfEntry_Object(
    (1, 3, 6, 1, 3, 96, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mplsOutSegmentPerfEntry.setStatus("current")
_MplsOutSegmentOctets_Type = Counter32
_MplsOutSegmentOctets_Object = MibTableColumn
mplsOutSegmentOctets = _MplsOutSegmentOctets_Object(
    (1, 3, 6, 1, 3, 96, 1, 7, 1, 1),
    _MplsOutSegmentOctets_Type()
)
mplsOutSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentOctets.setStatus("current")
_MplsOutSegmentPackets_Type = Counter32
_MplsOutSegmentPackets_Object = MibTableColumn
mplsOutSegmentPackets = _MplsOutSegmentPackets_Object(
    (1, 3, 6, 1, 3, 96, 1, 7, 1, 2),
    _MplsOutSegmentPackets_Type()
)
mplsOutSegmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPackets.setStatus("current")
_MplsOutSegmentErrors_Type = Counter32
_MplsOutSegmentErrors_Object = MibTableColumn
mplsOutSegmentErrors = _MplsOutSegmentErrors_Object(
    (1, 3, 6, 1, 3, 96, 1, 7, 1, 3),
    _MplsOutSegmentErrors_Type()
)
mplsOutSegmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentErrors.setStatus("current")
_MplsOutSegmentDiscards_Type = Counter32
_MplsOutSegmentDiscards_Object = MibTableColumn
mplsOutSegmentDiscards = _MplsOutSegmentDiscards_Object(
    (1, 3, 6, 1, 3, 96, 1, 7, 1, 4),
    _MplsOutSegmentDiscards_Type()
)
mplsOutSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentDiscards.setStatus("current")
_MplsOutSegmentHCOctets_Type = Counter64
_MplsOutSegmentHCOctets_Object = MibTableColumn
mplsOutSegmentHCOctets = _MplsOutSegmentHCOctets_Object(
    (1, 3, 6, 1, 3, 96, 1, 7, 1, 5),
    _MplsOutSegmentHCOctets_Type()
)
mplsOutSegmentHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentHCOctets.setStatus("current")
_MplsOutSegmentPerfDiscontinuityTime_Type = TimeStamp
_MplsOutSegmentPerfDiscontinuityTime_Object = MibTableColumn
mplsOutSegmentPerfDiscontinuityTime = _MplsOutSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 3, 96, 1, 7, 1, 6),
    _MplsOutSegmentPerfDiscontinuityTime_Type()
)
mplsOutSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPerfDiscontinuityTime.setStatus("current")


class _MplsXCIndexNext_Type(Integer32):
    """Custom type mplsXCIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsXCIndexNext_Type.__name__ = "Integer32"
_MplsXCIndexNext_Object = MibScalar
mplsXCIndexNext = _MplsXCIndexNext_Object(
    (1, 3, 6, 1, 3, 96, 1, 8),
    _MplsXCIndexNext_Type()
)
mplsXCIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCIndexNext.setStatus("current")
_MplsXCTable_Object = MibTable
mplsXCTable = _MplsXCTable_Object(
    (1, 3, 6, 1, 3, 96, 1, 9)
)
if mibBuilder.loadTexts:
    mplsXCTable.setStatus("current")
_MplsXCEntry_Object = MibTableRow
mplsXCEntry = _MplsXCEntry_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1)
)
mplsXCEntry.setIndexNames(
    (0, "MPLS-LSR-MIB", "mplsXCIndex"),
    (0, "MPLS-LSR-MIB", "mplsInSegmentIfIndex"),
    (0, "MPLS-LSR-MIB", "mplsInSegmentLabel"),
    (0, "MPLS-LSR-MIB", "mplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    mplsXCEntry.setStatus("current")


class _MplsXCIndex_Type(Integer32):
    """Custom type mplsXCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsXCIndex_Type.__name__ = "Integer32"
_MplsXCIndex_Object = MibTableColumn
mplsXCIndex = _MplsXCIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1, 1),
    _MplsXCIndex_Type()
)
mplsXCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsXCIndex.setStatus("current")
_MplsXCLspId_Type = MplsLSPID
_MplsXCLspId_Object = MibTableColumn
mplsXCLspId = _MplsXCLspId_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1, 2),
    _MplsXCLspId_Type()
)
mplsXCLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCLspId.setStatus("current")


class _MplsXCLabelStackIndex_Type(Integer32):
    """Custom type mplsXCLabelStackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsXCLabelStackIndex_Type.__name__ = "Integer32"
_MplsXCLabelStackIndex_Object = MibTableColumn
mplsXCLabelStackIndex = _MplsXCLabelStackIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1, 3),
    _MplsXCLabelStackIndex_Type()
)
mplsXCLabelStackIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCLabelStackIndex.setStatus("current")


class _MplsXCIsPersistent_Type(TruthValue):
    """Custom type mplsXCIsPersistent based on TruthValue"""
    defaultValue = 2


_MplsXCIsPersistent_Type.__name__ = "TruthValue"
_MplsXCIsPersistent_Object = MibTableColumn
mplsXCIsPersistent = _MplsXCIsPersistent_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1, 4),
    _MplsXCIsPersistent_Type()
)
mplsXCIsPersistent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCIsPersistent.setStatus("current")
_MplsXCOwner_Type = MplsObjectOwner
_MplsXCOwner_Object = MibTableColumn
mplsXCOwner = _MplsXCOwner_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1, 5),
    _MplsXCOwner_Type()
)
mplsXCOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCOwner.setStatus("current")
_MplsXCRowStatus_Type = RowStatus
_MplsXCRowStatus_Object = MibTableColumn
mplsXCRowStatus = _MplsXCRowStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1, 6),
    _MplsXCRowStatus_Type()
)
mplsXCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCRowStatus.setStatus("current")
_MplsXCStorageType_Type = StorageType
_MplsXCStorageType_Object = MibTableColumn
mplsXCStorageType = _MplsXCStorageType_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1, 7),
    _MplsXCStorageType_Type()
)
mplsXCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCStorageType.setStatus("current")


class _MplsXCAdminStatus_Type(Integer32):
    """Custom type mplsXCAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_MplsXCAdminStatus_Type.__name__ = "Integer32"
_MplsXCAdminStatus_Object = MibTableColumn
mplsXCAdminStatus = _MplsXCAdminStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1, 8),
    _MplsXCAdminStatus_Type()
)
mplsXCAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCAdminStatus.setStatus("current")


class _MplsXCOperStatus_Type(Integer32):
    """Custom type mplsXCOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_MplsXCOperStatus_Type.__name__ = "Integer32"
_MplsXCOperStatus_Object = MibTableColumn
mplsXCOperStatus = _MplsXCOperStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 9, 1, 9),
    _MplsXCOperStatus_Type()
)
mplsXCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCOperStatus.setStatus("current")


class _MplsMaxLabelStackDepth_Type(Integer32):
    """Custom type mplsMaxLabelStackDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsMaxLabelStackDepth_Type.__name__ = "Integer32"
_MplsMaxLabelStackDepth_Object = MibScalar
mplsMaxLabelStackDepth = _MplsMaxLabelStackDepth_Object(
    (1, 3, 6, 1, 3, 96, 1, 10),
    _MplsMaxLabelStackDepth_Type()
)
mplsMaxLabelStackDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMaxLabelStackDepth.setStatus("current")


class _MplsLabelStackIndexNext_Type(Integer32):
    """Custom type mplsLabelStackIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsLabelStackIndexNext_Type.__name__ = "Integer32"
_MplsLabelStackIndexNext_Object = MibScalar
mplsLabelStackIndexNext = _MplsLabelStackIndexNext_Object(
    (1, 3, 6, 1, 3, 96, 1, 11),
    _MplsLabelStackIndexNext_Type()
)
mplsLabelStackIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLabelStackIndexNext.setStatus("current")
_MplsLabelStackTable_Object = MibTable
mplsLabelStackTable = _MplsLabelStackTable_Object(
    (1, 3, 6, 1, 3, 96, 1, 12)
)
if mibBuilder.loadTexts:
    mplsLabelStackTable.setStatus("current")
_MplsLabelStackEntry_Object = MibTableRow
mplsLabelStackEntry = _MplsLabelStackEntry_Object(
    (1, 3, 6, 1, 3, 96, 1, 12, 1)
)
mplsLabelStackEntry.setIndexNames(
    (0, "MPLS-LSR-MIB", "mplsLabelStackIndex"),
    (0, "MPLS-LSR-MIB", "mplsLabelStackLabelIndex"),
)
if mibBuilder.loadTexts:
    mplsLabelStackEntry.setStatus("current")


class _MplsLabelStackIndex_Type(Integer32):
    """Custom type mplsLabelStackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLabelStackIndex_Type.__name__ = "Integer32"
_MplsLabelStackIndex_Object = MibTableColumn
mplsLabelStackIndex = _MplsLabelStackIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 12, 1, 1),
    _MplsLabelStackIndex_Type()
)
mplsLabelStackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLabelStackIndex.setStatus("current")


class _MplsLabelStackLabelIndex_Type(Integer32):
    """Custom type mplsLabelStackLabelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLabelStackLabelIndex_Type.__name__ = "Integer32"
_MplsLabelStackLabelIndex_Object = MibTableColumn
mplsLabelStackLabelIndex = _MplsLabelStackLabelIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 12, 1, 2),
    _MplsLabelStackLabelIndex_Type()
)
mplsLabelStackLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLabelStackLabelIndex.setStatus("current")
_MplsLabelStackLabel_Type = MplsLabel
_MplsLabelStackLabel_Object = MibTableColumn
mplsLabelStackLabel = _MplsLabelStackLabel_Object(
    (1, 3, 6, 1, 3, 96, 1, 12, 1, 3),
    _MplsLabelStackLabel_Type()
)
mplsLabelStackLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackLabel.setStatus("current")
_MplsLabelStackRowStatus_Type = RowStatus
_MplsLabelStackRowStatus_Object = MibTableColumn
mplsLabelStackRowStatus = _MplsLabelStackRowStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 12, 1, 4),
    _MplsLabelStackRowStatus_Type()
)
mplsLabelStackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackRowStatus.setStatus("current")
_MplsLabelStackStorageType_Type = StorageType
_MplsLabelStackStorageType_Object = MibTableColumn
mplsLabelStackStorageType = _MplsLabelStackStorageType_Object(
    (1, 3, 6, 1, 3, 96, 1, 12, 1, 5),
    _MplsLabelStackStorageType_Type()
)
mplsLabelStackStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackStorageType.setStatus("current")


class _MplsTrafficParamIndexNext_Type(Integer32):
    """Custom type mplsTrafficParamIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTrafficParamIndexNext_Type.__name__ = "Integer32"
_MplsTrafficParamIndexNext_Object = MibScalar
mplsTrafficParamIndexNext = _MplsTrafficParamIndexNext_Object(
    (1, 3, 6, 1, 3, 96, 1, 13),
    _MplsTrafficParamIndexNext_Type()
)
mplsTrafficParamIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrafficParamIndexNext.setStatus("current")
_MplsTrafficParamTable_Object = MibTable
mplsTrafficParamTable = _MplsTrafficParamTable_Object(
    (1, 3, 6, 1, 3, 96, 1, 14)
)
if mibBuilder.loadTexts:
    mplsTrafficParamTable.setStatus("current")
_MplsTrafficParamEntry_Object = MibTableRow
mplsTrafficParamEntry = _MplsTrafficParamEntry_Object(
    (1, 3, 6, 1, 3, 96, 1, 14, 1)
)
mplsTrafficParamEntry.setIndexNames(
    (0, "MPLS-LSR-MIB", "mplsTrafficParamIndex"),
)
if mibBuilder.loadTexts:
    mplsTrafficParamEntry.setStatus("current")


class _MplsTrafficParamIndex_Type(Integer32):
    """Custom type mplsTrafficParamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTrafficParamIndex_Type.__name__ = "Integer32"
_MplsTrafficParamIndex_Object = MibTableColumn
mplsTrafficParamIndex = _MplsTrafficParamIndex_Object(
    (1, 3, 6, 1, 3, 96, 1, 14, 1, 1),
    _MplsTrafficParamIndex_Type()
)
mplsTrafficParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTrafficParamIndex.setStatus("current")
_MplsTrafficParamMaxRate_Type = MplsBitRate
_MplsTrafficParamMaxRate_Object = MibTableColumn
mplsTrafficParamMaxRate = _MplsTrafficParamMaxRate_Object(
    (1, 3, 6, 1, 3, 96, 1, 14, 1, 2),
    _MplsTrafficParamMaxRate_Type()
)
mplsTrafficParamMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTrafficParamMaxRate.setUnits("kilobits per second")
_MplsTrafficParamMeanRate_Type = MplsBitRate
_MplsTrafficParamMeanRate_Object = MibTableColumn
mplsTrafficParamMeanRate = _MplsTrafficParamMeanRate_Object(
    (1, 3, 6, 1, 3, 96, 1, 14, 1, 3),
    _MplsTrafficParamMeanRate_Type()
)
mplsTrafficParamMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTrafficParamMeanRate.setUnits("kilobits per second")
_MplsTrafficParamMaxBurstSize_Type = MplsBurstSize
_MplsTrafficParamMaxBurstSize_Object = MibTableColumn
mplsTrafficParamMaxBurstSize = _MplsTrafficParamMaxBurstSize_Object(
    (1, 3, 6, 1, 3, 96, 1, 14, 1, 4),
    _MplsTrafficParamMaxBurstSize_Type()
)
mplsTrafficParamMaxBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTrafficParamMaxBurstSize.setUnits("bytes")
_MplsTrafficParamRowStatus_Type = RowStatus
_MplsTrafficParamRowStatus_Object = MibTableColumn
mplsTrafficParamRowStatus = _MplsTrafficParamRowStatus_Object(
    (1, 3, 6, 1, 3, 96, 1, 14, 1, 5),
    _MplsTrafficParamRowStatus_Type()
)
mplsTrafficParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamRowStatus.setStatus("current")
_MplsTrafficParamStorageType_Type = StorageType
_MplsTrafficParamStorageType_Object = MibTableColumn
mplsTrafficParamStorageType = _MplsTrafficParamStorageType_Object(
    (1, 3, 6, 1, 3, 96, 1, 14, 1, 6),
    _MplsTrafficParamStorageType_Type()
)
mplsTrafficParamStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamStorageType.setStatus("current")


class _MplsInSegmentTrapEnable_Type(TruthValue):
    """Custom type mplsInSegmentTrapEnable based on TruthValue"""
    defaultValue = 2


_MplsInSegmentTrapEnable_Type.__name__ = "TruthValue"
_MplsInSegmentTrapEnable_Object = MibScalar
mplsInSegmentTrapEnable = _MplsInSegmentTrapEnable_Object(
    (1, 3, 6, 1, 3, 96, 1, 15),
    _MplsInSegmentTrapEnable_Type()
)
mplsInSegmentTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsInSegmentTrapEnable.setStatus("current")


class _MplsOutSegmentTrapEnable_Type(TruthValue):
    """Custom type mplsOutSegmentTrapEnable based on TruthValue"""
    defaultValue = 2


_MplsOutSegmentTrapEnable_Type.__name__ = "TruthValue"
_MplsOutSegmentTrapEnable_Object = MibScalar
mplsOutSegmentTrapEnable = _MplsOutSegmentTrapEnable_Object(
    (1, 3, 6, 1, 3, 96, 1, 16),
    _MplsOutSegmentTrapEnable_Type()
)
mplsOutSegmentTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsOutSegmentTrapEnable.setStatus("current")


class _MplsXCTrapEnable_Type(TruthValue):
    """Custom type mplsXCTrapEnable based on TruthValue"""
    defaultValue = 2


_MplsXCTrapEnable_Type.__name__ = "TruthValue"
_MplsXCTrapEnable_Object = MibScalar
mplsXCTrapEnable = _MplsXCTrapEnable_Object(
    (1, 3, 6, 1, 3, 96, 1, 17),
    _MplsXCTrapEnable_Type()
)
mplsXCTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsXCTrapEnable.setStatus("current")
_MplsLsrNotifications_ObjectIdentity = ObjectIdentity
mplsLsrNotifications = _MplsLsrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 96, 2)
)
_MplsLsrConformance_ObjectIdentity = ObjectIdentity
mplsLsrConformance = _MplsLsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 96, 3)
)
_MplsLsrGroups_ObjectIdentity = ObjectIdentity
mplsLsrGroups = _MplsLsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 96, 3, 1)
)
_MplsLsrCompliances_ObjectIdentity = ObjectIdentity
mplsLsrCompliances = _MplsLsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 96, 3, 2)
)
mplsInterfaceConfEntry.registerAugmentions(
    ("MPLS-LSR-MIB",
     "mplsInterfacePerfEntry")
)
mplsInterfacePerfEntry.setIndexNames(*mplsInterfaceConfEntry.getIndexNames())
mplsInSegmentEntry.registerAugmentions(
    ("MPLS-LSR-MIB",
     "mplsInSegmentPerfEntry")
)
mplsInSegmentPerfEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions(
    ("MPLS-LSR-MIB",
     "mplsOutSegmentPerfEntry")
)
mplsOutSegmentPerfEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())

# Managed Objects groups

mplsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 1)
)
mplsInterfaceGroup.setObjects(
      *(("MPLS-LSR-MIB", "mplsInterfaceLabelMinIn"),
        ("MPLS-LSR-MIB", "mplsInterfaceLabelMaxIn"),
        ("MPLS-LSR-MIB", "mplsInterfaceLabelMinOut"),
        ("MPLS-LSR-MIB", "mplsInterfaceLabelMaxOut"),
        ("MPLS-LSR-MIB", "mplsInterfaceTotalBandwidth"),
        ("MPLS-LSR-MIB", "mplsInterfaceAvailableBandwidth"),
        ("MPLS-LSR-MIB", "mplsInterfaceTotalBuffer"),
        ("MPLS-LSR-MIB", "mplsInterfaceAvailableBuffer"),
        ("MPLS-LSR-MIB", "mplsInterfaceLabelParticipationType"),
        ("MPLS-LSR-MIB", "mplsInterfaceConfStorageType"))
)
if mibBuilder.loadTexts:
    mplsInterfaceGroup.setStatus("current")

mplsInSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 2)
)
mplsInSegmentGroup.setObjects(
      *(("MPLS-LSR-MIB", "mplsInSegmentNPop"),
        ("MPLS-LSR-MIB", "mplsInSegmentAddrFamily"),
        ("MPLS-LSR-MIB", "mplsInSegmentXCIndex"),
        ("MPLS-LSR-MIB", "mplsInSegmentOctets"),
        ("MPLS-LSR-MIB", "mplsInSegmentDiscards"),
        ("MPLS-LSR-MIB", "mplsInSegmentOwner"),
        ("MPLS-LSR-MIB", "mplsInSegmentAdminStatus"),
        ("MPLS-LSR-MIB", "mplsInSegmentOperStatus"),
        ("MPLS-LSR-MIB", "mplsInSegmentRowStatus"),
        ("MPLS-LSR-MIB", "mplsInSegmentTrapEnable"),
        ("MPLS-LSR-MIB", "mplsInSegmentStorageType"),
        ("MPLS-LSR-MIB", "mplsInSegmentTrafficParamPtr"))
)
if mibBuilder.loadTexts:
    mplsInSegmentGroup.setStatus("current")

mplsOutSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 3)
)
mplsOutSegmentGroup.setObjects(
      *(("MPLS-LSR-MIB", "mplsOutSegmentIndexNext"),
        ("MPLS-LSR-MIB", "mplsOutSegmentIfIndex"),
        ("MPLS-LSR-MIB", "mplsOutSegmentPushTopLabel"),
        ("MPLS-LSR-MIB", "mplsOutSegmentTopLabel"),
        ("MPLS-LSR-MIB", "mplsOutSegmentNextHopIpAddrType"),
        ("MPLS-LSR-MIB", "mplsOutSegmentNextHopIpv4Addr"),
        ("MPLS-LSR-MIB", "mplsOutSegmentNextHopIpv6Addr"),
        ("MPLS-LSR-MIB", "mplsOutSegmentXCIndex"),
        ("MPLS-LSR-MIB", "mplsOutSegmentOwner"),
        ("MPLS-LSR-MIB", "mplsOutSegmentOctets"),
        ("MPLS-LSR-MIB", "mplsOutSegmentDiscards"),
        ("MPLS-LSR-MIB", "mplsOutSegmentErrors"),
        ("MPLS-LSR-MIB", "mplsOutSegmentAdminStatus"),
        ("MPLS-LSR-MIB", "mplsOutSegmentOperStatus"),
        ("MPLS-LSR-MIB", "mplsOutSegmentRowStatus"),
        ("MPLS-LSR-MIB", "mplsOutSegmentTrapEnable"),
        ("MPLS-LSR-MIB", "mplsOutSegmentStorageType"),
        ("MPLS-LSR-MIB", "mplsOutSegmentTrafficParamPtr"))
)
if mibBuilder.loadTexts:
    mplsOutSegmentGroup.setStatus("current")

mplsXCGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 4)
)
mplsXCGroup.setObjects(
      *(("MPLS-LSR-MIB", "mplsXCIndexNext"),
        ("MPLS-LSR-MIB", "mplsXCLspId"),
        ("MPLS-LSR-MIB", "mplsXCLabelStackIndex"),
        ("MPLS-LSR-MIB", "mplsXCOwner"),
        ("MPLS-LSR-MIB", "mplsXCAdminStatus"),
        ("MPLS-LSR-MIB", "mplsXCOperStatus"),
        ("MPLS-LSR-MIB", "mplsXCRowStatus"),
        ("MPLS-LSR-MIB", "mplsXCTrapEnable"),
        ("MPLS-LSR-MIB", "mplsXCStorageType"))
)
if mibBuilder.loadTexts:
    mplsXCGroup.setStatus("current")

mplsPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 5)
)
mplsPerfGroup.setObjects(
      *(("MPLS-LSR-MIB", "mplsInSegmentOctets"),
        ("MPLS-LSR-MIB", "mplsInSegmentPackets"),
        ("MPLS-LSR-MIB", "mplsInSegmentErrors"),
        ("MPLS-LSR-MIB", "mplsInSegmentDiscards"),
        ("MPLS-LSR-MIB", "mplsOutSegmentOctets"),
        ("MPLS-LSR-MIB", "mplsOutSegmentPackets"),
        ("MPLS-LSR-MIB", "mplsOutSegmentDiscards"),
        ("MPLS-LSR-MIB", "mplsInterfaceInLabelsUsed"),
        ("MPLS-LSR-MIB", "mplsInterfaceInPackets"),
        ("MPLS-LSR-MIB", "mplsInterfaceInDiscards"),
        ("MPLS-LSR-MIB", "mplsInterfaceFailedLabelLookup"),
        ("MPLS-LSR-MIB", "mplsInterfaceOutPackets"),
        ("MPLS-LSR-MIB", "mplsInterfaceOutDiscards"),
        ("MPLS-LSR-MIB", "mplsInterfaceOutFragments"),
        ("MPLS-LSR-MIB", "mplsInterfaceOutLabelsUsed"))
)
if mibBuilder.loadTexts:
    mplsPerfGroup.setStatus("current")

mplsHCInSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 6)
)
mplsHCInSegmentPerfGroup.setObjects(
    ("MPLS-LSR-MIB", "mplsInSegmentHCOctets")
)
if mibBuilder.loadTexts:
    mplsHCInSegmentPerfGroup.setStatus("current")

mplsHCOutSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 7)
)
mplsHCOutSegmentPerfGroup.setObjects(
    ("MPLS-LSR-MIB", "mplsOutSegmentHCOctets")
)
if mibBuilder.loadTexts:
    mplsHCOutSegmentPerfGroup.setStatus("current")

mplsTrafficParamGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 8)
)
mplsTrafficParamGroup.setObjects(
      *(("MPLS-LSR-MIB", "mplsTrafficParamIndexNext"),
        ("MPLS-LSR-MIB", "mplsTrafficParamMaxRate"),
        ("MPLS-LSR-MIB", "mplsTrafficParamMeanRate"),
        ("MPLS-LSR-MIB", "mplsTrafficParamMaxBurstSize"),
        ("MPLS-LSR-MIB", "mplsTrafficParamRowStatus"),
        ("MPLS-LSR-MIB", "mplsTrafficParamStorageType"))
)
if mibBuilder.loadTexts:
    mplsTrafficParamGroup.setStatus("current")

mplsXCIsPersistentGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 9)
)
mplsXCIsPersistentGroup.setObjects(
    ("MPLS-LSR-MIB", "mplsXCIsPersistent")
)
if mibBuilder.loadTexts:
    mplsXCIsPersistentGroup.setStatus("current")

mplsXCIsNotPersistentGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 10)
)
mplsXCIsNotPersistentGroup.setObjects(
    ("MPLS-LSR-MIB", "mplsXCIsPersistent")
)
if mibBuilder.loadTexts:
    mplsXCIsNotPersistentGroup.setStatus("current")

mplsLabelStackGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 11)
)
mplsLabelStackGroup.setObjects(
      *(("MPLS-LSR-MIB", "mplsLabelStackLabel"),
        ("MPLS-LSR-MIB", "mplsLabelStackRowStatus"),
        ("MPLS-LSR-MIB", "mplsLabelStackStorageType"),
        ("MPLS-LSR-MIB", "mplsMaxLabelStackDepth"),
        ("MPLS-LSR-MIB", "mplsLabelStackIndexNext"))
)
if mibBuilder.loadTexts:
    mplsLabelStackGroup.setStatus("current")

mplsSegmentDiscontinuityGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 12)
)
mplsSegmentDiscontinuityGroup.setObjects(
      *(("MPLS-LSR-MIB", "mplsInSegmentPerfDiscontinuityTime"),
        ("MPLS-LSR-MIB", "mplsOutSegmentPerfDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mplsSegmentDiscontinuityGroup.setStatus("current")


# Notification objects

mplsInSegmentUp = NotificationType(
    (1, 3, 6, 1, 3, 96, 2, 1)
)
mplsInSegmentUp.setObjects(
      *(("MPLS-LSR-MIB", "mplsInSegmentIfIndex"),
        ("MPLS-LSR-MIB", "mplsInSegmentLabel"),
        ("MPLS-LSR-MIB", "mplsInSegmentAdminStatus"),
        ("MPLS-LSR-MIB", "mplsInSegmentOperStatus"))
)
if mibBuilder.loadTexts:
    mplsInSegmentUp.setStatus(
        "current"
    )

mplsInSegmentDown = NotificationType(
    (1, 3, 6, 1, 3, 96, 2, 2)
)
mplsInSegmentDown.setObjects(
      *(("MPLS-LSR-MIB", "mplsInSegmentIfIndex"),
        ("MPLS-LSR-MIB", "mplsInSegmentLabel"),
        ("MPLS-LSR-MIB", "mplsInSegmentAdminStatus"),
        ("MPLS-LSR-MIB", "mplsInSegmentOperStatus"))
)
if mibBuilder.loadTexts:
    mplsInSegmentDown.setStatus(
        "current"
    )

mplsOutSegmentUp = NotificationType(
    (1, 3, 6, 1, 3, 96, 2, 3)
)
mplsOutSegmentUp.setObjects(
      *(("MPLS-LSR-MIB", "mplsOutSegmentIndex"),
        ("MPLS-LSR-MIB", "mplsInSegmentAdminStatus"),
        ("MPLS-LSR-MIB", "mplsInSegmentOperStatus"))
)
if mibBuilder.loadTexts:
    mplsOutSegmentUp.setStatus(
        "current"
    )

mplsOutSegmentDown = NotificationType(
    (1, 3, 6, 1, 3, 96, 2, 4)
)
mplsOutSegmentDown.setObjects(
      *(("MPLS-LSR-MIB", "mplsOutSegmentIndex"),
        ("MPLS-LSR-MIB", "mplsInSegmentAdminStatus"),
        ("MPLS-LSR-MIB", "mplsInSegmentOperStatus"))
)
if mibBuilder.loadTexts:
    mplsOutSegmentDown.setStatus(
        "current"
    )

mplsXCUp = NotificationType(
    (1, 3, 6, 1, 3, 96, 2, 5)
)
mplsXCUp.setObjects(
      *(("MPLS-LSR-MIB", "mplsXCIndex"),
        ("MPLS-LSR-MIB", "mplsInSegmentIfIndex"),
        ("MPLS-LSR-MIB", "mplsInSegmentLabel"),
        ("MPLS-LSR-MIB", "mplsOutSegmentIndex"),
        ("MPLS-LSR-MIB", "mplsXCAdminStatus"),
        ("MPLS-LSR-MIB", "mplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    mplsXCUp.setStatus(
        "current"
    )

mplsXCDown = NotificationType(
    (1, 3, 6, 1, 3, 96, 2, 6)
)
mplsXCDown.setObjects(
      *(("MPLS-LSR-MIB", "mplsXCIndex"),
        ("MPLS-LSR-MIB", "mplsInSegmentIfIndex"),
        ("MPLS-LSR-MIB", "mplsInSegmentLabel"),
        ("MPLS-LSR-MIB", "mplsOutSegmentIndex"),
        ("MPLS-LSR-MIB", "mplsXCAdminStatus"),
        ("MPLS-LSR-MIB", "mplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    mplsXCDown.setStatus(
        "current"
    )


# Notifications groups

mplsLsrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 96, 3, 1, 13)
)
mplsLsrNotificationGroup.setObjects(
      *(("MPLS-LSR-MIB", "mplsInSegmentUp"),
        ("MPLS-LSR-MIB", "mplsInSegmentDown"),
        ("MPLS-LSR-MIB", "mplsOutSegmentUp"),
        ("MPLS-LSR-MIB", "mplsOutSegmentDown"),
        ("MPLS-LSR-MIB", "mplsXCUp"),
        ("MPLS-LSR-MIB", "mplsXCDown"))
)
if mibBuilder.loadTexts:
    mplsLsrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsLsrModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 96, 3, 2, 1)
)
mplsLsrModuleCompliance.setObjects(
      *(("MPLS-LSR-MIB", "mplsInSegmentGroup"),
        ("MPLS-LSR-MIB", "mplsOutSegmentGroup"),
        ("MPLS-LSR-MIB", "mplsXCGroup"),
        ("MPLS-LSR-MIB", "mplsInterfaceGroup"),
        ("MPLS-LSR-MIB", "mplsPerfGroup"),
        ("MPLS-LSR-MIB", "mplsSegmentDiscontinuityGroup"),
        ("MPLS-LSR-MIB", "mplsHCInSegmentPerfGroup"),
        ("MPLS-LSR-MIB", "mplsHCOutSegmentPerfGroup"),
        ("MPLS-LSR-MIB", "mplsTrafficParamGroup"),
        ("MPLS-LSR-MIB", "mplsXCIsPersistentGroup"),
        ("MPLS-LSR-MIB", "mplsXCIsNotPersistentGroup"))
)
if mibBuilder.loadTexts:
    mplsLsrModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LSR-MIB",
    **{"MplsLSPID": MplsLSPID,
       "MplsLabel": MplsLabel,
       "MplsBitRate": MplsBitRate,
       "MplsBurstSize": MplsBurstSize,
       "MplsBufferSize": MplsBufferSize,
       "MplsObjectOwner": MplsObjectOwner,
       "mplsLsrMIB": mplsLsrMIB,
       "mplsLsrObjects": mplsLsrObjects,
       "mplsInterfaceConfTable": mplsInterfaceConfTable,
       "mplsInterfaceConfEntry": mplsInterfaceConfEntry,
       "mplsInterfaceConfIndex": mplsInterfaceConfIndex,
       "mplsInterfaceLabelMinIn": mplsInterfaceLabelMinIn,
       "mplsInterfaceLabelMaxIn": mplsInterfaceLabelMaxIn,
       "mplsInterfaceLabelMinOut": mplsInterfaceLabelMinOut,
       "mplsInterfaceLabelMaxOut": mplsInterfaceLabelMaxOut,
       "mplsInterfaceTotalBandwidth": mplsInterfaceTotalBandwidth,
       "mplsInterfaceAvailableBandwidth": mplsInterfaceAvailableBandwidth,
       "mplsInterfaceTotalBuffer": mplsInterfaceTotalBuffer,
       "mplsInterfaceAvailableBuffer": mplsInterfaceAvailableBuffer,
       "mplsInterfaceLabelParticipationType": mplsInterfaceLabelParticipationType,
       "mplsInterfaceConfStorageType": mplsInterfaceConfStorageType,
       "mplsInterfacePerfTable": mplsInterfacePerfTable,
       "mplsInterfacePerfEntry": mplsInterfacePerfEntry,
       "mplsInterfaceInLabelsUsed": mplsInterfaceInLabelsUsed,
       "mplsInterfaceInPackets": mplsInterfaceInPackets,
       "mplsInterfaceInDiscards": mplsInterfaceInDiscards,
       "mplsInterfaceFailedLabelLookup": mplsInterfaceFailedLabelLookup,
       "mplsInterfaceOutLabelsUsed": mplsInterfaceOutLabelsUsed,
       "mplsInterfaceOutPackets": mplsInterfaceOutPackets,
       "mplsInterfaceOutDiscards": mplsInterfaceOutDiscards,
       "mplsInterfaceOutFragments": mplsInterfaceOutFragments,
       "mplsInSegmentTable": mplsInSegmentTable,
       "mplsInSegmentEntry": mplsInSegmentEntry,
       "mplsInSegmentIfIndex": mplsInSegmentIfIndex,
       "mplsInSegmentLabel": mplsInSegmentLabel,
       "mplsInSegmentNPop": mplsInSegmentNPop,
       "mplsInSegmentAddrFamily": mplsInSegmentAddrFamily,
       "mplsInSegmentXCIndex": mplsInSegmentXCIndex,
       "mplsInSegmentOwner": mplsInSegmentOwner,
       "mplsInSegmentTrafficParamPtr": mplsInSegmentTrafficParamPtr,
       "mplsInSegmentRowStatus": mplsInSegmentRowStatus,
       "mplsInSegmentStorageType": mplsInSegmentStorageType,
       "mplsInSegmentAdminStatus": mplsInSegmentAdminStatus,
       "mplsInSegmentOperStatus": mplsInSegmentOperStatus,
       "mplsInSegmentPerfTable": mplsInSegmentPerfTable,
       "mplsInSegmentPerfEntry": mplsInSegmentPerfEntry,
       "mplsInSegmentOctets": mplsInSegmentOctets,
       "mplsInSegmentPackets": mplsInSegmentPackets,
       "mplsInSegmentErrors": mplsInSegmentErrors,
       "mplsInSegmentDiscards": mplsInSegmentDiscards,
       "mplsInSegmentHCOctets": mplsInSegmentHCOctets,
       "mplsInSegmentPerfDiscontinuityTime": mplsInSegmentPerfDiscontinuityTime,
       "mplsOutSegmentIndexNext": mplsOutSegmentIndexNext,
       "mplsOutSegmentTable": mplsOutSegmentTable,
       "mplsOutSegmentEntry": mplsOutSegmentEntry,
       "mplsOutSegmentIndex": mplsOutSegmentIndex,
       "mplsOutSegmentIfIndex": mplsOutSegmentIfIndex,
       "mplsOutSegmentPushTopLabel": mplsOutSegmentPushTopLabel,
       "mplsOutSegmentTopLabel": mplsOutSegmentTopLabel,
       "mplsOutSegmentNextHopIpAddrType": mplsOutSegmentNextHopIpAddrType,
       "mplsOutSegmentNextHopIpv4Addr": mplsOutSegmentNextHopIpv4Addr,
       "mplsOutSegmentNextHopIpv6Addr": mplsOutSegmentNextHopIpv6Addr,
       "mplsOutSegmentXCIndex": mplsOutSegmentXCIndex,
       "mplsOutSegmentOwner": mplsOutSegmentOwner,
       "mplsOutSegmentTrafficParamPtr": mplsOutSegmentTrafficParamPtr,
       "mplsOutSegmentRowStatus": mplsOutSegmentRowStatus,
       "mplsOutSegmentStorageType": mplsOutSegmentStorageType,
       "mplsOutSegmentAdminStatus": mplsOutSegmentAdminStatus,
       "mplsOutSegmentOperStatus": mplsOutSegmentOperStatus,
       "mplsOutSegmentPerfTable": mplsOutSegmentPerfTable,
       "mplsOutSegmentPerfEntry": mplsOutSegmentPerfEntry,
       "mplsOutSegmentOctets": mplsOutSegmentOctets,
       "mplsOutSegmentPackets": mplsOutSegmentPackets,
       "mplsOutSegmentErrors": mplsOutSegmentErrors,
       "mplsOutSegmentDiscards": mplsOutSegmentDiscards,
       "mplsOutSegmentHCOctets": mplsOutSegmentHCOctets,
       "mplsOutSegmentPerfDiscontinuityTime": mplsOutSegmentPerfDiscontinuityTime,
       "mplsXCIndexNext": mplsXCIndexNext,
       "mplsXCTable": mplsXCTable,
       "mplsXCEntry": mplsXCEntry,
       "mplsXCIndex": mplsXCIndex,
       "mplsXCLspId": mplsXCLspId,
       "mplsXCLabelStackIndex": mplsXCLabelStackIndex,
       "mplsXCIsPersistent": mplsXCIsPersistent,
       "mplsXCOwner": mplsXCOwner,
       "mplsXCRowStatus": mplsXCRowStatus,
       "mplsXCStorageType": mplsXCStorageType,
       "mplsXCAdminStatus": mplsXCAdminStatus,
       "mplsXCOperStatus": mplsXCOperStatus,
       "mplsMaxLabelStackDepth": mplsMaxLabelStackDepth,
       "mplsLabelStackIndexNext": mplsLabelStackIndexNext,
       "mplsLabelStackTable": mplsLabelStackTable,
       "mplsLabelStackEntry": mplsLabelStackEntry,
       "mplsLabelStackIndex": mplsLabelStackIndex,
       "mplsLabelStackLabelIndex": mplsLabelStackLabelIndex,
       "mplsLabelStackLabel": mplsLabelStackLabel,
       "mplsLabelStackRowStatus": mplsLabelStackRowStatus,
       "mplsLabelStackStorageType": mplsLabelStackStorageType,
       "mplsTrafficParamIndexNext": mplsTrafficParamIndexNext,
       "mplsTrafficParamTable": mplsTrafficParamTable,
       "mplsTrafficParamEntry": mplsTrafficParamEntry,
       "mplsTrafficParamIndex": mplsTrafficParamIndex,
       "mplsTrafficParamMaxRate": mplsTrafficParamMaxRate,
       "mplsTrafficParamMeanRate": mplsTrafficParamMeanRate,
       "mplsTrafficParamMaxBurstSize": mplsTrafficParamMaxBurstSize,
       "mplsTrafficParamRowStatus": mplsTrafficParamRowStatus,
       "mplsTrafficParamStorageType": mplsTrafficParamStorageType,
       "mplsInSegmentTrapEnable": mplsInSegmentTrapEnable,
       "mplsOutSegmentTrapEnable": mplsOutSegmentTrapEnable,
       "mplsXCTrapEnable": mplsXCTrapEnable,
       "mplsLsrNotifications": mplsLsrNotifications,
       "mplsInSegmentUp": mplsInSegmentUp,
       "mplsInSegmentDown": mplsInSegmentDown,
       "mplsOutSegmentUp": mplsOutSegmentUp,
       "mplsOutSegmentDown": mplsOutSegmentDown,
       "mplsXCUp": mplsXCUp,
       "mplsXCDown": mplsXCDown,
       "mplsLsrConformance": mplsLsrConformance,
       "mplsLsrGroups": mplsLsrGroups,
       "mplsInterfaceGroup": mplsInterfaceGroup,
       "mplsInSegmentGroup": mplsInSegmentGroup,
       "mplsOutSegmentGroup": mplsOutSegmentGroup,
       "mplsXCGroup": mplsXCGroup,
       "mplsPerfGroup": mplsPerfGroup,
       "mplsHCInSegmentPerfGroup": mplsHCInSegmentPerfGroup,
       "mplsHCOutSegmentPerfGroup": mplsHCOutSegmentPerfGroup,
       "mplsTrafficParamGroup": mplsTrafficParamGroup,
       "mplsXCIsPersistentGroup": mplsXCIsPersistentGroup,
       "mplsXCIsNotPersistentGroup": mplsXCIsNotPersistentGroup,
       "mplsLabelStackGroup": mplsLabelStackGroup,
       "mplsSegmentDiscontinuityGroup": mplsSegmentDiscontinuityGroup,
       "mplsLsrNotificationGroup": mplsLsrNotificationGroup,
       "mplsLsrCompliances": mplsLsrCompliances,
       "mplsLsrModuleCompliance": mplsLsrModuleCompliance}
)
