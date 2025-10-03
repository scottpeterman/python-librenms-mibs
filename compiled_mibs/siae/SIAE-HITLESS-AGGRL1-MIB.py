# SNMP MIB module (SIAE-HITLESS-AGGRL1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-HITLESS-AGGRL1-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:00 2025
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

(aggrL1Entry,) = mibBuilder.importSymbols(
    "SIAE-AGGRL1-MANAGEMENT-MIB",
    "aggrL1Entry")

(linkSettingsEntry,
 linkStatusEntry) = mibBuilder.importSymbols(
    "SIAE-RADIO-SYSTEM-MIB",
    "linkSettingsEntry",
    "linkStatusEntry")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

hitlessAggregationL1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98)
)
if mibBuilder.loadTexts:
    hitlessAggregationL1.setRevisions(
        ("2016-02-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HlAggrL1MibVersion_Type = Integer32
_HlAggrL1MibVersion_Object = MibScalar
hlAggrL1MibVersion = _HlAggrL1MibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 1),
    _HlAggrL1MibVersion_Type()
)
hlAggrL1MibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlAggrL1MibVersion.setStatus("current")
_HlAggrL1Table_Object = MibTable
hlAggrL1Table = _HlAggrL1Table_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 2)
)
if mibBuilder.loadTexts:
    hlAggrL1Table.setStatus("current")
_HlAggrL1Entry_Object = MibTableRow
hlAggrL1Entry = _HlAggrL1Entry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 2, 1)
)
if mibBuilder.loadTexts:
    hlAggrL1Entry.setStatus("current")


class _HlAggrL1Mode_Type(Integer32):
    """Custom type hlAggrL1Mode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hlAggrL1Auto", 1),
          ("hlAggrL1Manual", 2))
    )


_HlAggrL1Mode_Type.__name__ = "Integer32"
_HlAggrL1Mode_Object = MibTableColumn
hlAggrL1Mode = _HlAggrL1Mode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 2, 1, 1),
    _HlAggrL1Mode_Type()
)
hlAggrL1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hlAggrL1Mode.setStatus("current")


class _HlAggrL1Behaviour_Type(Integer32):
    """Custom type hlAggrL1Behaviour based on Integer32"""
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
        *(("hlAggrL1AllSurvive", 1),
          ("hlAggrL1OneSurvive", 2),
          ("hlAggrL1NoneSurvive", 3))
    )


_HlAggrL1Behaviour_Type.__name__ = "Integer32"
_HlAggrL1Behaviour_Object = MibTableColumn
hlAggrL1Behaviour = _HlAggrL1Behaviour_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 2, 1, 2),
    _HlAggrL1Behaviour_Type()
)
hlAggrL1Behaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hlAggrL1Behaviour.setStatus("current")
_HlLinkSettingsTable_Object = MibTable
hlLinkSettingsTable = _HlLinkSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 3)
)
if mibBuilder.loadTexts:
    hlLinkSettingsTable.setStatus("current")
_HlLinkSettingsEntry_Object = MibTableRow
hlLinkSettingsEntry = _HlLinkSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 3, 1)
)
if mibBuilder.loadTexts:
    hlLinkSettingsEntry.setStatus("current")
_LinkHitlessProfile_Type = Integer32
_LinkHitlessProfile_Object = MibTableColumn
linkHitlessProfile = _LinkHitlessProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 3, 1, 1),
    _LinkHitlessProfile_Type()
)
linkHitlessProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkHitlessProfile.setStatus("current")
_HlLinkStatusTable_Object = MibTable
hlLinkStatusTable = _HlLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 4)
)
if mibBuilder.loadTexts:
    hlLinkStatusTable.setStatus("current")
_HlLinkStatusEntry_Object = MibTableRow
hlLinkStatusEntry = _HlLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 4, 1)
)
if mibBuilder.loadTexts:
    hlLinkStatusEntry.setStatus("current")


class _LinkHitlessZone_Type(Integer32):
    """Custom type linkHitlessZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("goodZone", 1),
          ("hitlessZone", 2),
          ("badZone", 3))
    )


_LinkHitlessZone_Type.__name__ = "Integer32"
_LinkHitlessZone_Object = MibTableColumn
linkHitlessZone = _LinkHitlessZone_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 98, 4, 1, 1),
    _LinkHitlessZone_Type()
)
linkHitlessZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkHitlessZone.setStatus("current")
aggrL1Entry.registerAugmentions(
    ("SIAE-HITLESS-AGGRL1-MIB",
     "hlAggrL1Entry")
)
hlAggrL1Entry.setIndexNames(*aggrL1Entry.getIndexNames())
linkSettingsEntry.registerAugmentions(
    ("SIAE-HITLESS-AGGRL1-MIB",
     "hlLinkSettingsEntry")
)
hlLinkSettingsEntry.setIndexNames(*linkSettingsEntry.getIndexNames())
linkStatusEntry.registerAugmentions(
    ("SIAE-HITLESS-AGGRL1-MIB",
     "hlLinkStatusEntry")
)
hlLinkStatusEntry.setIndexNames(*linkStatusEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-HITLESS-AGGRL1-MIB",
    **{"hitlessAggregationL1": hitlessAggregationL1,
       "hlAggrL1MibVersion": hlAggrL1MibVersion,
       "hlAggrL1Table": hlAggrL1Table,
       "hlAggrL1Entry": hlAggrL1Entry,
       "hlAggrL1Mode": hlAggrL1Mode,
       "hlAggrL1Behaviour": hlAggrL1Behaviour,
       "hlLinkSettingsTable": hlLinkSettingsTable,
       "hlLinkSettingsEntry": hlLinkSettingsEntry,
       "linkHitlessProfile": linkHitlessProfile,
       "hlLinkStatusTable": hlLinkStatusTable,
       "hlLinkStatusEntry": hlLinkStatusEntry,
       "linkHitlessZone": linkHitlessZone}
)
