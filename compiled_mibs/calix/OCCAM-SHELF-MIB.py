# SNMP MIB module (OCCAM-SHELF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\OCCAM-SHELF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:25 2025
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

(occamGenericHardwareModules,) = mibBuilder.importSymbols(
    "OCCAM-REG-MODULE",
    "occamGenericHardwareModules")

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
 internet,
 iso,
 private) = mibBuilder.importSymbols(
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
    "internet",
    "iso",
    "private")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

occamShelfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    occamShelfMib.setRevisions(
        ("2001-04-27 10:51",
         "2007-02-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ValidValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("not-valid", 2))
    )



class ShelfControllerRoleValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class ShelfSlotIndexValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class ShelfIndexValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class ShelfControllerPeerFoundStatusValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("peer-found", 1),
          ("peer-not-found", 2))
    )



class CardOperationalStatusValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class CardRoleValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("card", 2),
          ("shelf-controller", 3))
    )



class SlotsInShelfValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class CardPresenceStatusValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("removed", 2))
    )



class ShelfControllerRedundancyStateValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )



class ShelfRedundancyStatusValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundant", 1),
          ("not-redundant", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ShelfMibObjects_ObjectIdentity = ObjectIdentity
shelfMibObjects = _ShelfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1)
)
_CardIpAddress_Type = IpAddress
_CardIpAddress_Object = MibScalar
cardIpAddress = _CardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 1),
    _CardIpAddress_Type()
)
cardIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIpAddress.setStatus("current")
_CardShelfIndex_Type = ShelfIndexValue
_CardShelfIndex_Object = MibScalar
cardShelfIndex = _CardShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 2),
    _CardShelfIndex_Type()
)
cardShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardShelfIndex.setStatus("current")
_CardSlotIndex_Type = ShelfSlotIndexValue
_CardSlotIndex_Object = MibScalar
cardSlotIndex = _CardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 3),
    _CardSlotIndex_Type()
)
cardSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSlotIndex.setStatus("current")
_CardShelfSlots_Type = SlotsInShelfValue
_CardShelfSlots_Object = MibScalar
cardShelfSlots = _CardShelfSlots_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 4),
    _CardShelfSlots_Type()
)
cardShelfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardShelfSlots.setStatus("current")
_CardRole_Type = CardRoleValue
_CardRole_Object = MibScalar
cardRole = _CardRole_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 5),
    _CardRole_Type()
)
cardRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardRole.setStatus("current")
_ShelfControllerPeerIpAddress_Type = IpAddress
_ShelfControllerPeerIpAddress_Object = MibScalar
shelfControllerPeerIpAddress = _ShelfControllerPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 6),
    _ShelfControllerPeerIpAddress_Type()
)
shelfControllerPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfControllerPeerIpAddress.setStatus("current")
_ShelfControllerPeerFoundStatus_Type = ShelfControllerPeerFoundStatusValue
_ShelfControllerPeerFoundStatus_Object = MibScalar
shelfControllerPeerFoundStatus = _ShelfControllerPeerFoundStatus_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 7),
    _ShelfControllerPeerFoundStatus_Type()
)
shelfControllerPeerFoundStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfControllerPeerFoundStatus.setStatus("current")
_ShelfControllerRole_Type = ShelfControllerRoleValue
_ShelfControllerRole_Object = MibScalar
shelfControllerRole = _ShelfControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 8),
    _ShelfControllerRole_Type()
)
shelfControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfControllerRole.setStatus("current")
_ShelfControllerRedundancyState_Type = ShelfControllerRedundancyStateValue
_ShelfControllerRedundancyState_Object = MibScalar
shelfControllerRedundancyState = _ShelfControllerRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 9),
    _ShelfControllerRedundancyState_Type()
)
shelfControllerRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfControllerRedundancyState.setStatus("current")
_ShelfClusterIpAddress_Type = IpAddress
_ShelfClusterIpAddress_Object = MibScalar
shelfClusterIpAddress = _ShelfClusterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 10),
    _ShelfClusterIpAddress_Type()
)
shelfClusterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfClusterIpAddress.setStatus("current")
_ShelfRedundancyStatus_Type = ShelfRedundancyStatusValue
_ShelfRedundancyStatus_Object = MibScalar
shelfRedundancyStatus = _ShelfRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 11),
    _ShelfRedundancyStatus_Type()
)
shelfRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfRedundancyStatus.setStatus("current")
_BlcConfigChangeString_Type = DisplayString
_BlcConfigChangeString_Object = MibScalar
blcConfigChangeString = _BlcConfigChangeString_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 12),
    _BlcConfigChangeString_Type()
)
blcConfigChangeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blcConfigChangeString.setStatus("current")
_ShelfSlotTable_Object = MibTable
shelfSlotTable = _ShelfSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 13)
)
if mibBuilder.loadTexts:
    shelfSlotTable.setStatus("current")
_ShelfSlotEntry_Object = MibTableRow
shelfSlotEntry = _ShelfSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 13, 1)
)
shelfSlotEntry.setIndexNames(
    (0, "OCCAM-SHELF-MIB", "shelfSlotIndex"),
)
if mibBuilder.loadTexts:
    shelfSlotEntry.setStatus("current")
_ShelfSlotIndex_Type = ShelfSlotIndexValue
_ShelfSlotIndex_Object = MibTableColumn
shelfSlotIndex = _ShelfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 13, 1, 1),
    _ShelfSlotIndex_Type()
)
shelfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSlotIndex.setStatus("current")
_ShelfCardIpAddress_Type = IpAddress
_ShelfCardIpAddress_Object = MibTableColumn
shelfCardIpAddress = _ShelfCardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 13, 1, 2),
    _ShelfCardIpAddress_Type()
)
shelfCardIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardIpAddress.setStatus("current")
_ShelfCardPresenceStatus_Type = CardPresenceStatusValue
_ShelfCardPresenceStatus_Object = MibTableColumn
shelfCardPresenceStatus = _ShelfCardPresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 13, 1, 3),
    _ShelfCardPresenceStatus_Type()
)
shelfCardPresenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardPresenceStatus.setStatus("current")
_ShelfCardOperationalStatus_Type = CardOperationalStatusValue
_ShelfCardOperationalStatus_Object = MibTableColumn
shelfCardOperationalStatus = _ShelfCardOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 13, 1, 4),
    _ShelfCardOperationalStatus_Type()
)
shelfCardOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardOperationalStatus.setStatus("current")
_ShelfSlotRowStatus_Type = ValidValue
_ShelfSlotRowStatus_Object = MibTableColumn
shelfSlotRowStatus = _ShelfSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 13, 1, 5),
    _ShelfSlotRowStatus_Type()
)
shelfSlotRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSlotRowStatus.setStatus("current")
_ResyncTrigger_Type = TimeTicks
_ResyncTrigger_Object = MibScalar
resyncTrigger = _ResyncTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 14),
    _ResyncTrigger_Type()
)
resyncTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resyncTrigger.setStatus("current")
_ResyncTriggerAll_Type = TimeTicks
_ResyncTriggerAll_Object = MibScalar
resyncTriggerAll = _ResyncTriggerAll_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 15),
    _ResyncTriggerAll_Type()
)
resyncTriggerAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resyncTriggerAll.setStatus("current")
_ResyncActiveAlarms_Type = DisplayString
_ResyncActiveAlarms_Object = MibScalar
resyncActiveAlarms = _ResyncActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 16),
    _ResyncActiveAlarms_Type()
)
resyncActiveAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resyncActiveAlarms.setStatus("current")
_ResyncEvents_Type = DisplayString
_ResyncEvents_Object = MibScalar
resyncEvents = _ResyncEvents_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 1, 17),
    _ResyncEvents_Type()
)
resyncEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resyncEvents.setStatus("current")
_ShelfMibTraps_ObjectIdentity = ObjectIdentity
shelfMibTraps = _ShelfMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 2)
)

# Managed Objects groups


# Notification objects

cardPresenceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 2, 1)
)
cardPresenceNotification.setObjects(
      *(("OCCAM-SHELF-MIB", "cardIpAddress"),
        ("OCCAM-SHELF-MIB", "cardShelfIndex"),
        ("OCCAM-SHELF-MIB", "cardSlotIndex"),
        ("OCCAM-SHELF-MIB", "shelfCardPresenceStatus"))
)
if mibBuilder.loadTexts:
    cardPresenceNotification.setStatus(
        "current"
    )

cardOperationalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 2, 2)
)
cardOperationalNotification.setObjects(
      *(("OCCAM-SHELF-MIB", "cardIpAddress"),
        ("OCCAM-SHELF-MIB", "cardShelfIndex"),
        ("OCCAM-SHELF-MIB", "cardSlotIndex"),
        ("OCCAM-SHELF-MIB", "shelfCardOperationalStatus"))
)
if mibBuilder.loadTexts:
    cardOperationalNotification.setStatus(
        "current"
    )

shelfControllerFailoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 2, 3)
)
shelfControllerFailoverNotification.setObjects(
      *(("OCCAM-SHELF-MIB", "cardIpAddress"),
        ("OCCAM-SHELF-MIB", "cardShelfIndex"),
        ("OCCAM-SHELF-MIB", "cardSlotIndex"),
        ("OCCAM-SHELF-MIB", "shelfControllerPeerIpAddress"),
        ("OCCAM-SHELF-MIB", "shelfControllerRole"),
        ("OCCAM-SHELF-MIB", "shelfControllerRedundancyState"))
)
if mibBuilder.loadTexts:
    shelfControllerFailoverNotification.setStatus(
        "current"
    )

shelfControllerForcedFailoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 2, 4)
)
shelfControllerForcedFailoverNotification.setObjects(
      *(("OCCAM-SHELF-MIB", "cardIpAddress"),
        ("OCCAM-SHELF-MIB", "cardShelfIndex"),
        ("OCCAM-SHELF-MIB", "cardSlotIndex"),
        ("OCCAM-SHELF-MIB", "shelfControllerPeerIpAddress"),
        ("OCCAM-SHELF-MIB", "shelfControllerRole"),
        ("OCCAM-SHELF-MIB", "shelfControllerRedundancyState"))
)
if mibBuilder.loadTexts:
    shelfControllerForcedFailoverNotification.setStatus(
        "current"
    )

peerFoundNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 2, 5)
)
peerFoundNotification.setObjects(
      *(("OCCAM-SHELF-MIB", "cardIpAddress"),
        ("OCCAM-SHELF-MIB", "cardShelfIndex"),
        ("OCCAM-SHELF-MIB", "cardSlotIndex"),
        ("OCCAM-SHELF-MIB", "shelfControllerPeerIpAddress"),
        ("OCCAM-SHELF-MIB", "shelfControllerRole"),
        ("OCCAM-SHELF-MIB", "shelfControllerRedundancyState"),
        ("OCCAM-SHELF-MIB", "shelfControllerPeerFoundStatus"))
)
if mibBuilder.loadTexts:
    peerFoundNotification.setStatus(
        "current"
    )

configChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 2, 6)
)
configChangedNotification.setObjects(
      *(("OCCAM-SHELF-MIB", "cardIpAddress"),
        ("OCCAM-SHELF-MIB", "cardShelfIndex"),
        ("OCCAM-SHELF-MIB", "cardSlotIndex"),
        ("OCCAM-SHELF-MIB", "blcConfigChangeString"))
)
if mibBuilder.loadTexts:
    configChangedNotification.setStatus(
        "current"
    )

shelfRedundancyChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3, 3, 2, 7)
)
shelfRedundancyChangeNotification.setObjects(
      *(("OCCAM-SHELF-MIB", "cardIpAddress"),
        ("OCCAM-SHELF-MIB", "cardShelfIndex"),
        ("OCCAM-SHELF-MIB", "cardSlotIndex"),
        ("OCCAM-SHELF-MIB", "shelfControllerRole"),
        ("OCCAM-SHELF-MIB", "shelfControllerRedundancyState"),
        ("OCCAM-SHELF-MIB", "shelfRedundancyStatus"))
)
if mibBuilder.loadTexts:
    shelfRedundancyChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCCAM-SHELF-MIB",
    **{"ValidValue": ValidValue,
       "ShelfControllerRoleValue": ShelfControllerRoleValue,
       "ShelfSlotIndexValue": ShelfSlotIndexValue,
       "ShelfIndexValue": ShelfIndexValue,
       "ShelfControllerPeerFoundStatusValue": ShelfControllerPeerFoundStatusValue,
       "CardOperationalStatusValue": CardOperationalStatusValue,
       "CardRoleValue": CardRoleValue,
       "SlotsInShelfValue": SlotsInShelfValue,
       "CardPresenceStatusValue": CardPresenceStatusValue,
       "ShelfControllerRedundancyStateValue": ShelfControllerRedundancyStateValue,
       "ShelfRedundancyStatusValue": ShelfRedundancyStatusValue,
       "occamShelfMib": occamShelfMib,
       "shelfMibObjects": shelfMibObjects,
       "cardIpAddress": cardIpAddress,
       "cardShelfIndex": cardShelfIndex,
       "cardSlotIndex": cardSlotIndex,
       "cardShelfSlots": cardShelfSlots,
       "cardRole": cardRole,
       "shelfControllerPeerIpAddress": shelfControllerPeerIpAddress,
       "shelfControllerPeerFoundStatus": shelfControllerPeerFoundStatus,
       "shelfControllerRole": shelfControllerRole,
       "shelfControllerRedundancyState": shelfControllerRedundancyState,
       "shelfClusterIpAddress": shelfClusterIpAddress,
       "shelfRedundancyStatus": shelfRedundancyStatus,
       "blcConfigChangeString": blcConfigChangeString,
       "shelfSlotTable": shelfSlotTable,
       "shelfSlotEntry": shelfSlotEntry,
       "shelfSlotIndex": shelfSlotIndex,
       "shelfCardIpAddress": shelfCardIpAddress,
       "shelfCardPresenceStatus": shelfCardPresenceStatus,
       "shelfCardOperationalStatus": shelfCardOperationalStatus,
       "shelfSlotRowStatus": shelfSlotRowStatus,
       "resyncTrigger": resyncTrigger,
       "resyncTriggerAll": resyncTriggerAll,
       "resyncActiveAlarms": resyncActiveAlarms,
       "resyncEvents": resyncEvents,
       "shelfMibTraps": shelfMibTraps,
       "cardPresenceNotification": cardPresenceNotification,
       "cardOperationalNotification": cardOperationalNotification,
       "shelfControllerFailoverNotification": shelfControllerFailoverNotification,
       "shelfControllerForcedFailoverNotification": shelfControllerForcedFailoverNotification,
       "peerFoundNotification": peerFoundNotification,
       "configChangedNotification": configChangedNotification,
       "shelfRedundancyChangeNotification": shelfRedundancyChangeNotification}
)
