# SNMP MIB module (BLUECOAT-SG-FAILOVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecoat\BLUECOAT-SG-FAILOVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:39 2025
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

bluecoatSGFailoverMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13)
)
if mibBuilder.loadTexts:
    bluecoatSGFailoverMIB.setRevisions(
        ("2011-12-20 03:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FailoverMessageString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_BluecoatSgFailoverMIBObjects_ObjectIdentity = ObjectIdentity
bluecoatSgFailoverMIBObjects = _BluecoatSgFailoverMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 1)
)
_BluecoatSgFailoverValues_ObjectIdentity = ObjectIdentity
bluecoatSgFailoverValues = _BluecoatSgFailoverValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 1, 1)
)
_BluecoatSgFailoverMessage_Type = FailoverMessageString
_BluecoatSgFailoverMessage_Object = MibScalar
bluecoatSgFailoverMessage = _BluecoatSgFailoverMessage_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 1, 1, 1),
    _BluecoatSgFailoverMessage_Type()
)
bluecoatSgFailoverMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bluecoatSgFailoverMessage.setStatus("current")
_BluecoatSgFailoverMIBNotifications_ObjectIdentity = ObjectIdentity
bluecoatSgFailoverMIBNotifications = _BluecoatSgFailoverMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 2)
)
_BluecoatSgFailoverMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
bluecoatSgFailoverMIBNotificationsPrefix = _BluecoatSgFailoverMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 2, 0)
)

# Managed Objects groups


# Notification objects

bluecoatSgFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 13, 2, 0, 1)
)
bluecoatSgFailoverTrap.setObjects(
    ("BLUECOAT-SG-FAILOVER-MIB", "bluecoatSgFailoverMessage")
)
if mibBuilder.loadTexts:
    bluecoatSgFailoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-FAILOVER-MIB",
    **{"FailoverMessageString": FailoverMessageString,
       "bluecoatSGFailoverMIB": bluecoatSGFailoverMIB,
       "bluecoatSgFailoverMIBObjects": bluecoatSgFailoverMIBObjects,
       "bluecoatSgFailoverValues": bluecoatSgFailoverValues,
       "bluecoatSgFailoverMessage": bluecoatSgFailoverMessage,
       "bluecoatSgFailoverMIBNotifications": bluecoatSgFailoverMIBNotifications,
       "bluecoatSgFailoverMIBNotificationsPrefix": bluecoatSgFailoverMIBNotificationsPrefix,
       "bluecoatSgFailoverTrap": bluecoatSgFailoverTrap}
)
