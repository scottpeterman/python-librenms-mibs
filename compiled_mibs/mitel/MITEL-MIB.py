# SNMP MIB module (MITEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mitel\MITEL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:42 2025
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mitel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
if mibBuilder.loadTexts:
    mitel.setRevisions(
        ("2014-02-11 12:00",
         "2011-07-14 00:00",
         "2006-01-01 00:00",
         "2005-04-12 21:34",
         "2004-02-23 00:00",
         "1999-02-23 00:00",
         "1996-04-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MitelIfType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dnic", 1)
    )



class MitelNotifyTransportType(TextualConvention, Integer32):
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
        *(("mitelNotifTransV1Trap", 1),
          ("mitelNotifTransV2Trap", 2),
          ("mitelNotifTransInform", 3))
    )



# MIB Managed Objects in the order of their OIDs

_MitelIdentification_ObjectIdentity = ObjectIdentity
mitelIdentification = _MitelIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1)
)
if mibBuilder.loadTexts:
    mitelIdentification.setStatus("current")
_MitelIdMgmtPlatforms_ObjectIdentity = ObjectIdentity
mitelIdMgmtPlatforms = _MitelIdMgmtPlatforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 1)
)
if mibBuilder.loadTexts:
    mitelIdMgmtPlatforms.setStatus("current")
_MitelIdCallServers_ObjectIdentity = ObjectIdentity
mitelIdCallServers = _MitelIdCallServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2)
)
if mibBuilder.loadTexts:
    mitelIdCallServers.setStatus("current")
_MitelIdCsMc2_ObjectIdentity = ObjectIdentity
mitelIdCsMc2 = _MitelIdCsMc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mitelIdCsMc2.setStatus("current")
_MitelIdCs2000Light_ObjectIdentity = ObjectIdentity
mitelIdCs2000Light = _MitelIdCs2000Light_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mitelIdCs2000Light.setStatus("current")
_MitelIdCsIpera3000_ObjectIdentity = ObjectIdentity
mitelIdCsIpera3000 = _MitelIdCsIpera3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mitelIdCsIpera3000.setStatus("current")
_MitelIdTerminals_ObjectIdentity = ObjectIdentity
mitelIdTerminals = _MitelIdTerminals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 3)
)
if mibBuilder.loadTexts:
    mitelIdTerminals.setStatus("current")
_MitelIdInterfaces_ObjectIdentity = ObjectIdentity
mitelIdInterfaces = _MitelIdInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 4)
)
if mibBuilder.loadTexts:
    mitelIdInterfaces.setStatus("current")
_MitelIdCtiPlatforms_ObjectIdentity = ObjectIdentity
mitelIdCtiPlatforms = _MitelIdCtiPlatforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 5)
)
if mibBuilder.loadTexts:
    mitelIdCtiPlatforms.setStatus("current")
_MitelIdApplicationPlatforms_ObjectIdentity = ObjectIdentity
mitelIdApplicationPlatforms = _MitelIdApplicationPlatforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 6)
)
if mibBuilder.loadTexts:
    mitelIdApplicationPlatforms.setStatus("current")
_MitelExperimental_ObjectIdentity = ObjectIdentity
mitelExperimental = _MitelExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 2)
)
if mibBuilder.loadTexts:
    mitelExperimental.setStatus("current")
_MitelExtensions_ObjectIdentity = ObjectIdentity
mitelExtensions = _MitelExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 3)
)
if mibBuilder.loadTexts:
    mitelExtensions.setStatus("current")
_MitelExtInterfaces_ObjectIdentity = ObjectIdentity
mitelExtInterfaces = _MitelExtInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2)
)
if mibBuilder.loadTexts:
    mitelExtInterfaces.setStatus("current")
_MitelIfNumber_Type = Integer32
_MitelIfNumber_Object = MibScalar
mitelIfNumber = _MitelIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2, 1),
    _MitelIfNumber_Type()
)
mitelIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIfNumber.setStatus("current")
_MitelIfTable_Object = MibTable
mitelIfTable = _MitelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mitelIfTable.setStatus("current")
_MitelIfTableEntry_Object = MibTableRow
mitelIfTableEntry = _MitelIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1)
)
mitelIfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mitelIfTableEntry.setStatus("current")
_MitelIfTblType_Type = MitelIfType
_MitelIfTblType_Object = MibTableColumn
mitelIfTblType = _MitelIfTblType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1, 1),
    _MitelIfTblType_Type()
)
mitelIfTblType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIfTblType.setStatus("current")
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
if mibBuilder.loadTexts:
    mitelProprietary.setStatus("current")
_MitelPropApplications_ObjectIdentity = ObjectIdentity
mitelPropApplications = _MitelPropApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1)
)
if mibBuilder.loadTexts:
    mitelPropApplications.setStatus("current")
_MitelAppCallServer_ObjectIdentity = ObjectIdentity
mitelAppCallServer = _MitelAppCallServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mitelAppCallServer.setStatus("current")
_MitelPropTransmission_ObjectIdentity = ObjectIdentity
mitelPropTransmission = _MitelPropTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2)
)
if mibBuilder.loadTexts:
    mitelPropTransmission.setStatus("current")
_MitelPropProtocols_ObjectIdentity = ObjectIdentity
mitelPropProtocols = _MitelPropProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 3)
)
if mibBuilder.loadTexts:
    mitelPropProtocols.setStatus("current")
_MitelPropUtilities_ObjectIdentity = ObjectIdentity
mitelPropUtilities = _MitelPropUtilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 4)
)
if mibBuilder.loadTexts:
    mitelPropUtilities.setStatus("current")
_MitelPropHardware_ObjectIdentity = ObjectIdentity
mitelPropHardware = _MitelPropHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 5)
)
if mibBuilder.loadTexts:
    mitelPropHardware.setStatus("current")
_MitelPropNotifications_ObjectIdentity = ObjectIdentity
mitelPropNotifications = _MitelPropNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6)
)
if mibBuilder.loadTexts:
    mitelPropNotifications.setStatus("current")
_MitelPropReset_ObjectIdentity = ObjectIdentity
mitelPropReset = _MitelPropReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 7)
)
if mibBuilder.loadTexts:
    mitelPropReset.setStatus("current")
_MitelPropCommon_ObjectIdentity = ObjectIdentity
mitelPropCommon = _MitelPropCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9)
)
if mibBuilder.loadTexts:
    mitelPropCommon.setStatus("current")
_MitelConformance_ObjectIdentity = ObjectIdentity
mitelConformance = _MitelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5)
)
if mibBuilder.loadTexts:
    mitelConformance.setStatus("current")
_MitelConfCompliances_ObjectIdentity = ObjectIdentity
mitelConfCompliances = _MitelConfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 1)
)
if mibBuilder.loadTexts:
    mitelConfCompliances.setStatus("current")
_MitelConfGroups_ObjectIdentity = ObjectIdentity
mitelConfGroups = _MitelConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2)
)
if mibBuilder.loadTexts:
    mitelConfGroups.setStatus("current")
_MitelGrpCommon_ObjectIdentity = ObjectIdentity
mitelGrpCommon = _MitelGrpCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mitelGrpCommon.setStatus("current")
_MitelGrpCs2000_ObjectIdentity = ObjectIdentity
mitelGrpCs2000 = _MitelGrpCs2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 3)
)
if mibBuilder.loadTexts:
    mitelGrpCs2000.setStatus("current")
_MitelGrpIpera3000_ObjectIdentity = ObjectIdentity
mitelGrpIpera3000 = _MitelGrpIpera3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 4)
)
if mibBuilder.loadTexts:
    mitelGrpIpera3000.setStatus("current")
_MitelConfAgents_ObjectIdentity = ObjectIdentity
mitelConfAgents = _MitelConfAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 3)
)
if mibBuilder.loadTexts:
    mitelConfAgents.setStatus("current")

# Managed Objects groups

mitelGrpCmnInterfaces = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 6)
)
mitelGrpCmnInterfaces.setObjects(
      *(("MITEL-MIB", "mitelIfNumber"),
        ("MITEL-MIB", "mitelIfTblType"))
)
if mibBuilder.loadTexts:
    mitelGrpCmnInterfaces.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mitelComplMitel = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1027, 5, 1, 1)
)
mitelComplMitel.setObjects(
    ("MITEL-MIB", "mitelGrpCmnInterfaces")
)
if mibBuilder.loadTexts:
    mitelComplMitel.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-MIB",
    **{"MitelIfType": MitelIfType,
       "MitelNotifyTransportType": MitelNotifyTransportType,
       "mitel": mitel,
       "mitelIdentification": mitelIdentification,
       "mitelIdMgmtPlatforms": mitelIdMgmtPlatforms,
       "mitelIdCallServers": mitelIdCallServers,
       "mitelIdCsMc2": mitelIdCsMc2,
       "mitelIdCs2000Light": mitelIdCs2000Light,
       "mitelIdCsIpera3000": mitelIdCsIpera3000,
       "mitelIdTerminals": mitelIdTerminals,
       "mitelIdInterfaces": mitelIdInterfaces,
       "mitelIdCtiPlatforms": mitelIdCtiPlatforms,
       "mitelIdApplicationPlatforms": mitelIdApplicationPlatforms,
       "mitelExperimental": mitelExperimental,
       "mitelExtensions": mitelExtensions,
       "mitelExtInterfaces": mitelExtInterfaces,
       "mitelIfNumber": mitelIfNumber,
       "mitelIfTable": mitelIfTable,
       "mitelIfTableEntry": mitelIfTableEntry,
       "mitelIfTblType": mitelIfTblType,
       "mitelProprietary": mitelProprietary,
       "mitelPropApplications": mitelPropApplications,
       "mitelAppCallServer": mitelAppCallServer,
       "mitelPropTransmission": mitelPropTransmission,
       "mitelPropProtocols": mitelPropProtocols,
       "mitelPropUtilities": mitelPropUtilities,
       "mitelPropHardware": mitelPropHardware,
       "mitelPropNotifications": mitelPropNotifications,
       "mitelPropReset": mitelPropReset,
       "mitelPropCommon": mitelPropCommon,
       "mitelConformance": mitelConformance,
       "mitelConfCompliances": mitelConfCompliances,
       "mitelComplMitel": mitelComplMitel,
       "mitelConfGroups": mitelConfGroups,
       "mitelGrpCommon": mitelGrpCommon,
       "mitelGrpCmnInterfaces": mitelGrpCmnInterfaces,
       "mitelGrpCs2000": mitelGrpCs2000,
       "mitelGrpIpera3000": mitelGrpIpera3000,
       "mitelConfAgents": mitelConfAgents}
)
