# SNMP MIB module (WISI-GTSETTINGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wisi\WISI-GTSETTINGS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:20 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(gtModule,) = mibBuilder.importSymbols(
    "WISI-GTMODULES-MIB",
    "gtModule")

(gtUnit,) = mibBuilder.importSymbols(
    "WISI-TANGRAM-MIB",
    "gtUnit")


# MODULE-IDENTITY

gtSettingsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5)
)
if mibBuilder.loadTexts:
    gtSettingsMIB.setRevisions(
        ("2016-09-08 00:00",
         "2015-07-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GtSettingsNotifications_ObjectIdentity = ObjectIdentity
gtSettingsNotifications = _GtSettingsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 0)
)
_GtSettingsObjects_ObjectIdentity = ObjectIdentity
gtSettingsObjects = _GtSettingsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1)
)
_GtGeneral_ObjectIdentity = ObjectIdentity
gtGeneral = _GtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1)
)
_GtSWOptionsTable_Object = MibTable
gtSWOptionsTable = _GtSWOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    gtSWOptionsTable.setStatus("current")
_GtSWOptionsEntry_Object = MibTableRow
gtSWOptionsEntry = _GtSWOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 1, 1)
)
gtSWOptionsEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTSETTINGS-MIB", "gtSWOptionsIdx"),
)
if mibBuilder.loadTexts:
    gtSWOptionsEntry.setStatus("current")


class _GtSWOptionsIdx_Type(Unsigned32):
    """Custom type gtSWOptionsIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GtSWOptionsIdx_Type.__name__ = "Unsigned32"
_GtSWOptionsIdx_Object = MibTableColumn
gtSWOptionsIdx = _GtSWOptionsIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 1, 1, 1),
    _GtSWOptionsIdx_Type()
)
gtSWOptionsIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtSWOptionsIdx.setStatus("current")


class _GtSWOption_Type(DisplayString):
    """Custom type gtSWOption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_GtSWOption_Type.__name__ = "DisplayString"
_GtSWOption_Object = MibTableColumn
gtSWOption = _GtSWOption_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 1, 1, 2),
    _GtSWOption_Type()
)
gtSWOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtSWOption.setStatus("current")
_GtSLATable_Object = MibTable
gtSLATable = _GtSLATable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gtSLATable.setStatus("current")
_GtSLAEntry_Object = MibTableRow
gtSLAEntry = _GtSLAEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 2, 1)
)
gtSLAEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
)
if mibBuilder.loadTexts:
    gtSLAEntry.setStatus("current")


class _GtSLARegistered_Type(Integer32):
    """Custom type gtSLARegistered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_GtSLARegistered_Type.__name__ = "Integer32"
_GtSLARegistered_Object = MibTableColumn
gtSLARegistered = _GtSLARegistered_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 2, 1, 1),
    _GtSLARegistered_Type()
)
gtSLARegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtSLARegistered.setStatus("current")


class _GtSLAExpires_Type(DisplayString):
    """Custom type gtSLAExpires based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_GtSLAExpires_Type.__name__ = "DisplayString"
_GtSLAExpires_Object = MibTableColumn
gtSLAExpires = _GtSLAExpires_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 2, 1, 2),
    _GtSLAExpires_Type()
)
gtSLAExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtSLAExpires.setStatus("current")
_GtSyslogTable_Object = MibTable
gtSyslogTable = _GtSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    gtSyslogTable.setStatus("current")
_GtSyslogEntry_Object = MibTableRow
gtSyslogEntry = _GtSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 3, 1)
)
gtSyslogEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
)
if mibBuilder.loadTexts:
    gtSyslogEntry.setStatus("current")


class _GtSyslogState_Type(Integer32):
    """Custom type gtSyslogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtSyslogState_Type.__name__ = "Integer32"
_GtSyslogState_Object = MibTableColumn
gtSyslogState = _GtSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 3, 1, 1),
    _GtSyslogState_Type()
)
gtSyslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtSyslogState.setStatus("current")
_GtSyslogIP_Type = IpAddress
_GtSyslogIP_Object = MibTableColumn
gtSyslogIP = _GtSyslogIP_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 1, 3, 1, 2),
    _GtSyslogIP_Type()
)
gtSyslogIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtSyslogIP.setStatus("current")
_GtSwitch_ObjectIdentity = ObjectIdentity
gtSwitch = _GtSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2)
)
_GtNetworkTable_Object = MibTable
gtNetworkTable = _GtNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gtNetworkTable.setStatus("current")
_GtNetworkEntry_Object = MibTableRow
gtNetworkEntry = _GtNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 1, 1)
)
gtNetworkEntry.setIndexNames(
    (0, "WISI-GTSETTINGS-MIB", "gtNetworkVLAN"),
)
if mibBuilder.loadTexts:
    gtNetworkEntry.setStatus("current")


class _GtNetworkVLAN_Type(Unsigned32):
    """Custom type gtNetworkVLAN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_GtNetworkVLAN_Type.__name__ = "Unsigned32"
_GtNetworkVLAN_Object = MibTableColumn
gtNetworkVLAN = _GtNetworkVLAN_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 1, 1, 1),
    _GtNetworkVLAN_Type()
)
gtNetworkVLAN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtNetworkVLAN.setStatus("current")


class _GtNetworkName_Type(DisplayString):
    """Custom type gtNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_GtNetworkName_Type.__name__ = "DisplayString"
_GtNetworkName_Object = MibTableColumn
gtNetworkName = _GtNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 1, 1, 2),
    _GtNetworkName_Type()
)
gtNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNetworkName.setStatus("current")


class _GtNetworkIGMPQuerierState_Type(Integer32):
    """Custom type gtNetworkIGMPQuerierState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("forced", 1),
          ("auto", 2))
    )


_GtNetworkIGMPQuerierState_Type.__name__ = "Integer32"
_GtNetworkIGMPQuerierState_Object = MibTableColumn
gtNetworkIGMPQuerierState = _GtNetworkIGMPQuerierState_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 1, 1, 3),
    _GtNetworkIGMPQuerierState_Type()
)
gtNetworkIGMPQuerierState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNetworkIGMPQuerierState.setStatus("current")
_GtNetworkIGMPQuerierIP_Type = IpAddress
_GtNetworkIGMPQuerierIP_Object = MibTableColumn
gtNetworkIGMPQuerierIP = _GtNetworkIGMPQuerierIP_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 1, 1, 4),
    _GtNetworkIGMPQuerierIP_Type()
)
gtNetworkIGMPQuerierIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNetworkIGMPQuerierIP.setStatus("current")


class _GtNetworkIGMPSnoopingState_Type(Integer32):
    """Custom type gtNetworkIGMPSnoopingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("blockMulticast", 2))
    )


_GtNetworkIGMPSnoopingState_Type.__name__ = "Integer32"
_GtNetworkIGMPSnoopingState_Object = MibTableColumn
gtNetworkIGMPSnoopingState = _GtNetworkIGMPSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 1, 1, 5),
    _GtNetworkIGMPSnoopingState_Type()
)
gtNetworkIGMPSnoopingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNetworkIGMPSnoopingState.setStatus("current")
_GtNetworkPortsTable_Object = MibTable
gtNetworkPortsTable = _GtNetworkPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gtNetworkPortsTable.setStatus("current")
_GtNetworkPortsEntry_Object = MibTableRow
gtNetworkPortsEntry = _GtNetworkPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 2, 1)
)
gtNetworkPortsEntry.setIndexNames(
    (0, "WISI-GTSETTINGS-MIB", "gtNetworkPortVLAN"),
    (0, "WISI-GTSETTINGS-MIB", "gtNetworkPortNumber"),
)
if mibBuilder.loadTexts:
    gtNetworkPortsEntry.setStatus("current")


class _GtNetworkPortVLAN_Type(Unsigned32):
    """Custom type gtNetworkPortVLAN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_GtNetworkPortVLAN_Type.__name__ = "Unsigned32"
_GtNetworkPortVLAN_Object = MibTableColumn
gtNetworkPortVLAN = _GtNetworkPortVLAN_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 2, 1, 1),
    _GtNetworkPortVLAN_Type()
)
gtNetworkPortVLAN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtNetworkPortVLAN.setStatus("current")


class _GtNetworkPortNumber_Type(Unsigned32):
    """Custom type gtNetworkPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GtNetworkPortNumber_Type.__name__ = "Unsigned32"
_GtNetworkPortNumber_Object = MibTableColumn
gtNetworkPortNumber = _GtNetworkPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 2, 1, 2),
    _GtNetworkPortNumber_Type()
)
gtNetworkPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtNetworkPortNumber.setStatus("current")


class _GtNetworkPortName_Type(DisplayString):
    """Custom type gtNetworkPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_GtNetworkPortName_Type.__name__ = "DisplayString"
_GtNetworkPortName_Object = MibTableColumn
gtNetworkPortName = _GtNetworkPortName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 2, 1, 3),
    _GtNetworkPortName_Type()
)
gtNetworkPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNetworkPortName.setStatus("current")


class _GtNetworkPortState_Type(Integer32):
    """Custom type gtNetworkPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMember", 0),
          ("untagged", 1),
          ("tagged", 2))
    )


_GtNetworkPortState_Type.__name__ = "Integer32"
_GtNetworkPortState_Object = MibTableColumn
gtNetworkPortState = _GtNetworkPortState_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 2, 1, 4),
    _GtNetworkPortState_Type()
)
gtNetworkPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNetworkPortState.setStatus("current")
_GtPortsTable_Object = MibTable
gtPortsTable = _GtPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    gtPortsTable.setStatus("current")
_GtPortsEntry_Object = MibTableRow
gtPortsEntry = _GtPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 3, 1)
)
gtPortsEntry.setIndexNames(
    (0, "WISI-GTSETTINGS-MIB", "gtPortsNumber"),
)
if mibBuilder.loadTexts:
    gtPortsEntry.setStatus("current")


class _GtPortsNumber_Type(Unsigned32):
    """Custom type gtPortsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GtPortsNumber_Type.__name__ = "Unsigned32"
_GtPortsNumber_Object = MibTableColumn
gtPortsNumber = _GtPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 3, 1, 1),
    _GtPortsNumber_Type()
)
gtPortsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtPortsNumber.setStatus("current")


class _GtPortsName_Type(DisplayString):
    """Custom type gtPortsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_GtPortsName_Type.__name__ = "DisplayString"
_GtPortsName_Object = MibTableColumn
gtPortsName = _GtPortsName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 3, 1, 2),
    _GtPortsName_Type()
)
gtPortsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPortsName.setStatus("current")


class _GtPortsFloodMulticast_Type(Integer32):
    """Custom type gtPortsFloodMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtPortsFloodMulticast_Type.__name__ = "Integer32"
_GtPortsFloodMulticast_Object = MibTableColumn
gtPortsFloodMulticast = _GtPortsFloodMulticast_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 3, 1, 3),
    _GtPortsFloodMulticast_Type()
)
gtPortsFloodMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPortsFloodMulticast.setStatus("current")
_GtPortsBitrateReceive_Type = Integer32
_GtPortsBitrateReceive_Object = MibTableColumn
gtPortsBitrateReceive = _GtPortsBitrateReceive_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 3, 1, 4),
    _GtPortsBitrateReceive_Type()
)
gtPortsBitrateReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPortsBitrateReceive.setStatus("current")
_GtPortsBitrateTransmit_Type = Integer32
_GtPortsBitrateTransmit_Object = MibTableColumn
gtPortsBitrateTransmit = _GtPortsBitrateTransmit_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 3, 1, 5),
    _GtPortsBitrateTransmit_Type()
)
gtPortsBitrateTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPortsBitrateTransmit.setStatus("current")


class _GtPortsLinkup_Type(Integer32):
    """Custom type gtPortsLinkup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_GtPortsLinkup_Type.__name__ = "Integer32"
_GtPortsLinkup_Object = MibTableColumn
gtPortsLinkup = _GtPortsLinkup_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 3, 1, 6),
    _GtPortsLinkup_Type()
)
gtPortsLinkup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPortsLinkup.setStatus("current")


class _GtIGMPQuerierVersion_Type(Integer32):
    """Custom type gtIGMPQuerierVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1", 1),
          ("igmpv2", 2))
    )


_GtIGMPQuerierVersion_Type.__name__ = "Integer32"
_GtIGMPQuerierVersion_Object = MibScalar
gtIGMPQuerierVersion = _GtIGMPQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 4),
    _GtIGMPQuerierVersion_Type()
)
gtIGMPQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtIGMPQuerierVersion.setStatus("current")
_GtIGMPQuerierRobustness_Type = Integer32
_GtIGMPQuerierRobustness_Object = MibScalar
gtIGMPQuerierRobustness = _GtIGMPQuerierRobustness_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 5),
    _GtIGMPQuerierRobustness_Type()
)
gtIGMPQuerierRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtIGMPQuerierRobustness.setStatus("current")
_GtIGMPQueryInterval_Type = Integer32
_GtIGMPQueryInterval_Object = MibScalar
gtIGMPQueryInterval = _GtIGMPQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 6),
    _GtIGMPQueryInterval_Type()
)
gtIGMPQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtIGMPQueryInterval.setStatus("current")
_GtIGMPQueryStartupInterval_Type = Integer32
_GtIGMPQueryStartupInterval_Object = MibScalar
gtIGMPQueryStartupInterval = _GtIGMPQueryStartupInterval_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 7),
    _GtIGMPQueryStartupInterval_Type()
)
gtIGMPQueryStartupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtIGMPQueryStartupInterval.setStatus("current")
_GtIGMPQueryStartupCount_Type = Integer32
_GtIGMPQueryStartupCount_Object = MibScalar
gtIGMPQueryStartupCount = _GtIGMPQueryStartupCount_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 8),
    _GtIGMPQueryStartupCount_Type()
)
gtIGMPQueryStartupCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtIGMPQueryStartupCount.setStatus("current")
_GtIGMPLastMemberQueryInterval_Type = Integer32
_GtIGMPLastMemberQueryInterval_Object = MibScalar
gtIGMPLastMemberQueryInterval = _GtIGMPLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 9),
    _GtIGMPLastMemberQueryInterval_Type()
)
gtIGMPLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtIGMPLastMemberQueryInterval.setStatus("current")
_GtIGMPLastMemberQueryCount_Type = Integer32
_GtIGMPLastMemberQueryCount_Object = MibScalar
gtIGMPLastMemberQueryCount = _GtIGMPLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 10),
    _GtIGMPLastMemberQueryCount_Type()
)
gtIGMPLastMemberQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtIGMPLastMemberQueryCount.setStatus("current")
_GtIGMPQuerierResponseTime_Type = Integer32
_GtIGMPQuerierResponseTime_Object = MibScalar
gtIGMPQuerierResponseTime = _GtIGMPQuerierResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 11),
    _GtIGMPQuerierResponseTime_Type()
)
gtIGMPQuerierResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtIGMPQuerierResponseTime.setStatus("current")


class _GtNumSFP_Type(Unsigned32):
    """Custom type gtNumSFP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
    )


_GtNumSFP_Type.__name__ = "Unsigned32"
_GtNumSFP_Object = MibScalar
gtNumSFP = _GtNumSFP_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 12),
    _GtNumSFP_Type()
)
gtNumSFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNumSFP.setStatus("current")
_GtSFPTable_Object = MibTable
gtSFPTable = _GtSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 13)
)
if mibBuilder.loadTexts:
    gtSFPTable.setStatus("current")
_GtSFPEntry_Object = MibTableRow
gtSFPEntry = _GtSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 13, 1)
)
gtSFPEntry.setIndexNames(
    (0, "WISI-GTSETTINGS-MIB", "gtSFPNumber"),
)
if mibBuilder.loadTexts:
    gtSFPEntry.setStatus("current")


class _GtSFPNumber_Type(Unsigned32):
    """Custom type gtSFPNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
    )


_GtSFPNumber_Type.__name__ = "Unsigned32"
_GtSFPNumber_Object = MibTableColumn
gtSFPNumber = _GtSFPNumber_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 13, 1, 1),
    _GtSFPNumber_Type()
)
gtSFPNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtSFPNumber.setStatus("current")


class _GtSFPPlugged_Type(Integer32):
    """Custom type gtSFPPlugged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAttached", 0),
          ("attached", 1))
    )


_GtSFPPlugged_Type.__name__ = "Integer32"
_GtSFPPlugged_Object = MibTableColumn
gtSFPPlugged = _GtSFPPlugged_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 13, 1, 2),
    _GtSFPPlugged_Type()
)
gtSFPPlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtSFPPlugged.setStatus("current")


class _GtSFPLink_Type(Integer32):
    """Custom type gtSFPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_GtSFPLink_Type.__name__ = "Integer32"
_GtSFPLink_Object = MibTableColumn
gtSFPLink = _GtSFPLink_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 13, 1, 3),
    _GtSFPLink_Type()
)
gtSFPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtSFPLink.setStatus("current")


class _GtSFPType_Type(Integer32):
    """Custom type gtSFPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("copper", 0),
          ("fiber", 1))
    )


_GtSFPType_Type.__name__ = "Integer32"
_GtSFPType_Object = MibTableColumn
gtSFPType = _GtSFPType_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 13, 1, 4),
    _GtSFPType_Type()
)
gtSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtSFPType.setStatus("current")


class _GtSFPSpeed_Type(Unsigned32):
    """Custom type gtSFPSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GtSFPSpeed_Type.__name__ = "Unsigned32"
_GtSFPSpeed_Object = MibTableColumn
gtSFPSpeed = _GtSFPSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 2, 13, 1, 5),
    _GtSFPSpeed_Type()
)
gtSFPSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtSFPSpeed.setStatus("current")
if mibBuilder.loadTexts:
    gtSFPSpeed.setUnits("Mbit/s")
_GtNetworking_ObjectIdentity = ObjectIdentity
gtNetworking = _GtNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3)
)
_GtDNSTable_Object = MibTable
gtDNSTable = _GtDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    gtDNSTable.setStatus("current")
_GtDNSEntry_Object = MibTableRow
gtDNSEntry = _GtDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 1, 1)
)
gtDNSEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTSETTINGS-MIB", "gtDNSNumber"),
)
if mibBuilder.loadTexts:
    gtDNSEntry.setStatus("current")


class _GtDNSNumber_Type(Unsigned32):
    """Custom type gtDNSNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GtDNSNumber_Type.__name__ = "Unsigned32"
_GtDNSNumber_Object = MibTableColumn
gtDNSNumber = _GtDNSNumber_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 1, 1, 1),
    _GtDNSNumber_Type()
)
gtDNSNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtDNSNumber.setStatus("current")
if mibBuilder.loadTexts:
    gtDNSNumber.setUnits("slot")
_GtDNSServerIP_Type = IpAddress
_GtDNSServerIP_Object = MibTableColumn
gtDNSServerIP = _GtDNSServerIP_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 1, 1, 2),
    _GtDNSServerIP_Type()
)
gtDNSServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtDNSServerIP.setStatus("current")
_GtInterfaceTable_Object = MibTable
gtInterfaceTable = _GtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gtInterfaceTable.setStatus("current")
_GtInterfaceEntry_Object = MibTableRow
gtInterfaceEntry = _GtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1)
)
gtInterfaceEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTSETTINGS-MIB", "gtInterfaceNumber"),
)
if mibBuilder.loadTexts:
    gtInterfaceEntry.setStatus("current")


class _GtInterfaceNumber_Type(Unsigned32):
    """Custom type gtInterfaceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GtInterfaceNumber_Type.__name__ = "Unsigned32"
_GtInterfaceNumber_Object = MibTableColumn
gtInterfaceNumber = _GtInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 1),
    _GtInterfaceNumber_Type()
)
gtInterfaceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtInterfaceNumber.setStatus("current")


class _GtInterfaceName_Type(DisplayString):
    """Custom type gtInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GtInterfaceName_Type.__name__ = "DisplayString"
_GtInterfaceName_Object = MibTableColumn
gtInterfaceName = _GtInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 2),
    _GtInterfaceName_Type()
)
gtInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceName.setStatus("current")
_GtInterfaceMAC_Type = PhysAddress
_GtInterfaceMAC_Object = MibTableColumn
gtInterfaceMAC = _GtInterfaceMAC_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 3),
    _GtInterfaceMAC_Type()
)
gtInterfaceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtInterfaceMAC.setStatus("current")


class _GtInterfaceState_Type(Integer32):
    """Custom type gtInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_GtInterfaceState_Type.__name__ = "Integer32"
_GtInterfaceState_Object = MibTableColumn
gtInterfaceState = _GtInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 4),
    _GtInterfaceState_Type()
)
gtInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtInterfaceState.setStatus("current")
_GtInterfaceIPv4_Type = IpAddress
_GtInterfaceIPv4_Object = MibTableColumn
gtInterfaceIPv4 = _GtInterfaceIPv4_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 5),
    _GtInterfaceIPv4_Type()
)
gtInterfaceIPv4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceIPv4.setStatus("current")
_GtInterfaceIPv4Mask_Type = IpAddress
_GtInterfaceIPv4Mask_Object = MibTableColumn
gtInterfaceIPv4Mask = _GtInterfaceIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 6),
    _GtInterfaceIPv4Mask_Type()
)
gtInterfaceIPv4Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceIPv4Mask.setStatus("current")
_GtInterfaceIPv4Gateway_Type = IpAddress
_GtInterfaceIPv4Gateway_Object = MibTableColumn
gtInterfaceIPv4Gateway = _GtInterfaceIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 7),
    _GtInterfaceIPv4Gateway_Type()
)
gtInterfaceIPv4Gateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceIPv4Gateway.setStatus("current")


class _GtInterfaceVLAN_Type(Unsigned32):
    """Custom type gtInterfaceVLAN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_GtInterfaceVLAN_Type.__name__ = "Unsigned32"
_GtInterfaceVLAN_Object = MibTableColumn
gtInterfaceVLAN = _GtInterfaceVLAN_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 8),
    _GtInterfaceVLAN_Type()
)
gtInterfaceVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceVLAN.setStatus("current")


class _GtInterfaceIGMP_Type(Integer32):
    """Custom type gtInterfaceIGMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv2", 2),
          ("igmpv3", 3))
    )


_GtInterfaceIGMP_Type.__name__ = "Integer32"
_GtInterfaceIGMP_Object = MibTableColumn
gtInterfaceIGMP = _GtInterfaceIGMP_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 9),
    _GtInterfaceIGMP_Type()
)
gtInterfaceIGMP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceIGMP.setStatus("current")


class _GtInterfaceDHCPState_Type(Integer32):
    """Custom type gtInterfaceDHCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtInterfaceDHCPState_Type.__name__ = "Integer32"
_GtInterfaceDHCPState_Object = MibTableColumn
gtInterfaceDHCPState = _GtInterfaceDHCPState_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 10),
    _GtInterfaceDHCPState_Type()
)
gtInterfaceDHCPState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceDHCPState.setStatus("current")


class _GtInterfaceWebMgt_Type(Integer32):
    """Custom type gtInterfaceWebMgt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtInterfaceWebMgt_Type.__name__ = "Integer32"
_GtInterfaceWebMgt_Object = MibTableColumn
gtInterfaceWebMgt = _GtInterfaceWebMgt_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 11),
    _GtInterfaceWebMgt_Type()
)
gtInterfaceWebMgt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceWebMgt.setStatus("current")


class _GtInterfaceSNMP_Type(Integer32):
    """Custom type gtInterfaceSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtInterfaceSNMP_Type.__name__ = "Integer32"
_GtInterfaceSNMP_Object = MibTableColumn
gtInterfaceSNMP = _GtInterfaceSNMP_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 12),
    _GtInterfaceSNMP_Type()
)
gtInterfaceSNMP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceSNMP.setStatus("current")


class _GtInterfaceSimulcrypt_Type(Integer32):
    """Custom type gtInterfaceSimulcrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtInterfaceSimulcrypt_Type.__name__ = "Integer32"
_GtInterfaceSimulcrypt_Object = MibTableColumn
gtInterfaceSimulcrypt = _GtInterfaceSimulcrypt_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 13),
    _GtInterfaceSimulcrypt_Type()
)
gtInterfaceSimulcrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceSimulcrypt.setStatus("current")


class _GtInterfaceStreaming_Type(Integer32):
    """Custom type gtInterfaceStreaming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtInterfaceStreaming_Type.__name__ = "Integer32"
_GtInterfaceStreaming_Object = MibTableColumn
gtInterfaceStreaming = _GtInterfaceStreaming_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 14),
    _GtInterfaceStreaming_Type()
)
gtInterfaceStreaming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceStreaming.setStatus("current")


class _GtInterfaceCLI_Type(Integer32):
    """Custom type gtInterfaceCLI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtInterfaceCLI_Type.__name__ = "Integer32"
_GtInterfaceCLI_Object = MibTableColumn
gtInterfaceCLI = _GtInterfaceCLI_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 15),
    _GtInterfaceCLI_Type()
)
gtInterfaceCLI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceCLI.setStatus("current")


class _GtInterfaceUseVLAN_Type(Integer32):
    """Custom type gtInterfaceUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtInterfaceUseVLAN_Type.__name__ = "Integer32"
_GtInterfaceUseVLAN_Object = MibTableColumn
gtInterfaceUseVLAN = _GtInterfaceUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 16),
    _GtInterfaceUseVLAN_Type()
)
gtInterfaceUseVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceUseVLAN.setStatus("current")
_GtInterfaceIfIndex_Type = InterfaceIndex
_GtInterfaceIfIndex_Object = MibTableColumn
gtInterfaceIfIndex = _GtInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 17),
    _GtInterfaceIfIndex_Type()
)
gtInterfaceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceIfIndex.setStatus("current")
_GtInterfaceRowStatus_Type = RowStatus
_GtInterfaceRowStatus_Object = MibTableColumn
gtInterfaceRowStatus = _GtInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 3, 2, 1, 18),
    _GtInterfaceRowStatus_Type()
)
gtInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtInterfaceRowStatus.setStatus("current")
_GtHeadendSystemManagement_ObjectIdentity = ObjectIdentity
gtHeadendSystemManagement = _GtHeadendSystemManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 4)
)
_GtHMSTable_Object = MibTable
gtHMSTable = _GtHMSTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    gtHMSTable.setStatus("current")
_GtHMSEntry_Object = MibTableRow
gtHMSEntry = _GtHMSEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 4, 4, 1)
)
gtHMSEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
)
if mibBuilder.loadTexts:
    gtHMSEntry.setStatus("current")


class _GtHMSGroupName_Type(DisplayString):
    """Custom type gtHMSGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GtHMSGroupName_Type.__name__ = "DisplayString"
_GtHMSGroupName_Object = MibTableColumn
gtHMSGroupName = _GtHMSGroupName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 4, 4, 1, 1),
    _GtHMSGroupName_Type()
)
gtHMSGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtHMSGroupName.setStatus("current")


class _GtHMSComMethod_Type(DisplayString):
    """Custom type gtHMSComMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_GtHMSComMethod_Type.__name__ = "DisplayString"
_GtHMSComMethod_Object = MibTableColumn
gtHMSComMethod = _GtHMSComMethod_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 4, 4, 1, 2),
    _GtHMSComMethod_Type()
)
gtHMSComMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtHMSComMethod.setStatus("current")
_GtHMSNumMembers_Type = Integer32
_GtHMSNumMembers_Object = MibTableColumn
gtHMSNumMembers = _GtHMSNumMembers_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 4, 4, 1, 3),
    _GtHMSNumMembers_Type()
)
gtHMSNumMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtHMSNumMembers.setStatus("current")
_GtHMSNumAvailModules_Type = Integer32
_GtHMSNumAvailModules_Object = MibTableColumn
gtHMSNumAvailModules = _GtHMSNumAvailModules_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 4, 4, 1, 4),
    _GtHMSNumAvailModules_Type()
)
gtHMSNumAvailModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtHMSNumAvailModules.setStatus("current")
_GtDateAndTime_ObjectIdentity = ObjectIdentity
gtDateAndTime = _GtDateAndTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5)
)
_GtDateAndTimeTable_Object = MibTable
gtDateAndTimeTable = _GtDateAndTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 1)
)
if mibBuilder.loadTexts:
    gtDateAndTimeTable.setStatus("current")
_GtDateAndTimeEntry_Object = MibTableRow
gtDateAndTimeEntry = _GtDateAndTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 1, 1)
)
gtDateAndTimeEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
)
if mibBuilder.loadTexts:
    gtDateAndTimeEntry.setStatus("current")


class _GtCurrentTimeSource_Type(DisplayString):
    """Custom type gtCurrentTimeSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_GtCurrentTimeSource_Type.__name__ = "DisplayString"
_GtCurrentTimeSource_Object = MibTableColumn
gtCurrentTimeSource = _GtCurrentTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 1, 1, 1),
    _GtCurrentTimeSource_Type()
)
gtCurrentTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtCurrentTimeSource.setStatus("current")


class _GtTimeUTC_Type(DisplayString):
    """Custom type gtTimeUTC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_GtTimeUTC_Type.__name__ = "DisplayString"
_GtTimeUTC_Object = MibTableColumn
gtTimeUTC = _GtTimeUTC_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 1, 1, 2),
    _GtTimeUTC_Type()
)
gtTimeUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtTimeUTC.setStatus("current")


class _GtTimeLocal_Type(DisplayString):
    """Custom type gtTimeLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_GtTimeLocal_Type.__name__ = "DisplayString"
_GtTimeLocal_Object = MibTableColumn
gtTimeLocal = _GtTimeLocal_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 1, 1, 3),
    _GtTimeLocal_Type()
)
gtTimeLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtTimeLocal.setStatus("current")


class _GtTimeZone_Type(DisplayString):
    """Custom type gtTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_GtTimeZone_Type.__name__ = "DisplayString"
_GtTimeZone_Object = MibTableColumn
gtTimeZone = _GtTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 1, 1, 4),
    _GtTimeZone_Type()
)
gtTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtTimeZone.setStatus("current")


class _GtDaylightAdjustment_Type(Integer32):
    """Custom type gtDaylightAdjustment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtDaylightAdjustment_Type.__name__ = "Integer32"
_GtDaylightAdjustment_Object = MibTableColumn
gtDaylightAdjustment = _GtDaylightAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 1, 1, 5),
    _GtDaylightAdjustment_Type()
)
gtDaylightAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtDaylightAdjustment.setStatus("current")
_GtNTPServerTable_Object = MibTable
gtNTPServerTable = _GtNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    gtNTPServerTable.setStatus("current")
_GtNTPServerEntry_Object = MibTableRow
gtNTPServerEntry = _GtNTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 2, 1)
)
gtNTPServerEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTSETTINGS-MIB", "gtNTPServerNumber"),
)
if mibBuilder.loadTexts:
    gtNTPServerEntry.setStatus("current")


class _GtNTPServerNumber_Type(Unsigned32):
    """Custom type gtNTPServerNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GtNTPServerNumber_Type.__name__ = "Unsigned32"
_GtNTPServerNumber_Object = MibTableColumn
gtNTPServerNumber = _GtNTPServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 2, 1, 1),
    _GtNTPServerNumber_Type()
)
gtNTPServerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtNTPServerNumber.setStatus("current")
_GtNTPServerAddress_Type = DisplayString
_GtNTPServerAddress_Object = MibTableColumn
gtNTPServerAddress = _GtNTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 2, 1, 2),
    _GtNTPServerAddress_Type()
)
gtNTPServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtNTPServerAddress.setStatus("current")
_GtNTPServerRowStatus_Type = RowStatus
_GtNTPServerRowStatus_Object = MibTableColumn
gtNTPServerRowStatus = _GtNTPServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 5, 2, 1, 3),
    _GtNTPServerRowStatus_Type()
)
gtNTPServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtNTPServerRowStatus.setStatus("current")
_GtSNMP_ObjectIdentity = ObjectIdentity
gtSNMP = _GtSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6)
)
_GtSNMPTable_Object = MibTable
gtSNMPTable = _GtSNMPTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1)
)
if mibBuilder.loadTexts:
    gtSNMPTable.setStatus("current")
_GtSNMPEntry_Object = MibTableRow
gtSNMPEntry = _GtSNMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1)
)
gtSNMPEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
)
if mibBuilder.loadTexts:
    gtSNMPEntry.setStatus("current")


class _GtAgentState_Type(Integer32):
    """Custom type gtAgentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtAgentState_Type.__name__ = "Integer32"
_GtAgentState_Object = MibTableColumn
gtAgentState = _GtAgentState_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 1),
    _GtAgentState_Type()
)
gtAgentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtAgentState.setStatus("current")


class _GtAgentPort_Type(Unsigned32):
    """Custom type gtAgentPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GtAgentPort_Type.__name__ = "Unsigned32"
_GtAgentPort_Object = MibTableColumn
gtAgentPort = _GtAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 2),
    _GtAgentPort_Type()
)
gtAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtAgentPort.setStatus("current")


class _GtAgentSecurityLevel_Type(Integer32):
    """Custom type gtAgentSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthenticationOrEncryption", 1),
          ("authenticationNoEncryption", 2),
          ("authenticationAndEncryption", 3))
    )


_GtAgentSecurityLevel_Type.__name__ = "Integer32"
_GtAgentSecurityLevel_Object = MibTableColumn
gtAgentSecurityLevel = _GtAgentSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 3),
    _GtAgentSecurityLevel_Type()
)
gtAgentSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtAgentSecurityLevel.setStatus("current")


class _GtAgentComReadString_Type(DisplayString):
    """Custom type gtAgentComReadString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_GtAgentComReadString_Type.__name__ = "DisplayString"
_GtAgentComReadString_Object = MibTableColumn
gtAgentComReadString = _GtAgentComReadString_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 4),
    _GtAgentComReadString_Type()
)
gtAgentComReadString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtAgentComReadString.setStatus("current")


class _GtAgentComWriteString_Type(DisplayString):
    """Custom type gtAgentComWriteString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_GtAgentComWriteString_Type.__name__ = "DisplayString"
_GtAgentComWriteString_Object = MibTableColumn
gtAgentComWriteString = _GtAgentComWriteString_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 5),
    _GtAgentComWriteString_Type()
)
gtAgentComWriteString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtAgentComWriteString.setStatus("current")


class _GtTrapState_Type(Integer32):
    """Custom type gtTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtTrapState_Type.__name__ = "Integer32"
_GtTrapState_Object = MibTableColumn
gtTrapState = _GtTrapState_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 6),
    _GtTrapState_Type()
)
gtTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtTrapState.setStatus("current")


class _GtTrapSNMPVersion_Type(Integer32):
    """Custom type gtTrapSNMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version1", 0),
          ("version2c", 1),
          ("version3", 3))
    )


_GtTrapSNMPVersion_Type.__name__ = "Integer32"
_GtTrapSNMPVersion_Object = MibTableColumn
gtTrapSNMPVersion = _GtTrapSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 7),
    _GtTrapSNMPVersion_Type()
)
gtTrapSNMPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtTrapSNMPVersion.setStatus("current")


class _GtTrapUser_Type(DisplayString):
    """Custom type gtTrapUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_GtTrapUser_Type.__name__ = "DisplayString"
_GtTrapUser_Object = MibTableColumn
gtTrapUser = _GtTrapUser_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 8),
    _GtTrapUser_Type()
)
gtTrapUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtTrapUser.setStatus("current")


class _GtTrapSecurityLevel_Type(Integer32):
    """Custom type gtTrapSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthenticationOrEncryption", 1),
          ("authenticationNoEncryption", 2),
          ("authenticationAndEncryption", 3))
    )


_GtTrapSecurityLevel_Type.__name__ = "Integer32"
_GtTrapSecurityLevel_Object = MibTableColumn
gtTrapSecurityLevel = _GtTrapSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 9),
    _GtTrapSecurityLevel_Type()
)
gtTrapSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtTrapSecurityLevel.setStatus("current")


class _GtTrapComString_Type(DisplayString):
    """Custom type gtTrapComString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_GtTrapComString_Type.__name__ = "DisplayString"
_GtTrapComString_Object = MibTableColumn
gtTrapComString = _GtTrapComString_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 10),
    _GtTrapComString_Type()
)
gtTrapComString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtTrapComString.setStatus("current")


class _GtTrapPDU_Type(Integer32):
    """Custom type gtTrapPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(164,
              166,
              167)
        )
    )
    namedValues = NamedValues(
        *(("v1Trap", 164),
          ("inform", 166),
          ("v2Trap", 167))
    )


_GtTrapPDU_Type.__name__ = "Integer32"
_GtTrapPDU_Object = MibTableColumn
gtTrapPDU = _GtTrapPDU_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 1, 1, 11),
    _GtTrapPDU_Type()
)
gtTrapPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtTrapPDU.setStatus("current")
_GtTrapDestTable_Object = MibTable
gtTrapDestTable = _GtTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 2)
)
if mibBuilder.loadTexts:
    gtTrapDestTable.setStatus("current")
_GtTrapDestEntry_Object = MibTableRow
gtTrapDestEntry = _GtTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 2, 1)
)
gtTrapDestEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTSETTINGS-MIB", "gtTrapDestNumber"),
)
if mibBuilder.loadTexts:
    gtTrapDestEntry.setStatus("current")


class _GtTrapDestNumber_Type(Unsigned32):
    """Custom type gtTrapDestNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GtTrapDestNumber_Type.__name__ = "Unsigned32"
_GtTrapDestNumber_Object = MibTableColumn
gtTrapDestNumber = _GtTrapDestNumber_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 2, 1, 1),
    _GtTrapDestNumber_Type()
)
gtTrapDestNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtTrapDestNumber.setStatus("current")
_GtTrapDestIP_Type = IpAddress
_GtTrapDestIP_Object = MibTableColumn
gtTrapDestIP = _GtTrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 2, 1, 2),
    _GtTrapDestIP_Type()
)
gtTrapDestIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtTrapDestIP.setStatus("current")


class _GtTrapDestPort_Type(Unsigned32):
    """Custom type gtTrapDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GtTrapDestPort_Type.__name__ = "Unsigned32"
_GtTrapDestPort_Object = MibTableColumn
gtTrapDestPort = _GtTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 2, 1, 3),
    _GtTrapDestPort_Type()
)
gtTrapDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtTrapDestPort.setStatus("current")
_GtTrapDestRowStatus_Type = RowStatus
_GtTrapDestRowStatus_Object = MibTableColumn
gtTrapDestRowStatus = _GtTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 6, 2, 1, 4),
    _GtTrapDestRowStatus_Type()
)
gtTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtTrapDestRowStatus.setStatus("current")
_GtUser_ObjectIdentity = ObjectIdentity
gtUser = _GtUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7)
)
_GtUserTable_Object = MibTable
gtUserTable = _GtUserTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 1)
)
if mibBuilder.loadTexts:
    gtUserTable.setStatus("current")
_GtUserEntry_Object = MibTableRow
gtUserEntry = _GtUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 1, 1)
)
gtUserEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTSETTINGS-MIB", "gtUserIdx"),
    (0, "WISI-GTSETTINGS-MIB", "gtUserParamIdx"),
)
if mibBuilder.loadTexts:
    gtUserEntry.setStatus("current")
_GtUserIdx_Type = Unsigned32
_GtUserIdx_Object = MibTableColumn
gtUserIdx = _GtUserIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 1, 1, 1),
    _GtUserIdx_Type()
)
gtUserIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtUserIdx.setStatus("current")
_GtUserParamIdx_Type = Unsigned32
_GtUserParamIdx_Object = MibTableColumn
gtUserParamIdx = _GtUserParamIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 1, 1, 2),
    _GtUserParamIdx_Type()
)
gtUserParamIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtUserParamIdx.setStatus("current")


class _GtUserName_Type(DisplayString):
    """Custom type gtUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_GtUserName_Type.__name__ = "DisplayString"
_GtUserName_Object = MibTableColumn
gtUserName = _GtUserName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 1, 1, 3),
    _GtUserName_Type()
)
gtUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtUserName.setStatus("current")


class _GtUserPassword_Type(DisplayString):
    """Custom type gtUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_GtUserPassword_Type.__name__ = "DisplayString"
_GtUserPassword_Object = MibTableColumn
gtUserPassword = _GtUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 1, 1, 4),
    _GtUserPassword_Type()
)
gtUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtUserPassword.setStatus("current")
_GtUserGroup_Type = Integer32
_GtUserGroup_Object = MibTableColumn
gtUserGroup = _GtUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 1, 1, 5),
    _GtUserGroup_Type()
)
gtUserGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtUserGroup.setStatus("current")
_GtUserAccesslist_Type = Integer32
_GtUserAccesslist_Object = MibTableColumn
gtUserAccesslist = _GtUserAccesslist_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 1, 1, 6),
    _GtUserAccesslist_Type()
)
gtUserAccesslist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtUserAccesslist.setStatus("current")
_GtUserRowStatus_Type = RowStatus
_GtUserRowStatus_Object = MibTableColumn
gtUserRowStatus = _GtUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 1, 1, 7),
    _GtUserRowStatus_Type()
)
gtUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gtUserRowStatus.setStatus("current")
_GtGroupTable_Object = MibTable
gtGroupTable = _GtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 2)
)
if mibBuilder.loadTexts:
    gtGroupTable.setStatus("current")
_GtGroupEntry_Object = MibTableRow
gtGroupEntry = _GtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 2, 1)
)
gtGroupEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTSETTINGS-MIB", "gtGroupIdx"),
    (0, "WISI-GTSETTINGS-MIB", "gtGroupParamIdx"),
)
if mibBuilder.loadTexts:
    gtGroupEntry.setStatus("current")
_GtGroupIdx_Type = Unsigned32
_GtGroupIdx_Object = MibTableColumn
gtGroupIdx = _GtGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 2, 1, 1),
    _GtGroupIdx_Type()
)
gtGroupIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtGroupIdx.setStatus("current")
_GtGroupParamIdx_Type = Unsigned32
_GtGroupParamIdx_Object = MibTableColumn
gtGroupParamIdx = _GtGroupParamIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 2, 1, 2),
    _GtGroupParamIdx_Type()
)
gtGroupParamIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtGroupParamIdx.setStatus("current")


class _GtGroupName_Type(DisplayString):
    """Custom type gtGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_GtGroupName_Type.__name__ = "DisplayString"
_GtGroupName_Object = MibTableColumn
gtGroupName = _GtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 2, 1, 3),
    _GtGroupName_Type()
)
gtGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtGroupName.setStatus("current")
_GtGroupRights_Type = Integer32
_GtGroupRights_Object = MibTableColumn
gtGroupRights = _GtGroupRights_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 2, 1, 4),
    _GtGroupRights_Type()
)
gtGroupRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtGroupRights.setStatus("current")
_GtGroupAccesslist_Type = Integer32
_GtGroupAccesslist_Object = MibTableColumn
gtGroupAccesslist = _GtGroupAccesslist_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 2, 1, 5),
    _GtGroupAccesslist_Type()
)
gtGroupAccesslist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtGroupAccesslist.setStatus("current")
_GtAccesslistTable_Object = MibTable
gtAccesslistTable = _GtAccesslistTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 3)
)
if mibBuilder.loadTexts:
    gtAccesslistTable.setStatus("current")
_GtAccesslistEntry_Object = MibTableRow
gtAccesslistEntry = _GtAccesslistEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 3, 1)
)
gtAccesslistEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTSETTINGS-MIB", "gtAccesslistIdx"),
    (0, "WISI-GTSETTINGS-MIB", "gtAccesslistParamIdx"),
)
if mibBuilder.loadTexts:
    gtAccesslistEntry.setStatus("current")
_GtAccesslistIdx_Type = Unsigned32
_GtAccesslistIdx_Object = MibTableColumn
gtAccesslistIdx = _GtAccesslistIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 3, 1, 1),
    _GtAccesslistIdx_Type()
)
gtAccesslistIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtAccesslistIdx.setStatus("current")
_GtAccesslistParamIdx_Type = Unsigned32
_GtAccesslistParamIdx_Object = MibTableColumn
gtAccesslistParamIdx = _GtAccesslistParamIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 3, 1, 2),
    _GtAccesslistParamIdx_Type()
)
gtAccesslistParamIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtAccesslistParamIdx.setStatus("current")


class _GtAccesslistName_Type(DisplayString):
    """Custom type gtAccesslistName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_GtAccesslistName_Type.__name__ = "DisplayString"
_GtAccesslistName_Object = MibTableColumn
gtAccesslistName = _GtAccesslistName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 3, 1, 3),
    _GtAccesslistName_Type()
)
gtAccesslistName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtAccesslistName.setStatus("current")


class _GtAccesslistIPRange_Type(DisplayString):
    """Custom type gtAccesslistIPRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_GtAccesslistIPRange_Type.__name__ = "DisplayString"
_GtAccesslistIPRange_Object = MibTableColumn
gtAccesslistIPRange = _GtAccesslistIPRange_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 3, 1, 4),
    _GtAccesslistIPRange_Type()
)
gtAccesslistIPRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtAccesslistIPRange.setStatus("current")


class _GtCurrentUserName_Type(DisplayString):
    """Custom type gtCurrentUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_GtCurrentUserName_Type.__name__ = "DisplayString"
_GtCurrentUserName_Object = MibScalar
gtCurrentUserName = _GtCurrentUserName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 4),
    _GtCurrentUserName_Type()
)
gtCurrentUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtCurrentUserName.setStatus("current")


class _GtCurrentUserPassword_Type(DisplayString):
    """Custom type gtCurrentUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_GtCurrentUserPassword_Type.__name__ = "DisplayString"
_GtCurrentUserPassword_Object = MibScalar
gtCurrentUserPassword = _GtCurrentUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 5),
    _GtCurrentUserPassword_Type()
)
gtCurrentUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtCurrentUserPassword.setStatus("current")
_GtUserAuthTable_Object = MibTable
gtUserAuthTable = _GtUserAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 6)
)
if mibBuilder.loadTexts:
    gtUserAuthTable.setStatus("current")
_GtUserAuthEntry_Object = MibTableRow
gtUserAuthEntry = _GtUserAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 6, 1)
)
gtUserAuthEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
)
if mibBuilder.loadTexts:
    gtUserAuthEntry.setStatus("current")


class _GtUserAuthEnabled_Type(Integer32):
    """Custom type gtUserAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtUserAuthEnabled_Type.__name__ = "Integer32"
_GtUserAuthEnabled_Object = MibTableColumn
gtUserAuthEnabled = _GtUserAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 7, 6, 1, 1),
    _GtUserAuthEnabled_Type()
)
gtUserAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtUserAuthEnabled.setStatus("current")
_GtServices_ObjectIdentity = ObjectIdentity
gtServices = _GtServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 8)
)
_GtServicesTable_Object = MibTable
gtServicesTable = _GtServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 8, 1)
)
if mibBuilder.loadTexts:
    gtServicesTable.setStatus("current")
_GtServicesEntry_Object = MibTableRow
gtServicesEntry = _GtServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 8, 1, 1)
)
gtServicesEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
)
if mibBuilder.loadTexts:
    gtServicesEntry.setStatus("current")


class _GtWebEnable_Type(Integer32):
    """Custom type gtWebEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtWebEnable_Type.__name__ = "Integer32"
_GtWebEnable_Object = MibTableColumn
gtWebEnable = _GtWebEnable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 8, 1, 1, 1),
    _GtWebEnable_Type()
)
gtWebEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtWebEnable.setStatus("current")


class _GtWebAuth_Type(Integer32):
    """Custom type gtWebAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtWebAuth_Type.__name__ = "Integer32"
_GtWebAuth_Object = MibTableColumn
gtWebAuth = _GtWebAuth_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 8, 1, 1, 2),
    _GtWebAuth_Type()
)
gtWebAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtWebAuth.setStatus("current")


class _GtWebProtocol_Type(Integer32):
    """Custom type gtWebProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("http", 0),
          ("https", 1))
    )


_GtWebProtocol_Type.__name__ = "Integer32"
_GtWebProtocol_Object = MibTableColumn
gtWebProtocol = _GtWebProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 8, 1, 1, 3),
    _GtWebProtocol_Type()
)
gtWebProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtWebProtocol.setStatus("current")
_GtModuleBackup_ObjectIdentity = ObjectIdentity
gtModuleBackup = _GtModuleBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9)
)


class _GtChassisRedundancy_Type(Integer32):
    """Custom type gtChassisRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtChassisRedundancy_Type.__name__ = "Integer32"
_GtChassisRedundancy_Object = MibScalar
gtChassisRedundancy = _GtChassisRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 1),
    _GtChassisRedundancy_Type()
)
gtChassisRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtChassisRedundancy.setStatus("current")
_GtModuleBackupTable_Object = MibTable
gtModuleBackupTable = _GtModuleBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 2)
)
if mibBuilder.loadTexts:
    gtModuleBackupTable.setStatus("current")
_GtModuleBackupEntry_Object = MibTableRow
gtModuleBackupEntry = _GtModuleBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 2, 1)
)
gtModuleBackupEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
)
if mibBuilder.loadTexts:
    gtModuleBackupEntry.setStatus("current")


class _GtModuleBackupDate_Type(DisplayString):
    """Custom type gtModuleBackupDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )
    fixed_length = 30


_GtModuleBackupDate_Type.__name__ = "DisplayString"
_GtModuleBackupDate_Object = MibTableColumn
gtModuleBackupDate = _GtModuleBackupDate_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 2, 1, 1),
    _GtModuleBackupDate_Type()
)
gtModuleBackupDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleBackupDate.setStatus("current")
_GtModuleRedundancyGroup_Type = Integer32
_GtModuleRedundancyGroup_Object = MibTableColumn
gtModuleRedundancyGroup = _GtModuleRedundancyGroup_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 2, 1, 2),
    _GtModuleRedundancyGroup_Type()
)
gtModuleRedundancyGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtModuleRedundancyGroup.setStatus("current")


class _GtModuleRedundancyMode_Type(Integer32):
    """Custom type gtModuleRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("operational", 1),
          ("backup", 2))
    )


_GtModuleRedundancyMode_Type.__name__ = "Integer32"
_GtModuleRedundancyMode_Object = MibTableColumn
gtModuleRedundancyMode = _GtModuleRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 2, 1, 3),
    _GtModuleRedundancyMode_Type()
)
gtModuleRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtModuleRedundancyMode.setStatus("current")


class _GtModuleBackupControl_Type(Integer32):
    """Custom type gtModuleBackupControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("backup", 1),
          ("restore", 2),
          ("factoryReset", 3),
          ("downloadBackup", 4),
          ("uploadBackup", 5))
    )


_GtModuleBackupControl_Type.__name__ = "Integer32"
_GtModuleBackupControl_Object = MibTableColumn
gtModuleBackupControl = _GtModuleBackupControl_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 2, 1, 4),
    _GtModuleBackupControl_Type()
)
gtModuleBackupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtModuleBackupControl.setStatus("current")


class _GtModuleBackupStatus_Type(Integer32):
    """Custom type gtModuleBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("commandRunning", 1),
          ("commandSucceeded", 2),
          ("commandFailed", 3))
    )


_GtModuleBackupStatus_Type.__name__ = "Integer32"
_GtModuleBackupStatus_Object = MibTableColumn
gtModuleBackupStatus = _GtModuleBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 2, 1, 5),
    _GtModuleBackupStatus_Type()
)
gtModuleBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleBackupStatus.setStatus("current")


class _GtBackupControl_Type(Integer32):
    """Custom type gtBackupControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadPrivateKey", 1),
          ("createBackup", 2),
          ("deletePrivateKey", 3))
    )


_GtBackupControl_Type.__name__ = "Integer32"
_GtBackupControl_Object = MibScalar
gtBackupControl = _GtBackupControl_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 3),
    _GtBackupControl_Type()
)
gtBackupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtBackupControl.setStatus("current")


class _GtBackupStatus_Type(Integer32):
    """Custom type gtBackupStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("downloading", 1),
          ("downloadSuccessful", 2),
          ("downloadFailed", 3),
          ("createBackups", 4),
          ("uploading", 5),
          ("uploadSuccessful", 6),
          ("uploadFailed", 7),
          ("deletePrivateKeySuccessful", 8),
          ("deletePrivateKeyFailed", 9))
    )


_GtBackupStatus_Type.__name__ = "Integer32"
_GtBackupStatus_Object = MibScalar
gtBackupStatus = _GtBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 4),
    _GtBackupStatus_Type()
)
gtBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtBackupStatus.setStatus("current")


class _GtBackupPrivateKeyFilename_Type(DisplayString):
    """Custom type gtBackupPrivateKeyFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GtBackupPrivateKeyFilename_Type.__name__ = "DisplayString"
_GtBackupPrivateKeyFilename_Object = MibScalar
gtBackupPrivateKeyFilename = _GtBackupPrivateKeyFilename_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 5),
    _GtBackupPrivateKeyFilename_Type()
)
gtBackupPrivateKeyFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtBackupPrivateKeyFilename.setStatus("current")


class _GtBackupSFTPServer_Type(DisplayString):
    """Custom type gtBackupSFTPServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GtBackupSFTPServer_Type.__name__ = "DisplayString"
_GtBackupSFTPServer_Object = MibScalar
gtBackupSFTPServer = _GtBackupSFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 6),
    _GtBackupSFTPServer_Type()
)
gtBackupSFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtBackupSFTPServer.setStatus("current")


class _GtBackupSFTPPort_Type(Unsigned32):
    """Custom type gtBackupSFTPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GtBackupSFTPPort_Type.__name__ = "Unsigned32"
_GtBackupSFTPPort_Object = MibScalar
gtBackupSFTPPort = _GtBackupSFTPPort_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 7),
    _GtBackupSFTPPort_Type()
)
gtBackupSFTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtBackupSFTPPort.setStatus("current")


class _GtBackupSFTPUsername_Type(DisplayString):
    """Custom type gtBackupSFTPUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GtBackupSFTPUsername_Type.__name__ = "DisplayString"
_GtBackupSFTPUsername_Object = MibScalar
gtBackupSFTPUsername = _GtBackupSFTPUsername_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 8),
    _GtBackupSFTPUsername_Type()
)
gtBackupSFTPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtBackupSFTPUsername.setStatus("current")


class _GtBackupSFTPPassword_Type(DisplayString):
    """Custom type gtBackupSFTPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GtBackupSFTPPassword_Type.__name__ = "DisplayString"
_GtBackupSFTPPassword_Object = MibScalar
gtBackupSFTPPassword = _GtBackupSFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 9),
    _GtBackupSFTPPassword_Type()
)
gtBackupSFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtBackupSFTPPassword.setStatus("current")


class _GtBackupSFTPHostPublicKeyMD5_Type(DisplayString):
    """Custom type gtBackupSFTPHostPublicKeyMD5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_GtBackupSFTPHostPublicKeyMD5_Type.__name__ = "DisplayString"
_GtBackupSFTPHostPublicKeyMD5_Object = MibScalar
gtBackupSFTPHostPublicKeyMD5 = _GtBackupSFTPHostPublicKeyMD5_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 10),
    _GtBackupSFTPHostPublicKeyMD5_Type()
)
gtBackupSFTPHostPublicKeyMD5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtBackupSFTPHostPublicKeyMD5.setStatus("current")
_GtBackupSFTPFilename_Type = DisplayString
_GtBackupSFTPFilename_Object = MibScalar
gtBackupSFTPFilename = _GtBackupSFTPFilename_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 9, 11),
    _GtBackupSFTPFilename_Type()
)
gtBackupSFTPFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtBackupSFTPFilename.setStatus("current")
_GtModuleUpdate_ObjectIdentity = ObjectIdentity
gtModuleUpdate = _GtModuleUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10)
)


class _GtUpdateControl_Type(Integer32):
    """Custom type gtUpdateControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("downloadFirmware", 1),
          ("updateModules", 2),
          ("updateSwitch", 3),
          ("deleteAllFirmwareFiles", 4),
          ("deletePrivateKey", 5),
          ("updateEntitlements", 6))
    )


_GtUpdateControl_Type.__name__ = "Integer32"
_GtUpdateControl_Object = MibScalar
gtUpdateControl = _GtUpdateControl_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 1),
    _GtUpdateControl_Type()
)
gtUpdateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtUpdateControl.setStatus("current")


class _GtUpdateStatus_Type(Integer32):
    """Custom type gtUpdateStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("downloading", 1),
          ("downloadSuccessful", 2),
          ("downloadFailed", 3),
          ("updating", 4),
          ("updateSuccessful", 5),
          ("updateFailed", 6),
          ("deleteAllFirmwareFilesSuccessful", 7),
          ("deleteAllFirmwareFilesFailed", 8),
          ("deletePrivateKeySuccessful", 9),
          ("deletePrivateKeyFailed", 10))
    )


_GtUpdateStatus_Type.__name__ = "Integer32"
_GtUpdateStatus_Object = MibScalar
gtUpdateStatus = _GtUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 2),
    _GtUpdateStatus_Type()
)
gtUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtUpdateStatus.setStatus("current")


class _GtFilename_Type(DisplayString):
    """Custom type gtFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GtFilename_Type.__name__ = "DisplayString"
_GtFilename_Object = MibScalar
gtFilename = _GtFilename_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 3),
    _GtFilename_Type()
)
gtFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtFilename.setStatus("current")


class _GtSFTPServer_Type(DisplayString):
    """Custom type gtSFTPServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GtSFTPServer_Type.__name__ = "DisplayString"
_GtSFTPServer_Object = MibScalar
gtSFTPServer = _GtSFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 4),
    _GtSFTPServer_Type()
)
gtSFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtSFTPServer.setStatus("current")


class _GtSFTPPort_Type(Unsigned32):
    """Custom type gtSFTPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GtSFTPPort_Type.__name__ = "Unsigned32"
_GtSFTPPort_Object = MibScalar
gtSFTPPort = _GtSFTPPort_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 5),
    _GtSFTPPort_Type()
)
gtSFTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtSFTPPort.setStatus("current")


class _GtSFTPUsername_Type(DisplayString):
    """Custom type gtSFTPUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GtSFTPUsername_Type.__name__ = "DisplayString"
_GtSFTPUsername_Object = MibScalar
gtSFTPUsername = _GtSFTPUsername_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 6),
    _GtSFTPUsername_Type()
)
gtSFTPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtSFTPUsername.setStatus("current")


class _GtSFTPPassword_Type(DisplayString):
    """Custom type gtSFTPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GtSFTPPassword_Type.__name__ = "DisplayString"
_GtSFTPPassword_Object = MibScalar
gtSFTPPassword = _GtSFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 7),
    _GtSFTPPassword_Type()
)
gtSFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtSFTPPassword.setStatus("current")


class _GtSFTPHostPublicKeyMD5_Type(DisplayString):
    """Custom type gtSFTPHostPublicKeyMD5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_GtSFTPHostPublicKeyMD5_Type.__name__ = "DisplayString"
_GtSFTPHostPublicKeyMD5_Object = MibScalar
gtSFTPHostPublicKeyMD5 = _GtSFTPHostPublicKeyMD5_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 8),
    _GtSFTPHostPublicKeyMD5_Type()
)
gtSFTPHostPublicKeyMD5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtSFTPHostPublicKeyMD5.setStatus("current")
_GtUpdateFilesTable_Object = MibTable
gtUpdateFilesTable = _GtUpdateFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 9)
)
if mibBuilder.loadTexts:
    gtUpdateFilesTable.setStatus("current")
_GtUpdateFilesEntry_Object = MibTableRow
gtUpdateFilesEntry = _GtUpdateFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 9, 1)
)
gtUpdateFilesEntry.setIndexNames(
    (0, "WISI-GTSETTINGS-MIB", "gtUpdateFilesTableIdx"),
)
if mibBuilder.loadTexts:
    gtUpdateFilesEntry.setStatus("current")


class _GtUpdateFilesTableIdx_Type(Unsigned32):
    """Custom type gtUpdateFilesTableIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GtUpdateFilesTableIdx_Type.__name__ = "Unsigned32"
_GtUpdateFilesTableIdx_Object = MibTableColumn
gtUpdateFilesTableIdx = _GtUpdateFilesTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 9, 1, 1),
    _GtUpdateFilesTableIdx_Type()
)
gtUpdateFilesTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtUpdateFilesTableIdx.setStatus("current")


class _GtUpdateFile_Type(DisplayString):
    """Custom type gtUpdateFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GtUpdateFile_Type.__name__ = "DisplayString"
_GtUpdateFile_Object = MibTableColumn
gtUpdateFile = _GtUpdateFile_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 1, 10, 9, 1, 2),
    _GtUpdateFile_Type()
)
gtUpdateFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtUpdateFile.setStatus("current")
_GtSettingsConformance_ObjectIdentity = ObjectIdentity
gtSettingsConformance = _GtSettingsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 2)
)
_GtSettingsCompliances_ObjectIdentity = ObjectIdentity
gtSettingsCompliances = _GtSettingsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 2, 1)
)
_GtSettingsGroups_ObjectIdentity = ObjectIdentity
gtSettingsGroups = _GtSettingsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 2, 2)
)

# Managed Objects groups


# Notification objects

gtSettingsNotifyWebChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 0, 1)
)
gtSettingsNotifyWebChanged.setObjects(
      *(("WISI-GTSETTINGS-MIB", "gtWebEnable"),
        ("WISI-GTSETTINGS-MIB", "gtWebAuth"),
        ("WISI-GTSETTINGS-MIB", "gtWebProtocol"))
)
if mibBuilder.loadTexts:
    gtSettingsNotifyWebChanged.setStatus(
        "current"
    )

gtSettingsNotifyInterfaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 5, 0, 2)
)
gtSettingsNotifyInterfaceChanged.setObjects(
      *(("WISI-GTSETTINGS-MIB", "gtInterfaceName"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceVLAN"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceIPv4"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceIPv4Mask"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceIPv4Gateway"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceVLAN"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceIGMP"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceDHCPState"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceWebMgt"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceSNMP"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceSimulcrypt"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceStreaming"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceCLI"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceUseVLAN"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceIfIndex"),
        ("WISI-GTSETTINGS-MIB", "gtInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    gtSettingsNotifyInterfaceChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WISI-GTSETTINGS-MIB",
    **{"gtSettingsMIB": gtSettingsMIB,
       "gtSettingsNotifications": gtSettingsNotifications,
       "gtSettingsNotifyWebChanged": gtSettingsNotifyWebChanged,
       "gtSettingsNotifyInterfaceChanged": gtSettingsNotifyInterfaceChanged,
       "gtSettingsObjects": gtSettingsObjects,
       "gtGeneral": gtGeneral,
       "gtSWOptionsTable": gtSWOptionsTable,
       "gtSWOptionsEntry": gtSWOptionsEntry,
       "gtSWOptionsIdx": gtSWOptionsIdx,
       "gtSWOption": gtSWOption,
       "gtSLATable": gtSLATable,
       "gtSLAEntry": gtSLAEntry,
       "gtSLARegistered": gtSLARegistered,
       "gtSLAExpires": gtSLAExpires,
       "gtSyslogTable": gtSyslogTable,
       "gtSyslogEntry": gtSyslogEntry,
       "gtSyslogState": gtSyslogState,
       "gtSyslogIP": gtSyslogIP,
       "gtSwitch": gtSwitch,
       "gtNetworkTable": gtNetworkTable,
       "gtNetworkEntry": gtNetworkEntry,
       "gtNetworkVLAN": gtNetworkVLAN,
       "gtNetworkName": gtNetworkName,
       "gtNetworkIGMPQuerierState": gtNetworkIGMPQuerierState,
       "gtNetworkIGMPQuerierIP": gtNetworkIGMPQuerierIP,
       "gtNetworkIGMPSnoopingState": gtNetworkIGMPSnoopingState,
       "gtNetworkPortsTable": gtNetworkPortsTable,
       "gtNetworkPortsEntry": gtNetworkPortsEntry,
       "gtNetworkPortVLAN": gtNetworkPortVLAN,
       "gtNetworkPortNumber": gtNetworkPortNumber,
       "gtNetworkPortName": gtNetworkPortName,
       "gtNetworkPortState": gtNetworkPortState,
       "gtPortsTable": gtPortsTable,
       "gtPortsEntry": gtPortsEntry,
       "gtPortsNumber": gtPortsNumber,
       "gtPortsName": gtPortsName,
       "gtPortsFloodMulticast": gtPortsFloodMulticast,
       "gtPortsBitrateReceive": gtPortsBitrateReceive,
       "gtPortsBitrateTransmit": gtPortsBitrateTransmit,
       "gtPortsLinkup": gtPortsLinkup,
       "gtIGMPQuerierVersion": gtIGMPQuerierVersion,
       "gtIGMPQuerierRobustness": gtIGMPQuerierRobustness,
       "gtIGMPQueryInterval": gtIGMPQueryInterval,
       "gtIGMPQueryStartupInterval": gtIGMPQueryStartupInterval,
       "gtIGMPQueryStartupCount": gtIGMPQueryStartupCount,
       "gtIGMPLastMemberQueryInterval": gtIGMPLastMemberQueryInterval,
       "gtIGMPLastMemberQueryCount": gtIGMPLastMemberQueryCount,
       "gtIGMPQuerierResponseTime": gtIGMPQuerierResponseTime,
       "gtNumSFP": gtNumSFP,
       "gtSFPTable": gtSFPTable,
       "gtSFPEntry": gtSFPEntry,
       "gtSFPNumber": gtSFPNumber,
       "gtSFPPlugged": gtSFPPlugged,
       "gtSFPLink": gtSFPLink,
       "gtSFPType": gtSFPType,
       "gtSFPSpeed": gtSFPSpeed,
       "gtNetworking": gtNetworking,
       "gtDNSTable": gtDNSTable,
       "gtDNSEntry": gtDNSEntry,
       "gtDNSNumber": gtDNSNumber,
       "gtDNSServerIP": gtDNSServerIP,
       "gtInterfaceTable": gtInterfaceTable,
       "gtInterfaceEntry": gtInterfaceEntry,
       "gtInterfaceNumber": gtInterfaceNumber,
       "gtInterfaceName": gtInterfaceName,
       "gtInterfaceMAC": gtInterfaceMAC,
       "gtInterfaceState": gtInterfaceState,
       "gtInterfaceIPv4": gtInterfaceIPv4,
       "gtInterfaceIPv4Mask": gtInterfaceIPv4Mask,
       "gtInterfaceIPv4Gateway": gtInterfaceIPv4Gateway,
       "gtInterfaceVLAN": gtInterfaceVLAN,
       "gtInterfaceIGMP": gtInterfaceIGMP,
       "gtInterfaceDHCPState": gtInterfaceDHCPState,
       "gtInterfaceWebMgt": gtInterfaceWebMgt,
       "gtInterfaceSNMP": gtInterfaceSNMP,
       "gtInterfaceSimulcrypt": gtInterfaceSimulcrypt,
       "gtInterfaceStreaming": gtInterfaceStreaming,
       "gtInterfaceCLI": gtInterfaceCLI,
       "gtInterfaceUseVLAN": gtInterfaceUseVLAN,
       "gtInterfaceIfIndex": gtInterfaceIfIndex,
       "gtInterfaceRowStatus": gtInterfaceRowStatus,
       "gtHeadendSystemManagement": gtHeadendSystemManagement,
       "gtHMSTable": gtHMSTable,
       "gtHMSEntry": gtHMSEntry,
       "gtHMSGroupName": gtHMSGroupName,
       "gtHMSComMethod": gtHMSComMethod,
       "gtHMSNumMembers": gtHMSNumMembers,
       "gtHMSNumAvailModules": gtHMSNumAvailModules,
       "gtDateAndTime": gtDateAndTime,
       "gtDateAndTimeTable": gtDateAndTimeTable,
       "gtDateAndTimeEntry": gtDateAndTimeEntry,
       "gtCurrentTimeSource": gtCurrentTimeSource,
       "gtTimeUTC": gtTimeUTC,
       "gtTimeLocal": gtTimeLocal,
       "gtTimeZone": gtTimeZone,
       "gtDaylightAdjustment": gtDaylightAdjustment,
       "gtNTPServerTable": gtNTPServerTable,
       "gtNTPServerEntry": gtNTPServerEntry,
       "gtNTPServerNumber": gtNTPServerNumber,
       "gtNTPServerAddress": gtNTPServerAddress,
       "gtNTPServerRowStatus": gtNTPServerRowStatus,
       "gtSNMP": gtSNMP,
       "gtSNMPTable": gtSNMPTable,
       "gtSNMPEntry": gtSNMPEntry,
       "gtAgentState": gtAgentState,
       "gtAgentPort": gtAgentPort,
       "gtAgentSecurityLevel": gtAgentSecurityLevel,
       "gtAgentComReadString": gtAgentComReadString,
       "gtAgentComWriteString": gtAgentComWriteString,
       "gtTrapState": gtTrapState,
       "gtTrapSNMPVersion": gtTrapSNMPVersion,
       "gtTrapUser": gtTrapUser,
       "gtTrapSecurityLevel": gtTrapSecurityLevel,
       "gtTrapComString": gtTrapComString,
       "gtTrapPDU": gtTrapPDU,
       "gtTrapDestTable": gtTrapDestTable,
       "gtTrapDestEntry": gtTrapDestEntry,
       "gtTrapDestNumber": gtTrapDestNumber,
       "gtTrapDestIP": gtTrapDestIP,
       "gtTrapDestPort": gtTrapDestPort,
       "gtTrapDestRowStatus": gtTrapDestRowStatus,
       "gtUser": gtUser,
       "gtUserTable": gtUserTable,
       "gtUserEntry": gtUserEntry,
       "gtUserIdx": gtUserIdx,
       "gtUserParamIdx": gtUserParamIdx,
       "gtUserName": gtUserName,
       "gtUserPassword": gtUserPassword,
       "gtUserGroup": gtUserGroup,
       "gtUserAccesslist": gtUserAccesslist,
       "gtUserRowStatus": gtUserRowStatus,
       "gtGroupTable": gtGroupTable,
       "gtGroupEntry": gtGroupEntry,
       "gtGroupIdx": gtGroupIdx,
       "gtGroupParamIdx": gtGroupParamIdx,
       "gtGroupName": gtGroupName,
       "gtGroupRights": gtGroupRights,
       "gtGroupAccesslist": gtGroupAccesslist,
       "gtAccesslistTable": gtAccesslistTable,
       "gtAccesslistEntry": gtAccesslistEntry,
       "gtAccesslistIdx": gtAccesslistIdx,
       "gtAccesslistParamIdx": gtAccesslistParamIdx,
       "gtAccesslistName": gtAccesslistName,
       "gtAccesslistIPRange": gtAccesslistIPRange,
       "gtCurrentUserName": gtCurrentUserName,
       "gtCurrentUserPassword": gtCurrentUserPassword,
       "gtUserAuthTable": gtUserAuthTable,
       "gtUserAuthEntry": gtUserAuthEntry,
       "gtUserAuthEnabled": gtUserAuthEnabled,
       "gtServices": gtServices,
       "gtServicesTable": gtServicesTable,
       "gtServicesEntry": gtServicesEntry,
       "gtWebEnable": gtWebEnable,
       "gtWebAuth": gtWebAuth,
       "gtWebProtocol": gtWebProtocol,
       "gtModuleBackup": gtModuleBackup,
       "gtChassisRedundancy": gtChassisRedundancy,
       "gtModuleBackupTable": gtModuleBackupTable,
       "gtModuleBackupEntry": gtModuleBackupEntry,
       "gtModuleBackupDate": gtModuleBackupDate,
       "gtModuleRedundancyGroup": gtModuleRedundancyGroup,
       "gtModuleRedundancyMode": gtModuleRedundancyMode,
       "gtModuleBackupControl": gtModuleBackupControl,
       "gtModuleBackupStatus": gtModuleBackupStatus,
       "gtBackupControl": gtBackupControl,
       "gtBackupStatus": gtBackupStatus,
       "gtBackupPrivateKeyFilename": gtBackupPrivateKeyFilename,
       "gtBackupSFTPServer": gtBackupSFTPServer,
       "gtBackupSFTPPort": gtBackupSFTPPort,
       "gtBackupSFTPUsername": gtBackupSFTPUsername,
       "gtBackupSFTPPassword": gtBackupSFTPPassword,
       "gtBackupSFTPHostPublicKeyMD5": gtBackupSFTPHostPublicKeyMD5,
       "gtBackupSFTPFilename": gtBackupSFTPFilename,
       "gtModuleUpdate": gtModuleUpdate,
       "gtUpdateControl": gtUpdateControl,
       "gtUpdateStatus": gtUpdateStatus,
       "gtFilename": gtFilename,
       "gtSFTPServer": gtSFTPServer,
       "gtSFTPPort": gtSFTPPort,
       "gtSFTPUsername": gtSFTPUsername,
       "gtSFTPPassword": gtSFTPPassword,
       "gtSFTPHostPublicKeyMD5": gtSFTPHostPublicKeyMD5,
       "gtUpdateFilesTable": gtUpdateFilesTable,
       "gtUpdateFilesEntry": gtUpdateFilesEntry,
       "gtUpdateFilesTableIdx": gtUpdateFilesTableIdx,
       "gtUpdateFile": gtUpdateFile,
       "gtSettingsConformance": gtSettingsConformance,
       "gtSettingsCompliances": gtSettingsCompliances,
       "gtSettingsGroups": gtSettingsGroups}
)
