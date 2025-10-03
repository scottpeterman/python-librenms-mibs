# SNMP MIB module (PACKETLOGIC-NIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\procera\PACKETLOGIC-NIC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:17 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hw,) = mibBuilder.importSymbols(
    "PACKETLOGIC-HW-MIB",
    "hw")

(packetlogic2,) = mibBuilder.importSymbols(
    "PACKETLOGIC-MIB",
    "packetlogic2")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2)
)
if mibBuilder.loadTexts:
    nic.setRevisions(
        ("2019-09-12 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Slots_Object = MibTable
slots = _Slots_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1)
)
if mibBuilder.loadTexts:
    slots.setStatus("current")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1)
)
slotEntry.setIndexNames(
    (0, "PACKETLOGIC-NIC-MIB", "slotEntryIndex"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("current")
_SlotLabel_Type = DisplayString
_SlotLabel_Object = MibTableColumn
slotLabel = _SlotLabel_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 1),
    _SlotLabel_Type()
)
slotLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotLabel.setStatus("current")
_SlotState_Type = DisplayString
_SlotState_Object = MibTableColumn
slotState = _SlotState_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 2),
    _SlotState_Type()
)
slotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotState.setStatus("current")
_SlotBypass_Type = DisplayString
_SlotBypass_Object = MibTableColumn
slotBypass = _SlotBypass_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 3),
    _SlotBypass_Type()
)
slotBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBypass.setStatus("current")
_SlotChannels_Type = DisplayString
_SlotChannels_Object = MibTableColumn
slotChannels = _SlotChannels_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 4),
    _SlotChannels_Type()
)
slotChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotChannels.setStatus("current")
_SlotInterface_Type = DisplayString
_SlotInterface_Object = MibTableColumn
slotInterface = _SlotInterface_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 5),
    _SlotInterface_Type()
)
slotInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotInterface.setStatus("current")
_SlotPartNo_Type = DisplayString
_SlotPartNo_Object = MibTableColumn
slotPartNo = _SlotPartNo_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 6),
    _SlotPartNo_Type()
)
slotPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPartNo.setStatus("current")
_SlotPorts_Type = DisplayString
_SlotPorts_Object = MibTableColumn
slotPorts = _SlotPorts_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 7),
    _SlotPorts_Type()
)
slotPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPorts.setStatus("current")
_SlotSpeed_Type = DisplayString
_SlotSpeed_Object = MibTableColumn
slotSpeed = _SlotSpeed_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 8),
    _SlotSpeed_Type()
)
slotSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSpeed.setStatus("current")


class _SlotEntryIndex_Type(Integer32):
    """Custom type slotEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlotEntryIndex_Type.__name__ = "Integer32"
_SlotEntryIndex_Object = MibTableColumn
slotEntryIndex = _SlotEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 1, 1, 999),
    _SlotEntryIndex_Type()
)
slotEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slotEntryIndex.setStatus("current")
_Channels_Object = MibTable
channels = _Channels_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2)
)
if mibBuilder.loadTexts:
    channels.setStatus("current")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1)
)
channelEntry.setIndexNames(
    (0, "PACKETLOGIC-NIC-MIB", "channelEntryIndex"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("current")
_ChannelLocation_Type = DisplayString
_ChannelLocation_Object = MibTableColumn
channelLocation = _ChannelLocation_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 1),
    _ChannelLocation_Type()
)
channelLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelLocation.setStatus("current")
_ChannelLabel_Type = DisplayString
_ChannelLabel_Object = MibTableColumn
channelLabel = _ChannelLabel_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 2),
    _ChannelLabel_Type()
)
channelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelLabel.setStatus("current")
_ChannelSlot_Type = DisplayString
_ChannelSlot_Object = MibTableColumn
channelSlot = _ChannelSlot_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 3),
    _ChannelSlot_Type()
)
channelSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelSlot.setStatus("current")


class _ChannelEntryIndex_Type(Integer32):
    """Custom type channelEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ChannelEntryIndex_Type.__name__ = "Integer32"
_ChannelEntryIndex_Object = MibTableColumn
channelEntryIndex = _ChannelEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 2, 1, 999),
    _ChannelEntryIndex_Type()
)
channelEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelEntryIndex.setStatus("current")
_TotalThroughput_Type = DisplayString
_TotalThroughput_Object = MibScalar
totalThroughput = _TotalThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 2, 3),
    _TotalThroughput_Type()
)
totalThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalThroughput.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-NIC-MIB",
    **{"nic": nic,
       "slots": slots,
       "slotEntry": slotEntry,
       "slotLabel": slotLabel,
       "slotState": slotState,
       "slotBypass": slotBypass,
       "slotChannels": slotChannels,
       "slotInterface": slotInterface,
       "slotPartNo": slotPartNo,
       "slotPorts": slotPorts,
       "slotSpeed": slotSpeed,
       "slotEntryIndex": slotEntryIndex,
       "channels": channels,
       "channelEntry": channelEntry,
       "channelLocation": channelLocation,
       "channelLabel": channelLabel,
       "channelSlot": channelSlot,
       "channelEntryIndex": channelEntryIndex,
       "totalThroughput": totalThroughput}
)
