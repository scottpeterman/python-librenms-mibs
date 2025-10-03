# SNMP MIB module (SL-RETIMER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-RETIMER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:03 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(slService,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "slService")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slRetimer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlRetimerConfig_ObjectIdentity = ObjectIdentity
slRetimerConfig = _SlRetimerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1)
)
_SlRetimerConfigTable_Object = MibTable
slRetimerConfigTable = _SlRetimerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    slRetimerConfigTable.setStatus("current")
_SlRetimerConfigEntry_Object = MibTableRow
slRetimerConfigEntry = _SlRetimerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1, 1)
)
slRetimerConfigEntry.setIndexNames(
    (0, "SL-RETIMER-MIB", "slRetimerLineIndex"),
)
if mibBuilder.loadTexts:
    slRetimerConfigEntry.setStatus("current")
_SlRetimerLineIndex_Type = InterfaceIndex
_SlRetimerLineIndex_Object = MibTableColumn
slRetimerLineIndex = _SlRetimerLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1, 1, 1),
    _SlRetimerLineIndex_Type()
)
slRetimerLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slRetimerLineIndex.setStatus("current")
_SlRetimerResetPmCounters_Type = Integer32
_SlRetimerResetPmCounters_Object = MibTableColumn
slRetimerResetPmCounters = _SlRetimerResetPmCounters_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1, 1, 2),
    _SlRetimerResetPmCounters_Type()
)
slRetimerResetPmCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slRetimerResetPmCounters.setStatus("current")
_SlRetimerStat_ObjectIdentity = ObjectIdentity
slRetimerStat = _SlRetimerStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 2)
)
_SlRetimerPm_ObjectIdentity = ObjectIdentity
slRetimerPm = _SlRetimerPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3)
)
_SlRetimerCurrentTable_Object = MibTable
slRetimerCurrentTable = _SlRetimerCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    slRetimerCurrentTable.setStatus("current")
_SlRetimerCurrentEntry_Object = MibTableRow
slRetimerCurrentEntry = _SlRetimerCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1)
)
slRetimerCurrentEntry.setIndexNames(
    (0, "SL-RETIMER-MIB", "slRetimerCurrentIndex"),
)
if mibBuilder.loadTexts:
    slRetimerCurrentEntry.setStatus("current")
_SlRetimerCurrentIndex_Type = InterfaceIndex
_SlRetimerCurrentIndex_Object = MibTableColumn
slRetimerCurrentIndex = _SlRetimerCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1, 1),
    _SlRetimerCurrentIndex_Type()
)
slRetimerCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slRetimerCurrentIndex.setStatus("current")
_SlRetimerCurrentRxRllES_Type = Integer32
_SlRetimerCurrentRxRllES_Object = MibTableColumn
slRetimerCurrentRxRllES = _SlRetimerCurrentRxRllES_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1, 2),
    _SlRetimerCurrentRxRllES_Type()
)
slRetimerCurrentRxRllES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slRetimerCurrentRxRllES.setStatus("current")
_SlRetimerCurrentRxK285ES_Type = Integer32
_SlRetimerCurrentRxK285ES_Object = MibTableColumn
slRetimerCurrentRxK285ES = _SlRetimerCurrentRxK285ES_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1, 3),
    _SlRetimerCurrentRxK285ES_Type()
)
slRetimerCurrentRxK285ES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slRetimerCurrentRxK285ES.setStatus("current")
_SlRetimerTraps_ObjectIdentity = ObjectIdentity
slRetimerTraps = _SlRetimerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 7)
)

# Managed Objects groups


# Notification objects

slRetimerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 7, 1)
)
slRetimerStatusChange.setObjects(
    ("SL-RETIMER-MIB", "slRetimerLineIndex")
)
if mibBuilder.loadTexts:
    slRetimerStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-RETIMER-MIB",
    **{"slRetimer": slRetimer,
       "slRetimerConfig": slRetimerConfig,
       "slRetimerConfigTable": slRetimerConfigTable,
       "slRetimerConfigEntry": slRetimerConfigEntry,
       "slRetimerLineIndex": slRetimerLineIndex,
       "slRetimerResetPmCounters": slRetimerResetPmCounters,
       "slRetimerStat": slRetimerStat,
       "slRetimerPm": slRetimerPm,
       "slRetimerCurrentTable": slRetimerCurrentTable,
       "slRetimerCurrentEntry": slRetimerCurrentEntry,
       "slRetimerCurrentIndex": slRetimerCurrentIndex,
       "slRetimerCurrentRxRllES": slRetimerCurrentRxRllES,
       "slRetimerCurrentRxK285ES": slRetimerCurrentRxK285ES,
       "slRetimerTraps": slRetimerTraps,
       "slRetimerStatusChange": slRetimerStatusChange}
)
