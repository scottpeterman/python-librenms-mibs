# SNMP MIB module (CIENA-WS-PTP-PLUGGABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-PTP-PLUGGABLE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:14 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(cwsPtpTxStatusEntry,) = mibBuilder.importSymbols(
    "CIENA-WS-PTP-MIB",
    "cwsPtpTxStatusEntry")

(ChannelsNumber,
 PtpId) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "ChannelsNumber",
    "PtpId")

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

cienaWsPtpPluggableMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10)
)
if mibBuilder.loadTexts:
    cienaWsPtpPluggableMIB.setRevisions(
        ("2017-02-28 00:00",
         "2016-12-12 00:00",
         "2016-06-14 00:00",
         "2015-04-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaWsPtpPluggableObjects_ObjectIdentity = ObjectIdentity
cienaWsPtpPluggableObjects = _CienaWsPtpPluggableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 1)
)
_CienaWsPtpPluggableConformance_ObjectIdentity = ObjectIdentity
cienaWsPtpPluggableConformance = _CienaWsPtpPluggableConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2)
)
_CienaWsPtpPluggableGroups_ObjectIdentity = ObjectIdentity
cienaWsPtpPluggableGroups = _CienaWsPtpPluggableGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2, 1)
)
_CienaWsPtpPluggableCompliances_ObjectIdentity = ObjectIdentity
cienaWsPtpPluggableCompliances = _CienaWsPtpPluggableCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2, 2)
)
_CwsPtpAugPtpPluggableTxStatusTable_Object = MibTable
cwsPtpAugPtpPluggableTxStatusTable = _CwsPtpAugPtpPluggableTxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 3)
)
if mibBuilder.loadTexts:
    cwsPtpAugPtpPluggableTxStatusTable.setStatus("current")
_CwsPtpAugPtpPluggableTxStatusEntry_Object = MibTableRow
cwsPtpAugPtpPluggableTxStatusEntry = _CwsPtpAugPtpPluggableTxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 3, 1)
)
if mibBuilder.loadTexts:
    cwsPtpAugPtpPluggableTxStatusEntry.setStatus("current")
_CwsPtpPluggableTxStatusLossOfSignal_Type = TruthValue
_CwsPtpPluggableTxStatusLossOfSignal_Object = MibTableColumn
cwsPtpPluggableTxStatusLossOfSignal = _CwsPtpPluggableTxStatusLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 3, 1, 1),
    _CwsPtpPluggableTxStatusLossOfSignal_Type()
)
cwsPtpPluggableTxStatusLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPluggableTxStatusLossOfSignal.setStatus("current")
_CwsPtpPluggableTxStatusLossOfLock_Type = TruthValue
_CwsPtpPluggableTxStatusLossOfLock_Object = MibTableColumn
cwsPtpPluggableTxStatusLossOfLock = _CwsPtpPluggableTxStatusLossOfLock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 3, 1, 2),
    _CwsPtpPluggableTxStatusLossOfLock_Type()
)
cwsPtpPluggableTxStatusLossOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPtpPluggableTxStatusLossOfLock.setStatus("current")
cwsPtpTxStatusEntry.registerAugmentions(
    ("CIENA-WS-PTP-PLUGGABLE-MIB",
     "cwsPtpAugPtpPluggableTxStatusEntry")
)
cwsPtpAugPtpPluggableTxStatusEntry.setIndexNames(*cwsPtpTxStatusEntry.getIndexNames())

# Managed Objects groups

cienaWsPtpPluggableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2, 1, 1)
)
cienaWsPtpPluggableGroup.setObjects(
      *(("CIENA-WS-PTP-PLUGGABLE-MIB", "cwsPtpPluggableTxStatusLossOfSignal"),
        ("CIENA-WS-PTP-PLUGGABLE-MIB", "cwsPtpPluggableTxStatusLossOfLock"))
)
if mibBuilder.loadTexts:
    cienaWsPtpPluggableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsPtpPluggableCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2, 2, 1)
)
cienaWsPtpPluggableCompliance.setObjects(
    ("CIENA-WS-PTP-PLUGGABLE-MIB", "cienaWsPtpPluggableGroup")
)
if mibBuilder.loadTexts:
    cienaWsPtpPluggableCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-PTP-PLUGGABLE-MIB",
    **{"cienaWsPtpPluggableMIB": cienaWsPtpPluggableMIB,
       "cienaWsPtpPluggableObjects": cienaWsPtpPluggableObjects,
       "cienaWsPtpPluggableConformance": cienaWsPtpPluggableConformance,
       "cienaWsPtpPluggableGroups": cienaWsPtpPluggableGroups,
       "cienaWsPtpPluggableGroup": cienaWsPtpPluggableGroup,
       "cienaWsPtpPluggableCompliances": cienaWsPtpPluggableCompliances,
       "cienaWsPtpPluggableCompliance": cienaWsPtpPluggableCompliance,
       "cwsPtpAugPtpPluggableTxStatusTable": cwsPtpAugPtpPluggableTxStatusTable,
       "cwsPtpAugPtpPluggableTxStatusEntry": cwsPtpAugPtpPluggableTxStatusEntry,
       "cwsPtpPluggableTxStatusLossOfSignal": cwsPtpPluggableTxStatusLossOfSignal,
       "cwsPtpPluggableTxStatusLossOfLock": cwsPtpPluggableTxStatusLossOfLock}
)
