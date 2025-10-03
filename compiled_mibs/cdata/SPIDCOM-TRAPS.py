# SNMP MIB module (SPIDCOM-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\SPIDCOM-TRAPS
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:06 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(plcBasePortIndex,) = mibBuilder.importSymbols(
    "SPC200",
    "plcBasePortIndex")

(ItuAlarmProbableCause,
 ItuAlarmType,
 neAlarmActivePhoto) = mibBuilder.importSymbols(
    "SPIDCOM-ALARM-MIB",
    "ItuAlarmProbableCause",
    "ItuAlarmType",
    "neAlarmActivePhoto")

(specificSpidcomTrap,) = mibBuilder.importSymbols(
    "SPIDCOM-NOTIFICATION-MIB",
    "specificSpidcomTrap")


# MODULE-IDENTITY

trapsDefinition = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

deviceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 1)
)
if mibBuilder.loadTexts:
    deviceDown.setStatus(
        "current"
    )

deviceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 2)
)
if mibBuilder.loadTexts:
    deviceUp.setStatus(
        "current"
    )

maxAttenuation = NotificationType(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 3)
)
if mibBuilder.loadTexts:
    maxAttenuation.setStatus(
        "current"
    )

maxNoise = NotificationType(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 4)
)
if mibBuilder.loadTexts:
    maxNoise.setStatus(
        "current"
    )


# Notifications groups

linkUpDownNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 11)
)
linkUpDownNotificationsGroup.setObjects(
      *(("SPIDCOM-TRAPS", "deviceUp"),
        ("SPIDCOM-TRAPS", "deviceDown"))
)
if mibBuilder.loadTexts:
    linkUpDownNotificationsGroup.setStatus(
        "current"
    )

maxAttenuationNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 12)
)
maxAttenuationNotificationsGroup.setObjects(
    ("SPIDCOM-TRAPS", "maxAttenuation")
)
if mibBuilder.loadTexts:
    maxAttenuationNotificationsGroup.setStatus(
        "current"
    )

maxNoiseNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22764, 4, 1, 13)
)
maxNoiseNotificationsGroup.setObjects(
    ("SPIDCOM-TRAPS", "maxNoise")
)
if mibBuilder.loadTexts:
    maxNoiseNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPIDCOM-TRAPS",
    **{"trapsDefinition": trapsDefinition,
       "deviceDown": deviceDown,
       "deviceUp": deviceUp,
       "maxAttenuation": maxAttenuation,
       "maxNoise": maxNoise,
       "linkUpDownNotificationsGroup": linkUpDownNotificationsGroup,
       "maxAttenuationNotificationsGroup": maxAttenuationNotificationsGroup,
       "maxNoiseNotificationsGroup": maxNoiseNotificationsGroup}
)
