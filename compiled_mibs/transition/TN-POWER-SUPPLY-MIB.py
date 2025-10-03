# SNMP MIB module (TN-POWER-SUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-POWER-SUPPLY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:12 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnPowerSupply = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20)
)
if mibBuilder.loadTexts:
    tnPowerSupply.setRevisions(
        ("2013-03-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnPowerSupplyPowerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnPowerSupplyEnvMonNotifications_ObjectIdentity = ObjectIdentity
tnPowerSupplyEnvMonNotifications = _TnPowerSupplyEnvMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 1)
)
_TnPowerSupplyMIBObject_ObjectIdentity = ObjectIdentity
tnPowerSupplyMIBObject = _TnPowerSupplyMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 2)
)
_TnPowerSupplyTable_Object = MibTable
tnPowerSupplyTable = _TnPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 2, 1)
)
if mibBuilder.loadTexts:
    tnPowerSupplyTable.setStatus("current")
_TnPowerSupplyEntry_Object = MibTableRow
tnPowerSupplyEntry = _TnPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 2, 1, 1)
)
tnPowerSupplyEntry.setIndexNames(
    (0, "TN-POWER-SUPPLY-MIB", "tnPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    tnPowerSupplyEntry.setStatus("current")
_TnPowerSupplyIndex_Type = Unsigned32
_TnPowerSupplyIndex_Object = MibTableColumn
tnPowerSupplyIndex = _TnPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 2, 1, 1, 1),
    _TnPowerSupplyIndex_Type()
)
tnPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPowerSupplyIndex.setStatus("current")
_TnPowerSupplyPresent_Type = TruthValue
_TnPowerSupplyPresent_Object = MibTableColumn
tnPowerSupplyPresent = _TnPowerSupplyPresent_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 2, 1, 1, 2),
    _TnPowerSupplyPresent_Type()
)
tnPowerSupplyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerSupplyPresent.setStatus("current")
_TnPowerSupplyPowerType_Type = TnPowerSupplyPowerType
_TnPowerSupplyPowerType_Object = MibTableColumn
tnPowerSupplyPowerType = _TnPowerSupplyPowerType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 2, 1, 1, 3),
    _TnPowerSupplyPowerType_Type()
)
tnPowerSupplyPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerSupplyPowerType.setStatus("current")
_TnPowerSupplyPowered_Type = TruthValue
_TnPowerSupplyPowered_Object = MibTableColumn
tnPowerSupplyPowered = _TnPowerSupplyPowered_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 2, 1, 1, 4),
    _TnPowerSupplyPowered_Type()
)
tnPowerSupplyPowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerSupplyPowered.setStatus("current")
_TnPowerSupplyFanRPM_Type = Unsigned32
_TnPowerSupplyFanRPM_Object = MibTableColumn
tnPowerSupplyFanRPM = _TnPowerSupplyFanRPM_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 2, 1, 1, 5),
    _TnPowerSupplyFanRPM_Type()
)
tnPowerSupplyFanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerSupplyFanRPM.setStatus("current")
_TnPowerSupplyTemperature_Type = Integer32
_TnPowerSupplyTemperature_Object = MibTableColumn
tnPowerSupplyTemperature = _TnPowerSupplyTemperature_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 2, 1, 1, 6),
    _TnPowerSupplyTemperature_Type()
)
tnPowerSupplyTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerSupplyTemperature.setStatus("current")
_TnPowerSupplyMibConformance_ObjectIdentity = ObjectIdentity
tnPowerSupplyMibConformance = _TnPowerSupplyMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 3)
)

# Managed Objects groups


# Notification objects

tnPowerSupplyEnvMonFailureNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 1, 1)
)
tnPowerSupplyEnvMonFailureNotif.setObjects(
    ("TN-POWER-SUPPLY-MIB", "tnPowerSupplyPowered")
)
if mibBuilder.loadTexts:
    tnPowerSupplyEnvMonFailureNotif.setStatus(
        "current"
    )

tnPowerSupplyEnvMonTemperatureNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 20, 1, 2)
)
tnPowerSupplyEnvMonTemperatureNotif.setObjects(
    ("TN-POWER-SUPPLY-MIB", "tnPowerSupplyTemperature")
)
if mibBuilder.loadTexts:
    tnPowerSupplyEnvMonTemperatureNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-POWER-SUPPLY-MIB",
    **{"TnPowerSupplyPowerType": TnPowerSupplyPowerType,
       "tnPowerSupply": tnPowerSupply,
       "tnPowerSupplyEnvMonNotifications": tnPowerSupplyEnvMonNotifications,
       "tnPowerSupplyEnvMonFailureNotif": tnPowerSupplyEnvMonFailureNotif,
       "tnPowerSupplyEnvMonTemperatureNotif": tnPowerSupplyEnvMonTemperatureNotif,
       "tnPowerSupplyMIBObject": tnPowerSupplyMIBObject,
       "tnPowerSupplyTable": tnPowerSupplyTable,
       "tnPowerSupplyEntry": tnPowerSupplyEntry,
       "tnPowerSupplyIndex": tnPowerSupplyIndex,
       "tnPowerSupplyPresent": tnPowerSupplyPresent,
       "tnPowerSupplyPowerType": tnPowerSupplyPowerType,
       "tnPowerSupplyPowered": tnPowerSupplyPowered,
       "tnPowerSupplyFanRPM": tnPowerSupplyFanRPM,
       "tnPowerSupplyTemperature": tnPowerSupplyTemperature,
       "tnPowerSupplyMibConformance": tnPowerSupplyMibConformance}
)
