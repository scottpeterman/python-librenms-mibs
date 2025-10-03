# SNMP MIB module (TN-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-PTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:15 2025
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

(InetAddress,
 InetAddressType,
 ModuleIdentity,
 ObjectIdentity) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "ModuleIdentity",
    "ObjectIdentity")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123)
)
if mibBuilder.loadTexts:
    tnPtpMIB.setRevisions(
        ("2013-11-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnPtp_ObjectIdentity = ObjectIdentity
tnPtp = _TnPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1)
)
_TnPtpClkModesTable_Object = MibTable
tnPtpClkModesTable = _TnPtpClkModesTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 1)
)
if mibBuilder.loadTexts:
    tnPtpClkModesTable.setStatus("current")
_TnPtpClkModesEntry_Object = MibTableRow
tnPtpClkModesEntry = _TnPtpClkModesEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 1, 1)
)
tnPtpClkModesEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnPtpClkModesEntry.setStatus("current")


class _TnPtpInState_Type(Integer32):
    """Custom type tnPtpInState based on Integer32"""
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


_TnPtpInState_Type.__name__ = "Integer32"
_TnPtpInState_Object = MibTableColumn
tnPtpInState = _TnPtpInState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 1, 1, 1),
    _TnPtpInState_Type()
)
tnPtpInState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpInState.setStatus("current")


class _TnPtpOutState_Type(Integer32):
    """Custom type tnPtpOutState based on Integer32"""
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


_TnPtpOutState_Type.__name__ = "Integer32"
_TnPtpOutState_Object = MibTableColumn
tnPtpOutState = _TnPtpOutState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 1, 1, 2),
    _TnPtpOutState_Type()
)
tnPtpOutState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpOutState.setStatus("current")


class _TnPtpInFreq_Type(Integer32):
    """Custom type tnPtpInFreq based on Integer32"""
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
        *(("onePps", 0),
          ("f8kHz", 1),
          ("f64kHz", 2),
          ("f1544kHz", 3),
          ("f2048kHz", 4),
          ("f10000kHz", 5),
          ("f19440kHz", 6),
          ("f25Mhz", 7))
    )


_TnPtpInFreq_Type.__name__ = "Integer32"
_TnPtpInFreq_Object = MibTableColumn
tnPtpInFreq = _TnPtpInFreq_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 1, 1, 3),
    _TnPtpInFreq_Type()
)
tnPtpInFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpInFreq.setStatus("current")
_TnPtpOutFreq_Type = Integer32
_TnPtpOutFreq_Object = MibTableColumn
tnPtpOutFreq = _TnPtpOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 1, 1, 4),
    _TnPtpOutFreq_Type()
)
tnPtpOutFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpOutFreq.setStatus("current")


class _TnPtpImpedance_Type(Integer32):
    """Custom type tnPtpImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("imp50", 1),
          ("imp75", 2),
          ("hi-Z", 3))
    )


_TnPtpImpedance_Type.__name__ = "Integer32"
_TnPtpImpedance_Object = MibTableColumn
tnPtpImpedance = _TnPtpImpedance_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 1, 1, 5),
    _TnPtpImpedance_Type()
)
tnPtpImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpImpedance.setStatus("current")
_TnPtpActualInFreq_Type = Integer32
_TnPtpActualInFreq_Object = MibTableColumn
tnPtpActualInFreq = _TnPtpActualInFreq_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 1, 1, 6),
    _TnPtpActualInFreq_Type()
)
tnPtpActualInFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpActualInFreq.setStatus("current")
_TnPtpActualOutFreq_Type = Integer32
_TnPtpActualOutFreq_Object = MibTableColumn
tnPtpActualOutFreq = _TnPtpActualOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 1, 1, 7),
    _TnPtpActualOutFreq_Type()
)
tnPtpActualOutFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpActualOutFreq.setStatus("current")
_TnPtpCreateClkConfTable_Object = MibTable
tnPtpCreateClkConfTable = _TnPtpCreateClkConfTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2)
)
if mibBuilder.loadTexts:
    tnPtpCreateClkConfTable.setStatus("current")
_TnPtpCreateClkConfEntry_Object = MibTableRow
tnPtpCreateClkConfEntry = _TnPtpCreateClkConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1)
)
tnPtpCreateClkConfEntry.setIndexNames(
    (0, "TN-PTP-MIB", "tnPtpCreateClkConfIndex"),
)
if mibBuilder.loadTexts:
    tnPtpCreateClkConfEntry.setStatus("current")
_TnPtpCreateClkConfIndex_Type = Integer32
_TnPtpCreateClkConfIndex_Object = MibTableColumn
tnPtpCreateClkConfIndex = _TnPtpCreateClkConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 1),
    _TnPtpCreateClkConfIndex_Type()
)
tnPtpCreateClkConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpCreateClkConfIndex.setStatus("current")


class _TnPtpDeviceType_Type(Integer32):
    """Custom type tnPtpDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("ordBound", 1),
          ("p2pTransp", 2),
          ("e2eTransp", 3),
          ("masterOnly", 4),
          ("slaveOnly", 5))
    )


_TnPtpDeviceType_Type.__name__ = "Integer32"
_TnPtpDeviceType_Object = MibTableColumn
tnPtpDeviceType = _TnPtpDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 2),
    _TnPtpDeviceType_Type()
)
tnPtpDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpDeviceType.setStatus("current")
_TnPtpTwoStepFlag_Type = TruthValue
_TnPtpTwoStepFlag_Object = MibTableColumn
tnPtpTwoStepFlag = _TnPtpTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 3),
    _TnPtpTwoStepFlag_Type()
)
tnPtpTwoStepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpTwoStepFlag.setStatus("current")


class _TnPtpClockId_Type(OctetString):
    """Custom type tnPtpClockId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnPtpClockId_Type.__name__ = "OctetString"
_TnPtpClockId_Object = MibTableColumn
tnPtpClockId = _TnPtpClockId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 4),
    _TnPtpClockId_Type()
)
tnPtpClockId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockId.setStatus("current")
_TnPtpOneWay_Type = TruthValue
_TnPtpOneWay_Object = MibTableColumn
tnPtpOneWay = _TnPtpOneWay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 5),
    _TnPtpOneWay_Type()
)
tnPtpOneWay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpOneWay.setStatus("current")


class _TnPtpProtocol_Type(Integer32):
    """Custom type tnPtpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("ipv4multi", 1),
          ("ipv4uni", 2))
    )


_TnPtpProtocol_Type.__name__ = "Integer32"
_TnPtpProtocol_Object = MibTableColumn
tnPtpProtocol = _TnPtpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 6),
    _TnPtpProtocol_Type()
)
tnPtpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpProtocol.setStatus("current")
_TnPtpVLANTag_Type = TruthValue
_TnPtpVLANTag_Object = MibTableColumn
tnPtpVLANTag = _TnPtpVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 7),
    _TnPtpVLANTag_Type()
)
tnPtpVLANTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpVLANTag.setStatus("current")
_TnPtpVID_Type = Integer32
_TnPtpVID_Object = MibTableColumn
tnPtpVID = _TnPtpVID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 8),
    _TnPtpVID_Type()
)
tnPtpVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpVID.setStatus("current")
_TnPtpPCP_Type = Integer32
_TnPtpPCP_Object = MibTableColumn
tnPtpPCP = _TnPtpPCP_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 9),
    _TnPtpPCP_Type()
)
tnPtpPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPCP.setStatus("current")
_TnPtpClkConfRowStatus_Type = RowStatus
_TnPtpClkConfRowStatus_Object = MibTableColumn
tnPtpClkConfRowStatus = _TnPtpClkConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 2, 1, 10),
    _TnPtpClkConfRowStatus_Type()
)
tnPtpClkConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClkConfRowStatus.setStatus("current")
_TnPtpClkConf0Table_Object = MibTable
tnPtpClkConf0Table = _TnPtpClkConf0Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3)
)
if mibBuilder.loadTexts:
    tnPtpClkConf0Table.setStatus("current")
_TnPtpClkConf0Entry_Object = MibTableRow
tnPtpClkConf0Entry = _TnPtpClkConf0Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3, 1)
)
tnPtpClkConf0Entry.setIndexNames(
    (0, "TN-PTP-MIB", "tnPtpClkConf0Index"),
)
if mibBuilder.loadTexts:
    tnPtpClkConf0Entry.setStatus("current")
_TnPtpClkConf0Index_Type = Integer32
_TnPtpClkConf0Index_Object = MibTableColumn
tnPtpClkConf0Index = _TnPtpClkConf0Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3, 1, 1),
    _TnPtpClkConf0Index_Type()
)
tnPtpClkConf0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClkConf0Index.setStatus("current")
_TnPtpDefaultDom_Type = Integer32
_TnPtpDefaultDom_Object = MibTableColumn
tnPtpDefaultDom = _TnPtpDefaultDom_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3, 1, 2),
    _TnPtpDefaultDom_Type()
)
tnPtpDefaultDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpDefaultDom.setStatus("current")


class _TnPtpDefaultClockQuality_Type(OctetString):
    """Custom type tnPtpDefaultClockQuality based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnPtpDefaultClockQuality_Type.__name__ = "OctetString"
_TnPtpDefaultClockQuality_Object = MibTableColumn
tnPtpDefaultClockQuality = _TnPtpDefaultClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3, 1, 3),
    _TnPtpDefaultClockQuality_Type()
)
tnPtpDefaultClockQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpDefaultClockQuality.setStatus("current")
_TnPtpDefaultPri1_Type = Integer32
_TnPtpDefaultPri1_Object = MibTableColumn
tnPtpDefaultPri1 = _TnPtpDefaultPri1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3, 1, 4),
    _TnPtpDefaultPri1_Type()
)
tnPtpDefaultPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpDefaultPri1.setStatus("current")
_TnPtpDefaultPri2_Type = Integer32
_TnPtpDefaultPri2_Object = MibTableColumn
tnPtpDefaultPri2 = _TnPtpDefaultPri2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3, 1, 5),
    _TnPtpDefaultPri2_Type()
)
tnPtpDefaultPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpDefaultPri2.setStatus("current")


class _TnPtpTime_Type(OctetString):
    """Custom type tnPtpTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnPtpTime_Type.__name__ = "OctetString"
_TnPtpTime_Object = MibTableColumn
tnPtpTime = _TnPtpTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3, 1, 6),
    _TnPtpTime_Type()
)
tnPtpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpTime.setStatus("current")


class _TnPtpAdjustMethod_Type(Integer32):
    """Custom type tnPtpAdjustMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("vcxo", 2),
          ("software", 3))
    )


_TnPtpAdjustMethod_Type.__name__ = "Integer32"
_TnPtpAdjustMethod_Object = MibTableColumn
tnPtpAdjustMethod = _TnPtpAdjustMethod_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3, 1, 7),
    _TnPtpAdjustMethod_Type()
)
tnPtpAdjustMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpAdjustMethod.setStatus("current")


class _TnPtpSynce_Type(Integer32):
    """Custom type tnPtpSynce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("sync", 2))
    )


_TnPtpSynce_Type.__name__ = "Integer32"
_TnPtpSynce_Object = MibTableColumn
tnPtpSynce = _TnPtpSynce_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 3, 1, 8),
    _TnPtpSynce_Type()
)
tnPtpSynce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpSynce.setStatus("current")
_TnPtpClkConfTable_Object = MibTable
tnPtpClkConfTable = _TnPtpClkConfTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4)
)
if mibBuilder.loadTexts:
    tnPtpClkConfTable.setStatus("current")
_TnPtpClkConfEntry_Object = MibTableRow
tnPtpClkConfEntry = _TnPtpClkConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1)
)
tnPtpClkConfEntry.setIndexNames(
    (0, "TN-PTP-MIB", "tnPtpClkConfIndex"),
)
if mibBuilder.loadTexts:
    tnPtpClkConfEntry.setStatus("current")
_TnPtpClkConfIndex_Type = Integer32
_TnPtpClkConfIndex_Object = MibTableColumn
tnPtpClkConfIndex = _TnPtpClkConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 1),
    _TnPtpClkConfIndex_Type()
)
tnPtpClkConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpClkConfIndex.setStatus("current")
_TnPtpStpRm_Type = Integer32
_TnPtpStpRm_Object = MibTableColumn
tnPtpStpRm = _TnPtpStpRm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 2),
    _TnPtpStpRm_Type()
)
tnPtpStpRm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpStpRm.setStatus("current")


class _TnPtpOffset_Type(OctetString):
    """Custom type tnPtpOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnPtpOffset_Type.__name__ = "OctetString"
_TnPtpOffset_Object = MibTableColumn
tnPtpOffset = _TnPtpOffset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 3),
    _TnPtpOffset_Type()
)
tnPtpOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpOffset.setStatus("current")


class _TnPtpPathDelay_Type(OctetString):
    """Custom type tnPtpPathDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnPtpPathDelay_Type.__name__ = "OctetString"
_TnPtpPathDelay_Object = MibTableColumn
tnPtpPathDelay = _TnPtpPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 4),
    _TnPtpPathDelay_Type()
)
tnPtpPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPathDelay.setStatus("current")
_TnPtpDelayFilter_Type = Integer32
_TnPtpDelayFilter_Object = MibTableColumn
tnPtpDelayFilter = _TnPtpDelayFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 5),
    _TnPtpDelayFilter_Type()
)
tnPtpDelayFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpDelayFilter.setStatus("current")
_TnPtpFilterPeriod_Type = Integer32
_TnPtpFilterPeriod_Object = MibTableColumn
tnPtpFilterPeriod = _TnPtpFilterPeriod_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 6),
    _TnPtpFilterPeriod_Type()
)
tnPtpFilterPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpFilterPeriod.setStatus("current")
_TnPtpFilterDist_Type = Integer32
_TnPtpFilterDist_Object = MibTableColumn
tnPtpFilterDist = _TnPtpFilterDist_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 7),
    _TnPtpFilterDist_Type()
)
tnPtpFilterDist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpFilterDist.setStatus("current")


class _TnPtpParentPortId_Type(OctetString):
    """Custom type tnPtpParentPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnPtpParentPortId_Type.__name__ = "OctetString"
_TnPtpParentPortId_Object = MibTableColumn
tnPtpParentPortId = _TnPtpParentPortId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 8),
    _TnPtpParentPortId_Type()
)
tnPtpParentPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpParentPortId.setStatus("current")
_TnPtpParentPort_Type = Integer32
_TnPtpParentPort_Object = MibTableColumn
tnPtpParentPort = _TnPtpParentPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 9),
    _TnPtpParentPort_Type()
)
tnPtpParentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpParentPort.setStatus("current")
_TnPtpParentPStat_Type = TruthValue
_TnPtpParentPStat_Object = MibTableColumn
tnPtpParentPStat = _TnPtpParentPStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 10),
    _TnPtpParentPStat_Type()
)
tnPtpParentPStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpParentPStat.setStatus("current")
_TnPtpParentVar_Type = Integer32
_TnPtpParentVar_Object = MibTableColumn
tnPtpParentVar = _TnPtpParentVar_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 11),
    _TnPtpParentVar_Type()
)
tnPtpParentVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpParentVar.setStatus("current")
_TnPtpParentChgRate_Type = Integer32
_TnPtpParentChgRate_Object = MibTableColumn
tnPtpParentChgRate = _TnPtpParentChgRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 12),
    _TnPtpParentChgRate_Type()
)
tnPtpParentChgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpParentChgRate.setStatus("current")


class _TnPtpParentGMId_Type(OctetString):
    """Custom type tnPtpParentGMId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnPtpParentGMId_Type.__name__ = "OctetString"
_TnPtpParentGMId_Object = MibTableColumn
tnPtpParentGMId = _TnPtpParentGMId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 13),
    _TnPtpParentGMId_Type()
)
tnPtpParentGMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpParentGMId.setStatus("current")


class _TnPtpParentGMQual_Type(OctetString):
    """Custom type tnPtpParentGMQual based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnPtpParentGMQual_Type.__name__ = "OctetString"
_TnPtpParentGMQual_Object = MibTableColumn
tnPtpParentGMQual = _TnPtpParentGMQual_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 14),
    _TnPtpParentGMQual_Type()
)
tnPtpParentGMQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpParentGMQual.setStatus("current")
_TnPtpParentPri1_Type = Integer32
_TnPtpParentPri1_Object = MibTableColumn
tnPtpParentPri1 = _TnPtpParentPri1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 15),
    _TnPtpParentPri1_Type()
)
tnPtpParentPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpParentPri1.setStatus("current")
_TnPtpParentPri2_Type = Integer32
_TnPtpParentPri2_Object = MibTableColumn
tnPtpParentPri2 = _TnPtpParentPri2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 4, 1, 16),
    _TnPtpParentPri2_Type()
)
tnPtpParentPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpParentPri2.setStatus("current")
_TnPtpClkConf2Table_Object = MibTable
tnPtpClkConf2Table = _TnPtpClkConf2Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5)
)
if mibBuilder.loadTexts:
    tnPtpClkConf2Table.setStatus("current")
_TnPtpClkConf2Entry_Object = MibTableRow
tnPtpClkConf2Entry = _TnPtpClkConf2Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1)
)
tnPtpClkConf2Entry.setIndexNames(
    (0, "TN-PTP-MIB", "tnPtpClkConfIndex2"),
)
if mibBuilder.loadTexts:
    tnPtpClkConf2Entry.setStatus("current")
_TnPtpClkConfIndex2_Type = Integer32
_TnPtpClkConfIndex2_Object = MibTableColumn
tnPtpClkConfIndex2 = _TnPtpClkConfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 1),
    _TnPtpClkConfIndex2_Type()
)
tnPtpClkConfIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpClkConfIndex2.setStatus("current")
_TnPtpUtcOffset_Type = Integer32
_TnPtpUtcOffset_Object = MibTableColumn
tnPtpUtcOffset = _TnPtpUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 2),
    _TnPtpUtcOffset_Type()
)
tnPtpUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpUtcOffset.setStatus("current")
_TnPtpValid_Type = TruthValue
_TnPtpValid_Object = MibTableColumn
tnPtpValid = _TnPtpValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 3),
    _TnPtpValid_Type()
)
tnPtpValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpValid.setStatus("current")
_TnPtpLeap59_Type = TruthValue
_TnPtpLeap59_Object = MibTableColumn
tnPtpLeap59 = _TnPtpLeap59_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 4),
    _TnPtpLeap59_Type()
)
tnPtpLeap59.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpLeap59.setStatus("current")
_TnPtpLeap61_Type = TruthValue
_TnPtpLeap61_Object = MibTableColumn
tnPtpLeap61 = _TnPtpLeap61_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 5),
    _TnPtpLeap61_Type()
)
tnPtpLeap61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpLeap61.setStatus("current")
_TnPtpTimeTrac_Type = TruthValue
_TnPtpTimeTrac_Object = MibTableColumn
tnPtpTimeTrac = _TnPtpTimeTrac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 6),
    _TnPtpTimeTrac_Type()
)
tnPtpTimeTrac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpTimeTrac.setStatus("current")
_TnPtpFreqTrac_Type = TruthValue
_TnPtpFreqTrac_Object = MibTableColumn
tnPtpFreqTrac = _TnPtpFreqTrac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 7),
    _TnPtpFreqTrac_Type()
)
tnPtpFreqTrac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpFreqTrac.setStatus("current")
_TnPtpTimeScale_Type = TruthValue
_TnPtpTimeScale_Object = MibTableColumn
tnPtpTimeScale = _TnPtpTimeScale_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 8),
    _TnPtpTimeScale_Type()
)
tnPtpTimeScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpTimeScale.setStatus("current")
_TnPtpTimeSource_Type = Integer32
_TnPtpTimeSource_Object = MibTableColumn
tnPtpTimeSource = _TnPtpTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 9),
    _TnPtpTimeSource_Type()
)
tnPtpTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpTimeSource.setStatus("current")
_TnPtpDisplay_Type = TruthValue
_TnPtpDisplay_Object = MibTableColumn
tnPtpDisplay = _TnPtpDisplay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 10),
    _TnPtpDisplay_Type()
)
tnPtpDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpDisplay.setStatus("current")
_TnPtpPEnable_Type = TruthValue
_TnPtpPEnable_Object = MibTableColumn
tnPtpPEnable = _TnPtpPEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 11),
    _TnPtpPEnable_Type()
)
tnPtpPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpPEnable.setStatus("current")
_TnPtpIEnable_Type = TruthValue
_TnPtpIEnable_Object = MibTableColumn
tnPtpIEnable = _TnPtpIEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 12),
    _TnPtpIEnable_Type()
)
tnPtpIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpIEnable.setStatus("current")
_TnPtpDEnable_Type = TruthValue
_TnPtpDEnable_Object = MibTableColumn
tnPtpDEnable = _TnPtpDEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 13),
    _TnPtpDEnable_Type()
)
tnPtpDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpDEnable.setStatus("current")
_TnPtpPConstant_Type = Integer32
_TnPtpPConstant_Object = MibTableColumn
tnPtpPConstant = _TnPtpPConstant_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 14),
    _TnPtpPConstant_Type()
)
tnPtpPConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpPConstant.setStatus("current")
_TnPtpIConstant_Type = Integer32
_TnPtpIConstant_Object = MibTableColumn
tnPtpIConstant = _TnPtpIConstant_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 15),
    _TnPtpIConstant_Type()
)
tnPtpIConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpIConstant.setStatus("current")
_TnPtpDConstant_Type = Integer32
_TnPtpDConstant_Object = MibTableColumn
tnPtpDConstant = _TnPtpDConstant_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 16),
    _TnPtpDConstant_Type()
)
tnPtpDConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpDConstant.setStatus("current")
_TnPtpServoDelayFilter_Type = Integer32
_TnPtpServoDelayFilter_Object = MibTableColumn
tnPtpServoDelayFilter = _TnPtpServoDelayFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 5, 1, 17),
    _TnPtpServoDelayFilter_Type()
)
tnPtpServoDelayFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpServoDelayFilter.setStatus("current")
_TnPtpUnicastSlaveTable_Object = MibTable
tnPtpUnicastSlaveTable = _TnPtpUnicastSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 6)
)
if mibBuilder.loadTexts:
    tnPtpUnicastSlaveTable.setStatus("current")
_TnPtpUnicastSlaveEntry_Object = MibTableRow
tnPtpUnicastSlaveEntry = _TnPtpUnicastSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 6, 1)
)
tnPtpUnicastSlaveEntry.setIndexNames(
    (0, "TN-PTP-MIB", "tnPtpUnicastInstIndex"),
    (0, "TN-PTP-MIB", "tnPtpUnicastSlaveIndex"),
)
if mibBuilder.loadTexts:
    tnPtpUnicastSlaveEntry.setStatus("current")
_TnPtpUnicastInstIndex_Type = Integer32
_TnPtpUnicastInstIndex_Object = MibTableColumn
tnPtpUnicastInstIndex = _TnPtpUnicastInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 6, 1, 1),
    _TnPtpUnicastInstIndex_Type()
)
tnPtpUnicastInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpUnicastInstIndex.setStatus("current")
_TnPtpUnicastSlaveIndex_Type = Integer32
_TnPtpUnicastSlaveIndex_Object = MibTableColumn
tnPtpUnicastSlaveIndex = _TnPtpUnicastSlaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 6, 1, 2),
    _TnPtpUnicastSlaveIndex_Type()
)
tnPtpUnicastSlaveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpUnicastSlaveIndex.setStatus("current")
_TnPtpUnicastDuration_Type = Integer32
_TnPtpUnicastDuration_Object = MibTableColumn
tnPtpUnicastDuration = _TnPtpUnicastDuration_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 6, 1, 3),
    _TnPtpUnicastDuration_Type()
)
tnPtpUnicastDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpUnicastDuration.setStatus("current")
_TnPtpIPAddress_Type = InetAddress
_TnPtpIPAddress_Object = MibTableColumn
tnPtpIPAddress = _TnPtpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 6, 1, 4),
    _TnPtpIPAddress_Type()
)
tnPtpIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpIPAddress.setStatus("current")
_TnPtpGrant_Type = Integer32
_TnPtpGrant_Object = MibTableColumn
tnPtpGrant = _TnPtpGrant_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 6, 1, 5),
    _TnPtpGrant_Type()
)
tnPtpGrant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpGrant.setStatus("current")


class _TnPtpCommState_Type(Integer32):
    """Custom type tnPtpCommState based on Integer32"""
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
        *(("idle", 1),
          ("init", 2),
          ("conn", 3),
          ("sell", 4),
          ("sync", 5))
    )


_TnPtpCommState_Type.__name__ = "Integer32"
_TnPtpCommState_Object = MibTableColumn
tnPtpCommState = _TnPtpCommState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 6, 1, 6),
    _TnPtpCommState_Type()
)
tnPtpCommState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPtpCommState.setStatus("current")
_TnPtpPortConfTable_Object = MibTable
tnPtpPortConfTable = _TnPtpPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7)
)
if mibBuilder.loadTexts:
    tnPtpPortConfTable.setStatus("current")
_TnPtpPortConfEntry_Object = MibTableRow
tnPtpPortConfEntry = _TnPtpPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1)
)
tnPtpPortConfEntry.setIndexNames(
    (0, "TN-PTP-MIB", "tnPtpPortConfInstIndex"),
    (0, "TN-PTP-MIB", "tnPtpPortConfIndex"),
)
if mibBuilder.loadTexts:
    tnPtpPortConfEntry.setStatus("current")
_TnPtpPortConfInstIndex_Type = Integer32
_TnPtpPortConfInstIndex_Object = MibTableColumn
tnPtpPortConfInstIndex = _TnPtpPortConfInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 1),
    _TnPtpPortConfInstIndex_Type()
)
tnPtpPortConfInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpPortConfInstIndex.setStatus("current")
_TnPtpPortConfIndex_Type = Integer32
_TnPtpPortConfIndex_Object = MibTableColumn
tnPtpPortConfIndex = _TnPtpPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 2),
    _TnPtpPortConfIndex_Type()
)
tnPtpPortConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpPortConfIndex.setStatus("current")
_TnPtpStat_Type = OctetString
_TnPtpStat_Object = MibTableColumn
tnPtpStat = _TnPtpStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 3),
    _TnPtpStat_Type()
)
tnPtpStat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpStat.setStatus("current")
_TnPtpMDR_Type = Integer32
_TnPtpMDR_Object = MibTableColumn
tnPtpMDR = _TnPtpMDR_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 4),
    _TnPtpMDR_Type()
)
tnPtpMDR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpMDR.setStatus("current")
_TnPtpMeanPath_Type = OctetString
_TnPtpMeanPath_Object = MibTableColumn
tnPtpMeanPath = _TnPtpMeanPath_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 5),
    _TnPtpMeanPath_Type()
)
tnPtpMeanPath.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpMeanPath.setStatus("current")
_TnPtpAnv_Type = Integer32
_TnPtpAnv_Object = MibTableColumn
tnPtpAnv = _TnPtpAnv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 6),
    _TnPtpAnv_Type()
)
tnPtpAnv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpAnv.setStatus("current")
_TnPtpATO_Type = Integer32
_TnPtpATO_Object = MibTableColumn
tnPtpATO = _TnPtpATO_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 7),
    _TnPtpATO_Type()
)
tnPtpATO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpATO.setStatus("current")
_TnPtpSyv_Type = Integer32
_TnPtpSyv_Object = MibTableColumn
tnPtpSyv = _TnPtpSyv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 8),
    _TnPtpSyv_Type()
)
tnPtpSyv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpSyv.setStatus("current")
_TnPtpSyncIntErr_Type = TruthValue
_TnPtpSyncIntErr_Object = MibTableColumn
tnPtpSyncIntErr = _TnPtpSyncIntErr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 9),
    _TnPtpSyncIntErr_Type()
)
tnPtpSyncIntErr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpSyncIntErr.setStatus("current")


class _TnPtpDim_Type(Integer32):
    """Custom type tnPtpDim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 1),
          ("p2p", 2))
    )


_TnPtpDim_Type.__name__ = "Integer32"
_TnPtpDim_Object = MibTableColumn
tnPtpDim = _TnPtpDim_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 10),
    _TnPtpDim_Type()
)
tnPtpDim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpDim.setStatus("current")
_TnPtpMPR_Type = Integer32
_TnPtpMPR_Object = MibTableColumn
tnPtpMPR = _TnPtpMPR_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 11),
    _TnPtpMPR_Type()
)
tnPtpMPR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpMPR.setStatus("current")
_TnPtpDelayAsym_Type = Integer32
_TnPtpDelayAsym_Object = MibTableColumn
tnPtpDelayAsym = _TnPtpDelayAsym_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 12),
    _TnPtpDelayAsym_Type()
)
tnPtpDelayAsym.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpDelayAsym.setStatus("current")
_TnPtpIngerssLat_Type = Integer32
_TnPtpIngerssLat_Object = MibTableColumn
tnPtpIngerssLat = _TnPtpIngerssLat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 13),
    _TnPtpIngerssLat_Type()
)
tnPtpIngerssLat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpIngerssLat.setStatus("current")
_TnPtpEgressLat_Type = Integer32
_TnPtpEgressLat_Object = MibTableColumn
tnPtpEgressLat = _TnPtpEgressLat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 14),
    _TnPtpEgressLat_Type()
)
tnPtpEgressLat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpEgressLat.setStatus("current")
_TnPtpVersion_Type = Integer32
_TnPtpVersion_Object = MibTableColumn
tnPtpVersion = _TnPtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 15),
    _TnPtpVersion_Type()
)
tnPtpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpVersion.setStatus("current")
_TnPtpPortConfRowStatus_Type = RowStatus
_TnPtpPortConfRowStatus_Object = MibTableColumn
tnPtpPortConfRowStatus = _TnPtpPortConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 123, 1, 7, 1, 16),
    _TnPtpPortConfRowStatus_Type()
)
tnPtpPortConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortConfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-PTP-MIB",
    **{"tnPtpMIB": tnPtpMIB,
       "tnPtp": tnPtp,
       "tnPtpClkModesTable": tnPtpClkModesTable,
       "tnPtpClkModesEntry": tnPtpClkModesEntry,
       "tnPtpInState": tnPtpInState,
       "tnPtpOutState": tnPtpOutState,
       "tnPtpInFreq": tnPtpInFreq,
       "tnPtpOutFreq": tnPtpOutFreq,
       "tnPtpImpedance": tnPtpImpedance,
       "tnPtpActualInFreq": tnPtpActualInFreq,
       "tnPtpActualOutFreq": tnPtpActualOutFreq,
       "tnPtpCreateClkConfTable": tnPtpCreateClkConfTable,
       "tnPtpCreateClkConfEntry": tnPtpCreateClkConfEntry,
       "tnPtpCreateClkConfIndex": tnPtpCreateClkConfIndex,
       "tnPtpDeviceType": tnPtpDeviceType,
       "tnPtpTwoStepFlag": tnPtpTwoStepFlag,
       "tnPtpClockId": tnPtpClockId,
       "tnPtpOneWay": tnPtpOneWay,
       "tnPtpProtocol": tnPtpProtocol,
       "tnPtpVLANTag": tnPtpVLANTag,
       "tnPtpVID": tnPtpVID,
       "tnPtpPCP": tnPtpPCP,
       "tnPtpClkConfRowStatus": tnPtpClkConfRowStatus,
       "tnPtpClkConf0Table": tnPtpClkConf0Table,
       "tnPtpClkConf0Entry": tnPtpClkConf0Entry,
       "tnPtpClkConf0Index": tnPtpClkConf0Index,
       "tnPtpDefaultDom": tnPtpDefaultDom,
       "tnPtpDefaultClockQuality": tnPtpDefaultClockQuality,
       "tnPtpDefaultPri1": tnPtpDefaultPri1,
       "tnPtpDefaultPri2": tnPtpDefaultPri2,
       "tnPtpTime": tnPtpTime,
       "tnPtpAdjustMethod": tnPtpAdjustMethod,
       "tnPtpSynce": tnPtpSynce,
       "tnPtpClkConfTable": tnPtpClkConfTable,
       "tnPtpClkConfEntry": tnPtpClkConfEntry,
       "tnPtpClkConfIndex": tnPtpClkConfIndex,
       "tnPtpStpRm": tnPtpStpRm,
       "tnPtpOffset": tnPtpOffset,
       "tnPtpPathDelay": tnPtpPathDelay,
       "tnPtpDelayFilter": tnPtpDelayFilter,
       "tnPtpFilterPeriod": tnPtpFilterPeriod,
       "tnPtpFilterDist": tnPtpFilterDist,
       "tnPtpParentPortId": tnPtpParentPortId,
       "tnPtpParentPort": tnPtpParentPort,
       "tnPtpParentPStat": tnPtpParentPStat,
       "tnPtpParentVar": tnPtpParentVar,
       "tnPtpParentChgRate": tnPtpParentChgRate,
       "tnPtpParentGMId": tnPtpParentGMId,
       "tnPtpParentGMQual": tnPtpParentGMQual,
       "tnPtpParentPri1": tnPtpParentPri1,
       "tnPtpParentPri2": tnPtpParentPri2,
       "tnPtpClkConf2Table": tnPtpClkConf2Table,
       "tnPtpClkConf2Entry": tnPtpClkConf2Entry,
       "tnPtpClkConfIndex2": tnPtpClkConfIndex2,
       "tnPtpUtcOffset": tnPtpUtcOffset,
       "tnPtpValid": tnPtpValid,
       "tnPtpLeap59": tnPtpLeap59,
       "tnPtpLeap61": tnPtpLeap61,
       "tnPtpTimeTrac": tnPtpTimeTrac,
       "tnPtpFreqTrac": tnPtpFreqTrac,
       "tnPtpTimeScale": tnPtpTimeScale,
       "tnPtpTimeSource": tnPtpTimeSource,
       "tnPtpDisplay": tnPtpDisplay,
       "tnPtpPEnable": tnPtpPEnable,
       "tnPtpIEnable": tnPtpIEnable,
       "tnPtpDEnable": tnPtpDEnable,
       "tnPtpPConstant": tnPtpPConstant,
       "tnPtpIConstant": tnPtpIConstant,
       "tnPtpDConstant": tnPtpDConstant,
       "tnPtpServoDelayFilter": tnPtpServoDelayFilter,
       "tnPtpUnicastSlaveTable": tnPtpUnicastSlaveTable,
       "tnPtpUnicastSlaveEntry": tnPtpUnicastSlaveEntry,
       "tnPtpUnicastInstIndex": tnPtpUnicastInstIndex,
       "tnPtpUnicastSlaveIndex": tnPtpUnicastSlaveIndex,
       "tnPtpUnicastDuration": tnPtpUnicastDuration,
       "tnPtpIPAddress": tnPtpIPAddress,
       "tnPtpGrant": tnPtpGrant,
       "tnPtpCommState": tnPtpCommState,
       "tnPtpPortConfTable": tnPtpPortConfTable,
       "tnPtpPortConfEntry": tnPtpPortConfEntry,
       "tnPtpPortConfInstIndex": tnPtpPortConfInstIndex,
       "tnPtpPortConfIndex": tnPtpPortConfIndex,
       "tnPtpStat": tnPtpStat,
       "tnPtpMDR": tnPtpMDR,
       "tnPtpMeanPath": tnPtpMeanPath,
       "tnPtpAnv": tnPtpAnv,
       "tnPtpATO": tnPtpATO,
       "tnPtpSyv": tnPtpSyv,
       "tnPtpSyncIntErr": tnPtpSyncIntErr,
       "tnPtpDim": tnPtpDim,
       "tnPtpMPR": tnPtpMPR,
       "tnPtpDelayAsym": tnPtpDelayAsym,
       "tnPtpIngerssLat": tnPtpIngerssLat,
       "tnPtpEgressLat": tnPtpEgressLat,
       "tnPtpVersion": tnPtpVersion,
       "tnPtpPortConfRowStatus": tnPtpPortConfRowStatus}
)
