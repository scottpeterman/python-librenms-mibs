# SNMP MIB module (IBMESCONCUB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ibm\IBMESCONCUB-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:00:57 2025
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

(Counter32,
 Integer32,
 IpAddress,
 enterprises) = mibBuilder.importSymbols(
    "SNMPv2-SMI-v1",
    "Counter32",
    "Integer32",
    "IpAddress",
    "enterprises")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(MacAddress,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "MacAddress")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmIROCescon_ObjectIdentity = ObjectIdentity
ibmIROCescon = _IbmIROCescon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14)
)
_EsconPortData_ObjectIdentity = ObjectIdentity
esconPortData = _EsconPortData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1)
)
_EsconPortTable_Object = MibTable
esconPortTable = _EsconPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1)
)
if mibBuilder.loadTexts:
    esconPortTable.setStatus("mandatory")
_EsconPortEntry_Object = MibTableRow
esconPortEntry = _EsconPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1, 1)
)
esconPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    esconPortEntry.setStatus("mandatory")


class _EsconPortInFiberStatus_Type(Integer32):
    """Custom type esconPortInFiberStatus based on Integer32"""
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
        *(("inLoff", 1),
          ("inOls", 2),
          ("inIdle", 3),
          ("inUnknown", 4))
    )


_EsconPortInFiberStatus_Type.__name__ = "Integer32"
_EsconPortInFiberStatus_Object = MibTableColumn
esconPortInFiberStatus = _EsconPortInFiberStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1, 1, 1),
    _EsconPortInFiberStatus_Type()
)
esconPortInFiberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortInFiberStatus.setStatus("mandatory")


class _EsconPortOutFiberStatus_Type(Integer32):
    """Custom type esconPortOutFiberStatus based on Integer32"""
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
        *(("outDisableReq", 1),
          ("outDisableForced", 2),
          ("outLoffForced", 3),
          ("outOls", 4),
          ("outOlsForced", 5),
          ("outEnable", 6),
          ("outError", 7))
    )


_EsconPortOutFiberStatus_Type.__name__ = "Integer32"
_EsconPortOutFiberStatus_Object = MibTableColumn
esconPortOutFiberStatus = _EsconPortOutFiberStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1, 1, 2),
    _EsconPortOutFiberStatus_Type()
)
esconPortOutFiberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortOutFiberStatus.setStatus("mandatory")
_EsconLinkData_ObjectIdentity = ObjectIdentity
esconLinkData = _EsconLinkData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2)
)
_EsconLinkTable_Object = MibTable
esconLinkTable = _EsconLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1)
)
if mibBuilder.loadTexts:
    esconLinkTable.setStatus("mandatory")
_EsconLinkEntry_Object = MibTableRow
esconLinkEntry = _EsconLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1)
)
esconLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IBMESCONCUB-MIB", "esconLinkHostLinkAddress"),
    (0, "IBMESCONCUB-MIB", "esconLinkControlUnitAddress"),
    (0, "IBMESCONCUB-MIB", "esconLinkPartitionNumber"),
)
if mibBuilder.loadTexts:
    esconLinkEntry.setStatus("mandatory")


class _EsconLinkHostLinkAddress_Type(OctetString):
    """Custom type esconLinkHostLinkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_EsconLinkHostLinkAddress_Type.__name__ = "OctetString"
_EsconLinkHostLinkAddress_Object = MibTableColumn
esconLinkHostLinkAddress = _EsconLinkHostLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 1),
    _EsconLinkHostLinkAddress_Type()
)
esconLinkHostLinkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esconLinkHostLinkAddress.setStatus("mandatory")


class _EsconLinkControlUnitAddress_Type(OctetString):
    """Custom type esconLinkControlUnitAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_EsconLinkControlUnitAddress_Type.__name__ = "OctetString"
_EsconLinkControlUnitAddress_Object = MibTableColumn
esconLinkControlUnitAddress = _EsconLinkControlUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 2),
    _EsconLinkControlUnitAddress_Type()
)
esconLinkControlUnitAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esconLinkControlUnitAddress.setStatus("mandatory")


class _EsconLinkPartitionNumber_Type(OctetString):
    """Custom type esconLinkPartitionNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_EsconLinkPartitionNumber_Type.__name__ = "OctetString"
_EsconLinkPartitionNumber_Object = MibTableColumn
esconLinkPartitionNumber = _EsconLinkPartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 3),
    _EsconLinkPartitionNumber_Type()
)
esconLinkPartitionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esconLinkPartitionNumber.setStatus("mandatory")


class _EsconLinkStatus_Type(Integer32):
    """Custom type esconLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hlpNotEstab", 1),
          ("hlpEstab", 2),
          ("hlpError", 3))
    )


_EsconLinkStatus_Type.__name__ = "Integer32"
_EsconLinkStatus_Object = MibTableColumn
esconLinkStatus = _EsconLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 4),
    _EsconLinkStatus_Type()
)
esconLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconLinkStatus.setStatus("mandatory")
_EsconStationData_ObjectIdentity = ObjectIdentity
esconStationData = _EsconStationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3)
)
_EsconStationTable_Object = MibTable
esconStationTable = _EsconStationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1)
)
if mibBuilder.loadTexts:
    esconStationTable.setStatus("mandatory")
_EsconStationEntry_Object = MibTableRow
esconStationEntry = _EsconStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1)
)
esconStationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IBMESCONCUB-MIB", "esconStationHostLinkAddress"),
    (0, "IBMESCONCUB-MIB", "esconStationControlUnitAddress"),
    (0, "IBMESCONCUB-MIB", "esconStationPartitionNumber"),
    (0, "IBMESCONCUB-MIB", "esconStationDeviceAddress"),
)
if mibBuilder.loadTexts:
    esconStationEntry.setStatus("mandatory")


class _EsconStationHostLinkAddress_Type(OctetString):
    """Custom type esconStationHostLinkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_EsconStationHostLinkAddress_Type.__name__ = "OctetString"
_EsconStationHostLinkAddress_Object = MibTableColumn
esconStationHostLinkAddress = _EsconStationHostLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 1),
    _EsconStationHostLinkAddress_Type()
)
esconStationHostLinkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esconStationHostLinkAddress.setStatus("mandatory")


class _EsconStationControlUnitAddress_Type(OctetString):
    """Custom type esconStationControlUnitAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_EsconStationControlUnitAddress_Type.__name__ = "OctetString"
_EsconStationControlUnitAddress_Object = MibTableColumn
esconStationControlUnitAddress = _EsconStationControlUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 2),
    _EsconStationControlUnitAddress_Type()
)
esconStationControlUnitAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esconStationControlUnitAddress.setStatus("mandatory")


class _EsconStationPartitionNumber_Type(OctetString):
    """Custom type esconStationPartitionNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_EsconStationPartitionNumber_Type.__name__ = "OctetString"
_EsconStationPartitionNumber_Object = MibTableColumn
esconStationPartitionNumber = _EsconStationPartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 3),
    _EsconStationPartitionNumber_Type()
)
esconStationPartitionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esconStationPartitionNumber.setStatus("mandatory")


class _EsconStationDeviceAddress_Type(OctetString):
    """Custom type esconStationDeviceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_EsconStationDeviceAddress_Type.__name__ = "OctetString"
_EsconStationDeviceAddress_Object = MibTableColumn
esconStationDeviceAddress = _EsconStationDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 4),
    _EsconStationDeviceAddress_Type()
)
esconStationDeviceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esconStationDeviceAddress.setStatus("mandatory")


class _EsconStationState_Type(Integer32):
    """Custom type esconStationState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("cpDefined", 2),
          ("cpReset", 3),
          ("cpActive", 4),
          ("cpDelete", 5),
          ("cpAbend", 6),
          ("cldpWait", 7),
          ("cldpDefinedl", 8),
          ("cldpError", 9),
          ("cldpLoad", 10),
          ("cldpDump", 11),
          ("deletePending", 12),
          ("deleted", 13),
          ("cpXidExpected", 14))
    )


_EsconStationState_Type.__name__ = "Integer32"
_EsconStationState_Object = MibTableColumn
esconStationState = _EsconStationState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 5),
    _EsconStationState_Type()
)
esconStationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationState.setStatus("mandatory")


class _EsconStationAttentionDelay_Type(Integer32):
    """Custom type esconStationAttentionDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 420),
    )


_EsconStationAttentionDelay_Type.__name__ = "Integer32"
_EsconStationAttentionDelay_Object = MibTableColumn
esconStationAttentionDelay = _EsconStationAttentionDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 6),
    _EsconStationAttentionDelay_Type()
)
esconStationAttentionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconStationAttentionDelay.setStatus("mandatory")


class _EsconStationAttentionTimeOut_Type(Integer32):
    """Custom type esconStationAttentionTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 840),
    )


_EsconStationAttentionTimeOut_Type.__name__ = "Integer32"
_EsconStationAttentionTimeOut_Object = MibTableColumn
esconStationAttentionTimeOut = _EsconStationAttentionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 7),
    _EsconStationAttentionTimeOut_Type()
)
esconStationAttentionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconStationAttentionTimeOut.setStatus("mandatory")


class _EsconStationMaxBfru_Type(Integer32):
    """Custom type esconStationMaxBfru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EsconStationMaxBfru_Type.__name__ = "Integer32"
_EsconStationMaxBfru_Object = MibTableColumn
esconStationMaxBfru = _EsconStationMaxBfru_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 8),
    _EsconStationMaxBfru_Type()
)
esconStationMaxBfru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationMaxBfru.setStatus("mandatory")


class _EsconStationUnitSize_Type(Integer32):
    """Custom type esconStationUnitSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4000),
    )


_EsconStationUnitSize_Type.__name__ = "Integer32"
_EsconStationUnitSize_Object = MibTableColumn
esconStationUnitSize = _EsconStationUnitSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 9),
    _EsconStationUnitSize_Type()
)
esconStationUnitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationUnitSize.setStatus("mandatory")


class _EsconStationMaxMsgSizeReceived_Type(Integer32):
    """Custom type esconStationMaxMsgSizeReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EsconStationMaxMsgSizeReceived_Type.__name__ = "Integer32"
_EsconStationMaxMsgSizeReceived_Object = MibTableColumn
esconStationMaxMsgSizeReceived = _EsconStationMaxMsgSizeReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 10),
    _EsconStationMaxMsgSizeReceived_Type()
)
esconStationMaxMsgSizeReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconStationMaxMsgSizeReceived.setStatus("mandatory")


class _EsconStationMaxMsgSizeSent_Type(Integer32):
    """Custom type esconStationMaxMsgSizeSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EsconStationMaxMsgSizeSent_Type.__name__ = "Integer32"
_EsconStationMaxMsgSizeSent_Object = MibTableColumn
esconStationMaxMsgSizeSent = _EsconStationMaxMsgSizeSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 11),
    _EsconStationMaxMsgSizeSent_Type()
)
esconStationMaxMsgSizeSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconStationMaxMsgSizeSent.setStatus("mandatory")
_EsconStationDataPacketsOkReceived_Type = Counter32
_EsconStationDataPacketsOkReceived_Object = MibTableColumn
esconStationDataPacketsOkReceived = _EsconStationDataPacketsOkReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 12),
    _EsconStationDataPacketsOkReceived_Type()
)
esconStationDataPacketsOkReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationDataPacketsOkReceived.setStatus("mandatory")
_EsconStationDataPacketsKoReceived_Type = Counter32
_EsconStationDataPacketsKoReceived_Object = MibTableColumn
esconStationDataPacketsKoReceived = _EsconStationDataPacketsKoReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 13),
    _EsconStationDataPacketsKoReceived_Type()
)
esconStationDataPacketsKoReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationDataPacketsKoReceived.setStatus("mandatory")
_EsconStationDataPacketsSent_Type = Counter32
_EsconStationDataPacketsSent_Object = MibTableColumn
esconStationDataPacketsSent = _EsconStationDataPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 14),
    _EsconStationDataPacketsSent_Type()
)
esconStationDataPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationDataPacketsSent.setStatus("mandatory")
_EsconStationTotalFramesSent_Type = Counter32
_EsconStationTotalFramesSent_Object = MibTableColumn
esconStationTotalFramesSent = _EsconStationTotalFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 15),
    _EsconStationTotalFramesSent_Type()
)
esconStationTotalFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationTotalFramesSent.setStatus("mandatory")
_EsconStationDataPacketsRetransmitted_Type = Counter32
_EsconStationDataPacketsRetransmitted_Object = MibTableColumn
esconStationDataPacketsRetransmitted = _EsconStationDataPacketsRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 16),
    _EsconStationDataPacketsRetransmitted_Type()
)
esconStationDataPacketsRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationDataPacketsRetransmitted.setStatus("mandatory")
_EsconStationPositiveAckDataPackets_Type = Counter32
_EsconStationPositiveAckDataPackets_Object = MibTableColumn
esconStationPositiveAckDataPackets = _EsconStationPositiveAckDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 17),
    _EsconStationPositiveAckDataPackets_Type()
)
esconStationPositiveAckDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationPositiveAckDataPackets.setStatus("mandatory")
_EsconStationSecondChanceAttentions_Type = Counter32
_EsconStationSecondChanceAttentions_Object = MibTableColumn
esconStationSecondChanceAttentions = _EsconStationSecondChanceAttentions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 18),
    _EsconStationSecondChanceAttentions_Type()
)
esconStationSecondChanceAttentions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationSecondChanceAttentions.setStatus("mandatory")
_EsconStationCommandsRetried_Type = Counter32
_EsconStationCommandsRetried_Object = MibTableColumn
esconStationCommandsRetried = _EsconStationCommandsRetried_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 19),
    _EsconStationCommandsRetried_Type()
)
esconStationCommandsRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconStationCommandsRetried.setStatus("mandatory")
_EsconConformance_ObjectIdentity = ObjectIdentity
esconConformance = _EsconConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMESCONCUB-MIB",
    **{"ibmIROCescon": ibmIROCescon,
       "esconPortData": esconPortData,
       "esconPortTable": esconPortTable,
       "esconPortEntry": esconPortEntry,
       "esconPortInFiberStatus": esconPortInFiberStatus,
       "esconPortOutFiberStatus": esconPortOutFiberStatus,
       "esconLinkData": esconLinkData,
       "esconLinkTable": esconLinkTable,
       "esconLinkEntry": esconLinkEntry,
       "esconLinkHostLinkAddress": esconLinkHostLinkAddress,
       "esconLinkControlUnitAddress": esconLinkControlUnitAddress,
       "esconLinkPartitionNumber": esconLinkPartitionNumber,
       "esconLinkStatus": esconLinkStatus,
       "esconStationData": esconStationData,
       "esconStationTable": esconStationTable,
       "esconStationEntry": esconStationEntry,
       "esconStationHostLinkAddress": esconStationHostLinkAddress,
       "esconStationControlUnitAddress": esconStationControlUnitAddress,
       "esconStationPartitionNumber": esconStationPartitionNumber,
       "esconStationDeviceAddress": esconStationDeviceAddress,
       "esconStationState": esconStationState,
       "esconStationAttentionDelay": esconStationAttentionDelay,
       "esconStationAttentionTimeOut": esconStationAttentionTimeOut,
       "esconStationMaxBfru": esconStationMaxBfru,
       "esconStationUnitSize": esconStationUnitSize,
       "esconStationMaxMsgSizeReceived": esconStationMaxMsgSizeReceived,
       "esconStationMaxMsgSizeSent": esconStationMaxMsgSizeSent,
       "esconStationDataPacketsOkReceived": esconStationDataPacketsOkReceived,
       "esconStationDataPacketsKoReceived": esconStationDataPacketsKoReceived,
       "esconStationDataPacketsSent": esconStationDataPacketsSent,
       "esconStationTotalFramesSent": esconStationTotalFramesSent,
       "esconStationDataPacketsRetransmitted": esconStationDataPacketsRetransmitted,
       "esconStationPositiveAckDataPackets": esconStationPositiveAckDataPackets,
       "esconStationSecondChanceAttentions": esconStationSecondChanceAttentions,
       "esconStationCommandsRetried": esconStationCommandsRetried,
       "esconConformance": esconConformance}
)
